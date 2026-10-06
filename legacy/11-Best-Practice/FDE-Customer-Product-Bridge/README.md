# FDE-Customer-Product-Bridge

- **分类**：`11-Best-Practice`
- **成熟度**：`usable`
- **版本**：`1.0.0`（源自 OpenClaw `fde-customer-product-bridge`）
- **一句话**：FDE 客户-产品-研发连接器——把客户现场转化为内部行动

---

## 适用场景

- 客户需求调研 / 访谈提纲 / 调研纪要
- 现场 Demo 脚本与客户讲解
- 客户案例包装与标杆故事
- 客户反馈转产品需求 / 研发任务 / 验收标准
- 客户汇报与方案说明材料

## 问题定义

FDE 的核心价值之一是把**客户现场**同时服务四个对象：客户（可信度）、销售/方案（推进抓手）、产品（场景与优先级）、研发（边界与验收）。本 Skill 提供四条标准工作流，避免「客户原话直接当需求」或「Demo 按产品菜单讲」。

## 方法论框架

### 基本原则

1. **先还原现场，再抽象需求**
2. **三种语言并行翻译**：客户语言 / 产品语言 / 研发语言
3. **Demo 服务于客户业务路径**，不按功能菜单
4. **案例必须可复用**，说明适用边界
5. **区分事实、判断和待验证**

### 四条工作流

| 工作流 | 产出 |
| --- | --- |
| **A 客户需求调研** | 访谈提纲 + 调研纪要（流程表、痛点、产品/研发输入） |
| **B 现场 Demo** | Demo 脚本（故事线、演示步骤、异议回应、备用方案） |
| **C 案例包装** | 客户案例（可复制条件、讲解版本分角色） |
| **D 反馈转产品/研发** | 产品研发反馈单（边界、异常路径、验收标准） |

## 输入 / 输出

### 输入

- 客户名称 / 行业 / 规模
- 工作流类型（A/B/C/D）
- 已知业务流程与痛点
- 输出受众（客户 / 销售 / 产品 / 研发）

### 输出

- 结构化 Markdown 文档（见 `SKILL.md` 各工作流模板）
- 待验证问题清单
- 下一步行动表（Owner / 截止时间）

## 执行步骤

### 工作流 A：调研

1. 按六段访谈提纲执行（背景→流程→痛点→现有方案→成功标准→推进条件）
2. 填写调研纪要模板
3. 输出产品/研发输入表与待验证项

### 工作流 B：Demo

1. 明确 Demo 目标与听众角色
2. 设计故事线（场景→痛点→路径→结果→价值）
3. 编写演示步骤与异议回应
4. 准备网络/数据/权限备用方案

### 工作流 C：案例

1. 判断是否满足案例包装五条件
2. 填写案例结构（背景→问题→方案→过程→结果→可复制条件）
3. 输出面向客户/销售/研发的讲解版本

### 工作流 D：反馈转化

1. 六维判断（真实性、频次、价值、复用性、成本、时机）
2. 填写产品研发反馈单
3. 明确功能边界、异常路径与验收标准

## 捆绑资源

| 资源 | 路径 |
| --- | --- |
| 完整工作流与模板 | `SKILL.md` |
| Agent 元数据 | `_meta.json` |

## 常见误区

- ❌ 客户原话未经还原直接写入 PRD
- ❌ Demo 从产品功能菜单讲起
- ❌ 案例写成宣传稿，无可复制条件
- ❌ 研发反馈单缺少异常路径与验收标准
- ❌ 未经授权承诺价格、合同、交付周期

## 交付物清单

- [ ] 调研纪要或 Demo 脚本或案例或反馈单（按工作流）
- [ ] 事实 / 判断 / 待验证 三类标注清晰
- [ ] 产品侧：场景、价值、复用性、优先级
- [ ] 研发侧：输入、输出、边界、异常、验收
- [ ] 质量自检 7 项全部通过

## 与国内 FDE 生态关联

- 上游：`01-Foundation/Communication-Script-Library`、`02-Discovery/Business-Interview`
- 并行：`11-Best-Practice/FDE-Full-Lifecycle`
- 下游：`03-Solution-Design/PRD-Generator`、`07-Operations/FDE-Adoption-Growth`

## 关联 Skill

- [AIBP-Collaboration-Playbook](../../02-Discovery/AIBP-Collaboration-Playbook/README.md) — 双负责人协作
- [Executive-Communication-Framework](../../02-Discovery/Executive-Communication-Framework/README.md) — 客户汇报
- [Consultative-Problem-Solving](../../02-Discovery/Consultative-Problem-Solving/README.md) — PoC 假设来源
- [PRD-Generator](../../03-Solution-Design/PRD-Generator/README.md) — 反馈转规格
- [FDE-Adoption-Growth](../../07-Operations/FDE-Adoption-Growth/README.md) — 采纳运营

## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.1 | 2026-07-12 | FDE 场景增强：PoC/Beta/生产、AIBP、信创、采纳交叉引用 |
| v1.0.0 | 2026-07-12 | 从 `fde-customer-product-bridge-1.0.0` 迁移至 FDE-Skills 标准结构 |
