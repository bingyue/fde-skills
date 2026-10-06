---
name: cost-assessment
display_name: 成本评估 / Cost assessment
description: 成本评估 / Cost assessment：需要预算推理、存储、集成和运维总成本。交付cost-model.md，包含证据、决策与失败处置。
version: 1.0.0
category: business
tags:
- business
- cost
- assessment
scenario: 需要预算推理、存储、集成和运维总成本
goal: 交付可复验的 cost-model.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要预算推理、存储、集成和运维总成本
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 任务量、token分布、模型价格日期、人工复核、基础设施
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: cost-model.md
  type: markdown
  description: 成本评估 / Cost assessment的评审交付物
  required_fields:
  - 单位成本
  - 固定变动
  - 峰值
  - 复核
  - 敏感性
  - 预算告警
workflow:
- id: step-1
  action: 按任务追踪输入输出token和工具次数
  evidence: 记录本步骤的来源、判断和未决问题，写入 cost-model.md。
- id: step-2
  action: 分摊固定设施与集成维护
  evidence: 记录本步骤的来源、判断和未决问题，写入 cost-model.md。
- id: step-3
  action: 计算平均和高分位负载成本
  evidence: 记录本步骤的来源、判断和未决问题，写入 cost-model.md。
- id: step-4
  action: 模拟采用率、缓存和模型变化
  evidence: 记录本步骤的来源、判断和未决问题，写入 cost-model.md。
constraints:
- 使用核验价格与币种日期；不只报单次模型费用
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 公式可复算；固定成本与变动成本分开；预算超限有策略
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
    criterion: 公式可复算；固定成本与变动成本分开；预算超限有策略
    severity: critical
  - id: boundary-gate
    criterion: 使用核验价格与币种日期；不只报单次模型费用
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 成本评估 / Cost assessment

需要预算推理、存储、集成和运维总成本。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按任务追踪输入输出token和工具次数。
2. 分摊固定设施与集成维护。
3. 计算平均和高分位负载成本。
4. 模拟采用率、缓存和模型变化。

## 边界与失败处理

- 使用核验价格与币种日期；不只报单次模型费用。
- 没有价格证据时标估算，保留价格参数不写实时报价。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `cost-model.md`。完成后核对：公式可复算；固定成本与变动成本分开；预算超限有策略。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
