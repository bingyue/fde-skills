---
name: hallucination-evaluation
display_name: 幻觉评测 / Hallucination evaluation
description: 幻觉评测 / Hallucination evaluation：需要衡量模型无依据事实与错误确定性。交付hallucination-report.md，包含证据、决策与失败处置。
version: 1.0.0
category: evaluation
tags:
- evaluation
- hallucination
scenario: 需要衡量模型无依据事实与错误确定性
goal: 交付可复验的 hallucination-report.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要衡量模型无依据事实与错误确定性
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 回答、权威证据、可验证事实标注、未知问题
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: hallucination-report.md
  type: markdown
  description: 幻觉评测 / Hallucination evaluation的评审交付物
  required_fields:
  - 原子声明
  - 支持证据
  - 矛盾
  - 不可验证
  - 拒答
  - 严重性
workflow:
- id: step-1
  action: 拆回答为可核验声明
  evidence: 记录本步骤的来源、判断和未决问题，写入 hallucination-report.md。
- id: step-2
  action: 区分有支持、矛盾、缺支持、主观建议
  evidence: 记录本步骤的来源、判断和未决问题，写入 hallucination-report.md。
- id: step-3
  action: 设置答案为空和证据冲突挑战
  evidence: 记录本步骤的来源、判断和未决问题，写入 hallucination-report.md。
- id: step-4
  action: 按声明和任务两个分母报告风险
  evidence: 记录本步骤的来源、判断和未决问题，写入 hallucination-report.md。
constraints:
- 无法核实不自动等于事实错误；评审需显示证据
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 高风险错误单列；评审分歧有裁决；不能只报整体平均
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
    criterion: 高风险错误单列；评审分歧有裁决；不能只报整体平均
    severity: critical
  - id: boundary-gate
    criterion: 无法核实不自动等于事实错误；评审需显示证据
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 幻觉评测 / Hallucination evaluation

需要衡量模型无依据事实与错误确定性。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 拆回答为可核验声明。
2. 区分有支持、矛盾、缺支持、主观建议。
3. 设置答案为空和证据冲突挑战。
4. 按声明和任务两个分母报告风险。

## 边界与失败处理

- 无法核实不自动等于事实错误；评审需显示证据。
- 没有权威来源时标不可验证，不伪造正确答案。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `hallucination-report.md`。完成后核对：高风险错误单列；评审分歧有裁决；不能只报整体平均。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
