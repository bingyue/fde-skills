"""Compile one canonical Skill source into each agent's native Skill directory."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml

from . import __license__
from .library import LibraryError, Skill, json_text, load_yaml, safe_path


def compose(skill: Skill, root: Path, industry: str | None) -> dict:
    result = {"skill": skill.metadata}
    if industry:
        path = safe_path(root / "industries", f"{industry}/pack.yaml")
        if not path.is_file():
            raise LibraryError(f"Unknown industry: {industry}")
        pack = load_yaml(path.read_text(encoding="utf-8"))
        if skill.name not in pack["extends"]:
            raise LibraryError(f"{industry} does not extend {skill.name}")
        result["industry"] = pack
        result["composition"] = (
            "Core constraints AND industry constraints; conflicting rules require review."
        )
    return result


def render(skill: Skill, contract: dict) -> str:
    meta = skill.metadata
    native = {
        "name": skill.name,
        "description": meta["description"],
        "license": meta["license"],
        "metadata": {
            "fde-version": meta["version"],
            "fde-category": meta["category"],
            "fde-status": meta["status"],
        },
    }
    body = skill.body + "\n\n## FDE execution contract\n\n"
    body += "Read [the complete contract](references/fde-contract.yaml) before execution. "
    body += "Use supplied evidence; report missing inputs, decisions and failed gates.\n\n"
    body += "### Inputs\n\n" + "\n".join(
        f"- `{v['name']}` ({'required' if v['required'] else 'optional'}): {v['description']}"
        for v in meta["inputs"]
    )
    body += "\n\n### Outputs\n\n" + "\n".join(
        f"- `{v['name']}`: " + ", ".join(v["required_fields"]) for v in meta["outputs"]
    )
    body += "\n\n### Quality gates\n\n" + "\n".join(
        "- " + v for v in meta["quality_criteria"] + meta["constraints"]
    )
    if "industry" in contract:
        body += "\n\n### Industry overlay\n\n" + contract["composition"] + "\n\n"
        body += "\n".join("- " + v for v in contract["industry"]["constraints"])
        body += "\n\nUse industry terminology, metrics, scenarios and knowledge in the contract."
    return (
        "---\n"
        + yaml.safe_dump(native, allow_unicode=True, sort_keys=False)
        + "---\n\n"
        + body
        + "\n"
    )


def export(
    root: Path,
    skills: list[Skill],
    agent: str,
    output: Path,
    industry: str | None = None,
    force: bool = False,
) -> list[str]:
    config_path = safe_path(root / "adapters", f"{agent}/adapter.json")
    if not config_path.is_file():
        raise LibraryError(f"Unknown adapter: {agent}")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    output = output.absolute()
    planned: dict[str, bytes] = {}
    for skill in skills:
        contract = compose(skill, root, industry)
        prefix = f"{config['directory']}/{skill.name}"
        for path in sorted(skill.path.parent.rglob("*")):
            if path.is_file() and path.name != "SKILL.md":
                rel = path.relative_to(skill.path.parent).as_posix()
                safe_path(skill.path.parent, rel)
                planned[f"{prefix}/{rel}"] = path.read_bytes()
        planned[f"{prefix}/SKILL.md"] = render(skill, contract).encode()
        planned[f"{prefix}/references/fde-contract.yaml"] = yaml.safe_dump(
            contract, allow_unicode=True, sort_keys=False
        ).encode()
        if f"{prefix}/LICENSE" not in planned:
            if skill.metadata["license"] != __license__:
                raise LibraryError(
                    f"{skill.name}: a Skill not using {__license__} requires its own LICENSE file"
                )
            planned[f"{prefix}/LICENSE"] = (root / "LICENSE").read_bytes()
            notice = root / "NOTICE.md"
            if notice.is_file() and f"{prefix}/NOTICE.md" not in planned:
                planned[f"{prefix}/NOTICE.md"] = notice.read_bytes()
    manifest_rel = f".fde/exports/{agent}.json"
    manifest_path = safe_path(output, manifest_rel)
    previous = (
        json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest_path.exists()
        else {"files": {}}
    )
    # Preflight every write before touching the destination. --force only permits
    # replacing a file this adapter previously generated, never an unrelated file.
    for relative, data in planned.items():
        path = safe_path(output, relative)
        if path.exists():
            current = path.read_bytes()
            if current == data:
                continue
            recorded = previous["files"].get(relative)
            if not recorded:
                raise LibraryError(f"Refusing to overwrite unmanaged file: {path}")
            if hashlib.sha256(current).hexdigest() != recorded and not force:
                raise LibraryError(
                    f"Generated file was edited: {path}; review before using --force"
                )
    manifest = dict(previous)
    manifest.update({"adapter": agent, "format_version": 1})
    manifest["files"] = {
        **previous["files"],
        **{p: hashlib.sha256(v).hexdigest() for p, v in planned.items()},
    }
    for relative, data in planned.items():
        path = safe_path(output, relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json_text(manifest), encoding="utf-8")
    return sorted(planned)
