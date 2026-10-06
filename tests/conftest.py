from pathlib import Path
import shutil

import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def root():
    return ROOT


@pytest.fixture
def library(tmp_path):
    for name in ("schemas", "templates", "adapters"):
        shutil.copytree(ROOT / name, tmp_path / name)
    for name in ("LICENSE", "NOTICE.md"):
        shutil.copy2(ROOT / name, tmp_path / name)
    for category, name in [
        ("discovery", "customer-interview"),
        ("diagnosis", "enterprise-ai-diagnosis"),
    ]:
        dest = tmp_path / "skills" / category / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(ROOT / "skills" / category / name, dest)
    return tmp_path
