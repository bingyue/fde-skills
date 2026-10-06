# Quick start

Use Python 3.10 or newer. From this repository run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
fde --version
fde list --category knowledge
fde search RAG --json
fde show enterprise-ai-diagnosis
fde validate
```

Use `fde --root /path/to/library ...` to choose an explicit library. Otherwise the CLI searches the working directory and its parents, then the source checkout or library bundled in the installed wheel. No global agent directory is modified.

## Choose a path

For a customer project, export a small set of relevant Skills into its existing directory:

```bash
fde export codex --skill customer-discovery --skill enterprise-ai-diagnosis --output ../customer-project
```

For a new library of your own, initialize an empty source layout:

```bash
fde init ./my-library
fde --root ./my-library skill create supplier-onboarding --category discovery
```

Initialization fails before writing if a managed target file already exists. It does not clone this Git repository or copy its history. Inside FDE Skills itself, skip init and add the Skill directly. For non-interactive use, always supply a name to `skill create`.

## Verify and package

```bash
fde validate --no-registry
fde registry build
fde validate
pytest
python -m build
```

The wheel includes the active Skills, packs, templates, schemas, adapter profiles and index. Historical third-party imports are excluded. Install the built wheel in a clean virtual environment to confirm the bundled library works outside this checkout. See [release practice](../best-practices/releasing.md).
