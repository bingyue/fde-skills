---
name: 30-day-industry-learning
display_name: 30 天行业学习 / 30-day industry learning
description: 30 天行业学习 / 30-day industry learning：工程师需要在一个月形成可交付行业理解。交付learning-plan.md，包含证据、决策与失败处置。
version: 1.0.0
category: discovery
tags:
- discovery
- '30'
- day
- industry
- learning
scenario: 工程师需要在一个月形成可交付行业理解
goal: 交付可复验的 learning-plan.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 工程师需要在一个月形成可交付行业理解
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 目标行业、每日时间、可访问专家与资料
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: learning-plan.md
  type: markdown
  description: 30 天行业学习 / 30-day industry learning的评审交付物
  required_fields:
  - 周目标
  - 每日任务
  - 产物
  - 验证人
  - 复盘
workflow:
- id: step-1
  action: 第1周画价值链和术语表
  evidence: 记录本步骤的来源、判断和未决问题，写入 learning-plan.md。
- id: step-2
  action: 第2周观察真实任务并访谈角色
  evidence: 记录本步骤的来源、判断和未决问题，写入 learning-plan.md。
- id: step-3
  action: 第3周盘点数据与验证一个小场景
  evidence: 记录本步骤的来源、判断和未决问题，写入 learning-plan.md。
- id: step-4
  action: 第4周完成方案、评测设计和专家回讲
  evidence: 记录本步骤的来源、判断和未决问题，写入 learning-plan.md。
constraints:
- 不能用读书数量替代业务理解；无现场访问时明确替代证据
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每周有可审阅产物；第30天能讲清任务、风险、指标和验证路径
- 缺失关键证据时输出 blocked 与最小补证动作；不能把示例阈值视为客户已同意。
tools:
- name: workspace-files
  purpose: 读取授权材料并保存交付物；不依赖特定厂商。
  required: true
dependencies: []
examples:
- name: worked-example
  path: examples/example.yaml
evaluation:
  method: 使用正例与反例逐条审阅输出和操作记录；数值任务复算指标，系统任务验证后置条件。
  checks:
  - id: domain-gate
    criterion: 每周有可审阅产物；第30天能讲清任务、风险、指标和验证路径
    severity: critical
  - id: boundary-gate
    criterion: 不能用读书数量替代业务理解；无现场访问时明确替代证据
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 30 天行业学习 / 30-day industry learning

工程师需要在一个月形成可交付行业理解。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 第1周画价值链和术语表。
2. 第2周观察真实任务并访谈角色。
3. 第3周盘点数据与验证一个小场景。
4. 第4周完成方案、评测设计和专家回讲。

## 边界与失败处理

- 不能用读书数量替代业务理解；无现场访问时明确替代证据。
- 约不到专家时使用公开案例做暂定模型并记录验证缺口。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `learning-plan.md`。完成后核对：每周有可审阅产物；第30天能讲清任务、风险、指标和验证路径。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
