# Communication-Script-Library

- **分类**：`01-Foundation`
- **成熟度**：`usable`
- **一句话**：面向高层/业务/IT/合规/一线的标准沟通话术库

---

## 适用场景

- Kickoff 对齐
- 周度 Demo 反馈收集
- 范围变更沟通
- 延期与风险通报
- 上线前预期校准


## 问题定义

FDE 技术表达与业务方理解错位，导致范围漂移、预期失控和协作摩擦。


## 方法论框架

**五类对象话术**：高管（价值/ROI/风险）、业务（流程/采纳）、IT（集成/权限）、合规（边界/人审）、一线（培训/反馈）。
**结构**：情境 → 目标 → 话术 → 禁忌 → 追问清单。


## 输入 / 输出

### 输入

- 会议类型
- 参会角色
- 当前项目阶段
- 已知争议点

### 输出

- 分角色话术包
- 追问清单
- 禁忌词列表
- 邮件/飞书消息模板


## 执行步骤

1. 识别会议类型与对象
2. 选对应话术模块
3. 填入项目上下文
4. 预演关键追问
5. 会后更新话术库


## 常见误区

- ❌ 对高层讲技术细节
- ❌ 对业务回避概率性边界
- ❌ 缺少追问清单导致会议无结论


## 交付物清单

- [ ] 话术库文档
- [ ] 会议模板
- [ ] 消息模板


## 与国内 FDE 生态关联

业务沟通话术落地；与 Expectation-Management、Executive-Communication 配套。


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

- [Expectation-Management-Script](../../02-Discovery/Expectation-Management-Script/README.md) — AI 概率性边界话术
- [Executive-Communication-Framework](../../02-Discovery/Executive-Communication-Framework/README.md) — 高层汇报话术
- [AIBP-Collaboration-Playbook](../../02-Discovery/AIBP-Collaboration-Playbook/README.md) — 双负责人协作沟通


## 场景深潜

### 场景 1：Kickoff 对齐

**触发信号**：PoC/Beta/生产任一阶段出现「Kickoff 对齐」相关诉求、阻塞或复盘需求。

**关键动作**：识别会议类型与对象

**FDE 注意**：避免 对高层讲技术细节

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：周度 Demo 反馈收集

**触发信号**：PoC/Beta/生产任一阶段出现「周度 Demo 反馈收集」相关诉求、阻塞或复盘需求。

**关键动作**：选对应话术模块

**FDE 注意**：避免 对业务回避概率性边界

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：范围变更沟通

**触发信号**：PoC/Beta/生产任一阶段出现「范围变更沟通」相关诉求、阻塞或复盘需求。

**关键动作**：填入项目上下文

**FDE 注意**：避免 缺少追问清单导致会议无结论

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：延期与风险通报

**触发信号**：PoC/Beta/生产任一阶段出现「延期与风险通报」相关诉求、阻塞或复盘需求。

**关键动作**：预演关键追问

**FDE 注意**：避免 对高层讲技术细节

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 5：上线前预期校准

**触发信号**：PoC/Beta/生产任一阶段出现「上线前预期校准」相关诉求、阻塞或复盘需求。

**关键动作**：会后更新话术库

**FDE 注意**：避免 对业务回避概率性边界

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

**Q1：执行【Communication-Script-Library】时如何避免「对高层讲技术细节」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：PoC 延期通报。

**应用本 Skill 前**：项目组用技术日志向业务 Owner 解释延期，引发信任危机。

**应用本 Skill 后**：
1. 按【Communication-Script-Library】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：业务 Owner 书面确认新里程碑。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

