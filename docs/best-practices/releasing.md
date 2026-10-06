# Releasing

The distributable library is built from the active canonical sources under AGPL-3.0-only, with LICENSE and NOTICE.md included. Historical imports in legacy/ are retained with original provenance but excluded from wheel, sdist and adapter exports. Git history is preserved; a public Git archive still contains historical material, whose original terms continue to apply. Earlier license grants remain valid; see [NOTICE](../../NOTICE.md).

```bash
python -m pip install -e '.[dev]'
fde validate
pytest
ruff check src tests scripts setup.py
python -m build
```

Inspect wheel/sdist contents for active resources and absence of `legacy/`, logs, credentials and build artifacts. Install the wheel in a fresh environment outside the repository and run `fde list`, `fde validate`, `fde init`, `fde skill create` and one export. Validate the source distribution can rebuild the same resource set.

Update CHANGELOG, versions, official adapter source checks and Roadmap. Do not mark field readiness or client runtime testing complete based solely on structural checks. Publishing a release, pushing tags or uploading to PyPI is a separate maintainer action.

Local Markdown file links and declared examples are checked offline in CI. External URLs and live vendor behavior require periodic manual review; network availability is not a prerequisite for normal validation.
