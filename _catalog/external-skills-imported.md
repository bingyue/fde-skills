# External Skills Imported

从 Skillhub / skills.sh 拉取并落地到当前仓库的外部 Skill。

导入日期：2026-07-11（taxonomy 更新：2026-07-12）  
落地路径：`.agents/skills/`

## 导入结果总览

- 已导入：19
- 未导入：1（`railwayapp/railway-skills@deployment`）

## 新 taxonomy 映射说明

外部 Skill **不单独建顶层目录**，映射到 11 目录体系下的本库 Skill 作为参考实现。详见 [`fde-skill-map.md`](./fde-skill-map.md)。

## 明细（已导入）

| skill | source | local_path | suggested_category (2026) | maps_to |
| --- | --- | --- | --- | --- |
| deployment-engineer | charon-fan/agent-playbook | `.agents/skills/deployment-engineer` | 05-Deployment | Private-Deployment-Gateway |
| deployment-pipeline-design | wshobson/agents | `.agents/skills/deployment-pipeline-design` | 05-Deployment | Private-Deployment-Gateway |
| enterprise-sales | refoundai/lenny-skills | `.agents/skills/enterprise-sales` | 02-Discovery | Consultative-Problem-Solving |
| enterprise-user-management-ai-analytics | aradotso/data-skills | `.agents/skills/enterprise-user-management-ai-analytics` | 07-Operations | SQL-Dashboard-Brief |
| langchain-rag | langchain-ai/langchain-skills | `.agents/skills/langchain-rag` | 04-AI-Delivery | RAG-Evaluation |
| rag-implementation | wshobson/agents | `.agents/skills/rag-implementation` | 04-AI-Delivery | RAG-Evaluation |
| rag-architect | jeffallan/claude-skills | `.agents/skills/rag-architect` | 04-AI-Delivery | RAG-Evaluation |
| mcp-builder | anthropics/skills | `.agents/skills/mcp-builder` | 04-AI-Delivery | Tool-Audit |
| mcp-apps-builder | mcp-use/mcp-use | `.agents/skills/mcp-apps-builder` | 04-AI-Delivery | Tool-Audit |
| crm-automation | claude-office-skills/skills | `.agents/skills/crm-automation` | 07-Operations | Customer-Service-Bot（参考） |
| crm-data-quality | hubspot/agent-cli-skills | `.agents/skills/crm-data-quality` | 07-Operations | —（参考） |
| tiktok-shop-customer-service | nexscope-ai/ecommerce-skills | `.agents/skills/tiktok-shop-customer-service` | 07-Operations | Customer-Service-Bot |
| cs-sop | asgard-ai-platform/skills | `.agents/skills/cs-sop` | 07-Operations | Customer-Service-Bot |
| supply-chain-risk-auditor | trailofbits/skills | `.agents/skills/supply-chain-risk-auditor` | 09-Industry | —（参考） |
| supply-chain-optimizer | travisjneuman/.claude | `.agents/skills/supply-chain-optimizer` | 09-Industry | —（参考） |
| security-review | getsentry/skills | `.agents/skills/security-review` | 08-Security-Compliance | RBAC-Audit |
| security-requirement-extraction | wshobson/agents | `.agents/skills/security-requirement-extraction` | 08-Security-Compliance | RBAC-Audit |
| designing-growth-loops | refoundai/lenny-skills | `.agents/skills/designing-growth-loops` | 07-Operations | FDE-Adoption-Growth |
| saas-revenue-growth-metrics | deanpeters/product-manager-skills | `.agents/skills/saas-revenue-growth-metrics` | 07-Operations | FDE-Adoption-Growth |

## 未导入条目

| skill | source | status | note |
| --- | --- | --- | --- |
| deployment | railwayapp/railway-skills | failed | 偏海外 PaaS，与国内私有化主线不符；安装后未生成本地目录 |

## 咨询 Reference（另册）

咨询/PPT 类 Skill 不在 `.agents/skills/`，已落地 `11-Best-Practice/references/`（6 个）。  
详见 [`consulting-references.md`](./consulting-references.md)。
