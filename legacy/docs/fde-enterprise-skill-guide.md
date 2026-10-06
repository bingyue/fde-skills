---
title: "FDE 企业落地典型 Skill 分类与使用说明"
subtitle: "基于 fde-skills 代码仓库的企业 AI 交付手册"
author: "FDE-Skills"
date: "2026-07-23"
lang: "zh-CN"
toc: true
toc-depth: 3
numbersections: true
geometry: "margin=20mm"
fontsize: "10.5pt"
CJKmainfont: "PingFang SC"
---

# 阅读说明

本文面向承担企业 AI 项目售前、发现、方案、PoC、部署、集成、运营与产品化工作的 FDE、Applied AI 工程师、解决方案架构师、产品经理和项目负责人。

文档基于当前工作目录的实际内容编写，盘点基线为 **2026-07-23**：

- 31 个纳入 [`INDEX.md`](../INDEX.md) 的核心 Skill；
- 11 个交付分类；
- 6 个咨询与汇报 Reference；
- 19 个位于 [`.agents/skills/`](../.agents/skills/) 的外部镜像 Skill；
- 1 个不计入核心 Skill 数的求职模板包；
- 当前核心目录中 8 个带 `SKILL.md` 的 Agent 原生 Skill。

> 版本口径：仓库 [`README.md`](../README.md) 记录的版本为 v0.2.0；本文反映的是编写当日工作树，而不只反映最近一次 Git 提交。

本文不是把 31 个 Skill 简单罗列成工具菜单，而是回答四个企业落地问题：

1. 当前项目处于哪个交付阶段？
2. 这一阶段应该调用哪些 Skill？
3. 每个 Skill 需要什么输入、产出什么交付物？
4. 何时可以进入下一阶段，何时必须回退补证据？

<div style="break-after: page;"></div>

# 一、结论先行

## 1.1 仓库定位

`fde-skills` 是一套面向国内企业 AI 交付的**能力操作系统**。它的基本单元不是零散 Prompt，也不是某个厂商工具的操作说明，而是能够重复执行、检查和验收的交付能力包。

仓库使用以下主链路组织能力：

```text
立项基线 → 需求发现 → 方案规格 → AI 构建与评估
     → 部署 → 企业集成 → 运营采纳 → 产品化复用

横切门禁：安全合规
横切资产：模板、方法论、行业示例、咨询 Reference
```

## 1.2 推荐的三层分类

| 层级 | 包含目录 | 企业用途 |
| --- | --- | --- |
| 主交付链 | 01–07 | 从立项、发现、设计、构建到生产采纳 |
| 横切门禁 | 08 Security-Compliance | 对数据、权限、工具和生产风险设门禁 |
| 方法与资产 | 09–11 | 提供行业样例、标准模板和全流程方法论 |

## 1.3 最重要的使用原则

- **先定阶段，再选 Skill**：不要从“我想用 Dify / LangChain”开始，应先判断处于发现、选型、评估还是生产阶段。
- **先证据，后方案**：访谈、流程、失败样本、数据约束和业务基线不足时，不直接输出生产方案。
- **一个主 Skill，若干辅 Skill**：一次任务应明确主交付物，避免把多个 Skill 拼成无法执行的大而全报告。
- **用验收文件结束任务**：`evaluation.md` 不是附录，而是判断是否过门的依据。
- **PoC 成功不等于企业落地**：生产部署、工作流集成、用户采纳和价值复盘必须单独管理。
- **项目结束必须资产化**：把单客户经验沉淀为模板、组件、评估集、产品需求或新的 Skill。

# 二、FDE 生命周期与目录映射

仓库的 11 类 Skill 可以映射到 FDE 的 Audit、Evals、Deployment 三阶段，并增加企业项目不可缺少的运营和产品化闭环。

| FDE 阶段 | 目标 | 主目录 | 关键问题 |
| --- | --- | --- | --- |
| Audit 审计 | 看清业务、组织、数据与约束 | 01 Foundation、02 Discovery | 问题是否真实、重要、可测？ |
| Evals 评估 | 形成方案并验证技术与业务假设 | 03 Solution-Design、04 AI-Delivery、08 Security-Compliance | 方案是否可行、可控、值得做？ |
| Deployment 部署 | 进入客户环境并稳定运行 | 05 Deployment、06 Integration | 能否安全上线并融入现有系统？ |
| Adoption 采纳 | 形成真实使用和业务结果 | 07 Operations、09 Industry | 用户是否持续使用并产生价值？ |
| Productization 产品化 | 把项目经验转成复用能力 | 10 Templates、11 Best-Practice | 哪些能力可标准化并复用？ |

## 2.1 七个 Stage Gate

| Gate | 必须回答 | 推荐 Skill | 过门证据 |
| --- | --- | --- | --- |
| G0 立项 | 谁决策、范围是什么、如何验收？ | Stakeholder-Mapping、SOW-Generator | 干系人图、SOW、升级路径 |
| G1 发现 | 问题、流程和基线是否清晰？ | Business-Interview、Process-Mapping、Consultative-Problem-Solving | 场景卡、As-Is、Issue Tree、基线 |
| G2 方案 | 主方案为何优于替代方案？ | PRD-Generator、FDE-PoC-Tech-Stack-Selector、API-Design-Review | PRD、TDR/ADR、接口契约、回退方案 |
| G3 评估 | 效果、风险和 ROI 是否达标？ | RAG-Evaluation、Tool-Audit、RBAC-Audit | Golden Dataset、评测报告、风险整改 |
| G4 生产 | 上线、监控、回滚和接管是否就绪？ | Private-Deployment-Gateway、Feishu-Integration | 部署架构、Runbook、联调记录、回滚预案 |
| G5 采纳 | 用户是否持续使用并产生价值？ | FDE-Adoption-Growth、Customer-Service-Bot、SQL-Dashboard-Brief | 采纳漏斗、业务看板、运营 SOP |
| G6 复用 | 本次经验如何进入产品和下一个项目？ | FDE-Customer-Product-Bridge、FDE-Full-Lifecycle、Templates | 复用组件、产品反馈、模板、复盘 |

> Gate 不是文档数量检查。只有当证据能支撑下一阶段决策时才算通过。

<div style="break-after: page;"></div>

# 三、11 类 Skill 的企业落地说明

## 3.1 01-Foundation：立项与交付基线

**何时使用**：新客户入场、项目范围不清、跨部门协作复杂、需要签署 PoC/SOW，或需要建立 FDE 个人能力基线时。

**典型输入**：组织架构、立项材料、预算周期、合规约束、历史争议、项目案例。

**典型输出**：干系人地图、SOW、里程碑、验收指标、沟通节奏、能力提升计划。

**完成标准**：决策人、业务 Owner、技术 Owner、范围外事项、变更机制和验收口径均已书面化。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [Stakeholder-Mapping](../01-Foundation/Stakeholder-Mapping/) | 决策链和阻力不清 | 干系人图、沟通频率、升级路径 | Business-Interview |
| [SOW-Generator](../01-Foundation/SOW-Generator/) | PoC 范围、周期、验收需固化 | SOW、里程碑、验收附件、变更流程 | SOW-Template |
| [FDE-Self-Assessment](../01-Foundation/FDE-Self-Assessment/) | 做职业或项目能力基线 | 四角色评分、短板、30/60/90 计划 | FDE-Growth-Roadmap |
| [FDE-Growth-Roadmap](../01-Foundation/FDE-Growth-Roadmap/) | 入行、求职、晋升或职业选择 | 能力差距、证据矩阵、成长实验 | Career-Job-Search |
| [Communication-Script-Library](../01-Foundation/Communication-Script-Library/) | 不同角色需要不同沟通口径 | 话术包、追问、禁忌词、消息模板 | Executive-Communication |

## 3.2 02-Discovery：需求发现与咨询式拆解

**何时使用**：客户只有模糊诉求、现状流程不可见、AI 价值点不清、期望不现实，或主系统改造阻力过大。

**典型输入**：客户需求、访谈纪要、SOP、失败样本、现有流程、组织背景、历史指标。

**典型输出**：场景卡、As-Is/To-Be、Issue Tree、验证假设、价值基线、沟通与协作机制。

**完成标准**：问题被定义为可证伪假设；明确目标用户、流程节点、输入输出、基线指标、AI 边界和人工兜底。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [Business-Interview](../02-Discovery/Business-Interview/) | 需要结构化访谈业务与一线用户 | 纪要、痛点、流程摘要、指标假设 | Process-Mapping |
| [Process-Mapping](../02-Discovery/Process-Mapping/) | 不知道 AI 插入哪个流程节点 | As-Is、AI 介入点、例外、耗时基线 | Consultative-Problem-Solving |
| [Consultative-Problem-Solving](../02-Discovery/Consultative-Problem-Solving/) | “建平台”等诉求过于宽泛 | Issue Tree、DIVE、PoC 假设、验证计划 | PRD-Generator |
| [FDE-Issue-Tree-Analysis](../02-Discovery/FDE-Issue-Tree-Analysis/) | RAG/Agent 失败原因复杂 | 多层问题树、Top 假设、证据与实验 | RAG-Evaluation / Tool-Audit |
| [Expectation-Management-Script](../02-Discovery/Expectation-Management-Script/) | 客户要求 100% 准确或全自动 | 边界话术、人审策略、迭代路线 | SOW-Generator |
| [Executive-Communication-Framework](../02-Discovery/Executive-Communication-Framework/) | 需要 5 分钟高层汇报和决策 | 一页纸、决策选项、ROI 简版 | SOW / Stage Gate |
| [AIBP-Collaboration-Playbook](../02-Discovery/AIBP-Collaboration-Playbook/) | FDE 与业务方职责不清 | 双签场景卡、RACI、周 Demo、升级路径 | PRD-Generator |
| [Sidecar-AI-Transformation](../02-Discovery/Sidecar-AI-Transformation/) | 主链路改造阻力大，想体外验证 | 适配判断、边界、接口、合并/终止条件 | Tech Stack Selector |

## 3.3 03-Solution-Design：方案规格与技术决策

**何时使用**：场景已收敛，需要把业务假设变成 PRD、技术栈、接口契约和 10 日 PoC 蓝图。

**典型输入**：场景卡、流程图、验收指标、数据与部署约束、现有 API、团队能力。

**典型输出**：PRD、用户故事、技术决策记录、分层技术栈、API 契约、降级方案、联调计划。

**完成标准**：存在唯一主方案、明确淘汰项、可执行计划和失败回退；所有“最新/支持/兼容”判断有当期证据。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [FDE-PoC-Tech-Stack-Selector](../03-Solution-Design/FDE-PoC-Tech-Stack-Selector/) | 两周内确定 PoC 技术路线 | 主/降级方案、证据表、架构、10 日计划 | RAG-Evaluation / Tool-Audit |
| [PRD-Generator](../03-Solution-Design/PRD-Generator/) | 场景卡需扩展为研发规格 | PRD、用户故事、验收标准、数据需求 | API-Design-Review |
| [API-Design-Review](../03-Solution-Design/API-Design-Review/) | 需要跨系统联调或动作执行 | 契约、风险、幂等/错误设计、联调计划 | Integration / Deployment |

> `FDE-PoC-Tech-Stack-Selector` 明确要求每次执行都联网检索。没有当期官方资料时，只能输出“待验证预选方案”，不能输出最终推荐。

## 3.4 04-AI-Delivery：AI 构建、评估与工具治理

**何时使用**：RAG/Agent 已有原型，需要建立 Golden Dataset、回归门禁，或审计 Agent/MCP 工具的 Schema、权限和失败模式。

**典型输入**：历史问题、失败样本、知识库、工具列表、API、权限模型、业务指标。

**典型输出**：评估集、指标矩阵、回归报告、工具风险分级、人工审批节点、整改计划。

**完成标准**：核心指标可重复测量；失败可归因；高风险动作受权限、确认、幂等、审计和回滚保护。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [RAG-Evaluation](../04-AI-Delivery/RAG-Evaluation/) | 知识库“感觉还行”但无法验收 | Golden Dataset、五层指标、回归门禁 | Private Deployment |
| [Tool-Audit](../04-AI-Delivery/Tool-Audit/) | Agent/MCP 能调用外部工具 | 工具审计、风险级别、人审节点、整改 | RBAC-Audit |

## 3.5 05-Deployment：私有化部署与模型网关

**何时使用**：客户要求数据不出域、内网隔离、信创兼容、统一模型路由，或需要从 PoC 进入生产。

**典型输入**：网络拓扑、国产化清单、部署约束、数据分级、SLA、容量与合规要求。

**典型输出**：部署架构、AI Gateway 配置、上线清单、监控与回滚、运维 Runbook。

**完成标准**：环境、密钥、日志、监控、回滚、灾备、责任边界和接管演练全部通过。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [Private-Deployment-Gateway](../05-Deployment/Private-Deployment-Gateway/) | 私有化、信创或多模型网关 | 部署架构、Gateway、上线清单、Runbook | Feishu / 业务系统集成 |

## 3.6 06-Integration：企业协同与系统集成

**何时使用**：AI 能力需要嵌入飞书消息、审批、多维表格或客户现有工作流，而不是停留在独立 Demo。

**典型输入**：应用权限、账号体系、业务流程、事件与 API、数据同步规则。

**典型输出**：集成方案、权限申请、联调记录、用户指引、失败重试与审计设计。

**完成标准**：身份映射、最小权限、幂等、错误处理、审计、消息触达和用户操作路径均验证。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [Feishu-Integration](../06-Integration/Feishu-Integration/) | 飞书消息/审批/多维表格接入 | 集成方案、权限清单、联调记录、指引 | FDE-Adoption-Growth |

## 3.7 07-Operations：运营采纳与价值持续化

**何时使用**：PoC 技术指标通过但使用率低，或需要把客服、看板、日报等能力变成持续运营机制。

**典型输入**：用户清单、使用日志、业务指标、知识库、工单、数据源、合同节点。

**典型输出**：采纳漏斗、Champion 机制、运营看板、客服 SOP、指标字典、培训与周复盘。

**完成标准**：有稳定活跃用户、明确业务结果、问题闭环、运营 Owner 和续约/扩展证据。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [Customer-Service-Bot](../07-Operations/Customer-Service-Bot/) | 客服问答、草稿、分流和人工升级 | Agent 方案、知识库、SOP、运营看板 | RAG-Evaluation |
| [FDE-Adoption-Growth](../07-Operations/FDE-Adoption-Growth/) | PoC 成功但没人持续使用 | 采纳计划、Champion、培训、成功看板 | Customer-Product Bridge |
| [SQL-Dashboard-Brief](../07-Operations/SQL-Dashboard-Brief/) | 需要经营或采纳指标看板 | 指标字典、SQL 逻辑、权限矩阵 | Executive Communication |

## 3.8 08-Security-Compliance：权限、安全与合规门禁

**何时使用**：涉及敏感数据、跨租户访问、Agent 工具执行、生产权限、审计日志或监管要求时。

**典型输入**：角色清单、数据分级、权限模型、日志、法规与内部控制要求。

**典型输出**：RBAC 矩阵、风险分级、审计报告、整改项、合规对照。

**完成标准**：默认拒绝、最小权限、职责分离、可追溯、定期复核和异常撤权机制齐备。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [RBAC-Audit](../08-Security-Compliance/RBAC-Audit/) | 上生产前需要权限和日志审计 | RBAC 报告、权限矩阵、整改、合规对照 | Deployment Gate |

## 3.9 09-Industry：行业场景样例

**何时使用**：需要用一个完整行业样例理解数据源、预警、推送、责任人和运营 SOP 如何组合。

**典型输入**：行业数据源、预警规则、推送渠道、运营责任人。

**典型输出**：日报、Agent 配置、预警规则、运营 SOP。

| Skill | 典型触发 | 核心产出 | 推荐后续 |
| --- | --- | --- | --- |
| [AI-Operations-Daily](../09-Industry/AI-Operations-Daily/) | 跨境/品牌运营日报与异常复盘 | 日报模板、预警规则、推送与 SOP | SQL-Dashboard-Brief |

> 行业目录应保持精简。新行业需求优先复用通用 Skill，再把行业差异沉淀为样例、数据字典或 Reference。

## 3.10 10-Templates：标准交付模板

**何时使用**：需要把已完成的分析快速装配成客户可签署、可评审或可持续更新的交付物。

| 资产 | 用途 | 注意事项 |
| --- | --- | --- |
| [SOW-Template](../10-Templates/SOW-Template/) | 填写标准 SOW、验收和变更条款 | 应由 SOW-Generator 的分析结果驱动 |
| [Career-Job-Search](../10-Templates/Career-Job-Search/) | JD 证据矩阵、求职漏斗、案例卡、作品集 | 补充模板包，不计入 31 个核心 Skill |

## 3.11 11-Best-Practice：方法论总控与复用闭环

**何时使用**：需要全流程总控、售前诊断、国内方法论、本土化对照，或把现场问题反馈给产品和研发。

| Skill | 典型触发 | 核心产出 | 推荐组合 |
| --- | --- | --- | --- |
| [Palantir-FDE-Pattern](../11-Best-Practice/Palantir-FDE-Pattern/) | 需要理解国际 FDE 模式及本土化边界 | 对照、可借鉴/不适用清单 | China-FDE Pattern |
| [China-FDE-Consulting-Pattern](../11-Best-Practice/China-FDE-Consulting-Pattern/) | 需要国内咨询式交付总纲 | 五环打法、会议地图、资产化清单 | Discovery 全套 |
| [FDE-Full-Lifecycle](../11-Best-Practice/FDE-Full-Lifecycle/) | 从 Audit 到 Deployment 全程总控 | 审计、方案、ROI、部署、抽象建议 | 作为总控 Skill |
| [Diagnostic-FDE](../11-Best-Practice/Diagnostic-FDE/) | ToB 售前需形成完整方案包 | 行业、诊断、架构、ROI、PoC 方案 | MECE / PPT Reference |
| [FDE-Customer-Product-Bridge](../11-Best-Practice/FDE-Customer-Product-Bridge/) | 客户需求需转成产品/研发输入 | 结构化需求、待验证问题、行动表 | Adoption / Product |

<div style="break-after: page;"></div>

# 四、如何在当前仓库中使用 Skill

## 4.1 先识别两种核心形态

当前仓库的 31 个核心 Skill 并非全部采用相同文件结构。

### 形态 A：Agent 原生 Skill

以下 8 个核心目录包含 `SKILL.md`，可被支持 Skill 发现机制的 Agent 读取：

1. `FDE-Growth-Roadmap`
2. `FDE-Self-Assessment`
3. `FDE-Issue-Tree-Analysis`
4. `Sidecar-AI-Transformation`
5. `FDE-PoC-Tech-Stack-Selector`
6. `FDE-Full-Lifecycle`
7. `Diagnostic-FDE`
8. `FDE-Customer-Product-Bridge`

使用方式：

```text
请使用 fde-poc-tech-stack-selector Skill。
项目背景：……
Primary Metric：……
周期/预算/团队：……
数据敏感级别与是否可出域：……
必须集成的系统：……
请输出唯一主方案、降级方案、淘汰项、10 日计划和 Go/No-Go。
```

注意：目录中存在 `SKILL.md` 不代表所有运行时都会自动注册。是否可直接按名称调用，取决于 Agent 客户端的 Skill 搜索路径和安装配置。不能自动发现时，使用下面的“显式路径模式”。

### 形态 B：四件套能力包

大多数核心目录采用：

```text
README.md       场景、方法论、输入输出、执行步骤
prompt.md       分阶段可复制 Prompt
checklist.md    准备、执行、验收、复盘检查项
evaluation.md   指标、门槛、失败处理与验收样例
workflow.md     少数关键 Skill 的标准流程（可选）
```

推荐顺序：

1. 先读 `README.md`，确认适用与不适用边界；
2. 从 `prompt.md` 选择与当前阶段匹配的 Prompt，不必一次运行全部；
3. 用真实项目上下文替换占位信息；
4. 按 `checklist.md` 执行并保留证据；
5. 用 `evaluation.md` 做自评或阶段评审；
6. 未达到门槛时回到输入、假设或方案层修正，不用润色掩盖证据缺口。

显式路径提示模板：

```text
请按本仓库 `02-Discovery/Business-Interview/` 能力包执行。

执行要求：
1. 先读取 README.md，确认适用边界；
2. 使用 prompt.md 中与“首次业务访谈”匹配的段落；
3. 将 checklist.md 作为过程门禁；
4. 用 evaluation.md 判断是否可进入流程建模；
5. 输出访谈纪要、痛点清单、流程摘要、指标假设和待确认问题。

客户背景：……
访谈对象：……
已知目标：……
约束与敏感信息：……
```

## 4.2 外部镜像 Skill 的定位

仓库 [`.agents/skills/`](../.agents/skills/) 中的 19 个 Skill 是工程和行业补充能力，并通过 [`skills-lock.json`](../skills-lock.json) 记录来源与哈希。

推荐把它们作为本地核心 Skill 的“实现增强”，不要替代主交付链：

| 核心能力 | 可组合的外部 Skill |
| --- | --- |
| RAG-Evaluation | `langchain-rag`、`rag-architect`、`rag-implementation` |
| Tool-Audit | `mcp-builder`、`mcp-apps-builder` |
| Private-Deployment-Gateway | `deployment-engineer`、`deployment-pipeline-design` |
| RBAC-Audit | `security-review`、`security-requirement-extraction` |
| Customer-Service-Bot | `cs-sop`、`tiktok-shop-customer-service` |
| FDE-Adoption-Growth | `designing-growth-loops`、`saas-revenue-growth-metrics` |
| SQL-Dashboard-Brief | `enterprise-user-management-ai-analytics` |
| Consultative-Problem-Solving | `enterprise-sales` |

组合规则：

- 本地核心 Skill 决定业务问题、交付物和验收门槛；
- 外部 Skill 提供实现细节、工程模式或行业参考；
- 对外部 Skill 的版本、许可、数据流和安全边界重新核验；
- 不因外部 Skill 已锁定哈希就假定其适合当前客户环境。

## 4.3 咨询 Reference 的定位

[`11-Best-Practice/references/`](../11-Best-Practice/references/) 下 6 个 Reference 不计入 31 个核心 Skill：

| Reference | 适合增强 |
| --- | --- |
| MECE | 问题树、金字塔表达、结构化结论 |
| McKinsey-Frameworks | 战略、组织、市场和经营框架选择 |
| McKinsey-Report | 行研和高层报告故事线 |
| McKinsey-PPT-Design | 麦肯锡风格 PPT 版式 |
| Elite-PPT-Pro | 多咨询风 PPT 双输出 |
| GE-Matrix-Analysis | 业务组合与优先级分析 |

Reference 只增强表达或分析框架，不能代替客户证据、技术验证和阶段验收。

# 五、六套典型企业落地组合

## 5.1 新客户 AI PoC：从模糊需求到生产

```text
Stakeholder-Mapping
→ Business-Interview
→ Process-Mapping
→ Consultative-Problem-Solving
→ SOW-Generator
→ PRD-Generator
→ FDE-PoC-Tech-Stack-Selector
→ RAG-Evaluation / Tool-Audit
→ RBAC-Audit
→ Private-Deployment-Gateway
→ Feishu-Integration
→ FDE-Adoption-Growth
→ FDE-Customer-Product-Bridge
```

主控建议：用 `FDE-Full-Lifecycle` 管理 Audit、Evals、Deployment，总链路中的各专项 Skill 负责具体交付物。

## 5.2 RAG / 企业知识库效果治理

```text
Business-Interview
→ Process-Mapping
→ FDE-Issue-Tree-Analysis
→ FDE-PoC-Tech-Stack-Selector
→ RAG-Evaluation
→ Private-Deployment-Gateway
→ FDE-Adoption-Growth
```

关键门禁：

- 先定义业务问题和“正确答案”；
- 先做小规模 Golden Dataset，再扩文档规模；
- 把解析、召回、重排、生成、引用和业务采纳分层评估；
- 上线前固定回归集、版本、日志和人工反馈入口。

## 5.3 Agent / MCP 工具型项目

```text
Consultative-Problem-Solving
→ PRD-Generator
→ API-Design-Review
→ FDE-PoC-Tech-Stack-Selector
→ Tool-Audit
→ RBAC-Audit
→ Deployment / Integration
```

关键门禁：

- 能用确定性工作流解决时，不使用多 Agent；
- 高风险动作必须有最小权限、显式确认、幂等、审计和回滚；
- 工具描述、参数 Schema、错误信息和超时必须可测试；
- 人工审批点应与风险等级匹配。

## 5.4 信创、内网或数据不出域

```text
Stakeholder-Mapping
→ Business-Interview
→ RBAC-Audit（前置）
→ FDE-PoC-Tech-Stack-Selector
→ Private-Deployment-Gateway
→ API-Design-Review
→ Feishu / 内部系统集成
→ 上线演练
```

关键门禁：不要把“私有化”简化为模型落在内网。还要覆盖身份、网络、密钥、日志、供应链、模型路由、容量、灾备、升级和运维接管。

## 5.5 主链路阻力大：Sidecar 体外验证

```text
Stakeholder-Mapping
→ Process-Mapping
→ Sidecar-AI-Transformation
→ AIBP-Collaboration-Playbook
→ FDE-PoC-Tech-Stack-Selector
→ 快速 PoC
→ Adoption Growth
→ 合并主链路 / 长期 Sidecar / 终止决策
```

Sidecar 不是绕开治理。必须预先定义数据同步、权限审计、失败回退，以及何时合并、保留或终止。

## 5.6 PoC 成功但没人用

```text
FDE-Adoption-Growth
→ Business-Interview（复访）
→ Process-Mapping（核对真实工作流）
→ Expectation-Management-Script
→ SQL-Dashboard-Brief
→ Executive-Communication-Framework
→ FDE-Customer-Product-Bridge
```

优先排查：

1. 用户是否在目标流程中真的需要该能力；
2. 使用成本是否高于原流程；
3. 输出是否可信、可解释并可继续行动；
4. 是否有 Champion、培训、反馈入口和运营 Owner；
5. 指标是否只测调用量，没有测任务成功和业务结果。

<div style="break-after: page;"></div>

# 六、角色使用指南

| 角色 | 首选入口 | 应承担的关键责任 |
| --- | --- | --- |
| FDE / 交付负责人 | FDE-Full-Lifecycle | 阶段总控、技术业务翻译、结果与复用 |
| AIBP / 业务 Owner | AIBP-Collaboration-Playbook | 业务真实性、优先级、用户与验收 |
| AI 工程师 | Tech Stack Selector、RAG-Evaluation、Tool-Audit | 可测原型、失败归因、工程质量 |
| 架构 / IT | API-Design-Review、Private Deployment | 集成、身份、网络、运维与接管 |
| 安全 / 合规 | RBAC-Audit、Tool-Audit | 数据、权限、审计和整改门禁 |
| 产品经理 | PRD-Generator、Customer-Product Bridge | 规格、需求抽象、路线反馈 |
| 客户成功 / 运营 | Adoption Growth、SQL Dashboard | 采纳、培训、反馈和价值持续化 |
| 高管 Sponsor | Executive Communication | 资源、优先级、阶段决策和冲突升级 |

# 七、标准执行模板

## 7.1 单次 Skill 任务卡

```text
任务名称：
主 Skill：
辅助 Skill：
当前 Stage Gate：

业务背景：
目标用户与流程节点：
当前问题与证据：
Primary Metric / 基线 / 目标值：
数据与权限条件：
部署和集成约束：
周期、预算、团队：
明确不做：

要求产出：
1.
2.
3.

验收方式：
失败时回退到：
Owner / 截止时间：
```

## 7.2 输出质量自检

- [ ] 是否清楚区分事实、假设、建议和待验证项？
- [ ] 是否说明输入数据的来源、时点和限制？
- [ ] 是否有唯一主方案和明确淘汰理由？
- [ ] 是否定义业务指标、技术指标和基线？
- [ ] 是否包含人工兜底、失败处理和回滚？
- [ ] 是否完成权限、隐私、合规和供应链检查？
- [ ] 是否给出 Owner、时间表和下一 Gate？
- [ ] 是否记录可复用资产和产品反馈？

# 八、仓库导航与实操

## 8.1 查找能力

```bash
cd /Users/admin/Documents/Github/fde-skills

# 查看全量分类与 31 个核心 Skill
open INDEX.md

# 搜索某类交付关键词
rg -n "Golden Dataset|私有化|RBAC|采纳" .

# 查看所有 Agent 原生 Skill
find . -name SKILL.md -not -path "./.git/*" | sort
```

## 8.2 阅读一个能力包

以 `RAG-Evaluation` 为例：

```bash
cd /Users/admin/Documents/Github/fde-skills/04-AI-Delivery/RAG-Evaluation
open README.md
open prompt.md
open checklist.md
open evaluation.md
```

## 8.3 使用全流程脚本

`FDE-Full-Lifecycle` 包含客户审计脚本：

```bash
cd /Users/admin/Documents/Github/fde-skills/11-Best-Practice/FDE-Full-Lifecycle
python3 scripts/client_audit.py --help
```

运行脚本前先检查参数，并使用新的输出路径，避免覆盖已有报告。客户数据应先脱敏，并遵守客户授权和本组织安全规范。

## 8.4 维护和新增 Skill

新增或升级能力时参考：

- [`SKILL-TEMPLATE.md`](../SKILL-TEMPLATE.md)：标准内容模板；
- [`CONTRIBUTING.md`](../CONTRIBUTING.md)：目录归类和贡献规范；
- [`_catalog/fde-skill-map.md`](../_catalog/fde-skill-map.md)：主/次分类映射；
- [`_catalog/backlog.md`](../_catalog/backlog.md)：待补能力；
- [`skills-lock.json`](../skills-lock.json)：外部 Skill 来源与完整性。

# 九、治理建议与当前注意事项

## 9.1 “usable” 不等于“validated”

当前索引把 31 个核心 Skill 标为 `usable`，表示内容结构可用于交付；它不自动代表已经在特定行业、规模或监管环境中现场验证。建议项目复盘后记录：

- 客户类型与约束；
- 使用了哪些步骤；
- 哪些产出被采用；
- 指标是否达到；
- 哪些内容失效；
- 是否应升级成熟度。

## 9.2 自动发现覆盖仍需补齐

当前 31 个核心 Skill 中有 8 个包含 `SKILL.md`。其余目录虽已有完整四件套，但对依赖标准 Skill 发现机制的 Agent 来说，需要显式提供路径。后续可按优先级补齐：

1. 高频主链路：Business-Interview、Process-Mapping、PRD-Generator；
2. 生产门禁：RAG-Evaluation、Tool-Audit、Private-Deployment-Gateway、RBAC-Audit；
3. 采纳闭环：FDE-Adoption-Growth；
4. 其余支撑能力。

## 9.3 技术选型必须保持时效性

模型、框架、许可证、云服务数据政策、国产算力兼容性变化很快。凡是涉及“最新、支持、兼容、可私有化、生产级”的结论，应在执行当天核对官方文档、Release 和许可。

## 9.4 企业数据与高风险动作

- 不把客户密钥、生产配置、个人信息和受监管数据发送到未批准服务；
- 原型优先使用脱敏、合成或最小必要数据；
- 高风险写操作、批量操作、外部消息和权限变更保留人工确认；
- 对脚本和生成代码做人工审查、依赖锁定、测试和回滚设计；
- 对客户交付结论保留证据链和决策记录。

# 十、PDF 导出说明

本 Markdown 采用适合 PDF 的结构：YAML 元数据、三级目录、短段落、分组表格和显式分页标记。推荐以下方式导出。

## 10.1 直接打印 HTML 版本

打开同目录的 `fde-enterprise-skill-guide.html`，在浏览器中选择：

```text
打印 → 另存为 PDF → A4 → 背景图形开启 → 页边距默认
```

这是视觉效果最稳定的方式。

## 10.2 使用 Pandoc + XeLaTeX

```bash
cd /Users/admin/Documents/Github/fde-skills
pandoc docs/fde-enterprise-skill-guide.md \
  --from=gfm+raw_html \
  --toc \
  --number-sections \
  --pdf-engine=xelatex \
  -V CJKmainfont="PingFang SC" \
  -V geometry:margin=20mm \
  -o docs/fde-enterprise-skill-guide.pdf
```

如果系统没有 `PingFang SC`，可替换为 `Noto Sans CJK SC`、`Source Han Sans SC` 或系统已安装的中文字体。

## 10.3 Typora / VS Code

- Typora：打开 Markdown，选择“文件 → 导出 → PDF”；
- VS Code：使用支持 Chromium 打印的 Markdown PDF 扩展；
- 导出前检查目录、中文字体、表格换行和分页位置。

# 附录 A：仓库资产口径

| 资产类型 | 数量 | 说明 |
| --- | ---: | --- |
| 核心 Skill | 31 | `INDEX.md` 纳入统计，成熟度为 usable |
| 交付分类 | 11 | 01 Foundation 至 11 Best-Practice |
| 核心 `SKILL.md` | 8 | 当前工作树实盘结果 |
| 咨询 Reference | 6 | 不计入核心 Skill |
| 外部镜像 Skill | 19 | 位于 `.agents/skills/`，由锁文件记录来源 |
| 补充模板包 | 1 | `10-Templates/Career-Job-Search` |

# 附录 B：最短选用指南

| 你现在遇到的问题 | 从这里开始 |
| --- | --- |
| 新客户入场，不清楚谁说了算 | Stakeholder-Mapping |
| 客户只说“要做智能体平台” | Consultative-Problem-Solving |
| 不知道真实流程和 AI 介入点 | Business-Interview → Process-Mapping |
| RAG/Agent 问题复杂，无法定位 | FDE-Issue-Tree-Analysis |
| 主链路改造阻力大 | Sidecar-AI-Transformation |
| PoC 不知道选什么栈 | FDE-PoC-Tech-Stack-Selector |
| RAG 效果无法量化 | RAG-Evaluation |
| Agent 工具权限和风险不清 | Tool-Audit → RBAC-Audit |
| 客户要求信创或数据不出域 | Private-Deployment-Gateway |
| AI 能力需要进入飞书 | Feishu-Integration |
| PoC 成功但没有持续使用 | FDE-Adoption-Growth |
| 需要一套完整售前方案 | Diagnostic-FDE |
| 需要从现场反馈到产品研发 | FDE-Customer-Product-Bridge |
| 需要全流程总控 | FDE-Full-Lifecycle |

---

**文档维护建议**：当 `INDEX.md`、目录数量、`SKILL.md` 覆盖或 Skill 成熟度变化时，同步更新本文的资产口径、分类表和调用说明。
