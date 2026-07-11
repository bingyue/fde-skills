# Stakeholder-Mapping

- **分类**：`01-Foundation`
- **成熟度**：`usable`
- **一句话**：AI 项目干系人识别、影响力分析与协作策略

---

## 适用场景

- 项目 Kickoff 前
- 范围争议时
- 上线推广前
- 续约/扩展评估


## 问题定义

AI 项目涉及业务、IT、数据、合规、一线等多方，缺少干系人地图导致决策慢、推不动。


## 方法论框架

**矩阵**：影响力 × 态度（支持/中立/反对）→ 策略（拉拢/说服/隔离/升级）。
**关键角色**：业务 Owner、AIBP、CIO/IT、安全合规、一线骨干、预算决策者。


## 输入 / 输出

### 输入

- 组织架构成稿
- 已知项目争议
- 历史协作经验

### 输出

- 干系人地图
- 沟通频率表
- 风险干系人清单
- 升级路径


## 执行步骤

1. 列出所有触达角色
2. 评估影响力与态度
3. 标注信息需求
4. 制定沟通策略
5. 与 FDE/AIBP 对齐
6. Kickoff 验证


## 常见误区

- ❌ 只映射业务忽略 IT/合规
- ❌ 未识别隐形反对者
- ❌ 地图做完不更新


## 交付物清单

- [ ] 干系人矩阵
- [ ] 沟通计划
- [ ] 升级路径图


## 与国内 FDE 生态关联

Kickoff 标准动作；与 SOW-Generator、AIBP-Collaboration 联动。


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

- [SOW-Generator](../SOW-Generator/README.md) — Kickoff 后书面化范围
- [AIBP-Collaboration-Playbook](../../02-Discovery/AIBP-Collaboration-Playbook/README.md) — 识别 AIBP 与业务 Owner
- [Business-Interview](../../02-Discovery/Business-Interview/README.md) — 干系人深度访谈


## 场景深潜

### 场景 1：项目 Kickoff 前

**触发信号**：PoC/Beta/生产任一阶段出现「项目 Kickoff 前」相关诉求、阻塞或复盘需求。

**关键动作**：列出所有触达角色

**FDE 注意**：避免 只映射业务忽略 IT/合规

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：范围争议时

**触发信号**：PoC/Beta/生产任一阶段出现「范围争议时」相关诉求、阻塞或复盘需求。

**关键动作**：评估影响力与态度

**FDE 注意**：避免 未识别隐形反对者

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：上线推广前

**触发信号**：PoC/Beta/生产任一阶段出现「上线推广前」相关诉求、阻塞或复盘需求。

**关键动作**：标注信息需求

**FDE 注意**：避免 地图做完不更新

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：续约/扩展评估

**触发信号**：PoC/Beta/生产任一阶段出现「续约/扩展评估」相关诉求、阻塞或复盘需求。

**关键动作**：制定沟通策略

**FDE 注意**：避免 只映射业务忽略 IT/合规

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

**Q1：执行【Stakeholder-Mapping】时如何避免「只映射业务忽略 IT/合规」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：政企 AI 立项。

**应用本 Skill 前**：IT 支持但合规未入场，上线前被否决。

**应用本 Skill 后**：
1. 按【Stakeholder-Mapping】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：合规评审前置 2 周完成。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

