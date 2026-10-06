---
name: go-live-checklist
display_name: 上线检查 / Go-live checklist
description: 上线检查 / Go-live checklist：试点即将进入真实企业业务流。交付go-live.md，包含证据、决策与失败处置。
version: 1.0.0
category: deployment
tags:
- deployment
- go
- live
- checklist
scenario: 试点即将进入真实企业业务流
goal: 交付可复验的 go-live.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 试点即将进入真实企业业务流
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 发布物、评测、安全、监控、值班和回滚证据
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: go-live.md
  type: markdown
  description: 上线检查 / Go-live checklist的评审交付物
  required_fields:
  - 检查项
  - 证据
  - owner
  - 状态
  - 风险例外
  - 发布决定
workflow:
- id: step-1
  action: 固定发布版本并汇集评测报告
  evidence: 记录本步骤的来源、判断和未决问题，写入 go-live.md。
- id: step-2
  action: 检查身份、容量、观测、备份与回滚
  evidence: 记录本步骤的来源、判断和未决问题，写入 go-live.md。
- id: step-3
  action: 让业务与运维分别验收职责
  evidence: 记录本步骤的来源、判断和未决问题，写入 go-live.md。
- id: step-4
  action: 决定go/no-go并限定灰度范围
  evidence: 记录本步骤的来源、判断和未决问题，写入 go-live.md。
constraints:
- 缺失关键证据不能勾选通过；风险例外必须有期限和责任人
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 关键项全有可复验记录；no-go条件明确
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
    criterion: 关键项全有可复验记录；no-go条件明确
    severity: critical
  - id: boundary-gate
    criterion: 缺失关键证据不能勾选通过；风险例外必须有期限和责任人
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 上线检查 / Go-live checklist

试点即将进入真实企业业务流。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 固定发布版本并汇集评测报告。
2. 检查身份、容量、观测、备份与回滚。
3. 让业务与运维分别验收职责。
4. 决定go/no-go并限定灰度范围。

## 边界与失败处理

- 缺失关键证据不能勾选通过；风险例外必须有期限和责任人。
- 回滚依赖不可逆数据库迁移时补备份和前向修复方案。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `go-live.md`。完成后核对：关键项全有可复验记录；no-go条件明确。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
