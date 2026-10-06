import json
import shutil
import sys

import pytest

from fde_skills.adapters import compose, export
from fde_skills.cli import main
from fde_skills.library import (
    LibraryError,
    link_errors,
    load_skills,
    load_yaml,
    read_skill,
    validate,
)


def test_search_and_show(root, capsys):
    assert main(["--root", str(root), "search", "rag", "--json"]) == 0
    found = json.loads(capsys.readouterr().out)
    assert "rag-architecture" in {s["name"] for s in found}
    assert main(["--root", str(root), "show", "enterprise-ai-diagnosis", "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["skill"]["name"] == "enterprise-ai-diagnosis"
    assert main(["--root", str(root), "show", "does-not-exist"]) == 2


def test_init_create_and_draft_gate(root, tmp_path):
    target = tmp_path / "my-library"
    assert main(["--root", str(root), "init", str(target)]) == 0
    for name in ("LICENSE", "NOTICE.md"):
        assert (target / name).read_bytes() == (root / name).read_bytes()
    assert validate(target) == []
    assert (
        main(
            [
                "--root",
                str(target),
                "skill",
                "create",
                "supplier-check",
                "--display-name",
                'Supplier: "review"',
            ]
        )
        == 0
    )
    path = target / "skills/discovery/supplier-check/SKILL.md"
    assert read_skill(path).metadata["display_name"] == 'Supplier: "review"'
    assert read_skill(path).metadata["license"] == "AGPL-3.0-only"
    assert any("draft" in e for e in validate(target, False))
    assert main(["--root", str(target), "registry", "build"]) == 2
    assert main(["--root", str(target), "skill", "create", "supplier-check"]) == 2


def test_interactive_create(library, monkeypatch):
    monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
    monkeypatch.setattr("builtins.input", lambda _: "interactive-skill")
    assert main(["--root", str(library), "skill", "create", "--category", "engineering"]) == 0
    created = read_skill(library / "skills/engineering/interactive-skill/SKILL.md")
    assert created.metadata["tags"] == ["engineering"]


def test_init_no_partial_overwrite(root, tmp_path):
    target = tmp_path / "existing"
    target.mkdir()
    (target / "README.md").write_text("customer work", encoding="utf-8")
    assert main(["--root", str(root), "init", str(target)]) == 2
    assert (target / "README.md").read_text(encoding="utf-8") == "customer work"
    assert not (target / "schemas").exists()


@pytest.mark.parametrize("name", ["../escape", "UPPER", "a--b", "-start", "x" * 65])
def test_invalid_scaffold_names(library, name):
    assert main(["--root", str(library), "skill", "create", "--", name]) == 2


@pytest.mark.parametrize(
    "agent,directory",
    [
        ("codex", ".agents"),
        ("claude-code", ".claude"),
        ("cursor", ".cursor"),
        ("opencode", ".opencode"),
    ],
)
def test_native_exports_are_portable(root, tmp_path, agent, directory):
    output = tmp_path / "export"
    skills = load_skills(root)
    first = export(root, skills, agent, output)
    hashes = {p: (output / p).read_bytes() for p in first}
    assert first == export(root, skills, agent, output)
    assert hashes == {p: (output / p).read_bytes() for p in first}
    for skill in skills:
        folder = output / directory / "skills" / skill.name
        native = read_skill(folder / "SKILL.md")
        assert set(native.metadata) == {"name", "description", "license", "metadata"}
        assert native.metadata["license"] == "AGPL-3.0-only"
        for name in ("LICENSE", "NOTICE.md"):
            assert (folder / name).read_bytes() == (root / name).read_bytes()
        assert all(isinstance(v, str) for v in native.metadata["metadata"].values())
        contract = load_yaml((folder / "references/fde-contract.yaml").read_text(encoding="utf-8"))
        assert contract["skill"] == skill.metadata
        assert link_errors(folder / "SKILL.md", folder) == []


def test_export_protects_modified_and_unmanaged_files(library, tmp_path):
    output = tmp_path / "project"
    skills = load_skills(library)
    export(library, skills, "codex", output)
    dest = output / ".agents/skills/customer-interview/SKILL.md"
    dest.write_text("customer edited this", encoding="utf-8")
    with pytest.raises(LibraryError, match="was edited"):
        export(library, skills, "codex", output)
    export(library, skills, "codex", output, force=True)
    assert dest.read_text(encoding="utf-8").startswith("---")
    (output / ".fde/exports/codex.json").unlink()
    dest.write_text("unmanaged now", encoding="utf-8")
    with pytest.raises(LibraryError, match="unmanaged"):
        export(library, skills, "codex", output, force=True)
    assert dest.read_text(encoding="utf-8") == "unmanaged now"


def test_symlink_export_escape(library, tmp_path):
    output = tmp_path / "project"
    output.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    try:
        (output / ".agents").symlink_to(outside, target_is_directory=True)
    except OSError:
        pytest.skip("Symlinks unavailable to this account")
    with pytest.raises(LibraryError):
        export(library, load_skills(library), "codex", output)
    assert not list(outside.iterdir())


@pytest.mark.parametrize(
    "industry", ["ecommerce", "foreign-trade", "manufacturing", "medical-beauty", "recruitment"]
)
def test_industry_composition_and_export(root, tmp_path, industry):
    skill = next(s for s in load_skills(root) if s.name == "enterprise-ai-diagnosis")
    original = list(skill.metadata["constraints"])
    result = compose(skill, root, industry)
    assert result["skill"]["constraints"] == original
    assert result["industry"]["constraints"]
    assert (
        main(
            [
                "--root",
                str(root),
                "export",
                "codex",
                "--industry",
                industry,
                "--output",
                str(tmp_path / industry),
            ]
        )
        == 0
    )


def test_unknown_pack_and_incompatible_skill(root):
    skills = load_skills(root)
    skill = next(s for s in skills if s.name == "docker-deployment")
    with pytest.raises(LibraryError, match="does not extend"):
        compose(skill, root, "medical-beauty")
    with pytest.raises(LibraryError, match="Unknown industry"):
        compose(skill, root, "not-present")


def test_export_retains_skill_specific_license(library, tmp_path):
    skill = load_skills(library)[0]
    skill.metadata["license"] = "Apache-2.0"
    with pytest.raises(LibraryError, match="own LICENSE"):
        export(library, [skill], "codex", tmp_path / "output")
    (skill.path.parent / "LICENSE").write_text("Original upstream license notice", encoding="utf-8")
    export(library, [skill], "codex", tmp_path / "output")
    notice = tmp_path / "output/.agents/skills" / skill.name / "LICENSE"
    assert notice.read_text(encoding="utf-8") == "Original upstream license notice"


def test_parent_file_conflict_is_detected_before_any_write(library, tmp_path):
    output = tmp_path / "output"
    folder = output / ".agents/skills"
    folder.mkdir(parents=True)
    (folder / "customer-interview").write_text("existing user file", encoding="utf-8")
    with pytest.raises(LibraryError, match="not a directory"):
        export(library, load_skills(library), "codex", output)
    assert sorted(p.name for p in folder.iterdir()) == ["customer-interview"]


def test_broken_pack_references(library, root):
    shutil.copytree(root / "industries/ecommerce", library / "industries/ecommerce")
    assert any("unknown core skill" in e for e in validate(library, False))
