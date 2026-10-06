# FDE Skill Specification 1.0

Canonical path: `skills/<category>/<name>/SKILL.md`. UTF-8 Markdown starts with YAML front matter. [JSON Schema](../../schemas/skill.schema.json) is authoritative; [example Schema](../../schemas/example.schema.json) validates worked examples. This FDE profile intentionally contains more structured fields than the generic Agent Skills standard; adapters compile it to the portable standard.

| Field | Type | Contract |
| --- | --- | --- |
| name | string | Lowercase ASCII/digits with single hyphens, 1–64 chars, identical to folder |
| display_name | string | Human-readable name, bilingual names welcome |
| description | string | Concrete action and trigger, 1–1024 chars |
| version | string | Semantic `major.minor.patch` |
| category | enum | One of the 12 repository categories |
| tags | unique string array | Search terms; no empty entries |
| scenario / goal | strings | Business situation and bounded delivery outcome |
| when_to_use / when_not_to_use | string arrays | Routing and exclusions |
| inputs | object array | name, description, required boolean, type: object/string/array/file |
| outputs | object array | name, type: markdown/json/jsonl/yaml/file, description, required_fields |
| workflow | object array | Unique step id, action, evidence |
| constraints | string array | Authority, domain and execution boundaries |
| quality_criteria | string array | Observable acceptance conditions, not vague quality slogans |
| tools | object array, may be empty | name, purpose, required; capabilities, never automatic permissions |
| dependencies | name array, may be empty | Existing Skill names, no cycles; prerequisite artifact may already exist |
| examples | object array | name and Skill-relative path to a worked YAML fixture |
| evaluation | object | method, checks (id/criterion/severity), regression_cases paths |
| license | string | SPDX identifier; canonical Skills use AGPL-3.0-only. A different license requires its own LICENSE and compatibility review |
| status | enum | draft / ready / field-validated |

Unknown top-level fields and duplicate YAML keys fail validation. Inputs, outputs, examples and gates may not be empty. Fields are machine-readable; the Markdown body explains decision points and failure recovery without repeating a large manual.

## Example and resource contract

Each Skill ships `examples/example.yaml` with:

```yaml
kind: synthetic
input:
  context:
    evidence: Concrete customer evidence
  constraints:
    boundary: Explicit authorization and resource limits
expected:
  artifact: deliverable.md
  decision: A worked expected result, with rationale
  required_fields: [evidence, decision, next_action]
checks: [An observable check]
negative_case:
  input: A realistic failure or unavailable input
  expected: Useful bounded recovery rather than a false pass
```

The expected artifact and required fields must match `outputs`. `evaluation.regression_cases` must exist. Local Markdown links resolve inside the Skill so that exports remain self-contained. File paths must be relative, without traversal or symlink escapes. Network links are references, not required downloads; CI validates local links offline.

## Versioning and maturity

Breaking changes to required inputs, output meaning or authorization boundaries increment major. Compatible workflow changes increment minor; typo and documentation corrections increment patch. `ready` means content is authored and passes repository checks. `field-validated` requires an anonymized validation record with context, evidence, reviewer and limitations; it does not mean universally suitable.

The scaffold is intentionally `draft` and contains TODO markers. Default `fde validate`, index publication and exports reject unfinished drafts. During local authoring use `fde validate --allow-draft --no-registry` only. Review is required before changing the status.

## Industry extension and platform compilation

[Industry packs](industry-packs.md) reference Skill names and append domain context. The four adapters retain name/description/license and string-valued metadata in native front matter. Rich structured metadata is preserved in `references/fde-contract.yaml` and important execution fields in the Markdown body. No adapter invents tool permissions or weakens constraints.
