# SOW-Generator

- **分类**：`01-Foundation`
- **成熟度**：`usable`
- **一句话**：AI PoC/MVP 项目工作说明书生成

---

## 适用场景

- 售前 PoC 签约
- 内部立项
- 范围变更重签
- 外包/联合交付


## 问题定义

AI 项目范围易漂移，口头约定导致验收争议和追加成本纠纷。


## 方法论框架

**SOW 核心章节**：目标与边界、交付物、里程碑、验收指标、数据与权限、风险与假设、变更机制。
**PoC 原则**：只验证核心假设，不承诺全量生产。


## 输入 / 输出

### 输入

- 场景卡
- 干系人地图
- 预算与时间约束
- 合规要求

### 输出

- SOW 正文
- 里程碑表
- 验收指标附件
- 变更流程


## 执行步骤

1. 从场景卡提取范围
2. 定义 In/Out Scope
3. 写里程碑与交付物
4. 绑定验收指标
5. 列假设与风险
6. 法务/商务评审


## 常见误区

- ❌ 范围过大一次做生产
- ❌ 验收指标模糊
- ❌ 忽略数据和权限前置条件


## 交付物清单

- [ ] SOW 文档
- [ ] 里程碑甘特
- [ ] 验收指标表


## 与国内 FDE 生态关联

国内政企 PoC 签约标配；模板见 10-Templates/SOW-Template。


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

- [SOW-Template](../../10-Templates/SOW-Template/README.md) — 标准模板基座
- [Stakeholder-Mapping](../Stakeholder-Mapping/README.md) — 签约方与决策链
- [Consultative-Problem-Solving](../../02-Discovery/Consultative-Problem-Solving/README.md) — PoC 假设与范围来源

### 外部工程参考

- `.agents/skills/enterprise-sales`


## 场景深潜

### 场景 1：售前 PoC 签约

**触发信号**：PoC/Beta/生产任一阶段出现「售前 PoC 签约」相关诉求、阻塞或复盘需求。

**关键动作**：从场景卡提取范围

**FDE 注意**：避免 范围过大一次做生产

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：内部立项

**触发信号**：PoC/Beta/生产任一阶段出现「内部立项」相关诉求、阻塞或复盘需求。

**关键动作**：定义 In/Out Scope

**FDE 注意**：避免 验收指标模糊

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：范围变更重签

**触发信号**：PoC/Beta/生产任一阶段出现「范围变更重签」相关诉求、阻塞或复盘需求。

**关键动作**：写里程碑与交付物

**FDE 注意**：避免 忽略数据和权限前置条件

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：外包/联合交付

**触发信号**：PoC/Beta/生产任一阶段出现「外包/联合交付」相关诉求、阻塞或复盘需求。

**关键动作**：绑定验收指标

**FDE 注意**：避免 范围过大一次做生产

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

**Q1：执行【SOW-Generator】时如何避免「范围过大一次做生产」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：智能客服 PoC。

**应用本 Skill 前**：口头约定「做智能客服」，验收时争议准确率指标。

**应用本 Skill 后**：
1. 按【SOW-Generator】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：PoC 4 周验收无追加纠纷。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

