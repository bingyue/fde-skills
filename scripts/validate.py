#!/usr/bin/env python3
"""Validate the repository without installing its console entry point."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fde_skills.cli import main  # noqa: E402

raise SystemExit(
    main(["--root", str(Path(__file__).resolve().parents[1]), "validate", *sys.argv[1:]])
)
