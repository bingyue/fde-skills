---
name: pain-point-analysis
display_name: 痛点识别 / Pain point analysis
description: 痛点识别 / Pain point analysis：客户抱怨很多但缺乏根因与优先级证据。交付pain-register.md，包含证据、决策与失败处置。
version: 1.0.0
category: diagnosis
tags:
- diagnosis
- pain
- point
- analysis
scenario: 客户抱怨很多但缺乏根因与优先级证据
goal: 交付可复验的 pain-register.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 客户抱怨很多但缺乏根因与优先级证据
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 访谈纪要、流程图、失败样本、损失记录
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: pain-register.md
  type: markdown
  description: 痛点识别 / Pain point analysis的评审交付物
  required_fields:
  - 症状
  - 根因假设
  - 证据
  - 影响
  - 验证实验
workflow:
- id: step-1
  action: 把抱怨改写为可观察结果偏差
  evidence: 记录本步骤的来源、判断和未决问题，写入 pain-register.md。
- id: step-2
  action: 用问题树拆解流程、数据、系统、行为原因
  evidence: 记录本步骤的来源、判断和未决问题，写入 pain-register.md。
- id: step-3
  action: 用反例检验因果并记录替代解释
  evidence: 记录本步骤的来源、判断和未决问题，写入 pain-register.md。
- id: step-4
  action: 以发生频率和单位损失估算影响区间
  evidence: 记录本步骤的来源、判断和未决问题，写入 pain-register.md。
constraints:
- 相关性不能当成根因；缺数字时保留区间假设
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个高影响痛点有验证方法和反证条件
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
    criterion: 每个高影响痛点有验证方法和反证条件
    severity: critical
  - id: boundary-gate
    criterion: 相关性不能当成根因；缺数字时保留区间假设
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 痛点识别 / Pain point analysis

客户抱怨很多但缺乏根因与优先级证据。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 把抱怨改写为可观察结果偏差。
2. 用问题树拆解流程、数据、系统、行为原因。
3. 用反例检验因果并记录替代解释。
4. 以发生频率和单位损失估算影响区间。

## 边界与失败处理

- 相关性不能当成根因；缺数字时保留区间假设。
- 看不到失败样本时不归因模型能力，先请求脱敏样本。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `pain-register.md`。完成后核对：每个高影响痛点有验证方法和反证条件。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
