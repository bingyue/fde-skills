from pathlib import Path
import json
import shutil

import pytest
import yaml

from fde_skills.library import (
    LibraryError,
    json_text,
    load_skills,
    load_yaml,
    read_skill,
    registry,
    validate,
)


def rewrite(path, change):
    skill = read_skill(path)
    change(skill.metadata)
    path.write_text(
        "---\n"
        + yaml.safe_dump(skill.metadata, allow_unicode=True, sort_keys=False)
        + "---\n"
        + skill.body,
        encoding="utf-8",
    )


def test_full_library(root):
    assert validate(root) == []
    assert len(load_skills(root)) >= 60


@pytest.mark.parametrize(
    "field", ["scenario", "inputs", "outputs", "workflow", "evaluation", "constraints", "name"]
)
def test_missing_contract_fields_rejected(library, field):
    path = next((library / "skills").glob("*/*/SKILL.md"))
    rewrite(path, lambda m: m.pop(field))
    assert any(field in e for e in validate(library, False))


def test_invalid_version_and_directory(library):
    path = next((library / "skills").glob("*/*/SKILL.md"))
    rewrite(path, lambda m: m.update(version="latest"))
    assert any("version" in e for e in validate(library, False))


def test_duplicate_yaml_keys_rejected():
    with pytest.raises(LibraryError, match="Duplicate"):
        load_yaml("name: first\nname: second\n")


def test_unsafe_yaml_rejected():
    with pytest.raises(LibraryError, match="Invalid YAML"):
        load_yaml("!!python/object/apply:os.system ['false']")


def test_broken_example_and_local_link(library):
    folder = library / "skills/discovery/customer-interview"
    (folder / "examples/example.yaml").unlink()
    path = folder / "SKILL.md"
    path.write_text(
        path.read_text(encoding="utf-8") + "\n[missing](assets/missing.md)\n", encoding="utf-8"
    )
    errors = validate(library, False)
    assert errors
    # Restore the fixture to expose independent broken-link diagnostics.
    root = Path(__file__).resolve().parents[1]
    shutil.copy2(
        root / "skills/discovery/customer-interview/examples/example.yaml",
        folder / "examples/example.yaml",
    )
    assert any("broken link" in e for e in validate(library, False))


def test_incomplete_example_rejected(library):
    path = library / "skills/discovery/customer-interview/examples/example.yaml"
    sample = load_yaml(path.read_text(encoding="utf-8"))
    sample.pop("negative_case")
    path.write_text(yaml.safe_dump(sample), encoding="utf-8")
    assert any("negative_case" in e for e in validate(library, False))


def test_example_inputs_must_match_contract(library):
    path = library / "skills/discovery/customer-interview/examples/example.yaml"
    sample = load_yaml(path.read_text(encoding="utf-8"))
    sample["input"].pop("constraints")
    sample["input"]["context"] = "not-an-object"
    path.write_text(yaml.safe_dump(sample), encoding="utf-8")
    errors = validate(library, False)
    assert any("missing required example input" in e for e in errors)
    assert any("nonempty object" in e for e in errors)


def test_example_output_mismatch(library):
    path = library / "skills/discovery/customer-interview/examples/example.yaml"
    sample = load_yaml(path.read_text(encoding="utf-8"))
    sample["expected"]["artifact"] = "invented.md"
    path.write_text(yaml.safe_dump(sample), encoding="utf-8")
    assert any("not declared" in e for e in validate(library, False))


def test_duplicate_name_and_content(library):
    src = library / "skills/discovery/customer-interview"
    dst = library / "skills/diagnosis/copy"
    shutil.copytree(src, dst)
    errors = validate(library, False)
    assert any("Duplicate skill name" in e for e in errors)
    assert any("Duplicate skill body" in e for e in errors)


def test_dependency_cycle_and_unknown(library):
    p = library / "skills/discovery/customer-interview/SKILL.md"
    q = library / "skills/diagnosis/enterprise-ai-diagnosis/SKILL.md"
    rewrite(p, lambda m: m.update(dependencies=["enterprise-ai-diagnosis", "not-present"]))
    rewrite(q, lambda m: m.update(dependencies=["customer-interview"]))
    errors = validate(library, False)
    assert any("unknown dependency" in e for e in errors)
    assert any("cycle" in e for e in errors)


def test_registry_detects_asset_change(library):
    (library / "skills.json").write_text(json_text(registry(library)), encoding="utf-8")
    assert validate(library) == []
    asset = library / "skills/discovery/customer-interview/assets/output-template.md"
    asset.write_text(
        asset.read_text(encoding="utf-8") + "\nUpdated review field.\n", encoding="utf-8"
    )
    assert any("stale" in e for e in validate(library))


def test_schema_itself_is_validated(library):
    p = library / "schemas/skill.schema.json"
    schema = json.loads(p.read_text(encoding="utf-8"))
    schema["type"] = "not-a-type"
    p.write_text(json.dumps(schema), encoding="utf-8")
    assert any("Invalid schema" in e for e in validate(library, False))


def test_reference_traversal_rejected(library):
    path = library / "skills/discovery/customer-interview/SKILL.md"
    rewrite(path, lambda m: m["examples"][0].update(path="../../../LICENSE"))
    assert any("Unsafe resource path" in e for e in validate(library, False))


def test_missing_frontmatter(library):
    path = library / "skills/discovery/customer-interview/SKILL.md"
    path.write_text("# A document without a contract\n", encoding="utf-8")
    assert any("front matter" in e for e in validate(library, False))
