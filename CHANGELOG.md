# Changelog

## Unreleased — 2026-10-07

- Make Chinese the default README and package introduction; provide English in README_EN.md and retain README_CN.md as a compatibility entry point.

- Refresh the English and Chinese READMEs with aligned project documentation, contribution paths, roadmap, author 邴越 (Bing Yue), FDE前线 and FDEChina.ai community links.
- Adopt GNU AGPL v3 only (AGPL-3.0-only) for the current original project at the author's direction. Preserve earlier grants and the original terms of historical third-party material.
- Synchronize package metadata, 60 canonical Skills, scaffolding, generated registry and adapter exports with the license declaration.
- Include the complete license and project notices in distributions, initialized libraries and native Skill exports; verify propagation through existing regression tests.

## 1.0.0 — 2026-10-06

- Standardize the product name as FDE Skills and the Python distribution as fde-skills.
- Introduce 60 canonical Skills across 12 categories, typed YAML contracts, JSON Schemas, output templates and positive/negative examples.
- Add five additive industry packs and four native Agent Skills adapters.
- Add the fde CLI for discovery, scaffolding, validation, indexing and safe exports.
- Add five full delivery case studies, an offline baseline and regression gates.
- Add bilingual onboarding, contribution tutorial, delivery framework, roadmap and CI.
- Preserve all previous content, including uncommitted edits, in a byte-verified migration archive; retire old generators from the supported pipeline.
- Supply the MIT license already declared in the previous README; preserve upstream terms and exclude historical imports from supported distributions.

## Earlier history

The repository began at commit `47e0550`, followed by `67cf686` and `504a52b`. The prior README recorded v0.1.0 (2026-07-11) and v0.2.0 (2026-07-12). Those records and the exact previous documents remain in [the legacy archive](legacy/README.md). This release does not rewrite commits or rename the already-correct GitHub remote.
