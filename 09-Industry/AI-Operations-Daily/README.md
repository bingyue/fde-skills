# AI-Operations-Daily

- **分类**：`09-Industry`
- **成熟度**：`usable`
- **一句话**：跨境/品牌 AI 运营日报（舆情+竞品+经营）

---

## 适用场景

- 品牌运营
- 跨境电商
- 市场部
- 增长团队日会


## 问题定义

运营决策缺每日 AI 辅助洞察，人盯多渠道效率低。


## 方法论框架

**日报结构**：舆情预警/竞品动态/经营异常/待办建议。
**Agent 链路**：采集→分析→分级→推送→人审。


## 输入 / 输出

### 输入

- 数据源账号
- 预警规则
- 推送渠道
- 责任人

### 输出

- 日报模板
- Agent 配置
- 预警规则表
- 运营 SOP


## 执行步骤

1. 定义日报栏目
2. 接数据源
3. 设预警阈值
4. 配置推送
5. 人审流程
6. 日会复盘


## 常见误区

- ❌ 无人工复核高风险
- ❌ 数据源不稳定
- ❌ 日报过多无人看


## 交付物清单

- [ ] 日报模板
- [ ] 规则表
- [ ] SOP


## 与国内 FDE 生态关联

行业高价值示例；可迁移到其他行业日报场景。


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

- [FDE-Adoption-Growth](../../07-Operations/FDE-Adoption-Growth/README.md) — 运营采纳模式
- [SQL-Dashboard-Brief](../../07-Operations/SQL-Dashboard-Brief/README.md) — 日报指标看板
- [Customer-Service-Bot](../../07-Operations/Customer-Service-Bot/README.md) — 舆情/客服联动


## 场景深潜

### 场景 1：品牌运营

**触发信号**：PoC/Beta/生产任一阶段出现「品牌运营」相关诉求、阻塞或复盘需求。

**关键动作**：定义日报栏目

**FDE 注意**：避免 无人工复核高风险

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：跨境电商

**触发信号**：PoC/Beta/生产任一阶段出现「跨境电商」相关诉求、阻塞或复盘需求。

**关键动作**：接数据源

**FDE 注意**：避免 数据源不稳定

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：市场部

**触发信号**：PoC/Beta/生产任一阶段出现「市场部」相关诉求、阻塞或复盘需求。

**关键动作**：设预警阈值

**FDE 注意**：避免 日报过多无人看

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：增长团队日会

**触发信号**：PoC/Beta/生产任一阶段出现「增长团队日会」相关诉求、阻塞或复盘需求。

**关键动作**：配置推送

**FDE 注意**：避免 无人工复核高风险

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

**Q1：执行【AI-Operations-Daily】时如何避免「无人工复核高风险」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：品牌跨境运营。

**应用本 Skill 前**：人盯 5 渠道舆情，日会无结构化输入。

**应用本 Skill 后**：
1. 按【AI-Operations-Daily】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：7 天稳定推送，捕获 2 次竞品异动。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

