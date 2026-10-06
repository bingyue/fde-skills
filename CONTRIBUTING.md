# Contributing to FDE Skills

Contribute a capability that changes a delivery decision or produces a verifiable artifact. Search existing Skills before adding one. Prefer improving an existing workflow or adding industry context to creating a near-duplicate.

1. Install with `python -m pip install -e '.[dev]'` in a virtual environment.
2. Run `fde search <task>` and choose one of the 12 categories.
3. Use `fde skill create <name> --category <category>`.
4. Complete the FDE contract, Markdown decisions, output template, worked input/output and a realistic negative case. Remove TODOs; then change `status` from `draft` to `ready`.
5. Run `fde validate --no-registry`, `fde registry build`, `fde validate`, `pytest` and `ruff check src tests scripts setup.py`.
6. Open a contribution describing the customer task, reused material and permission/license, expected artifact, failure behavior and validation evidence.

Follow [FDE Skill Specification](docs/skill-spec/README.md), [Skill development guidance](docs/best-practices/skill-development.md) and the [complete contribution tutorial](docs/getting-started/contribute-a-skill.md).

## Review criteria

- Concrete task and exclusions; no blanket activation for unrelated work.
- Required input evidence and authority are explicit.
- Workflow includes consequential decisions and recovery, not just generic prompts.
- Acceptance is observable; critical failures cannot be averaged away.
- A worked example and negative case demonstrate the boundary.
- Reusable assets are local, portable and appropriately licensed.
- No real customer identifiers, credentials, undisclosed model usage or fabricated validation.

## Contribution license

By submitting original contributions for inclusion, you agree to license them under **GNU AGPL v3 only (`AGPL-3.0-only`)**, the project's [license](LICENSE). Contributors retain copyright in their work. Submit material you own or have permission to contribute under compatible terms.

Third-party material requires an explicit source and license review, preserved notices and a clearly documented scope. A Skill with a different SPDX identifier must include its own `LICENSE`; a metadata field alone does not establish compatibility. See [NOTICE](NOTICE.md). Historical third-party archives require the same review before inclusion in an active Skill.

## Generated files and verification

Maintain canonical sources only. Generated index and adapters must be reproducible. Schema changes require migration guidance and tests. For code changes, add focused tests of user-visible behavior and failure boundaries. Docs-only changes need link checks, not artificial implementation-mirroring tests.
