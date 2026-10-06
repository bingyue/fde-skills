"""Small argparse CLI. Never invokes a model, deploys, or contacts a customer."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import sys

import yaml

from . import __version__
from .adapters import compose, export
from .library import (
    LibraryError,
    json_text,
    library_root,
    load_skills,
    load_yaml,
    markdown_index,
    registry,
    safe_path,
    select,
    validate,
)


def parser():
    p = argparse.ArgumentParser(prog="fde", description="FDE Skills library and delivery framework")
    p.add_argument("--version", action="version", version=__version__)
    p.add_argument("--root", type=Path, help="Explicit canonical library root")
    sub = p.add_subparsers(dest="command", required=True)
    for name in ("list", "search"):
        item = sub.add_parser(name)
        if name == "search":
            item.add_argument("query")
        item.add_argument("--category")
        item.add_argument("--json", action="store_true")
    show = sub.add_parser("show")
    show.add_argument("name")
    show.add_argument("--json", action="store_true")
    show.add_argument("--industry")
    init = sub.add_parser(
        "init", help="Create an empty local Skill library without overwriting files"
    )
    init.add_argument("directory", nargs="?", default=".", type=Path)
    skill = sub.add_parser("skill").add_subparsers(dest="skill_command", required=True)
    create = skill.add_parser("create")
    create.add_argument("name", nargs="?")
    create.add_argument("--category", default="discovery")
    create.add_argument("--display-name")
    check = sub.add_parser("validate")
    check.add_argument(
        "--no-registry", action="store_true", help="Validate sources before rebuilding index"
    )
    check.add_argument("--allow-draft", action="store_true", help="For local authoring only")
    reg = sub.add_parser("registry").add_subparsers(dest="registry_command", required=True)
    reg.add_parser("build")
    exp = sub.add_parser("export")
    exp.add_argument("agent", choices=["codex", "claude-code", "cursor", "opencode"])
    exp.add_argument("--output", type=Path, required=True)
    exp.add_argument(
        "--skill", action="append", dest="names", help="Repeat to select multiple skills"
    )
    exp.add_argument("--industry")
    exp.add_argument("--force", action="store_true")
    return p


def initialize(source: Path, target: Path):
    target = target.absolute()
    files = {}
    for folder in ("schemas", "templates", "adapters"):
        for path in (source / folder).rglob("*"):
            if path.is_file():
                files[path.relative_to(source).as_posix()] = path.read_bytes()
    files.update(
        {
            "LICENSE": (source / "LICENSE").read_bytes(),
            "skills.json": json_text({"spec_version": "1.0.0", "skills": []}).encode(),
            "fde.yaml": b"name: FDE Skills\nspec_version: 1.0.0\n",
            "README.md": b"# FDE Skills\n\nCreate with `fde skill create`, then validate and export.\n",
        }
    )
    if (source / "NOTICE.md").is_file():
        files["NOTICE.md"] = (source / "NOTICE.md").read_bytes()
    for relative in files:
        if safe_path(target, relative).exists():
            raise LibraryError(f"Initialization would overwrite {relative}")
    for relative, content in files.items():
        path = safe_path(target, relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    (target / "skills").mkdir(exist_ok=True)
    (target / "industries").mkdir(exist_ok=True)
    print(f"Initialized FDE Skills library: {target}")


def create_skill(root: Path, name: str | None, category: str, display_name: str | None):
    if name is None:
        if not sys.stdin.isatty():
            raise LibraryError(
                "Provide a skill name: fde skill create my-skill --category discovery"
            )
        name = input("Skill name (lowercase-hyphenated): ").strip()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise LibraryError(
            "Skill name must be 1–64 lowercase ASCII letters/digits with single hyphens"
        )
    schema = json.loads((root / "schemas/skill.schema.json").read_text(encoding="utf-8"))
    if category not in schema["properties"]["category"]["enum"]:
        raise LibraryError(f"Unknown category: {category}")
    if any(s.name == name for s in load_skills(root)):
        raise LibraryError(f"Skill already exists: {name}")
    target = safe_path(root, f"skills/{category}/{name}")
    if target.exists():
        raise LibraryError(f"Destination already exists: {target}")
    template = root / "templates/skill"
    shutil.copytree(template, target)
    # Replace YAML values structurally; display names may contain quotes or colons.
    from .library import read_skill

    source = read_skill(target / "SKILL.md")
    source.metadata.update(
        name=name, display_name=display_name or name, category=category, tags=[category]
    )
    body = source.body.replace("{{name}}", name)
    (target / "SKILL.md").write_text(
        "---\n"
        + yaml.safe_dump(source.metadata, allow_unicode=True, sort_keys=False)
        + "---\n\n"
        + body
        + "\n",
        encoding="utf-8",
    )
    print(f"Created draft: {target}; complete TODOs before fde validate")


def main(argv=None) -> int:
    args = parser().parse_args(argv)
    try:
        root = library_root(args.root)
        if args.command == "init":
            initialize(root, args.directory)
            return 0
        if args.command == "skill":
            create_skill(root, args.name, args.category, args.display_name)
            return 0
        if args.command == "validate":
            errors = validate(root, not args.no_registry, args.allow_draft)
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            print(
                f"Valid: {len(load_skills(root))} skills; metadata, schemas, examples, links, duplicates, packs and registry"
            )
            return 0
        if args.command in ("registry", "export"):
            errors = validate(root, check_registry=False)
            if errors:
                raise LibraryError("Source validation failed:\n" + "\n".join(errors))
        if args.command == "registry":
            (root / "skills.json").write_text(json_text(registry(root)), encoding="utf-8")
            (root / "INDEX.md").write_text(markdown_index(root), encoding="utf-8")
            print("Updated skills.json and INDEX.md")
            return 0
        skills = load_skills(root)
        if args.command in ("list", "search"):
            found = [
                s for s in skills if not args.category or s.metadata["category"] == args.category
            ]
            if args.command == "search":
                query = args.query.casefold()
                found = [
                    s
                    for s in found
                    if query in json.dumps(s.metadata, ensure_ascii=False).casefold()
                ]
            if args.json:
                print(json_text([s.metadata for s in found]), end="")
            else:
                for s in found:
                    print(f"{s.name:34} {s.metadata['category']:13} {s.metadata['display_name']}")
            return 0
        if args.command == "show":
            skill = select(skills, [args.name])[0]
            contract = compose(skill, root, args.industry)
            print(
                json_text(contract) if args.json else skill.path.read_text(encoding="utf-8"), end=""
            )
            if args.industry and not args.json:
                print(
                    "\nIndustry overlay:\n"
                    + yaml.safe_dump(contract["industry"], allow_unicode=True)
                )
            return 0
        if args.command == "export":
            selected = select(skills, args.names)
            if args.industry and not args.names:
                pack_path = safe_path(root / "industries", f"{args.industry}/pack.yaml")
                if not pack_path.is_file():
                    raise LibraryError(f"Unknown industry: {args.industry}")
                selected = select(
                    skills, load_yaml(pack_path.read_text(encoding="utf-8"))["extends"]
                )
            # Include explicit prerequisite Skills, but never recursively execute them.
            names = {s.name for s in selected}
            pending = list(selected)
            while pending:
                for dep in pending.pop().metadata["dependencies"]:
                    if dep not in names:
                        dependency = select(skills, [dep])[0]
                        names.add(dep)
                        pending.append(dependency)
            selected = select(skills, list(names))
            files = export(root, selected, args.agent, args.output, args.industry, args.force)
            print(f"Exported {len(selected)} skills / {len(files)} files to {args.output}")
            return 0
    except (LibraryError, OSError, ValueError, KeyError) as exc:
        print(f"fde: {exc}", file=sys.stderr)
        return 2
    return 0
