---
name: observability-design
display_name: 日志与可观测性 / Logging & Observability
description: 日志与可观测性 / Logging & Observability：需要追踪AI失败、成本和用户任务结果。交付observability.md，包含证据、决策与失败处置。
version: 1.0.0
category: engineering
tags:
- engineering
- observability
- design
scenario: 需要追踪AI失败、成本和用户任务结果
goal: 交付可复验的 observability.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要追踪AI失败、成本和用户任务结果
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 用户旅程、组件边界、隐私限制、SLO
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: observability.md
  type: markdown
  description: 日志与可观测性 / Logging & Observability的评审交付物
  required_fields:
  - trace
  - 事件schema
  - 指标
  - 脱敏
  - 保留
  - 告警
  - runbook
workflow:
- id: step-1
  action: 为任务、检索、模型、工具建立trace关联
  evidence: 记录本步骤的来源、判断和未决问题，写入 observability.md。
- id: step-2
  action: 记录版本、用量、延迟和结果状态
  evidence: 记录本步骤的来源、判断和未决问题，写入 observability.md。
- id: step-3
  action: 设日志最小化与分级访问
  evidence: 记录本步骤的来源、判断和未决问题，写入 observability.md。
- id: step-4
  action: 用注入故障验证告警能定位到owner
  evidence: 记录本步骤的来源、判断和未决问题，写入 observability.md。
constraints:
- 默认不记录完整敏感prompt；采样不能抹掉关键安全事件
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 一次失败可串联到组件与版本；告警有动作并经演练
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
    criterion: 一次失败可串联到组件与版本；告警有动作并经演练
    severity: critical
  - id: boundary-gate
    criterion: 默认不记录完整敏感prompt；采样不能抹掉关键安全事件
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 日志与可观测性 / Logging & Observability

需要追踪AI失败、成本和用户任务结果。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 为任务、检索、模型、工具建立trace关联。
2. 记录版本、用量、延迟和结果状态。
3. 设日志最小化与分级访问。
4. 用注入故障验证告警能定位到owner。

## 边界与失败处理

- 默认不记录完整敏感prompt；采样不能抹掉关键安全事件。
- trace丢关联时修复传播，不能靠全量记录用户文本替代。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `observability.md`。完成后核对：一次失败可串联到组件与版本；告警有动作并经演练。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
