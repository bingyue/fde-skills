# Release verification — FDE Skills 1.0.0

Date: 2026-10-06. Host: macOS arm64, Python 3.14.4. This record documents local verification before publication. For subsequent remote CI results, consult the repository Actions runs.

## Follow-up verification — 2026-10-07

- The first remote CI run exposed a migration-test portability issue: two Python interpreter caches were local and Git-ignored. The test now requires all 368 versioned assets and checks the two identified caches only when present; the original 370-entry inventory and local files remain unchanged.
- After that correction, a clean checkout from the staged Git index, without either cache, passed all 53 tests and `fde validate`. The visual update also passed text-boundary checks for eight bilingual diagrams; rebuilt source distributions include all 18 visual assets.
- Updated both READMEs with author 邴越 (Bing Yue), FDE前线, FDEChina.ai, project navigation and aligned contribution/community sections.
- Adopted AGPL-3.0-only for the current original project. The 2026-10-06 MIT entry below describes the earlier migration state; current terms and retained historical grants are documented in [NOTICE](../NOTICE.md).
- Updated all 60 Skill declarations, the creation template, package metadata, export defaults and generated registry. Distributions, initialized libraries and canonical exports include LICENSE and NOTICE.md.
- `fde validate` passed all 60 Skills, schemas, examples, local links, duplicates, packs and registry checks. Fixed an incoming README anchor after reorganizing its sections.
- `pytest -q`: **53 passed**, including the 370-file historical preservation check, all four adapters, scaffold licensing and preservation of separately licensed Skill notices.
- Ruff and `git diff --check` passed. Rebuilt wheel and sdist; the clean wheel smoke test verified author/license metadata, bundled notices and exported/initialized notices outside the source checkout.

## Requirement evidence

| Requirement | Evidence |
| --- | --- |
| Existing repository and Git history | Same fde-skills path and bingyue/fde-skills remote; original three commits retained |
| Preserve existing valid and uncommitted material | [370-entry inventory](migration/original-inventory.json); SHA-256 checks for 368 versioned assets plus two local caches when present |
| Original analysis and migration decisions | [Audit and 31 mappings](migration/README.md) |
| Unified product/package/docs names | [Chinese README](../README.md), [English README](../README_EN.md), [pyproject](../pyproject.toml); old names limited to historical references |
| Required root and category structure | 12 populated skills categories plus docs, industries, templates, examples, schemas, scripts, tests and adapters |
| Full Skill Specification | [Specification](skill-spec/README.md), strict [Skill Schema](../schemas/skill.schema.json), duplicate YAML keys rejected |
| 50 requested delivery tasks + 10 FDE core tasks | [Coverage manifest](migration/core-coverage.json) and independent required-name assertions in tests |
| Human/agent-readable definitions | 60 Markdown + YAML SKILL.md files; required inputs, outputs, workflows, constraints, examples and evaluation |
| Worked examples and failures | 60 worked fixtures with separate negative input and expected recovery, plus 60 output templates |
| Five reusable industry packs | [Pack specification](skill-spec/industry-packs.md); additive composition and reference checks |
| CLI and new-Skill template | [CLI](../src/fde_skills/cli.py); list/search/show/init/create/validate/index/export tests, including interactive create |
| Four adapters and current conventions | [Official-source research](getting-started/adapters.md); native format, full contract, copied assets and safe overwrite tests |
| Five end-to-end examples | Five case manifests, 40 stage artifacts, 60 synthetic checks; missing/duplicate external prediction handling |
| Business First / Evaluation Driven / From PoC to Production | Both READMEs and [delivery framework](concepts/delivery-framework.md) |
| Searchable registry | [skills.json](../skills.json); deterministic content hashes, stale detection and rebuilt human INDEX |
| CI required checks | [GitHub workflow](../.github/workflows/ci.yml); metadata/Schema/required fields/local links/example consistency/duplicate detection |
| Contribution guidance and tutorial | [CONTRIBUTING](../CONTRIBUTING.md), [development guide](best-practices/skill-development.md), [complete tutorial](getting-started/contribute-a-skill.md) |
| License continuity | MIT already declared in old README; LICENSE supplied; upstream terms retained and archived imports excluded from distributions |
| Five-phase Roadmap | [ROADMAP](../ROADMAP.md), with implemented foundations distinguished from future field/runtime validation |
| Runnable release | wheel + sdist built; clean-environment wheel installed outside source checkout; bundled commands and exports exercised |

## Verification commands

```bash
fde validate
pytest -q
ruff check src tests scripts setup.py
python -m build
python scripts/smoke_wheel.py
git diff --check
```

The final automated suite contains 53 tests. Five case runs each pass 12/12 guarded synthetic checks; their deliberately unguarded baselines fail. The 370 original-file hashes match. Registry/index rebuild is deterministic. The clean wheel test exercises bundled resources, list/search/show/validate, export, init and skill creation. The build generates the wheel from the source distribution, verifying that canonical JSONL and other resources survive both packaging stages.

## Corrections found through verification

- Removed a generated-index bootstrap dependency on an already-present index file.
- Aligned example input types with declared input contracts and added enforcement.
- Corrected the eval-dataset output type to JSONL and supplied actual JSONL records.
- Extended package resources so the JSONL example is included in both sdist and wheel; installed-library validation caught the missing asset.
- Normalized generated index whitespace and removed unused imports.
- Tested quoted display names, invalid names, interactive creation, source traversal, symlink exports, modified files unmanaged-file conflicts, parent-file conflicts and preservation of Skill-specific license notices.

## Practical limits

- Remote GitHub Actions is configured for Python 3.10/3.12/3.14 but has not been triggered by a push in this task.
- Native files comply with the researched directory/metadata conventions. Live behavior inside each commercial agent client has not been tested.
- Synthetic examples and deterministic baselines demonstrate contracts and failure gates, not real model quality or customer ROI. No Skill is marked field-validated.
- Historical third-party imports keep their original notices; some lack a documented license. They are preserved for history, excluded from the supported distribution, and require a source-specific rights check before separate redistribution.
- Local verification does not establish a PyPI release, a customer-system deployment or a passing remote CI run. Git publication and its CI results are recorded in the repository history and Actions runs.
