# Expectation-Management-Script

- **分类**：`02-Discovery`
- **成熟度**：`usable`
- **一句话**：AI 概率性边界与预期管理话术

---

## 适用场景

- PoC 启动
- Demo 后
- 效果争议时
- 上线前
- 续约谈判


## 问题定义

业务方按传统软件预期 AI，一次错误即否定全部价值，项目夭折。


## 方法论框架

**核心信息**：概率性、幻觉、错误率、人审策略、迭代路径、上线边界。
**话术结构**：承认局限 → 解释原因 → 给指标 → 给人审 → 给迭代计划。


## 输入 / 输出

### 输入

- 当前指标
- 失败样本
- 客户投诉点
- 合同范围

### 输出

- 预期管理话术包
- 指标解释一页纸
- 人审策略说明
- 迭代路线图


## 执行步骤

1. 梳理客户当前预期
2. 对比实际能力
3. 准备指标与样本
4. 编写分角色话术
5. 周度 Demo 持续校准
6. 书面确认边界


## 常见误区

- ❌ 过度承诺准确率
- ❌ 回避谈幻觉
- ❌ 缺少人审方案
- ❌ 不展示失败样本


## 交付物清单

- [ ] 话术包
- [ ] 指标一页纸
- [ ] 人审流程图


## 与国内 FDE 生态关联

预期管理落地；与 Executive-Communication 互补。


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

- [Executive-Communication-Framework](../Executive-Communication-Framework/README.md) — 高层预期校准
- [Communication-Script-Library](../../01-Foundation/Communication-Script-Library/README.md) — 分角色话术库
- [FDE-Adoption-Growth](../../07-Operations/FDE-Adoption-Growth/README.md) — 采纳阶段预期管理


## 场景深潜

### 场景 1：PoC 启动

**触发信号**：PoC/Beta/生产任一阶段出现「PoC 启动」相关诉求、阻塞或复盘需求。

**关键动作**：梳理客户当前预期

**FDE 注意**：避免 过度承诺准确率

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：Demo 后

**触发信号**：PoC/Beta/生产任一阶段出现「Demo 后」相关诉求、阻塞或复盘需求。

**关键动作**：对比实际能力

**FDE 注意**：避免 回避谈幻觉

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：效果争议时

**触发信号**：PoC/Beta/生产任一阶段出现「效果争议时」相关诉求、阻塞或复盘需求。

**关键动作**：准备指标与样本

**FDE 注意**：避免 缺少人审方案

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：上线前

**触发信号**：PoC/Beta/生产任一阶段出现「上线前」相关诉求、阻塞或复盘需求。

**关键动作**：编写分角色话术

**FDE 注意**：避免 不展示失败样本

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 5：续约谈判

**触发信号**：PoC/Beta/生产任一阶段出现「续约谈判」相关诉求、阻塞或复盘需求。

**关键动作**：周度 Demo 持续校准

**FDE 注意**：避免 过度承诺准确率

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

**Q1：执行【Expectation-Management-Script】时如何避免「过度承诺准确率」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：RAG Demo 后。

**应用本 Skill 前**：业务方认为「AI 应该 100% 准确」。

**应用本 Skill 后**：
1. 按【Expectation-Management-Script】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：客户书面确认 Beta 阶段人工复核 100%。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

