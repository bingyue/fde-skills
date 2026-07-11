# FDE-Growth-Roadmap

- **分类**：`01-Foundation`
- **成熟度**：`usable`
- **一句话**：将 FDE 成长路径与可验证交付物绑定

---

## 适用场景

- 新人 onboarding
- 季度成长复盘
- 晋升/转岗作品集规划
- 团队梯队建设


## 问题定义

学习与交付脱节，成长缺少可展示的作品集和里程碑交付物。


## 方法论框架

**三阶段成长**：Explorer（能跟项目）→ Builder（能主导 PoC）→ Owner（能复制打法）。
**绑定原则**：每个成长目标必须对应 1 份交付物（场景卡、评估集、Demo 录像、复盘报告）。


## 输入 / 输出

### 输入

- 当前 L 级自评
- 目标岗位 JD
- 可用项目机会

### 输出

- 成长路线图
- 季度里程碑
- 作品集清单
- 导师辅导计划


## 执行步骤

1. 明确目标角色画像
2. 盘点差距
3. 选 2-3 个里程碑项目
4. 定义每阶段交付物
5. 排期与导师机制
6. 季度复盘更新


## 常见误区

- ❌ 路线图只有课程没有项目
- ❌ 作品集缺验收指标
- ❌ 忽略软技能成长


## 交付物清单

- [ ] 成长路线图
- [ ] 作品集结构
- [ ] 季度 OKR


## 与国内 FDE 生态关联

连接自评与作品集；绑定商业化交付能力的个人成长路径。


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

- [FDE-Self-Assessment](../FDE-Self-Assessment/README.md) — 能力基线输入
- [Communication-Script-Library](../Communication-Script-Library/README.md) — 软技能成长路径
- [China-FDE-Consulting-Pattern](../../11-Best-Practice/China-FDE-Consulting-Pattern/README.md) — 交付阶段对照


## 场景深潜

### 场景 1：新人 onboarding

**触发信号**：PoC/Beta/生产任一阶段出现「新人 onboarding」相关诉求、阻塞或复盘需求。

**关键动作**：明确目标角色画像

**FDE 注意**：避免 路线图只有课程没有项目

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：季度成长复盘

**触发信号**：PoC/Beta/生产任一阶段出现「季度成长复盘」相关诉求、阻塞或复盘需求。

**关键动作**：盘点差距

**FDE 注意**：避免 作品集缺验收指标

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：晋升/转岗作品集规划

**触发信号**：PoC/Beta/生产任一阶段出现「晋升/转岗作品集规划」相关诉求、阻塞或复盘需求。

**关键动作**：选 2-3 个里程碑项目

**FDE 注意**：避免 忽略软技能成长

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：团队梯队建设

**触发信号**：PoC/Beta/生产任一阶段出现「团队梯队建设」相关诉求、阻塞或复盘需求。

**关键动作**：定义每阶段交付物

**FDE 注意**：避免 路线图只有课程没有项目

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

**Q1：执行【FDE-Growth-Roadmap】时如何避免「路线图只有课程没有项目」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：新人 FDE onboarding。

**应用本 Skill 前**：仅有课程学习记录，无可展示交付物。

**应用本 Skill 后**：
1. 按【FDE-Growth-Roadmap】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：90 天完成首个独立 PoC 主导。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

