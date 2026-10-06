#!/usr/bin/env python3
"""Exercise the wheel in a clean environment outside the source checkout."""

from email import policy
from email.parser import BytesParser
import json
from pathlib import Path
import subprocess
import tempfile
import venv
import zipfile


def main():
    root = Path(__file__).resolve().parents[1]
    wheels = sorted((root / "dist").glob("fde_skills-*.whl"))
    if len(wheels) != 1:
        raise SystemExit("Expected one built wheel in dist/")
    wheel = wheels[0]
    with zipfile.ZipFile(wheel) as archive:
        names = archive.namelist()
        assert not any("/legacy/" in n or "/logs/" in n for n in names)
        assert sum(n.endswith("/SKILL.md") and "/library/skills/" in n for n in names) >= 60
        assert "fde_skills/library/skills.json" in names
        metadata_path = next(n for n in names if n.endswith(".dist-info/METADATA"))
        metadata = BytesParser(policy=policy.default).parsebytes(archive.read(metadata_path))
        assert metadata["License-Expression"] == "AGPL-3.0-only"
        assert "邴越" in metadata["Author"]
        for name in ("LICENSE", "NOTICE.md"):
            expected = (root / name).read_bytes()
            assert archive.read(f"fde_skills/library/{name}") == expected
            dist_notice = next(n for n in names if n.endswith(f".dist-info/licenses/{name}"))
            assert archive.read(dist_notice) == expected
    with tempfile.TemporaryDirectory(prefix="fde-wheel-") as tmp:
        folder = Path(tmp)
        env = folder / "venv"
        venv.create(env, with_pip=True)
        binary = env / ("Scripts" if __import__("os").name == "nt" else "bin")
        python = binary / "python"
        subprocess.run([str(python), "-m", "pip", "install", str(wheel)], cwd=folder, check=True)
        cmd = [str(python), "-m", "fde_skills"]
        found = subprocess.check_output([*cmd, "list", "--json"], cwd=folder, text=True)
        assert len(json.loads(found)) >= 60
        for args in (
            ["validate"],
            ["search", "rag"],
            ["show", "enterprise-ai-diagnosis", "--json"],
            [
                "export",
                "codex",
                "--skill",
                "enterprise-ai-diagnosis",
                "--output",
                str(folder / "project"),
            ],
            ["init", str(folder / "custom")],
            ["--root", str(folder / "custom"), "skill", "create", "custom-discovery"],
        ):
            subprocess.run([*cmd, *args], cwd=folder, check=True, stdout=subprocess.DEVNULL)
        for name in ("LICENSE", "NOTICE.md"):
            expected = (root / name).read_bytes()
            exported = folder / "project/.agents/skills/enterprise-ai-diagnosis" / name
            assert exported.read_bytes() == expected
            assert (folder / "custom" / name).read_bytes() == expected
    print("Wheel smoke passed: bundled library, CLI, export, init, create and license notices")


if __name__ == "__main__":
    main()
