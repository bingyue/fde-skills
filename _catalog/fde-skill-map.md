# FDE Skill Map

将候选 Skill（本库 + 外部 + 本地 codex/agents）映射到 **11 目录交付体系**。

## 映射规则

| 交付阶段 | 目录 |
| --- | --- |
| 立项与基线 | `01-Foundation` |
| 发现与咨询 | `02-Discovery` |
| 方案与规格 | `03-Solution-Design` |
| AI 构建与评估 | `04-AI-Delivery` |
| 部署与网关 | `05-Deployment` |
| 企业集成 | `06-Integration` |
| 运营与采纳 | `07-Operations` |
| 安全合规 | `08-Security-Compliance` |
| 行业示例 | `09-Industry`（精简） |
| 模板 | `10-Templates` |
| 方法论 | `11-Best-Practice` |

**禁止**：按 CRM/ERP/工具拆顶层目录。CRM 类外部 Skill 映射到 `02-Discovery` 或 `07-Operations`。

## 本库 Skill 全映射

| skill | primary_category | secondary_category | reason |
| --- | --- | --- | --- |
| Stakeholder-Mapping | 01-Foundation | 02-Discovery | Kickoff 干系人分析 |
| SOW-Generator | 01-Foundation | 10-Templates | PoC 范围与验收书面化 |
| FDE-Self-Assessment | 01-Foundation | 11-Best-Practice | 四角色能力基线 |
| FDE-Growth-Roadmap | 01-Foundation | 11-Best-Practice | 成长与作品集绑定 |
| Communication-Script-Library | 01-Foundation | 02-Discovery | 分角色沟通话术 |
| Business-Interview | 02-Discovery | 01-Foundation | 结构化业务访谈 |
| Process-Mapping | 02-Discovery | 03-Solution-Design | 流程与 AI 介入点 |
| Consultative-Problem-Solving | 02-Discovery | 11-Best-Practice | Issue Tree + DIVE |
| Expectation-Management-Script | 02-Discovery | 08-Security-Compliance | 概率性边界与人审 |
| Executive-Communication-Framework | 02-Discovery | 07-Operations | 高层 ROI 与决策 |
| AIBP-Collaboration-Playbook | 02-Discovery | 07-Operations | FDE+AIBP 双负责人 |
| PRD-Generator | 03-Solution-Design | 02-Discovery | 场景卡扩展为 PRD |
| API-Design-Review | 03-Solution-Design | 06-Integration | 系统集成契约评审 |
| RAG-Evaluation | 04-AI-Delivery | 08-Security-Compliance | EDD 与 Golden Dataset |
| Tool-Audit | 04-AI-Delivery | 08-Security-Compliance | Agent/MCP 工具治理 |
| Private-Deployment-Gateway | 05-Deployment | 08-Security-Compliance | 私有化与 AI Gateway |
| Feishu-Integration | 06-Integration | 07-Operations | 飞书协同嵌入 |
| Customer-Service-Bot | 07-Operations | 04-AI-Delivery | 客服 RAG+工单运营 |
| FDE-Adoption-Growth | 07-Operations | 02-Discovery | 采纳漏斗与客户成功 |
| SQL-Dashboard-Brief | 07-Operations | 03-Solution-Design | 经营指标看板需求 |
| RBAC-Audit | 08-Security-Compliance | 04-AI-Delivery | 权限与合规审计 |
| AI-Operations-Daily | 09-Industry | 07-Operations | 跨境/品牌运营日报示例 |
| SOW-Template | 10-Templates | 01-Foundation | SOW 标准模板 |
| Palantir-FDE-Pattern | 11-Best-Practice | 01-Foundation | 国际 FDE 对照 |
| China-FDE-Consulting-Pattern | 11-Best-Practice | 02-Discovery | 国内咨询式总纲 |
| FDE-Full-Lifecycle | 11-Best-Practice | 01-Foundation | Audit/Evals/Deployment 全流程 |
| Diagnostic-FDE | 11-Best-Practice | 02-Discovery | ToB 12 步售前方案包 |
| FDE-Customer-Product-Bridge | 11-Best-Practice | 02-Discovery | 客户-产品-研发四工作流 |

## 咨询 Reference 映射（`11-Best-Practice/references/`）

不计入 28 个核心 Skill。详见 [`consulting-references.md`](./consulting-references.md)。

| reference | local_path | maps_to_local_skill | 用途 |
| --- | --- | --- | --- |
| MECE | `11-Best-Practice/references/MECE` | Consultative-Problem-Solving | MECE / 金字塔结构化 |
| McKinsey-Frameworks | `11-Best-Practice/references/McKinsey-Frameworks` | Diagnostic-FDE | 战略框架速查 |
| McKinsey-Report | `11-Best-Practice/references/McKinsey-Report` | Executive-Communication-Framework | 行研报告写作 |
| McKinsey-PPT-Design | `11-Best-Practice/references/McKinsey-PPT-Design` | Diagnostic-FDE | python-pptx PPT |
| Elite-PPT-Pro | `11-Best-Practice/references/Elite-PPT-Pro` | Executive-Communication-Framework | 多咨询风 PPT |
| GE-Matrix-Analysis | `11-Best-Practice/references/GE-Matrix-Analysis` | McKinsey-Frameworks | GE/麦肯锡矩阵 |

## 外部已导入 Skill 映射（新 taxonomy）

| skill | local_path | primary_category | maps_to_local_skill |
| --- | --- | --- | --- |
| deployment-engineer | `.agents/skills/deployment-engineer` | 05-Deployment | Private-Deployment-Gateway |
| deployment-pipeline-design | `.agents/skills/deployment-pipeline-design` | 05-Deployment | Private-Deployment-Gateway |
| langchain-rag | `.agents/skills/langchain-rag` | 04-AI-Delivery | RAG-Evaluation |
| rag-implementation | `.agents/skills/rag-implementation` | 04-AI-Delivery | RAG-Evaluation |
| rag-architect | `.agents/skills/rag-architect` | 04-AI-Delivery | RAG-Evaluation |
| mcp-builder | `.agents/skills/mcp-builder` | 04-AI-Delivery | Tool-Audit |
| mcp-apps-builder | `.agents/skills/mcp-apps-builder` | 04-AI-Delivery | Tool-Audit |
| security-review | `.agents/skills/security-review` | 08-Security-Compliance | RBAC-Audit |
| security-requirement-extraction | `.agents/skills/security-requirement-extraction` | 08-Security-Compliance | RBAC-Audit |
| cs-sop | `.agents/skills/cs-sop` | 07-Operations | Customer-Service-Bot |
| tiktok-shop-customer-service | `.agents/skills/tiktok-shop-customer-service` | 07-Operations | Customer-Service-Bot |
| designing-growth-loops | `.agents/skills/designing-growth-loops` | 07-Operations | FDE-Adoption-Growth |
| saas-revenue-growth-metrics | `.agents/skills/saas-revenue-growth-metrics` | 07-Operations | FDE-Adoption-Growth |
| enterprise-user-management-ai-analytics | `.agents/skills/enterprise-user-management-ai-analytics` | 07-Operations | SQL-Dashboard-Brief |
| enterprise-sales | `.agents/skills/enterprise-sales` | 02-Discovery | Consultative-Problem-Solving |
| crm-automation | `.agents/skills/crm-automation` | 07-Operations | —（参考，不单独建目录） |
| crm-data-quality | `.agents/skills/crm-data-quality` | 07-Operations | — |
| supply-chain-risk-auditor | `.agents/skills/supply-chain-risk-auditor` | 09-Industry | — |
| supply-chain-optimizer | `.agents/skills/supply-chain-optimizer` | 09-Industry | — |

## 本地 codex/agents 候选映射

| skill | source | primary_category | notes |
| --- | --- | --- | --- |
| idea-to-prd | codex | 03-Solution-Design | → PRD-Generator |
| growth-user-interview | codex | 02-Discovery | → Business-Interview |
| lark-bitable | codex | 06-Integration | → Feishu-Integration |
| cn-compliance-check | codex | 08-Security-Compliance | 合规扩展候选 |
| architecture-designer | agents | 03-Solution-Design | API/架构评审补充 |
| create-skill | cursor | 10-Templates | Skill 生产规范 |

## 精简策略（已执行）

- 删除 `Vercel-Deployment` → `Private-Deployment-Gateway`
- 删除 `Landing-Page-Brief` → `FDE-Adoption-Growth`
- 删除空目录 `02-Business`
- 不新增 CRM/ERP 顶层目录；以外部 Skill 参考 + Operations 场景覆盖
