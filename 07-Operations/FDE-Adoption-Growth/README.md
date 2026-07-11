# FDE-Adoption-Growth

- **分类**：`07-Operations`
- **成熟度**：`usable`
- **一句话**：企业 AI 采纳率提升与客户成功

---

## 适用场景

- PoC 后推广
- 采纳率低
- 续约前
- 多部门扩展


## 问题定义

项目技术成功但无人用，无法续约和扩展。


## 方法论框架

**采纳漏斗**：知晓→试用→常用→依赖→推广。
**动作**：培训、 champion 计划、反馈闭环、价值播报、使用看板。
**指标**：DAU/WAU、任务完成率、续约意向、NPS。


## 输入 / 输出

### 输入

- 用户名单
- 当前使用数据
- 价值案例
- 合同节点

### 输出

- 采纳增长计划
- 培训材料
- Champion 名单
- 客户成功看板


## 执行步骤

1. 诊断漏斗断点
2. 选 champion
3. 设计培训
4. 建反馈通道
5. 周度价值播报
6. 续约复盘


## 常见误区

- ❌ 只做培训不做 champion
- ❌ 无使用数据
- ❌ 价值不可量化


## 交付物清单

- [ ] 增长计划
- [ ] 培训包
- [ ] 看板


## 与国内 FDE 生态关联

替代 Landing-Page-Brief；覆盖客户成功与采纳运营指标。


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

- [AIBP-Collaboration-Playbook](../../02-Discovery/AIBP-Collaboration-Playbook/README.md) — Champion 与双负责人
- [Executive-Communication-Framework](../../02-Discovery/Executive-Communication-Framework/README.md) — 续约价值汇报
- [SQL-Dashboard-Brief](../SQL-Dashboard-Brief/README.md) — 采纳看板指标

### 外部工程参考

- `.agents/skills/designing-growth-loops`
- `.agents/skills/saas-revenue-growth-metrics`


## 场景深潜

### 场景 1：PoC 后推广

**触发信号**：PoC/Beta/生产任一阶段出现「PoC 后推广」相关诉求、阻塞或复盘需求。

**关键动作**：诊断漏斗断点

**FDE 注意**：避免 只做培训不做 champion

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：采纳率低

**触发信号**：PoC/Beta/生产任一阶段出现「采纳率低」相关诉求、阻塞或复盘需求。

**关键动作**：选 champion

**FDE 注意**：避免 无使用数据

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：续约前

**触发信号**：PoC/Beta/生产任一阶段出现「续约前」相关诉求、阻塞或复盘需求。

**关键动作**：设计培训

**FDE 注意**：避免 价值不可量化

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：多部门扩展

**触发信号**：PoC/Beta/生产任一阶段出现「多部门扩展」相关诉求、阻塞或复盘需求。

**关键动作**：建反馈通道

**FDE 注意**：避免 只做培训不做 champion

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

**Q1：执行【FDE-Adoption-Growth】时如何避免「只做培训不做 champion」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：PoC 成功但续约难。

**应用本 Skill 前**：技术验收通过，WAU < 5%。

**应用本 Skill 后**：
1. 按【FDE-Adoption-Growth】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：续约前 WAU 达 32%。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

