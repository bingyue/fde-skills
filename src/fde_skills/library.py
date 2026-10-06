"""Parsing, deterministic indexing and validation; no network or agent execution."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator


class LibraryError(ValueError):
    pass


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently losing metadata."""


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise LibraryError(f"Duplicate or non-string YAML key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def load_yaml(text: str):
    try:
        return yaml.load(text, Loader=UniqueLoader)
    except yaml.YAMLError as exc:
        raise LibraryError(f"Invalid YAML: {exc}") from exc


def json_text(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def library_root(explicit: str | Path | None = None) -> Path:
    if explicit is not None:
        root = Path(explicit).resolve()
        if not (root / "schemas/skill.schema.json").is_file():
            raise LibraryError(f"Not an FDE Skills library: {root}")
        return root
    for base in (Path.cwd(), Path(__file__).resolve().parents[2]):
        for root in (base, *base.parents):
            if (root / "schemas/skill.schema.json").is_file():
                return root
    bundled = Path(__file__).parent / "library"
    if (bundled / "schemas/skill.schema.json").is_file():
        return bundled
    raise LibraryError("Library not found. Use --root /path/to/fde-skills.")


def safe_path(base: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise LibraryError(f"Unsafe resource path: {relative}")
    full = base / path
    if not full.resolve().is_relative_to(base.resolve()):
        raise LibraryError(f"Resource escapes library: {relative}")
    cursor = base
    members = [base]
    for part in path.parts:
        cursor = cursor / part
        members.append(cursor)
    if any(p.is_symlink() for p in members):
        # Symlinks within source assets must never import files outside the package.
        raise LibraryError(f"Symlink resource is unsupported: {relative}")
    if any(p.exists() and not p.is_dir() for p in members[:-1]):
        raise LibraryError(f"Resource parent is not a directory: {relative}")
    return full


@dataclass
class Skill:
    path: Path
    metadata: dict
    body: str

    @property
    def name(self):
        return self.metadata["name"]


def read_skill(path: Path) -> Skill:
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not match:
        raise LibraryError(f"{path}: expected YAML front matter followed by Markdown")
    metadata = load_yaml(match[1])
    if not isinstance(metadata, dict):
        raise LibraryError(f"{path}: front matter must be an object")
    return Skill(path, metadata, match[2].strip())


def load_skills(root: Path) -> list[Skill]:
    return [read_skill(path) for path in sorted((root / "skills").glob("*/*/SKILL.md"))]


def select(skills: list[Skill], names: list[str] | None = None) -> list[Skill]:
    if not names:
        return skills
    by_name = {s.name: s for s in skills}
    missing = set(names) - by_name.keys()
    if missing:
        raise LibraryError("Unknown skills: " + ", ".join(sorted(missing)))
    return [by_name[n] for n in sorted(set(names))]


def skill_hash(skill: Skill) -> str:
    digest = hashlib.sha256()
    for path in sorted(skill.path.parent.rglob("*")):
        if path.is_file():
            safe_path(skill.path.parent, path.relative_to(skill.path.parent).as_posix())
            digest.update(path.relative_to(skill.path.parent).as_posix().encode())
            digest.update(b"\0")
            digest.update(path.read_bytes())
    return digest.hexdigest()


def registry(root: Path) -> dict:
    return {
        "spec_version": "1.0.0",
        "skills": [
            {
                **{
                    k: s.metadata[k]
                    for k in (
                        "name",
                        "display_name",
                        "description",
                        "version",
                        "category",
                        "tags",
                        "status",
                        "dependencies",
                        "license",
                    )
                },
                "path": s.path.relative_to(root).as_posix(),
                "sha256": skill_hash(s),
            }
            for s in sorted(load_skills(root), key=lambda s: s.name)
        ],
    }


def markdown_index(root: Path) -> str:
    skills = load_skills(root)
    result = f"# FDE Skills index\n\n{len(skills)} canonical Skills. Source: `skills/`; searchable machine index: [skills.json](skills.json).\n\n"
    for category in sorted({s.metadata["category"] for s in skills}):
        result += f"## {category}\n\n| Skill | Display name |\n| --- | --- |\n"
        for skill in sorted(skills, key=lambda s: s.name):
            if skill.metadata["category"] == category:
                result += f"| [{skill.name}]({skill.path.relative_to(root).as_posix()}) | {skill.metadata['display_name']} |\n"
        result += "\n"
    return result.rstrip() + "\n"


def schema_errors(root: Path, name: str, data, label: str) -> list[str]:
    schema = json.loads((root / "schemas" / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return [
        f"{label}: {'/'.join(map(str, e.path)) or '<root>'}: {e.message}"
        for e in Draft202012Validator(schema).iter_errors(data)
    ]


def link_errors(path: Path, boundary: Path, ignore_missing: set[Path] | None = None) -> list[str]:
    """Check inline/reference Markdown and HTML local file links, including anchors."""
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    links = re.findall(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text)
    links += re.findall(r"^\s*\[[^\]]+\]:\s*(\S+)", text, re.M)
    links += re.findall(r'(?:href|src)=["\']([^"\']+)["\']', text)
    errors = []
    for raw in links:
        raw = raw.strip("<>")
        url = urlsplit(raw)
        if url.scheme or raw.startswith("//"):
            continue
        dest = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
        if not dest.is_relative_to(boundary.resolve()):
            errors.append(f"{path}: link outside library: {raw}")
        elif not dest.exists() and dest not in (ignore_missing or set()):
            errors.append(f"{path}: broken link: {raw}")
        elif url.fragment and dest.suffix == ".md":
            anchors = []
            for heading in re.findall(r"^#{1,6}\s+(.+)$", dest.read_text(encoding="utf-8"), re.M):
                anchor = re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-")
                anchors.append(anchor)
            if unquote(url.fragment) not in anchors:
                errors.append(f"{path}: missing anchor: {raw}")
    return errors


def validate(root: Path, check_registry: bool = True, allow_draft: bool = False) -> list[str]:
    errors: list[str] = []
    from jsonschema.exceptions import SchemaError

    for schema_path in (root / "schemas").glob("*.json"):
        try:
            Draft202012Validator.check_schema(json.loads(schema_path.read_text(encoding="utf-8")))
        except (SchemaError, ValueError) as exc:
            errors.append(f"Invalid schema {schema_path}: {exc}")
    if errors:
        return errors
    skills: list[Skill] = []
    for path in sorted((root / "skills").rglob("SKILL.md")):
        try:
            safe_path(root, path.relative_to(root).as_posix())
            if len(path.relative_to(root).parts) != 4:
                raise LibraryError(f"{path}: expected skills/<category>/<name>/SKILL.md")
            skill = read_skill(path)
            bad = schema_errors(root, "skill.schema.json", skill.metadata, str(path))
            errors.extend(bad)
            if bad:
                continue
            skills.append(skill)
            meta = skill.metadata
            if meta["name"] != path.parent.name or meta["category"] != path.parent.parent.name:
                errors.append(f"{path}: name/category must match directories")
            if not skill.body.strip():
                errors.append(f"{path}: missing Markdown execution instructions")
            if not allow_draft and (
                meta["status"] == "draft" or "TODO" in path.read_text(encoding="utf-8")
            ):
                errors.append(f"{path}: unfinished draft; complete it before publishing")
            if len({s["id"] for s in meta["workflow"]}) != len(meta["workflow"]):
                errors.append(f"{path}: duplicate workflow IDs")
            for example in meta["examples"]:
                fixture_path = safe_path(path.parent, example["path"])
                fixture = load_yaml(fixture_path.read_text(encoding="utf-8"))
                fixture_errors = schema_errors(
                    root, "example.schema.json", fixture, str(fixture_path)
                )
                errors.extend(fixture_errors)
                if not fixture_errors:
                    sample_input = fixture["input"]
                    declarations = {i["name"]: i for i in meta["inputs"]}
                    for field, declaration in declarations.items():
                        if declaration["required"] and field not in sample_input:
                            errors.append(
                                f"{fixture_path}: missing required example input: {field}"
                            )
                        if field in sample_input:
                            expected_type = {
                                "object": dict,
                                "array": list,
                                "string": str,
                                "file": str,
                            }[declaration["type"]]
                            value = sample_input[field]
                            if not isinstance(value, expected_type) or not value:
                                errors.append(
                                    f"{fixture_path}: input {field} must be a nonempty {declaration['type']}"
                                )
                    outputs = {o["name"]: o for o in meta["outputs"]}
                    artifact = fixture["expected"]["artifact"]
                    if artifact not in outputs:
                        errors.append(f"{fixture_path}: expected artifact not declared in outputs")
                    elif set(outputs[artifact]["required_fields"]) != set(
                        fixture["expected"]["required_fields"]
                    ):
                        errors.append(f"{fixture_path}: output fields differ from Skill contract")
            for rel in meta["evaluation"]["regression_cases"]:
                if not safe_path(path.parent, rel).is_file():
                    errors.append(f"{path}: missing regression case: {rel}")
            for output in meta["outputs"]:
                suffix_types = {
                    ".md": "markdown",
                    ".json": "json",
                    ".jsonl": "jsonl",
                    ".yaml": "yaml",
                }
                inferred = suffix_types.get(Path(output["name"]).suffix)
                if inferred and output["type"] not in (inferred, "file"):
                    errors.append(f"{path}: output extension/type mismatch: {output['name']}")
            for file in path.parent.rglob("*"):
                if file.is_file():
                    safe_path(path.parent, file.relative_to(path.parent).as_posix())
                    if file.suffix == ".md":
                        errors.extend(link_errors(file, path.parent))
        except (LibraryError, OSError, ValueError) as exc:
            errors.append(str(exc))
    names = [s.name for s in skills]
    for name in sorted(set(names)):
        if names.count(name) > 1:
            errors.append(f"Duplicate skill name: {name}")
    descriptions, bodies = {}, {}
    for skill in skills:
        for key, seen, label in (
            (skill.metadata["description"].strip(), descriptions, "description"),
            (
                re.sub(r"\s+", " ", re.sub(r"^#.*$", "", skill.body, flags=re.M)).strip(),
                bodies,
                "body",
            ),
        ):
            if key in seen:
                errors.append(f"Duplicate skill {label}: {seen[key]} and {skill.name}")
            seen[key] = skill.name
        for dep in skill.metadata["dependencies"]:
            if dep not in names:
                errors.append(f"{skill.name}: unknown dependency: {dep}")
    graph = {s.name: s.metadata["dependencies"] for s in skills}
    visited, visiting = set(), set()

    def visit(name):
        if name in visiting:
            errors.append(f"Dependency cycle involving {name}")
            return
        if name in visited:
            return
        visiting.add(name)
        for dep in graph.get(name, []):
            visit(dep)
        visiting.remove(name)
        visited.add(name)

    for name in names:
        visit(name)
    for path in sorted((root / "industries").glob("*/pack.yaml")):
        try:
            pack = load_yaml(path.read_text(encoding="utf-8"))
            bad = schema_errors(root, "industry.schema.json", pack, str(path))
            errors.extend(bad)
            if bad:
                continue
            if pack["name"] != path.parent.name:
                errors.append(f"{path}: industry name must match directory")
            refs = pack["extends"] + [
                s for scenario in pack["scenarios"] for s in scenario["skills"]
            ]
            for ref in refs:
                if ref not in names:
                    errors.append(f"{path}: unknown core skill: {ref}")
            for ref in pack["cases"]:
                if not safe_path(path.parent, ref).is_file():
                    errors.append(f"{path}: missing industry case: {ref}")
        except (LibraryError, OSError, ValueError) as exc:
            errors.append(str(exc))
    generated = {root / "skills.json", root / "INDEX.md"} if not check_registry else set()
    for folder in ("docs", "industries", "examples", "adapters"):
        for path in (root / folder).rglob("*.md"):
            errors.extend(link_errors(path, root, generated))
    for path in root.glob("*.md"):
        errors.extend(link_errors(path, root, generated))
    if check_registry and not errors:
        try:
            if json.loads((root / "skills.json").read_text(encoding="utf-8")) != registry(root):
                errors.append("skills.json is stale; run fde registry build")
            index = root / "INDEX.md"
            if index.is_file() and index.read_text(encoding="utf-8") != markdown_index(root):
                errors.append("INDEX.md is stale; run fde registry build")
        except (OSError, ValueError) as exc:
            errors.append(f"Registry missing or invalid: {exc}")
    return errors
