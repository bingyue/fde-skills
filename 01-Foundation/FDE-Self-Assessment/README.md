# FDE-Self-Assessment

- **分类**：`01-Foundation`
- **成熟度**：`usable`
- **一句话**：国内 FDE 四角色能力自评与 30/60/90 补齐规划

---

## 适用场景

- 转岗前能力盘点
- PoC/Beta/生产阶段复盘
- 团队分层培养
- 售前能力评估


## 问题定义

FDE 角色边界模糊，缺乏统一自评基线，短板在 PoC 验收或上线门禁时集中暴露。


## 方法论框架

**四角色**：业务咨询 / 架构操盘 / AI 驯化 / 交付运营，各 L1-L4。
**方法**：案例证据打分 → 识别阻塞短板 → 绑定可交付物补齐 → 30/60/90 路线图。


## 输入 / 输出

### 输入

- 2 个项目案例
- 角色时间占比
- 客户反馈记录

### 输出

- 能力雷达
- 四角色评分卡
- 阻塞短板清单
- 30/60/90 计划


## 执行步骤

1. 收集项目节点证据
2. 四角色逐项打分
3. 标阻塞短板
4. 匹配 Skill 路径
5. 导师对齐
6. 输出路线图


## 常见误区

- ❌ 只评技术不评沟通
- ❌ 用学过工具代替交付过场景
- ❌ 计划过于抽象


## 交付物清单

- [ ] 自评表
- [ ] 雷达图
- [ ] 补齐路线图


## 与国内 FDE 生态关联

国内 FDE 四阶段能力地图的落地入口；联动 Growth-Roadmap、Communication-Script-Library。


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

- [FDE-Growth-Roadmap](../FDE-Growth-Roadmap/README.md) — 成长路线与作品集绑定
- [Communication-Script-Library](../Communication-Script-Library/README.md) — 沟通短板补齐
- [China-FDE-Consulting-Pattern](../../11-Best-Practice/China-FDE-Consulting-Pattern/README.md) — 四角色能力地图


## 场景深潜

### 场景 1：转岗前能力盘点

**触发信号**：PoC/Beta/生产任一阶段出现「转岗前能力盘点」相关诉求、阻塞或复盘需求。

**关键动作**：收集项目节点证据

**FDE 注意**：避免 只评技术不评沟通

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：PoC/Beta/生产阶段复盘

**触发信号**：PoC/Beta/生产任一阶段出现「PoC/Beta/生产阶段复盘」相关诉求、阻塞或复盘需求。

**关键动作**：四角色逐项打分

**FDE 注意**：避免 用学过工具代替交付过场景

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：团队分层培养

**触发信号**：PoC/Beta/生产任一阶段出现「团队分层培养」相关诉求、阻塞或复盘需求。

**关键动作**：标阻塞短板

**FDE 注意**：避免 计划过于抽象

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：售前能力评估

**触发信号**：PoC/Beta/生产任一阶段出现「售前能力评估」相关诉求、阻塞或复盘需求。

**关键动作**：匹配 Skill 路径

**FDE 注意**：避免 只评技术不评沟通

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

**Q1：执行【FDE-Self-Assessment】时如何避免「只评技术不评沟通」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：某金融客户 PoC 项目。

**应用本 Skill 前**：FDE 自评 L3 但沟通 L1，Beta 阶段业务方停止参加周度 Demo。

**应用本 Skill 后**：
1. 按【FDE-Self-Assessment】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：60 天后周度 Demo 恢复，生产上线门禁一次通过。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

