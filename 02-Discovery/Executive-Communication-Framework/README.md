# Executive-Communication-Framework

- **分类**：`02-Discovery`
- **成熟度**：`usable`
- **一句话**：面向高层/decision maker 的价值沟通框架

---

## 适用场景

- 立项汇报
- 阶段复盘
- 预算追加
- 续约
- 失败止损决策


## 问题定义

高层没时间看技术细节，FDE 若不会讲 ROI 和决策选项，项目难获持续支持。


## 方法论框架

**金字塔结构**：结论 → 3 个论据 → 数据 → 建议行动。
**高管关心**：ROI、风险、时间、竞品、组织影响、退出选项。
**一页纸**：问题/方案/指标/投入/风险/决策请求。


## 输入 / 输出

### 输入

- 场景卡
- 指标数据
- 竞品/行业对标
- 预算实际

### 输出

- 高管一页纸
- 汇报 Deck 大纲
- 决策选项表
- ROI 简版


## 执行步骤

1. 明确决策请求
2. 提炼 3 条论据
3. 量化 ROI
4. 准备风险与选项
5. 15min 预演
6. 汇报+纪要


## 常见误区

- ❌ 讲技术不讲决策
- ❌ ROI 无依据
- ❌ 缺少退出选项
- ❌ 汇报超时


## 交付物清单

- [ ] 高管一页纸
- [ ] Deck
- [ ] ROI 表


## 与国内 FDE 生态关联

高层沟通场景；与 FDE-Adoption-Growth 续约场景联动。


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

- [FDE-Adoption-Growth](../../07-Operations/FDE-Adoption-Growth/README.md) — 续约与价值播报
- [Expectation-Management-Script](../Expectation-Management-Script/README.md) — ROI 叙事中的边界声明
- [McKinsey-Report](../../11-Best-Practice/references/McKinsey-Report/SKILL.md) — 行研报告与 Deck 故事线


## 场景深潜

### 场景 1：立项汇报

**触发信号**：PoC/Beta/生产任一阶段出现「立项汇报」相关诉求、阻塞或复盘需求。

**关键动作**：明确决策请求

**FDE 注意**：避免 讲技术不讲决策

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：阶段复盘

**触发信号**：PoC/Beta/生产任一阶段出现「阶段复盘」相关诉求、阻塞或复盘需求。

**关键动作**：提炼 3 条论据

**FDE 注意**：避免 ROI 无依据

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：预算追加

**触发信号**：PoC/Beta/生产任一阶段出现「预算追加」相关诉求、阻塞或复盘需求。

**关键动作**：量化 ROI

**FDE 注意**：避免 缺少退出选项

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：续约

**触发信号**：PoC/Beta/生产任一阶段出现「续约」相关诉求、阻塞或复盘需求。

**关键动作**：准备风险与选项

**FDE 注意**：避免 汇报超时

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 5：失败止损决策

**触发信号**：PoC/Beta/生产任一阶段出现「失败止损决策」相关诉求、阻塞或复盘需求。

**关键动作**：15min 预演

**FDE 注意**：避免 讲技术不讲决策

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

**Q1：执行【Executive-Communication-Framework】时如何避免「讲技术不讲决策」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：预算追加汇报。

**应用本 Skill 前**：FDE 讲 30 分钟架构细节，高管无决策。

**应用本 Skill 后**：
1. 按【Executive-Communication-Framework】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：获得 Beta 扩展预算批准。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

