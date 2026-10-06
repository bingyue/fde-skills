"""Bundle the canonical library in wheels without a second editable source copy."""

from pathlib import Path
import shutil

from setuptools import setup
from setuptools.command.build_py import build_py


class BuildLibrary(build_py):
    def run(self):
        super().run()
        root = Path(__file__).parent
        target = Path(self.build_lib) / "fde_skills" / "library"
        if target.exists():
            shutil.rmtree(target)
        for name in ("skills", "industries", "schemas", "templates", "adapters"):
            shutil.copytree(
                root / name,
                target / name,
                ignore=shutil.ignore_patterns(
                    "__pycache__", "*.py[cod]", ".DS_Store", ".env", ".env.*"
                ),
            )
        for name in ("skills.json", "LICENSE", "NOTICE.md"):
            shutil.copy2(root / name, target / name)


setup(cmdclass={"build_py": BuildLibrary})
