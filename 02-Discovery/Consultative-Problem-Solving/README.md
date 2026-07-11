# Consultative-Problem-Solving

- **分类**：`02-Discovery`
- **成熟度**：`usable`
- **一句话**：咨询式问题拆解：Issue Tree + DIVE

---

## 适用场景

- 客户要平台而非场景
- 需求冲突多
- PoC 方向不明
- 售前方案梳理


## 问题定义

客户表层诉求常是「做智能体平台」，真实问题是流程、数据、组织或价值优先级。


## 方法论框架

### Issue Tree（问题树）

```
表层诉求 → 业务问题 → 数据问题 → 流程问题 → 组织问题
```

### DIVE 模型

1. **Diagnose**：瓶颈在数据/流程/系统/组织？
2. **Identify**：价值属于降本/增效/提质/控险/增长？
3. **Validate**：最小 PoC 假设与指标？
4. **Embed**：谁用/谁审/谁负责？如何嵌入流程？

### MECE 原则

同级问题相互独立、完全穷尽，避免遗漏合规或权限维度。


## 输入 / 输出

### 输入

- 客户需求描述
- 访谈纪要
- 流程图
- 组织背景

### 输出

- Issue Tree
- DIVE 分析表
- PoC 核心假设
- 验证计划
- 场景卡草稿


## 执行步骤

1. 重述表层诉求
2. 建 Issue Tree（MECE）
3. DIVE 逐层分析
4. 提炼 1-3 个 PoC 假设
5. 定义验证指标
6. 场景评审对齐


## 常见误区

- ❌ 直接接平台需求
- ❌ 问题树不够 MECE
- ❌ PoC 假设过多
- ❌ 未定义 Embed 责任人


## 交付物清单

- [ ] 问题树
- [ ] DIVE 表
- [ ] PoC 假设清单
- [ ] 场景卡


## 与国内 FDE 生态关联

国内 FDE 咨询式交付核心；China-FDE-Consulting-Pattern 的方法论单元。


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

- [China-FDE-Consulting-Pattern](../../11-Best-Practice/China-FDE-Consulting-Pattern/README.md) — 咨询式交付总纲
- [MECE](../../11-Best-Practice/references/MECE/SKILL.md) — 问题树 MECE 校验
- [Process-Mapping](../Process-Mapping/README.md) — Embed 流程嵌入点

### 外部工程参考

- `.agents/skills/enterprise-sales`


## 场景深潜

### 场景 1：客户要平台而非场景

**触发信号**：PoC/Beta/生产任一阶段出现「客户要平台而非场景」相关诉求、阻塞或复盘需求。

**关键动作**：重述表层诉求

**FDE 注意**：避免 直接接平台需求

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：需求冲突多

**触发信号**：PoC/Beta/生产任一阶段出现「需求冲突多」相关诉求、阻塞或复盘需求。

**关键动作**：建 Issue Tree（MECE）

**FDE 注意**：避免 问题树不够 MECE

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：PoC 方向不明

**触发信号**：PoC/Beta/生产任一阶段出现「PoC 方向不明」相关诉求、阻塞或复盘需求。

**关键动作**：DIVE 逐层分析

**FDE 注意**：避免 PoC 假设过多

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：售前方案梳理

**触发信号**：PoC/Beta/生产任一阶段出现「售前方案梳理」相关诉求、阻塞或复盘需求。

**关键动作**：提炼 1-3 个 PoC 假设

**FDE 注意**：避免 未定义 Embed 责任人

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

**Q1：执行【Consultative-Problem-Solving】时如何避免「直接接平台需求」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：智能体平台诉求。

**应用本 Skill 前**：客户要全公司统一 Agent 平台。

**应用本 Skill 后**：
1. 按【Consultative-Problem-Solving】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：PoC 周期 12 周→4 周。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

