# Business-Interview

- **分类**：`02-Discovery`
- **成熟度**：`usable`
- **一句话**：结构化业务访谈与需求澄清

---

## 适用场景

- 项目初期需求挖掘
- 场景评审前
- PoC 失败后重访
- 扩展新场景前


## 问题定义

客户表述多为解决方案而非问题，FDE 若直接接需求将建错系统。


## 方法论框架

**访谈结构**：背景 → 痛点 → 现有流程 → 成功标准 → 约束 → 样本。
**技巧**：5 Why、流程走查、异常场景追问、价值量化。


## 输入 / 输出

### 输入

- 访谈对象与角色
- 访谈提纲
- 保密协议状态

### 输出

- 访谈纪要
- 痛点清单
- 流程摘要
- 初步指标假设


## 执行步骤

1. 准备提纲与样本请求
2. 执行 45-60min 访谈
3. 当天发纪要确认
4. 提炼痛点与指标
5. 输入问题树/DIVE


## 常见误区

- ❌ 只问功能不问流程
- ❌ 未索要真实样本
- ❌ 纪要未书面确认


## 交付物清单

- [ ] 访谈纪要
- [ ] 痛点优先级
- [ ] 样本清单


## 与国内 FDE 生态关联

Discovery 入口；输出喂给 Consultative-Problem-Solving 和 PRD-Generator。


## 阶段门控

| 阶段 | 进入条件 | 退出标准 |
| --- | --- | --- |
| PoC 准备 | 干系人识别、场景卡草稿、数据/权限前置条件确认 | 范围与验收指标书面确认 |
| PoC/Beta 执行 | 方法论对齐、AIBP 双签场景卡 | 核心交付物初稿 + 周度 Demo ≥1 次 |
| 生产门禁 | RBAC/评估/人审/日志检查通过 | evaluation.md 指标 ≥80% |
| 复盘资产化 | 阶段结束或里程碑完成 | 可复用模板/评估集沉淀至 `10-Templates` 或 `_catalog` |


## 协作接口

| 角色 | 本 Skill 中的职责 | 交接物 |
| --- | --- | --- |
| FDE | 主导本 Skill 执行与交付 | 过程文档 + 验收材料 |
| AIBP | 提供业务口径、Ground Truth、验收反馈 | 场景卡 / 样本 / 指标定义 |
| 业务 Owner | 决策优先级与范围 | 签字确认的范围与验收 |
| IT/安全 | 评审权限、部署、信创/等保边界 | 评审意见与整改清单 |


## 关联 Skill

### 推荐组合

- [Consultative-Problem-Solving](../Consultative-Problem-Solving/README.md) — 访谈输出喂给问题树
- [Process-Mapping](../Process-Mapping/README.md) — 流程走查深化
- [PRD-Generator](../../03-Solution-Design/PRD-Generator/README.md) — 需求规格化

### 外部工程参考

- `.agents/skills/growth-user-interview`


## 场景深潜

### 场景 1：项目初期需求挖掘

**触发信号**：PoC/Beta/生产任一阶段出现「项目初期需求挖掘」相关诉求、阻塞或复盘需求。

**关键动作**：准备提纲与样本请求

**FDE 注意**：避免 只问功能不问流程

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：场景评审前

**触发信号**：PoC/Beta/生产任一阶段出现「场景评审前」相关诉求、阻塞或复盘需求。

**关键动作**：执行 45-60min 访谈

**FDE 注意**：避免 未索要真实样本

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：PoC 失败后重访

**触发信号**：PoC/Beta/生产任一阶段出现「PoC 失败后重访」相关诉求、阻塞或复盘需求。

**关键动作**：当天发纪要确认

**FDE 注意**：避免 纪要未书面确认

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：扩展新场景前

**触发信号**：PoC/Beta/生产任一阶段出现「扩展新场景前」相关诉求、阻塞或复盘需求。

**关键动作**：提炼痛点与指标

**FDE 注意**：避免 只问功能不问流程

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。



## 术语表

| 术语 | 含义 |
| --- | --- |
| FDE | Forward Deployed Engineer，嵌入客户现场的技术交付角色 |
| AIBP | AI Business Partner，业务效果与 Ground Truth 负责人 |
| PoC | Proof of Concept，验证核心假设的最小可运行版本 |
| Beta | 小范围试点，验证采纳与流程嵌入 |
| 信创 | 信息技术应用创新，国产化软硬件与合规要求 |
| EDD | Evaluation Driven Development，评估驱动开发 |
| Ground Truth | 业务真值样本，用于评估与验收 |
| 场景卡 | FDE 与 AIBP 对场景范围、指标、边界的共同协议 |
| 周度 Demo | 按周演示进展、收集反馈的项目节奏控制器 |
| 上线门禁 | 生产发布前对权限、评估、人审、日志的检查关卡 |


## 常见问题 FAQ

**Q1：执行【Business-Interview】时如何避免「只问功能不问流程」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：制造业质检场景。

**应用本 Skill 前**：客户要求「上视觉 AI 平台」。

**应用本 Skill 后**：
1. 按【Business-Interview】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：PoC 范围收敛到单产线 AOI 辅助。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

