# FDE-Skills

面向**国内 FDE（Forward Deployed Engineer）企业交付**的可复用能力库。

> Skill 是可复用的交付能力单元（Capability），不是 Prompt 碎片，也不是工具清单。  
> 一个优秀的 FDE，靠的不是记住多少 Prompt，而是积累一套能快速解决企业问题的 Skill 库。

**仓库地址**：[github.com/bingyue/fde-skills](https://github.com/bingyue/fde-skills)

---

## 这是什么

FDE-Skills 把 FDE 在企业现场的高频交付动作，沉淀为**可直接复用**的标准化能力包。每个 Skill 包含场景定义、方法论、执行步骤、Prompt、检查清单与验收指标，覆盖从立项到采纳的完整链路。

**适用人群**

- 转型 FDE / Applied AI 的工程师、咨询顾问、产品经理
- 在企业内推进 AI PoC → Beta → 生产的交付团队
- 需要把一次项目经验变成可复用资产的方法论实践者

---

## 核心理念

| 原则 | 说明 |
| --- | --- |
| 按交付场景分类 | 不按工具（Dify/Coze）或业务系统（CRM/ERP）碎片化 |
| 可交付、可评估 | 每个 Skill 有明确输入、输出、验收指标与失败处理 |
| 国内 FDE 主线 | 咨询式拆解 → 方案设计 → AI 交付 → 私有化部署 → 运营采纳 → 资产化 |
| 先本地化再引用 | 外部 Skill（skills.sh）下载到 `.agents/skills/` 后映射，不只贴链接 |

---

## 目录体系（11 + `_catalog`）

```text
01-Foundation          立项、干系人、SOW、自评、成长、话术
02-Discovery           访谈、流程、咨询式拆解、问题树诊断、预期管理、高层沟通、AIBP 协作、体外创新
03-Solution-Design     PRD、API 设计评审
04-AI-Delivery         RAG 评估、Agent 工具审计
05-Deployment          私有化网关、三层 PoC 路径
06-Integration         飞书等企业协同集成
07-Operations          客服 Bot、采纳增长、经营看板
08-Security-Compliance RBAC、合规审计
09-Industry            高价值行业示例（精简）
10-Templates           SOW 等交付模板
11-Best-Practice       方法论总纲、全流程、诊断型售前、客户-产品-研发桥接
  └─ references/       咨询/PPT 外部 Reference（MECE、麦肯锡系列等，不计入核心 Skill）
_catalog               索引、映射、外部导入编目
```

当前共 **30 个核心 Skill**，成熟度 `usable`。完整列表见 [`INDEX.md`](./INDEX.md)。

---

## 快速开始

### 1. 按交付阶段选用 Skill

```text
立项 → 01-Foundation（Stakeholder-Mapping, SOW-Generator）
发现 → 02-Discovery（Consultative-Problem-Solving, FDE-Issue-Tree-Analysis, Sidecar-AI-Transformation）
方案 → 03-Solution-Design（PRD-Generator, API-Design-Review）
AI   → 04-AI-Delivery（RAG-Evaluation, Tool-Audit）
部署 → 05-Deployment（Private-Deployment-Gateway）
运营 → 07-Operations（FDE-Adoption-Growth, Customer-Service-Bot）
```

### 2. 使用单个 Skill

进入对应目录，按顺序阅读：

1. `README.md` — 场景、方法论、步骤、误区、交付物
2. `prompt.md` — 分阶段 Prompt（可直接复制到 Agent）
3. `checklist.md` — 准备 / 执行 / 验收 / 复盘
4. `evaluation.md` — 指标矩阵与验收门槛
5. `workflow.md` — 部分关键 Skill 提供（如 DIVE、AIBP、私有化部署）

### 3. 国内 FDE 推荐入口

| 你想解决什么 | 从这里开始 |
| --- | --- |
| 不知道自己适不适合做 FDE | `01-Foundation/FDE-Self-Assessment` |
| 客户说「我要做智能体平台」 | `02-Discovery/Consultative-Problem-Solving` |
| AI 知识库 / Agent 效果问题复杂 | `02-Discovery/FDE-Issue-Tree-Analysis` |
| 主链路阻力大，想先体外验证 AI 价值 | `02-Discovery/Sidecar-AI-Transformation` |
| 客户期望 100% 自动化 | `02-Discovery/Expectation-Management-Script` |
| 向老板汇报 PoC 进展 | `02-Discovery/Executive-Communication-Framework` |
| FDE 与业务方分工不清 | `02-Discovery/AIBP-Collaboration-Playbook` |
| 信创/私有化部署 | `05-Deployment/Private-Deployment-Gateway` |
| PoC 成功但没人用 | `07-Operations/FDE-Adoption-Growth` |
| 理解国内 FDE 交付总纲 | `11-Best-Practice/China-FDE-Consulting-Pattern` |
| FDE 三阶段全流程（Audit/Evals/Deploy） | `11-Best-Practice/FDE-Full-Lifecycle` |
| ToB 售前完整方案包 | `11-Best-Practice/Diagnostic-FDE` |
| 客户现场转产品/研发 | `11-Best-Practice/FDE-Customer-Product-Bridge` |
| 结构化输出 / MECE | `11-Best-Practice/references/MECE` + `Consultative-Problem-Solving` |
| 麦肯锡风报告 / PPT | `11-Best-Practice/references/McKinsey-Report` → `McKinsey-PPT-Design` |

---

## Skill 标准结构

```text
<category>/<skill-name>/
├── README.md       # 150+ 行：场景、方法论、步骤、误区、交付物
├── prompt.md       # 分阶段多段 Prompt
├── checklist.md    # 准备 / 执行 / 验收 / 复盘
├── evaluation.md   # 指标、门槛、验收样例
├── workflow.md     # 关键 Skill 可选
└── assets/         # 模板样例（逐步补充）
```

**成熟度**：`draft` → `usable` → `validated`（需现场项目验证后升级）

---

## 外部 Skill 导入

来自 [skills.sh](https://skills.sh) 的候选 Skill 已下载到 `.agents/skills/`（19 个），并映射到本库分类。

咨询/PPT 类 Reference（6 个）落地于 `11-Best-Practice/references/`，与核心 Skill 组合使用。

- 工程类导入明细：[`_catalog/external-skills-imported.md`](./_catalog/external-skills-imported.md)
- 咨询 Reference 编目：[`_catalog/consulting-references.md`](./_catalog/consulting-references.md)
- 新增外部 Skill：先 `npx skills add <repo>@<skill>`，再登记编目

---

## 文档导航

| 文档 | 说明 |
| --- | --- |
| [`INDEX.md`](./INDEX.md) | 全量 Skill 索引与交付链路 |
| [`SOURCES.md`](./SOURCES.md) | 内容来源与引用规范 |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | 贡献指南与目录归类规则 |
| [`SKILL-TEMPLATE.md`](./SKILL-TEMPLATE.md) | 新建 Skill 模板 |
| [`_catalog/`](./_catalog/) | 映射表、待办、扩充脚本 |

---

## 版本记录

**v0.2.0（2026-07-12）**

- 目录从 17 个精简为 11 个交付目录 + `_catalog`
- 25 个 Skill 从骨架扩充为可交付内容
- 新增国内 FDE 主题：自评、成长路线、沟通话术、咨询式拆解、预期管理、AIBP 协作、采纳增长
- 外部 Skill 本地化导入 19 个

**v0.1.0（2026-07-11）**

- 初始化仓库与首批交付能力骨架

---

## License

MIT（待补充 LICENSE 文件）
