---
name: enterprise-acceptance
display_name: 企业交付验收 / Enterprise acceptance
description: 企业交付验收 / Enterprise acceptance：项目要证明合同需求和业务目标完成。交付acceptance-record.md，包含证据、决策与失败处置。
version: 1.0.0
category: delivery
tags:
- delivery
- enterprise
- acceptance
scenario: 项目要证明合同需求和业务目标完成
goal: 交付可复验的 acceptance-record.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 项目要证明合同需求和业务目标完成
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: SOW、需求追溯、评测与生产记录、培训和缺陷
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: acceptance-record.md
  type: markdown
  description: 企业交付验收 / Enterprise acceptance的评审交付物
  required_fields:
  - 需求ID
  - 证据
  - 业务结果
  - 缺陷
  - 例外
  - 签字
workflow:
- id: step-1
  action: 逐项追溯SOW到实现与验收
  evidence: 记录本步骤的来源、判断和未决问题，写入 acceptance-record.md。
- id: step-2
  action: 区分技术交付、用户采纳和价值验证
  evidence: 记录本步骤的来源、判断和未决问题，写入 acceptance-record.md。
- id: step-3
  action: 对未完成项约定责任与期限
  evidence: 记录本步骤的来源、判断和未决问题，写入 acceptance-record.md。
- id: step-4
  action: 由授权业务和运维代表签收
  evidence: 记录本步骤的来源、判断和未决问题，写入 acceptance-record.md。
constraints:
- 文档齐全不能替代业务结果；不得代签或伪造客户同意
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每项必须需求有通过/失败与证据；延期项有可追踪责任
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
    criterion: 每项必须需求有通过/失败与证据；延期项有可追踪责任
    severity: critical
  - id: boundary-gate
    criterion: 文档齐全不能替代业务结果；不得代签或伪造客户同意
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 企业交付验收 / Enterprise acceptance

项目要证明合同需求和业务目标完成。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 逐项追溯SOW到实现与验收。
2. 区分技术交付、用户采纳和价值验证。
3. 对未完成项约定责任与期限。
4. 由授权业务和运维代表签收。

## 边界与失败处理

- 文档齐全不能替代业务结果；不得代签或伪造客户同意。
- 签字人无授权时记录待批准，不以会议出席当验收。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `acceptance-record.md`。完成后核对：每项必须需求有通过/失败与证据；延期项有可追踪责任。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
