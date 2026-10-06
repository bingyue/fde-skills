# Customer-Service-Bot

- **分类**：`07-Operations`
- **成熟度**：`usable`
- **一句话**：客服知识库 + 工单分流 Agent 运营

---

## 适用场景

- 售后客服
- 内部 IT 帮助台
- 电商客服
- 政企热线辅助


## 问题定义

客服场景 PoC 多但采纳低，缺运营指标和失败闭环。


## 方法论框架

**链路**：知识库 RAG + 意图分流 + 工单创建 + 人审 + 反馈闭环。
**运营指标**：首响、准确率、采纳率、转人工率、满意度。


## 输入 / 输出

### 输入

- 知识库资料
- 历史工单
- 客服 SOP
- CRM/工单 API

### 输出

- 客服 Agent 方案
- 知识库清单
- 运营看板
- SOP 更新


## 执行步骤

1. 盘点高频问题
2. 建知识库
3. 设分流规则
4. 接入工单
5. 试点运营
6. 周度复盘


## 常见误区

- ❌ 无转人工策略
- ❌ 知识库不更新
- ❌ 缺采纳率跟踪


## 交付物清单

- [ ] 方案文档
- [ ] 看板
- [ ] 运营 SOP


## 与国内 FDE 生态关联

典型知识库工单 Agent 场景；cs-sop 可参考。


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

- [RAG-Evaluation](../../04-AI-Delivery/RAG-Evaluation/README.md) — 知识库评估
- [Feishu-Integration](../../06-Integration/Feishu-Integration/README.md) — 工单与消息推送
- [FDE-Adoption-Growth](../FDE-Adoption-Growth/README.md) — 客服采纳运营

### 外部工程参考

- `.agents/skills/cs-sop`
- `.agents/skills/tiktok-shop-customer-service`


## 场景深潜

### 场景 1：售后客服

**触发信号**：PoC/Beta/生产任一阶段出现「售后客服」相关诉求、阻塞或复盘需求。

**关键动作**：盘点高频问题

**FDE 注意**：避免 无转人工策略

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：内部 IT 帮助台

**触发信号**：PoC/Beta/生产任一阶段出现「内部 IT 帮助台」相关诉求、阻塞或复盘需求。

**关键动作**：建知识库

**FDE 注意**：避免 知识库不更新

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：电商客服

**触发信号**：PoC/Beta/生产任一阶段出现「电商客服」相关诉求、阻塞或复盘需求。

**关键动作**：设分流规则

**FDE 注意**：避免 缺采纳率跟踪

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：政企热线辅助

**触发信号**：PoC/Beta/生产任一阶段出现「政企热线辅助」相关诉求、阻塞或复盘需求。

**关键动作**：接入工单

**FDE 注意**：避免 无转人工策略

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

**Q1：执行【Customer-Service-Bot】时如何避免「无转人工策略」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：售后客服 PoC。

**应用本 Skill 前**：Bot 能答但无人用，转人工率 90%。

**应用本 Skill 后**：
1. 按【Customer-Service-Bot】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：Beta 首响降 35%，转人工 40%。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

