# China-FDE-Consulting-Pattern

- **分类**：`11-Best-Practice`
- **成熟度**：`usable`
- **一句话**：国内咨询式 FDE 交付打法总纲

---

## 适用场景

- 售前方案
- 交付方法论培训
- 团队标准化
- 对外白皮书


## 问题定义

国内 FDE 缺一套可复制的咨询+工程+运营总纲。


## 方法论框架

### 国内 FDE 五环

1. **嵌入**：进场、干系人、AIBP 组队
2. **咨询**：Issue Tree + DIVE + 场景卡
3. **构建**：三层 PoC + EDD + 私有化
4. **运营**：周度 Demo + 采纳增长 + 客户成功
5. **资产化**：模板/评估集/Prompt/Skill 沉淀

### 会议节奏

Kickoff → 场景评审 → 周度 Demo → 失败复盘 → 上线门禁 → 阶段复盘


## 输入 / 输出

### 输入

- 客户行业
- 项目阶段
- 团队组成

### 输出

- 交付打法白皮书
- 会议地图
- 资产化清单
- 报价层级说明


## 执行步骤

1. 诊断客户阶段
2. 选环组合
3. 排会议节奏
4. 定义资产化目标
5. 执行
6. 复盘沉淀


## 常见误区

- ❌ 只做 Demo 不咨询
- ❌ 无资产化
- ❌ 忽视采纳运营


## 交付物清单

- [ ] 白皮书
- [ ] 会议地图
- [ ] 资产清单


## 与国内 FDE 生态关联

本库方法论总纲；串联全部 Skill。


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

- [Consultative-Problem-Solving](../../02-Discovery/Consultative-Problem-Solving/README.md) — 咨询环核心
- [FDE-Full-Lifecycle](../FDE-Full-Lifecycle/README.md) — 构建与部署环
- [Diagnostic-FDE](../Diagnostic-FDE/README.md) — 售前方案包


## 场景深潜

### 场景 1：售前方案

**触发信号**：PoC/Beta/生产任一阶段出现「售前方案」相关诉求、阻塞或复盘需求。

**关键动作**：诊断客户阶段

**FDE 注意**：避免 只做 Demo 不咨询

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：交付方法论培训

**触发信号**：PoC/Beta/生产任一阶段出现「交付方法论培训」相关诉求、阻塞或复盘需求。

**关键动作**：选环组合

**FDE 注意**：避免 无资产化

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：团队标准化

**触发信号**：PoC/Beta/生产任一阶段出现「团队标准化」相关诉求、阻塞或复盘需求。

**关键动作**：排会议节奏

**FDE 注意**：避免 忽视采纳运营

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：对外白皮书

**触发信号**：PoC/Beta/生产任一阶段出现「对外白皮书」相关诉求、阻塞或复盘需求。

**关键动作**：定义资产化目标

**FDE 注意**：避免 只做 Demo 不咨询

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

**Q1：执行【China-FDE-Consulting-Pattern】时如何避免「只做 Demo 不咨询」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：交付标准化。

**应用本 Skill 前**：各项目打法不一致，新人上手慢。

**应用本 Skill 后**：
1. 按【China-FDE-Consulting-Pattern】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：团队统一 Kickoff→上线门禁节奏。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

