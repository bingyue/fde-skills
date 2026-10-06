# FDE Skills

**Open-source skills for Forward Deployed Engineers and Enterprise AI Delivery.**

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](pyproject.toml)
[![Validation](https://github.com/bingyue/fde-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/bingyue/fde-skills/actions/workflows/ci.yml)

**English** · [简体中文](README_CN.md) · [FDEChina.ai](https://fdechina.ai/) · [Skill index](INDEX.md) · [Documentation](docs/getting-started/quickstart.md) · [Contributing](CONTRIBUTING.md)

FDE Skills is an open-source **Skill Library and Delivery Framework** for Forward Deployed Engineers and enterprise AI practitioners. It helps Codex, Claude Code, Cursor and OpenCode follow a structured method for understanding a business, diagnosing needs, designing solutions, building systems, evaluating outcomes and completing delivery.

**FDE Skills goes beyond teaching AI to write code: it teaches AI to work like a Forward Deployed Engineer, from the first customer conversation to a system operating in production.**

| Principle | What it means in practice |
| --- | --- |
| **Business First** | Understand the workflow, stakeholders and business value before designing AI. |
| **Evaluation Driven** | Define evidence, measurable acceptance criteria and failure cases for every AI application. |
| **From PoC to Production** | Plan for deployment, operations, rollback and ownership from the start. |

## What you can do

- Turn a customer request into a diagnosis, opportunity map, scoped PoC and delivery plan.
- Design enterprise knowledge bases, RAG systems, agents, tools, permissions and human review.
- Build evaluation datasets and assess retrieval, hallucination, task success, security and cost.
- Prepare deployment, production acceptance, service levels and delivery handover.
- Reuse industry context and contribute lessons from real delivery work.

## Library at a glance

| Component | Available today |
| --- | --- |
| Core Skills | **60 Skills in 12 categories**, with structured contracts, workflows, quality gates, output templates and positive/negative examples |
| Industry packs | **5 packs**: ecommerce, foreign trade, manufacturing, medical beauty and recruitment |
| Agent adapters | **4 adapters**: Codex, Claude Code, Cursor and OpenCode, generated from one canonical source |
| Delivery examples | **5 end-to-end cases**, 40 stage artifacts and 60 executable synthetic checks |
| Engineering | Python CLI, JSON Schemas, searchable [registry](skills.json), automated validation and CI |

A Skill marked `ready` has been authored and structurally checked. It does not imply customer validation. Example data and evaluation results are synthetic unless explicitly documented otherwise.

## Quick start

Requires **Python 3.10+**. From a checkout of this repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'

fde list
fde search rag
fde show enterprise-ai-diagnosis
fde validate
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

Export Skills into an existing project:

```bash
fde export codex --skill enterprise-ai-diagnosis --output ../customer-project
fde export claude-code --industry foreign-trade --output ../customer-project
fde export cursor --skill rag-architecture --output ../customer-project
fde export opencode --skill delivery-handover --output ../customer-project
```

Exports include native `SKILL.md` files, the complete FDE contract, examples, templates and license notices. The CLI runs locally without model calls or credentials. See [adapter setup and behavior](docs/getting-started/adapters.md).

## How a Skill works

Each canonical Skill lives at `skills/<category>/<name>/SKILL.md`. Markdown instructions and YAML front matter define when to use it, required inputs, expected outputs, workflow, constraints, tools and evaluation criteria. Supporting files provide a worked example and an output template.

```text
Need → Discovery → Diagnosis → Solution → Architecture → Build → Eval → Deploy → Delivery
```

Each delivery gate requires evidence, an owner and a pass/fail decision. Missing inputs become a gap report; failed evaluations lead to remediation before progression. Read the [delivery framework](docs/concepts/delivery-framework.md) and [FDE Skill Specification](docs/skill-spec/README.md).

| Category | Representative Skills |
| --- | --- |
| discovery | customer-discovery, field-observation, industry-research |
| diagnosis | enterprise-ai-diagnosis, pain-point-analysis |
| solution | requirement-to-poc, poc-scope, technical-solution-design |
| architecture | system-architecture, rag-architecture, permission-model |
| knowledge | source-inventory, knowledge-base-design, retrieval-strategy |
| agent | agent-design, workflow-design, human-in-the-loop |
| ontology | ontology-design |
| engineering | evaluation-driven-development, mcp-design, observability-design |
| evaluation | rag-evaluation, tool-calling-evaluation, prompt-regression |
| deployment | docker-deployment, private-deployment, poc-to-production |
| delivery | enterprise-acceptance, sla-design, delivery-handover |
| business | roi-assessment, ai-opportunity-mapping, enterprise-ai-pricing |

Browse all 60 Skills in the [index](INDEX.md), or use `fde search <keyword>`.

## Industry packs and delivery examples

Industry packs reference core Skills and add knowledge, constraints, metrics, terminology and cases. This keeps domain knowledge reusable without duplicating workflows. See the [pack specification](docs/skill-spec/industry-packs.md).

| Pack | Focus |
| --- | --- |
| [Ecommerce](industries/ecommerce/README.md) | Product knowledge, customer service and operations |
| [Foreign trade](industries/foreign-trade/README.md) | Inquiries, follow-up, product knowledge, multilingual service and email drafts |
| [Manufacturing](industries/manufacturing/README.md) | Equipment knowledge, quality, SOPs, maintenance, supply chain and production data |
| [Medical beauty](industries/medical-beauty/README.md) | Service information, consultation routing, appointments and compliance boundaries |
| [Recruitment](industries/recruitment/README.md) | Role requirements, candidate evidence, interview support and human review |

Every case walks through Discovery, Diagnosis, Solution, Architecture, Build, Eval, Deploy and Delivery:

1. [Enterprise AI diagnosis](examples/01-enterprise-ai-diagnosis/README.md)
2. [Enterprise knowledge base](examples/02-enterprise-knowledge-base/README.md)
3. [Foreign trade sales agent](examples/03-foreign-trade-sales-agent/README.md)
4. [Medical beauty consultation and appointment agent](examples/04-medical-beauty-conversion-agent/README.md)
5. [Manufacturing knowledge agent](examples/05-manufacturing-knowledge-agent/README.md)

```bash
python scripts/run_example.py 02-enterprise-knowledge-base
```

These reproducible offline examples include deliberately failing baselines. Their checks demonstrate contracts and delivery gates; production model quality and business impact require evaluation with real systems and authorized data.

## Repository layout

```text
fde-skills/
├── skills/          # Canonical definitions in 12 delivery categories
├── industries/      # Five additive industry packs
├── adapters/        # Codex, Claude Code, Cursor and OpenCode profiles
├── templates/       # Skill scaffolds and delivery records
├── examples/        # Five complete delivery cases
├── schemas/         # Skill, example and industry JSON Schemas
├── src/fde_skills/   # CLI and offline example baseline
├── scripts/         # Validation, registry and example entry points
├── tests/           # Contract, CLI, adapter and regression tests
├── docs/            # Concepts, specification, guides and migration history
├── legacy/          # Preserved historical assets and upstream notices
└── skills.json      # Generated registry for search and future integrations
```

## Contributing

Contributions are welcome in Chinese or English: improve a Skill, add a verified failure case, extend an industry pack, improve an adapter or fix documentation. Start with the [contribution guide](CONTRIBUTING.md) and [complete Skill contribution tutorial](docs/getting-started/contribute-a-skill.md).

```bash
fde skill create supplier-onboarding --category discovery
# Complete the draft, output template and positive/negative examples.
fde registry build
fde validate
pytest -q
ruff check src tests scripts setup.py
```

Use `fde skill create` without a name for interactive creation, or `fde init ./my-library` to scaffold a separate library. Keep canonical definitions in `skills/` and regenerate derived files. Submit bug reports and proposals through [Issues](https://github.com/bingyue/fde-skills/issues), and changes through [Pull Requests](https://github.com/bingyue/fde-skills/pulls).

## Roadmap

| Phase | Direction | Status |
| --- | --- | --- |
| 1 | 50+ Core Skills | Initial library of 60 Skills implemented |
| 2 | Industry Skill Packs | Five initial packs; field validation ongoing |
| 3 | Codex / Claude Code / Cursor / OpenCode Adapters | Four exporters implemented; client runtime verification remains |
| 4 | FDE Blueprint Integration | Planned |
| 5 | Skill Registry / Marketplace | Local registry available; marketplace planned |

See the [detailed roadmap](ROADMAP.md), [changelog](CHANGELOG.md) and [verification record](docs/verification.md).

## Author and community

**Author and maintainer: [邴越 (Bing Yue)](https://github.com/bingyue).** Community contributions are welcome.

- **[FDEChina.ai · FDE中国社区](https://fdechina.ai/)** — enterprise AI delivery cases, methods, learning resources and community opportunities.
- **FDE前线** — follow the WeChat Official Account and WeChat Channels account by searching for **「FDE前线」**.
- **[FDE Skills on GitHub](https://github.com/bingyue/fde-skills)** — source code, Skills, proposals and contributions.

We welcome engineers, business practitioners and industry specialists who want to turn delivery experience into reusable, verifiable Skills. Use GitHub for repository issues and the community channels for broader FDE discussions.

## License

Copyright © 2026 **邴越 (Bing Yue) and FDE Skills contributors**.

The current original FDE Skills library, CLI, documentation, templates and examples are licensed under the **GNU Affero General Public License v3.0 only (`AGPL-3.0-only`)**. See the full [LICENSE](LICENSE).

When a modified covered program supports remote network interaction, AGPL section 13 requires offering its Corresponding Source to those remote users. Distribution and other conditions are set out in the license itself.

Historical third-party material retains its original terms and is excluded from supported packages and adapter exports. Earlier license grants are not revoked. See [NOTICE](NOTICE.md), [source provenance](SOURCES.md) and the [migration record](docs/migration/README.md).
