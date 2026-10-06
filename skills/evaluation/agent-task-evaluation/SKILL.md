---
name: agent-task-evaluation
display_name: Agent 任务成功率 / Agent task success
description: Agent 任务成功率 / Agent task success：Agent能调用工具但业务任务是否完成尚不明确。交付agent-eval-report.md，包含证据、决策与失败处置。
version: 1.0.0
category: evaluation
tags:
- evaluation
- agent
- task
scenario: Agent能调用工具但业务任务是否完成尚不明确
goal: 交付可复验的 agent-eval-report.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- Agent能调用工具但业务任务是否完成尚不明确
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 任务集、系统后置条件、工具轨迹、预算
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: agent-eval-report.md
  type: markdown
  description: Agent 任务成功率 / Agent task success的评审交付物
  required_fields:
  - 任务成功率
  - 部分完成
  - 副作用
  - 预算
  - 失败归因
workflow:
- id: step-1
  action: 将任务完成定义为可检查系统状态
  evidence: 记录本步骤的来源、判断和未决问题，写入 agent-eval-report.md。
- id: step-2
  action: 在隔离环境复放正常和异常任务
  evidence: 记录本步骤的来源、判断和未决问题，写入 agent-eval-report.md。
- id: step-3
  action: 测成功率、重复副作用、人工接管和成本
  evidence: 记录本步骤的来源、判断和未决问题，写入 agent-eval-report.md。
- id: step-4
  action: 对失败按规划、工具、数据、环境归因
  evidence: 记录本步骤的来源、判断和未决问题，写入 agent-eval-report.md。
constraints:
- 不能以Agent自述完成或工具HTTP200判定任务成功
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个成功都有后置条件证据；副作用和预算独立门槛
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
    criterion: 每个成功都有后置条件证据；副作用和预算独立门槛
    severity: critical
  - id: boundary-gate
    criterion: 不能以Agent自述完成或工具HTTP200判定任务成功
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Agent 任务成功率 / Agent task success

Agent能调用工具但业务任务是否完成尚不明确。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 将任务完成定义为可检查系统状态。
2. 在隔离环境复放正常和异常任务。
3. 测成功率、重复副作用、人工接管和成本。
4. 对失败按规划、工具、数据、环境归因。

## 边界与失败处理

- 不能以Agent自述完成或工具HTTP200判定任务成功。
- 无沙箱写入权限时仅测dry-run并说明不能证明实际任务完成。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `agent-eval-report.md`。完成后核对：每个成功都有后置条件证据；副作用和预算独立门槛。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
