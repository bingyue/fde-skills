# API-Design-Review

- **分类**：`03-Solution-Design`
- **成熟度**：`usable`
- **一句话**：企业系统集成 API 设计评审

---

## 适用场景

- Agent 接 CRM/ERP
- 飞书/工单集成
- MCP 工具设计
- PoC 转 MVP


## 问题定义

API 设计不当导致权限漏洞、联调失败和无法审计。


## 方法论框架

**评审维度**：契约清晰、幂等、错误码、分页、鉴权、审计日志、限流、版本。
**FDE 关注**：Agent 调用稳定性、超时重试、人工兜底。


## 输入 / 输出

### 输入

- 现有 API 文档
- 集成清单
- 权限模型

### 输出

- 评审意见
- API 契约草案
- 风险清单
- 联调计划


## 执行步骤

1. 收集集成需求
2. 评审契约
3. 检查安全
4. 定义联调用例
5. 签字基线


## 常见误区

- ❌ 忽略鉴权
- ❌ 无错误处理
- ❌ Agent 工具无超时


## 交付物清单

- [ ] 评审报告
- [ ] 契约文档
- [ ] 联调用例


## 与国内 FDE 生态关联

Integration 前置；与 Tool-Audit、RBAC-Audit 联动。


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

- [PRD-Generator](../PRD-Generator/README.md) — 集成需求来源
- [Feishu-Integration](../../06-Integration/Feishu-Integration/README.md) — 飞书/IM 集成契约
- [Tool-Audit](../../04-AI-Delivery/Tool-Audit/README.md) — Agent 工具契约


## 场景深潜

### 场景 1：Agent 接 CRM/ERP

**触发信号**：PoC/Beta/生产任一阶段出现「Agent 接 CRM/ERP」相关诉求、阻塞或复盘需求。

**关键动作**：收集集成需求

**FDE 注意**：避免 忽略鉴权

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：飞书/工单集成

**触发信号**：PoC/Beta/生产任一阶段出现「飞书/工单集成」相关诉求、阻塞或复盘需求。

**关键动作**：评审契约

**FDE 注意**：避免 无错误处理

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：MCP 工具设计

**触发信号**：PoC/Beta/生产任一阶段出现「MCP 工具设计」相关诉求、阻塞或复盘需求。

**关键动作**：检查安全

**FDE 注意**：避免 Agent 工具无超时

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：PoC 转 MVP

**触发信号**：PoC/Beta/生产任一阶段出现「PoC 转 MVP」相关诉求、阻塞或复盘需求。

**关键动作**：定义联调用例

**FDE 注意**：避免 忽略鉴权

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

**Q1：执行【API-Design-Review】时如何避免「忽略鉴权」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：Agent 接 ERP。

**应用本 Skill 前**：工具无超时重试，一次故障导致工单重复创建。

**应用本 Skill 后**：
1. 按【API-Design-Review】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：联调 3 天完成无 P0。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

