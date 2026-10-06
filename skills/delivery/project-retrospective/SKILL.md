---
name: project-retrospective
display_name: 项目复盘 / Project retrospective
description: 项目复盘 / Project retrospective：交付后需区分可复用经验与一次性补丁。交付retrospective.md，包含证据、决策与失败处置。
version: 1.0.0
category: delivery
tags:
- delivery
- project
- retrospective
scenario: 交付后需区分可复用经验与一次性补丁
goal: 交付可复验的 retrospective.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 交付后需区分可复用经验与一次性补丁
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 项目时间线、决策记录、指标、事故、客户反馈
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: retrospective.md
  type: markdown
  description: 项目复盘 / Project retrospective的评审交付物
  required_fields:
  - 预期实际
  - 根因
  - 有效做法
  - 改进
  - 资产
  - owner
workflow:
- id: step-1
  action: 重建关键决策和结果
  evidence: 记录本步骤的来源、判断和未决问题，写入 retrospective.md。
- id: step-2
  action: 对延误、错误与收益做证据归因
  evidence: 记录本步骤的来源、判断和未决问题，写入 retrospective.md。
- id: step-3
  action: 提炼可复用规则并列适用边界
  evidence: 记录本步骤的来源、判断和未决问题，写入 retrospective.md。
- id: step-4
  action: 把行动变为有owner和验证日期的改进项
  evidence: 记录本步骤的来源、判断和未决问题，写入 retrospective.md。
constraints:
- 避免责备个体或事后把已知结果写成当时显然结论
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个行动对应证据、负责人、验收物；记录未确定原因
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
    criterion: 每个行动对应证据、负责人、验收物；记录未确定原因
    severity: critical
  - id: boundary-gate
    criterion: 避免责备个体或事后把已知结果写成当时显然结论
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 项目复盘 / Project retrospective

交付后需区分可复用经验与一次性补丁。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 重建关键决策和结果。
2. 对延误、错误与收益做证据归因。
3. 提炼可复用规则并列适用边界。
4. 把行动变为有owner和验证日期的改进项。

## 边界与失败处理

- 避免责备个体或事后把已知结果写成当时显然结论。
- 没有决策记录时标回忆证据，先做补充访谈。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `retrospective.md`。完成后核对：每个行动对应证据、负责人、验收物；记录未确定原因。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
