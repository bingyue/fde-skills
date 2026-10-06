# 原仓库分析与迁移记录

> 许可更新（2026-10-07）：当前原创项目已按作者要求采用 AGPL-3.0-only，见 [LICENSE](../../LICENSE) 与 [NOTICE](../../NOTICE.md)。下文关于 MIT 的内容记录 2026-10-06 的迁移判断；历史许可和第三方条款继续保留。

审计日期：2026-10-06。原目录和远程已经是 `fde-skills` / `git@github.com:bingyue/fde-skills.git`。本次保持 Git 仓库与历史，产品展示名称统一为 **FDE Skills**。

## 原始状态

- HEAD：`504a52b`；此前还有 `67cf686`、`47e0550`，未重写历史。
- 原 README 声明31个核心能力包；11个编号目录加_catalog；8个核心包已有SKILL.md。绝大多数内容以README/prompt/checklist/evaluation四件套表达。
- 核心内容包括业务访谈、Issue Tree+DIVE、AIBP双负责人、三层PoC、EDD、私有化、采纳增长和产品化；另有职业发展与求职模板，保留作补充资料。
- 原有19个工程类外部导入、6个咨询参考，以及Diagnostic-FDE的嵌套子技能；其中部分缺少完整许可记录。
- 有若干Python工具：架构图、能力匹配、缺口分析、ROI、问卷和批量内容生成。没有正式Python包、CLI、Schema、测试或CI。
- 旧评价文件使用笼统的80%通过门槛，无法表达权限泄露等独立硬门槛；旧模板要求README行数，不能保证可执行性。
- 工作区已有未提交的自评、成长路线、沟通内容、求职模板和指南；本次一并保留。

## 分析与处置

| 内容 | 决定 | 原因 |
| --- | --- | --- |
| 31个既有核心包、有效方法论与职业资料 | 完整迁入legacy，并映射到新标准能力 | 保留深度内容与现场方法，标准入口改为可校验契约 |
| 旧Prompt/checklist/evaluation/workflow | 保留历史原文；新标准纳入独立步骤、边界和门禁 | 去除统一阈值与泛化四件套作为唯一标准 |
| 旧Python辅助工具 | 原位迁入legacy，保留源码与相对资源 | 不声称未经测试的旧脚本已成为受支持CLI功能 |
| _catalog批量生成器 | 归档，退出当前生成链路 | 避免覆盖新增手写内容和用户已有更新 |
| 外部镜像、咨询参考、锁文件 | 保留原条款与来源，不进入安装包和Adapter | 未核实的历史许可不能被新MIT声明覆盖 |
| 企业Skill指南、HTML和PPT版 | 保留在legacy/docs | 继续可读，作为旧版体系说明 |
| 运行日志、缓存 | 留在本地并忽略 | 不属于可发布库内容 |
| 产品名称、入口、包与索引 | 使用FDE Skills / fde-skills / fde | 统一品牌和可安装接口；没有重复新建项目 |

## 保留与兼容范围

[逐文件清单](original-inventory.json)记录370个原始文件的路径、迁移后路径与SHA-256。字节级核对覆盖已有未提交内容；`.gitignore`原文也在legacy保留。历史文件中的旧名称和路径是来源记录，不进行破坏性改写。原有Git提交、远程和历史均保留。

其中 368 份源文件与资产进入 Git，另外 2 份是 `_catalog/scripts/__pycache__/` 中的 Python 编译缓存，按上述缓存策略保留在本地并忽略。干净检出与 CI 必须验证全部 368 份版本化文件；本地缓存若存在，也继续核对其原始哈希。清单保留全部 370 条审计记录，原文件与哈希未改写。

新维护入口只扫描 `skills/*/*/SKILL.md`，避免将嵌套上游镜像误判为重复核心Skill。新的根INDEX与模板入口替代旧版链接；旧路径使用本表迁移到标准入口或legacy。归档中的旧脚本、外链和交叉引用不属于新CI支持范围，也不自动执行。

职业发展、求职辅导、飞书专项和历史咨询长文仍完整可读；映射表示任务关联，不声称新的通用Skill替代了全部专项深度。

## 核心映射

| 原能力包（保留原文） | 新标准入口 |
| --- | --- |
| [Communication-Script-Library](../../legacy/01-Foundation/Communication-Script-Library/README.md) | [customer-interview](../../skills/discovery/customer-interview/SKILL.md), [delivery-handover](../../skills/delivery/delivery-handover/SKILL.md) |
| [FDE-Growth-Roadmap](../../legacy/01-Foundation/FDE-Growth-Roadmap/README.md) | [30-day-industry-learning](../../skills/discovery/30-day-industry-learning/SKILL.md) |
| [FDE-Self-Assessment](../../legacy/01-Foundation/FDE-Self-Assessment/README.md) | [ai-maturity-assessment](../../skills/diagnosis/ai-maturity-assessment/SKILL.md) |
| [SOW-Generator](../../legacy/01-Foundation/SOW-Generator/README.md) | [poc-scope](../../skills/solution/poc-scope/SKILL.md), [enterprise-ai-pricing](../../skills/business/enterprise-ai-pricing/SKILL.md) |
| [Stakeholder-Mapping](../../legacy/01-Foundation/Stakeholder-Mapping/README.md) | [stakeholder-map](../../skills/discovery/stakeholder-map/SKILL.md) |
| [AIBP-Collaboration-Playbook](../../legacy/02-Discovery/AIBP-Collaboration-Playbook/README.md) | [stakeholder-map](../../skills/discovery/stakeholder-map/SKILL.md), [delivery-handover](../../skills/delivery/delivery-handover/SKILL.md) |
| [Business-Interview](../../legacy/02-Discovery/Business-Interview/README.md) | [customer-interview](../../skills/discovery/customer-interview/SKILL.md) |
| [Consultative-Problem-Solving](../../legacy/02-Discovery/Consultative-Problem-Solving/README.md) | [pain-point-analysis](../../skills/diagnosis/pain-point-analysis/SKILL.md), [enterprise-ai-diagnosis](../../skills/diagnosis/enterprise-ai-diagnosis/SKILL.md) |
| [Executive-Communication-Framework](../../legacy/02-Discovery/Executive-Communication-Framework/README.md) | [solution-brief](../../skills/solution/solution-brief/SKILL.md) |
| [Expectation-Management-Script](../../legacy/02-Discovery/Expectation-Management-Script/README.md) | [poc-scope](../../skills/solution/poc-scope/SKILL.md), [human-in-the-loop](../../skills/agent/human-in-the-loop/SKILL.md) |
| [FDE-Issue-Tree-Analysis](../../legacy/02-Discovery/FDE-Issue-Tree-Analysis/README.md) | [pain-point-analysis](../../skills/diagnosis/pain-point-analysis/SKILL.md), [enterprise-ai-diagnosis](../../skills/diagnosis/enterprise-ai-diagnosis/SKILL.md) |
| [Process-Mapping](../../legacy/02-Discovery/Process-Mapping/README.md) | [business-process-mapping](../../skills/discovery/business-process-mapping/SKILL.md) |
| [Sidecar-AI-Transformation](../../legacy/02-Discovery/Sidecar-AI-Transformation/README.md) | [requirement-to-poc](../../skills/solution/requirement-to-poc/SKILL.md), [poc-to-production](../../skills/deployment/poc-to-production/SKILL.md) |
| [API-Design-Review](../../legacy/03-Solution-Design/API-Design-Review/README.md) | [tool-design](../../skills/agent/tool-design/SKILL.md), [system-architecture](../../skills/architecture/system-architecture/SKILL.md) |
| [FDE-PoC-Tech-Stack-Selector](../../legacy/03-Solution-Design/FDE-PoC-Tech-Stack-Selector/README.md) | [technical-solution-design](../../skills/solution/technical-solution-design/SKILL.md) |
| [PRD-Generator](../../legacy/03-Solution-Design/PRD-Generator/README.md) | [prd-generation](../../skills/solution/prd-generation/SKILL.md) |
| [RAG-Evaluation](../../legacy/04-AI-Delivery/RAG-Evaluation/README.md) | [rag-evaluation](../../skills/evaluation/rag-evaluation/SKILL.md), [evaluation-driven-development](../../skills/engineering/evaluation-driven-development/SKILL.md) |
| [Tool-Audit](../../legacy/04-AI-Delivery/Tool-Audit/README.md) | [tool-calling-evaluation](../../skills/evaluation/tool-calling-evaluation/SKILL.md), [mcp-design](../../skills/engineering/mcp-design/SKILL.md) |
| [Private-Deployment-Gateway](../../legacy/05-Deployment/Private-Deployment-Gateway/README.md) | [private-deployment](../../skills/deployment/private-deployment/SKILL.md) |
| [Feishu-Integration](../../legacy/06-Integration/Feishu-Integration/README.md) | [tool-design](../../skills/agent/tool-design/SKILL.md), [workflow-design](../../skills/agent/workflow-design/SKILL.md) |
| [Customer-Service-Bot](../../legacy/07-Operations/Customer-Service-Bot/README.md) | [agent-design](../../skills/agent/agent-design/SKILL.md), [knowledge-base-design](../../skills/knowledge/knowledge-base-design/SKILL.md) |
| [FDE-Adoption-Growth](../../legacy/07-Operations/FDE-Adoption-Growth/README.md) | [enterprise-acceptance](../../skills/delivery/enterprise-acceptance/SKILL.md), [project-retrospective](../../skills/delivery/project-retrospective/SKILL.md) |
| [SQL-Dashboard-Brief](../../legacy/07-Operations/SQL-Dashboard-Brief/README.md) | [observability-design](../../skills/engineering/observability-design/SKILL.md), [cost-assessment](../../skills/business/cost-assessment/SKILL.md) |
| [RBAC-Audit](../../legacy/08-Security-Compliance/RBAC-Audit/README.md) | [permission-model](../../skills/architecture/permission-model/SKILL.md), [ai-security-testing](../../skills/evaluation/ai-security-testing/SKILL.md) |
| [AI-Operations-Daily](../../legacy/09-Industry/AI-Operations-Daily/README.md) | [industry-research](../../skills/discovery/industry-research/SKILL.md), [ai-opportunity-mapping](../../skills/business/ai-opportunity-mapping/SKILL.md) |
| [SOW-Template](../../legacy/10-Templates/SOW-Template/README.md) | [poc-scope](../../skills/solution/poc-scope/SKILL.md) |
| [China-FDE-Consulting-Pattern](../../legacy/11-Best-Practice/China-FDE-Consulting-Pattern/README.md) | [enterprise-ai-diagnosis](../../skills/diagnosis/enterprise-ai-diagnosis/SKILL.md), [delivery-handover](../../skills/delivery/delivery-handover/SKILL.md) |
| [Diagnostic-FDE](../../legacy/11-Best-Practice/Diagnostic-FDE/README.md) | [enterprise-ai-diagnosis](../../skills/diagnosis/enterprise-ai-diagnosis/SKILL.md), [industry-research](../../skills/discovery/industry-research/SKILL.md) |
| [FDE-Customer-Product-Bridge](../../legacy/11-Best-Practice/FDE-Customer-Product-Bridge/README.md) | [customer-discovery](../../skills/discovery/customer-discovery/SKILL.md), [prd-generation](../../skills/solution/prd-generation/SKILL.md) |
| [FDE-Full-Lifecycle](../../legacy/11-Best-Practice/FDE-Full-Lifecycle/README.md) | [requirement-to-poc](../../skills/solution/requirement-to-poc/SKILL.md), [poc-to-production](../../skills/deployment/poc-to-production/SKILL.md) |
| [Palantir-FDE-Pattern](../../legacy/11-Best-Practice/Palantir-FDE-Pattern/README.md) | [ontology-design](../../skills/ontology/ontology-design/SKILL.md), [field-observation](../../skills/discovery/field-observation/SKILL.md) |

## 新实现

[60项覆盖清单](core-coverage.json)对应用户要求的50个高价值场景和10个FDE核心场景。每项都有独立工作流、质量门禁、输出模板及正反例；五个行业Pack以扩展契约组合；五个案例展示完整交付阶段。

完整公开可分发安装包仅包括新维护的原创库内容。MIT沿用旧README声明；历史第三方材料保留原条款，详见[NOTICE](../../NOTICE.md)。是否公开再分发某个历史第三方文件仍需核验其具体版本授权；这不影响新CLI和标准库的安装包使用。
