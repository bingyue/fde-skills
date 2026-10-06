# Process-Mapping

- **分类**：`02-Discovery`
- **成熟度**：`usable`
- **一句话**：业务现状流程梳理与 AI 介入点标注

---

## 适用场景

- 场景评审
- PoC 范围界定
- 采纳率低时复盘
- 扩展自动化前


## 问题定义

不清楚真实流程和例外处理，AI 只能覆盖理想路径，一线不采纳。


## 方法论框架

**输出**：As-Is 流程图 + 痛点标注 + AI 介入点 + 不可自动化清单。
**方法**：现场跟岗、泳道图、异常分支、耗时/错误率标注。


## 输入 / 输出

### 输入

- 访谈纪要
- SOP 文档
- 一线配合安排

### 输出

- As-Is 流程图
- AI 介入点图
- 例外处理清单
- 耗时基线


## 执行步骤

1. 选端到端流程片段
2. 跟岗或工作坊
3. 画泳道图
4. 标介入点与边界
5. 业务确认
6. 转入场景卡


## 常见误区

- ❌ 只画主路径忽略异常
- ❌ 未标人工复核点
- ❌ 一线未参与确认


## 交付物清单

- [ ] 流程图
- [ ] 介入点图
- [ ] 确认纪要


## 与国内 FDE 生态关联

场景卡必填输入；场景评审会议核心材料。


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

- [Business-Interview](../Business-Interview/README.md) — 流程访谈输入
- [Consultative-Problem-Solving](../Consultative-Problem-Solving/README.md) — AI 介入点验证
- [PRD-Generator](../../03-Solution-Design/PRD-Generator/README.md) — 流程写入 PRD


## 场景深潜

### 场景 1：场景评审

**触发信号**：PoC/Beta/生产任一阶段出现「场景评审」相关诉求、阻塞或复盘需求。

**关键动作**：选端到端流程片段

**FDE 注意**：避免 只画主路径忽略异常

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：PoC 范围界定

**触发信号**：PoC/Beta/生产任一阶段出现「PoC 范围界定」相关诉求、阻塞或复盘需求。

**关键动作**：跟岗或工作坊

**FDE 注意**：避免 未标人工复核点

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：采纳率低时复盘

**触发信号**：PoC/Beta/生产任一阶段出现「采纳率低时复盘」相关诉求、阻塞或复盘需求。

**关键动作**：画泳道图

**FDE 注意**：避免 一线未参与确认

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：扩展自动化前

**触发信号**：PoC/Beta/生产任一阶段出现「扩展自动化前」相关诉求、阻塞或复盘需求。

**关键动作**：标介入点与边界

**FDE 注意**：避免 只画主路径忽略异常

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

**Q1：执行【Process-Mapping】时如何避免「只画主路径忽略异常」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：财务报销自动化。

**应用本 Skill 前**：只画主路径，忽略退单/补件分支。

**应用本 Skill 后**：
1. 按【Process-Mapping】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：Beta 采纳率从 12% 提升到 58%。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

