---
name: poc-to-production
display_name: PoC 到生产 / PoC to Production
description: PoC 到生产 / PoC to Production：PoC指标达标，需要补齐企业运行和采纳能力。交付production-plan.md，包含证据、决策与失败处置。
version: 1.0.0
category: deployment
tags:
- deployment
- poc
- to
- production
scenario: PoC指标达标，需要补齐企业运行和采纳能力
goal: 交付可复验的 production-plan.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- PoC指标达标，需要补齐企业运行和采纳能力
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: PoC报告、差距清单、生产需求、owner和预算
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: production-plan.md
  type: markdown
  description: PoC 到生产 / PoC to Production的评审交付物
  required_fields:
  - 差距
  - 依赖
  - 安全
  - 扩容
  - 运维
  - 灰度
  - 移交
workflow:
- id: step-1
  action: 将PoC假设与生产流量、数据、权限逐项对照
  evidence: 记录本步骤的来源、判断和未决问题，写入 production-plan.md。
- id: step-2
  action: 补测试、身份、观测、备份与恢复
  evidence: 记录本步骤的来源、判断和未决问题，写入 production-plan.md。
- id: step-3
  action: 按内部试用→受限Beta→灰度推进
  evidence: 记录本步骤的来源、判断和未决问题，写入 production-plan.md。
- id: step-4
  action: 每阶段独立审核技术与业务采纳证据
  evidence: 记录本步骤的来源、判断和未决问题，写入 production-plan.md。
constraints:
- 禁止把PoC数据和临时凭据直接带入生产
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个差距有负责人和门禁；灰度有回滚与值班；业务owner接管
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
    criterion: 每个差距有负责人和门禁；灰度有回滚与值班；业务owner接管
    severity: critical
  - id: boundary-gate
    criterion: 禁止把PoC数据和临时凭据直接带入生产
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# PoC 到生产 / PoC to Production

PoC指标达标，需要补齐企业运行和采纳能力。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 将PoC假设与生产流量、数据、权限逐项对照。
2. 补测试、身份、观测、备份与恢复。
3. 按内部试用→受限Beta→灰度推进。
4. 每阶段独立审核技术与业务采纳证据。

## 边界与失败处理

- 禁止把PoC数据和临时凭据直接带入生产。
- 无法验证隔离或恢复时保持PoC状态，不标生产完成。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `production-plan.md`。完成后核对：每个差距有负责人和门禁；灰度有回滚与值班；业务owner接管。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
