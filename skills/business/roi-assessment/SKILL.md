---
name: roi-assessment
display_name: ROI 评估 / ROI assessment
description: ROI 评估 / ROI assessment：PoC立项或复盘需要可追溯的价值模型。交付roi-model.md，包含证据、决策与失败处置。
version: 1.0.0
category: business
tags:
- business
- roi
- assessment
scenario: PoC立项或复盘需要可追溯的价值模型
goal: 交付可复验的 roi-model.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- PoC立项或复盘需要可追溯的价值模型
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 任务量、单位耗时、人工单价、采用率、开发和运营成本
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: roi-model.md
  type: markdown
  description: ROI 评估 / ROI assessment的评审交付物
  required_fields:
  - 假设
  - 收益公式
  - 成本
  - 净收益
  - 回本期
  - 敏感性
workflow:
- id: step-1
  action: 建立人工或规则基线并固定观察周期
  evidence: 记录本步骤的来源、判断和未决问题，写入 roi-model.md。
- id: step-2
  action: 用任务量×节省时间×采用率×可兑现比例估算收益
  evidence: 记录本步骤的来源、判断和未决问题，写入 roi-model.md。
- id: step-3
  action: 计入集成、复核、推理和维护全成本
  evidence: 记录本步骤的来源、判断和未决问题，写入 roi-model.md。
- id: step-4
  action: 输出保守/基准/乐观区间并区分预测与实测
  evidence: 记录本步骤的来源、判断和未决问题，写入 roi-model.md。
constraints:
- 节省工时不直接等于现金节省；收入增量需归因对照
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 公式单位一致；零或负净收益不生成虚假回本期
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
    criterion: 公式单位一致；零或负净收益不生成虚假回本期
    severity: critical
  - id: boundary-gate
    criterion: 节省工时不直接等于现金节省；收入增量需归因对照
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# ROI 评估 / ROI assessment

PoC立项或复盘需要可追溯的价值模型。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 建立人工或规则基线并固定观察周期。
2. 用任务量×节省时间×采用率×可兑现比例估算收益。
3. 计入集成、复核、推理和维护全成本。
4. 输出保守/基准/乐观区间并区分预测与实测。

## 边界与失败处理

- 节省工时不直接等于现金节省；收入增量需归因对照。
- 采用率未知时给敏感性范围，不报告确定收益。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `roi-model.md`。完成后核对：公式单位一致；零或负净收益不生成虚假回本期。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
