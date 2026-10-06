---
name: prompt-regression
display_name: Prompt 回归 / Prompt regression
description: Prompt 回归 / Prompt regression：prompt、模型或上下文变更可能破坏既有行为。交付prompt-regression.md，包含证据、决策与失败处置。
version: 1.0.0
category: evaluation
tags:
- evaluation
- prompt
- regression
scenario: prompt、模型或上下文变更可能破坏既有行为
goal: 交付可复验的 prompt-regression.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- prompt、模型或上下文变更可能破坏既有行为
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 基准版本、候选版本、冻结测试集、成本延迟预算
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: prompt-regression.md
  type: markdown
  description: Prompt 回归 / Prompt regression的评审交付物
  required_fields:
  - 版本
  - 配对结果
  - 关键切片
  - 波动
  - 退化
  - 发布决定
workflow:
- id: step-1
  action: 冻结模型设置与检索上下文
  evidence: 记录本步骤的来源、判断和未决问题，写入 prompt-regression.md。
- id: step-2
  action: 对同一任务配对运行新旧版本
  evidence: 记录本步骤的来源、判断和未决问题，写入 prompt-regression.md。
- id: step-3
  action: 对随机性重复抽样并报告不确定性
  evidence: 记录本步骤的来源、判断和未决问题，写入 prompt-regression.md。
- id: step-4
  action: 关键切片不退化才进入灰度
  evidence: 记录本步骤的来源、判断和未决问题，写入 prompt-regression.md。
constraints:
- 不凭少数精选Demo批准变更；不得用测试答案优化候选
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 有每例diff与aggregate；安全失败阻断；成本增量有解释
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
    criterion: 有每例diff与aggregate；安全失败阻断；成本增量有解释
    severity: critical
  - id: boundary-gate
    criterion: 不凭少数精选Demo批准变更；不得用测试答案优化候选
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Prompt 回归 / Prompt regression

prompt、模型或上下文变更可能破坏既有行为。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 冻结模型设置与检索上下文。
2. 对同一任务配对运行新旧版本。
3. 对随机性重复抽样并报告不确定性。
4. 关键切片不退化才进入灰度。

## 边界与失败处理

- 不凭少数精选Demo批准变更；不得用测试答案优化候选。
- 模型供应商漂移时记录实际版本并重新建基线。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `prompt-regression.md`。完成后核对：有每例diff与aggregate；安全失败阻断；成本增量有解释。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
