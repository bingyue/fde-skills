---
name: sla-design
display_name: SLA 设计 / SLA design
description: SLA 设计 / SLA design：企业需要约定可测服务承诺与故障响应。交付sla.md，包含证据、决策与失败处置。
version: 1.0.0
category: delivery
tags:
- delivery
- sla
- design
scenario: 企业需要约定可测服务承诺与故障响应
goal: 交付可复验的 sla.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 企业需要约定可测服务承诺与故障响应
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 业务关键度、架构能力、监测口径、值班资源
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: sla.md
  type: markdown
  description: SLA 设计 / SLA design的评审交付物
  required_fields:
  - SLI
  - SLO
  - 窗口
  - 排除项
  - 响应恢复
  - 误差预算
  - 升级
workflow:
- id: step-1
  action: 把用户可感知结果映射到SLI
  evidence: 记录本步骤的来源、判断和未决问题，写入 sla.md。
- id: step-2
  action: 定义测量点、窗口和分母
  evidence: 记录本步骤的来源、判断和未决问题，写入 sla.md。
- id: step-3
  action: 按成本与故障能力谈定SLO
  evidence: 记录本步骤的来源、判断和未决问题，写入 sla.md。
- id: step-4
  action: 绑定事件分级、响应、恢复与升级演练
  evidence: 记录本步骤的来源、判断和未决问题，写入 sla.md。
constraints:
- 不承诺无法测量或无人负责的可用性
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每项承诺有测量与责任角色；维护和依赖故障处理明确
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
    criterion: 每项承诺有测量与责任角色；维护和依赖故障处理明确
    severity: critical
  - id: boundary-gate
    criterion: 不承诺无法测量或无人负责的可用性
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# SLA 设计 / SLA design

企业需要约定可测服务承诺与故障响应。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 把用户可感知结果映射到SLI。
2. 定义测量点、窗口和分母。
3. 按成本与故障能力谈定SLO。
4. 绑定事件分级、响应、恢复与升级演练。

## 边界与失败处理

- 不承诺无法测量或无人负责的可用性。
- 没有夜间值班时不能承诺7×24人工响应。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `sla.md`。完成后核对：每项承诺有测量与责任角色；维护和依赖故障处理明确。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
