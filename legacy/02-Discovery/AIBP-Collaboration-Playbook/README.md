# AIBP-Collaboration-Playbook

- **分类**：`02-Discovery`
- **成熟度**：`usable`
- **一句话**：FDE 与 AIBP 协作边界与共创机制

---

## 适用场景

- PoC 组队
- 周度 Demo
- 验收争议
- 扩展场景
- 运营移交


## 问题定义

FDE 与 AIBP 职责模糊，Ground Truth 缺失，Demo 与业务效果脱节。


## 方法论框架

**分工**：AIBP=业务好结果+Ground Truth；FDE=稳定交付+技术资产。
**机制**：场景卡共创、周度 Demo 双负责人、失败样本共审、上线门禁联签。
**会议**：Kickoff/场景评审/周度Demo/失败复盘/上线门禁。


## 输入 / 输出

### 输入

- 项目角色名单
- 场景卡草稿
- 会议日历

### 输出

- 协作章程
- 场景卡（双签）
- 周度 Demo 模板
- RACI 表
- 升级路径


## 执行步骤

1. 定义 RACI
2. 共创场景卡
3. 建立周度 Demo 节奏
4. 共建 Golden Dataset
5. 联签上线门禁
6. 运营移交


## 常见误区

- ❌ AIBP 不参与样本
- ❌ FDE 独自定义验收
- ❌ 无周度节奏
- ❌ 运营移交断层


## 交付物清单

- [ ] 协作章程
- [ ] RACI
- [ ] 场景卡
- [ ] Demo 模板


## 与国内 FDE 生态关联

敏捷小组协作落地；国内 FDE+AIBP 双负责人模式。


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

- [Stakeholder-Mapping](../../01-Foundation/Stakeholder-Mapping/README.md) — 双负责人识别
- [FDE-Adoption-Growth](../../07-Operations/FDE-Adoption-Growth/README.md) — 运营移交与采纳
- [RAG-Evaluation](../../04-AI-Delivery/RAG-Evaluation/README.md) — Ground Truth 共建


## 场景深潜

### 场景 1：PoC 组队

**触发信号**：PoC/Beta/生产任一阶段出现「PoC 组队」相关诉求、阻塞或复盘需求。

**关键动作**：定义 RACI

**FDE 注意**：避免 AIBP 不参与样本

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 2：周度 Demo

**触发信号**：PoC/Beta/生产任一阶段出现「周度 Demo」相关诉求、阻塞或复盘需求。

**关键动作**：共创场景卡

**FDE 注意**：避免 FDE 独自定义验收

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 3：验收争议

**触发信号**：PoC/Beta/生产任一阶段出现「验收争议」相关诉求、阻塞或复盘需求。

**关键动作**：建立周度 Demo 节奏

**FDE 注意**：避免 无周度节奏

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 4：扩展场景

**触发信号**：PoC/Beta/生产任一阶段出现「扩展场景」相关诉求、阻塞或复盘需求。

**关键动作**：共建 Golden Dataset

**FDE 注意**：避免 运营移交断层

**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。

### 场景 5：运营移交

**触发信号**：PoC/Beta/生产任一阶段出现「运营移交」相关诉求、阻塞或复盘需求。

**关键动作**：联签上线门禁

**FDE 注意**：避免 AIBP 不参与样本

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

**Q1：执行【AIBP-Collaboration-Playbook】时如何避免「AIBP 不参与样本」？**

A：按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。

**Q2：私有化/信创/等保环境下有哪些额外约束？**

A：在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。

**Q3：与 AIBP 分工边界不清怎么办？**

A：回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。

**Q4：PoC 通过后如何衔接到 Beta/生产？**

A：输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。



## 案例片段（示意）

> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：PoC 组队。

**应用本 Skill 前**：FDE 独自定义验收，AIBP 未供 Ground Truth。

**应用本 Skill 后**：
1. 按【AIBP-Collaboration-Playbook】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：Golden Dataset 20 条由 AIBP 确认。


## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |
| v1.0 | 2026-07-12 | 目录重组后首次充实版 |

