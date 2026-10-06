# Private-Deployment-Gateway

- **分类**：`05-Deployment`
- **成熟度**：`usable`
- **一句话**：国内私有化部署与 AI Gateway 路径

---

## 适用场景

- 政企私有化
- 国产化要求
- 数据不出域
- PoC 转生产


## 问题定义

国内客户不能用公有云托管，需要私有化、网关、合规的可交付路径。


## 方法论框架

### 三层 PoC 路径

1. 开箱即用（Dify/MaxKB）快速验证
2. Vibe Coding 小范围定制
3. 工程化脚手架（FastAPI+网关+监控）

### AI Gateway

统一鉴权、模型路由、审计、限流、内容安全。


## 输入 / 输出

### 输入

- 部署约束
- 国产化清单
- 网络拓扑
- 合规要求

### 输出

- 部署架构图
- Gateway 配置
- 上线检查表
- 运维 Runbook


## 执行步骤

1. 评估部署约束
2. 选层级路径
3. 设计 Gateway
4. 权限与审计
5. PoC 部署
6. 生产检查
7. Runbook


## 常见误区

- ❌ PoC 工具直接上生产
- ❌ 无 Gateway 审计
- ❌ 忽略国产化兼容


## 交付物清单

- [ ] 架构图
- [ ] 部署清单
- [ ] Runbook


## 与国内 FDE 生态关联

国内私有化部署路径；替代 Vercel-Deployment。


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

- [RBAC-Audit](../../08-Security-Compliance/RBAC-Audit/README.md) — 私有化权限与等保
- [Tool-Audit](../Tool-Audit/README.md) — Gateway 工具审计
- [Feishu-Integration](../../06-Integration/Feishu-Integration/README.md) — 协同层集成

### 外部工程参考

- `.agents/skills/deployment-engineer`
- `.agents/skills/deployment-pipeline-design`


## 场景深潜

### 场景 1：政企私有化

**触发信号**：PoC/Beta/生产任一阶段出现「政企私有化」相关诉求、阻塞或复盘需求。

**关键动作**：评估部署约束

**FDE 注意**：避免 PoC 工具直接上生产

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：国产化要求

**触发信号**：PoC/Beta/生产任一阶段出现「国产化要求」相关诉求、阻塞或复盘需求。

**关键动作**：选层级路径

**FDE 注意**：避免 无 Gateway 审计

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：数据不出域

**触发信号**：PoC/Beta/生产任一阶段出现「数据不出域」相关诉求、阻塞或复盘需求。

**关键动作**：设计 Gateway

**FDE 注意**：避免 忽略国产化兼容

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：PoC 转生产

**触发信号**：PoC/Beta/生产任一阶段出现「PoC 转生产」相关诉求、阻塞或复盘需求。

**关键动作**：权限与审计

**FDE 注意**：避免 PoC 工具直接上生产

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

**Q1：执行【Private-Deployment-Gateway】时如何避免「PoC 工具直接上生产」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：信创私有化。

**应用本 Skill 前**：PoC 用公有云 Demo，生产无法迁移。

**应用本 Skill 后**：
1. 按【Private-Deployment-Gateway】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：PoC→生产同架构迁移 2 周完成。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

