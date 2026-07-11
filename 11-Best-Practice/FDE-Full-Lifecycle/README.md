# FDE-Full-Lifecycle

- **分类**：`11-Best-Practice`
- **成熟度**：`usable`
- **版本**：`1.0.0`（源自 ClawHub `fde`）
- **一句话**：FDE 全流程助手——审计 → 评估 → 部署 → 产品化抽象

---

## 适用场景

- 接到客户现场部署/交付任务，需要系统化方法论
- 将 AI 模型能力嵌入客户业务流程
- 评估 AI 落地可行性与业务价值
- 将定制化方案抽象为可复用平台能力
- FDE 面试准备或职业转型演练

## 问题定义

FDE 不是「按需求文档开发」的传统工程师，而是嵌入客户现场、以业务结果（outcome）为导向的复合角色。本 Skill 把 Palantir 起源的 FDE 模式与 Echo-Delta 协作、三阶段工作流和产品化飞轮整合为可执行交付包。

## 方法论框架

### FDE 三阶段工作流

| 阶段 | 目标 | 关键产出 |
| --- | --- | --- |
| **Audit 审计** | 理解真实业务流程，建立信任 | 痛点矩阵、数据盘点、技术约束、干系人图谱 |
| **Evals 评估** | 业务需求技术翻译，验证可行性 | 技术方案、POC 结果、ROI、风险矩阵 |
| **Deployment 部署** | 生产落地与持续迭代 | 可运行方案、UAT 报告、运维手册、价值报告 |

### Echo-Delta 协作模式

- **Echo（回声）**：行业专家视角，深度理解业务，不做技术假设
- **Delta（三角洲）**：FDE 工程师视角，快速原型、集成、部署
- 执行时在两个角色间灵活切换

### 产品化抽象闭环

```text
客户现场经验 → 沉淀解决方案 → 抽象平台能力 → 复用下一客户 → 效率指数增长
```

每个项目结束执行抽象检查：通用组件、行业 Know-how 模板化、反馈产品团队优先级。

## 输入 / 输出

### 输入

- 客户行业与业务背景
- 部署任务范围与周期
- 已知痛点或立项材料

### 输出

- 结构化客户审计报告（可用 `scripts/client_audit.py`）
- 技术方案与 POC 验证结论
- ROI 与风险矩阵
- 部署检查表与运维手册要点
- 产品化抽象建议清单

## 执行步骤

### 准备阶段

1. 加载 `references/fde-framework.md` 审计清单
2. 运行 `scripts/client_audit.py` 生成定制化审计问卷
3. 识别干系人并安排分角色访谈

### Audit 阶段

1. 利益相关者访谈（业务/技术/管理层）
2. 业务流程映射（As-Is）与痛点识别
3. 数据资产盘点与权限评估
4. 技术环境评估

### Evals 阶段

1. 需求技术翻译与 MVP 方案设计
2. 最小成本 POC 验证核心路径
3. 业务指标与技术指标映射
4. 风险识别与缓解方案

### Deployment 阶段

1. 快速原型开发与系统集成
2. UAT 与灰度上线
3. 迭代优化与知识转移
4. 产品化抽象检查

## 捆绑资源

| 资源 | 路径 | 用途 |
| --- | --- | --- |
| 方法论详解 | `references/fde-framework.md` | 审计清单、评估框架、部署检查表 |
| 技术工具包 | `references/fde-toolkit.md` | RAG、模型选型、集成模式 |
| 行业案例库 | `references/fde-cases.md` | 制造/农业/金融/医疗等行业案例 |
| 客户审计工具 | `scripts/client_audit.py` | 生成结构化审计问卷与报告 |
| Agent 调用入口 | `SKILL.md` | 完整三阶段工作流与使用指南 |

## 常见误区

- ❌ 跳过 Audit 直接写代码
- ❌ 只做功能交付（output）不追踪业务结果（outcome）
- ❌ 项目结束不做产品化抽象，无法形成飞轮
- ❌ Echo 与 Delta 角色混淆，过早做技术假设

## 交付物清单

- [ ] 客户审计报告
- [ ] 痛点优先级矩阵（影响 × 可行性）
- [ ] 技术方案与 POC 结论
- [ ] ROI 与风险矩阵
- [ ] 部署与运维要点
- [ ] 产品化抽象建议

## 与国内 FDE 生态关联

- 上游：`01-Foundation/Stakeholder-Mapping`、`02-Discovery/Business-Interview`
- 并行：`11-Best-Practice/China-FDE-Consulting-Pattern`（国内咨询式总纲）
- 下游：`05-Deployment/Private-Deployment-Gateway`、`07-Operations/FDE-Adoption-Growth`

## 关联 Skill

- `Palantir-FDE-Pattern` — 国际 FDE 模式对照
- `FDE-Customer-Product-Bridge` — 客户现场转产品/研发输入
- `Diagnostic-FDE` — ToB 售前 12 步方案包

## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.0.0 | 2026-07-12 | 从 ClawHub `fde-1.0.0` 迁移至 FDE-Skills 标准结构 |
