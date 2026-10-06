---
name: industry-research
display_name: 行业研究 / Industry research
description: 行业研究 / Industry research：FDE进入陌生行业需建立可验证的业务与约束模型。交付industry-brief.md，包含证据、决策与失败处置。
version: 1.0.0
category: discovery
tags:
- discovery
- industry
- research
scenario: FDE进入陌生行业需建立可验证的业务与约束模型
goal: 交付可复验的 industry-brief.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- FDE进入陌生行业需建立可验证的业务与约束模型
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 目标细分行业、地区、客户类型、研究期限
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: industry-brief.md
  type: markdown
  description: 行业研究 / Industry research的评审交付物
  required_fields:
  - 价值链
  - 工作流
  - 指标
  - 术语
  - 监管问题
  - 来源
  - 假设
workflow:
- id: step-1
  action: 界定细分市场和研究问题
  evidence: 记录本步骤的来源、判断和未决问题，写入 industry-brief.md。
- id: step-2
  action: 优先查官方统计、监管与一手企业资料
  evidence: 记录本步骤的来源、判断和未决问题，写入 industry-brief.md。
- id: step-3
  action: 把价值链映射到客户角色和信息流
  evidence: 记录本步骤的来源、判断和未决问题，写入 industry-brief.md。
- id: step-4
  action: 用客户访谈验证行业常识在该企业是否成立
  evidence: 记录本步骤的来源、判断和未决问题，写入 industry-brief.md。
constraints:
- 注明来源、日期与地区；行业平均不能代替客户基线
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 事实和推断分栏；每个关键结论有来源；列待验证问题
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
    criterion: 事实和推断分栏；每个关键结论有来源；列待验证问题
    severity: critical
  - id: boundary-gate
    criterion: 注明来源、日期与地区；行业平均不能代替客户基线
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 行业研究 / Industry research

FDE进入陌生行业需建立可验证的业务与约束模型。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 界定细分市场和研究问题。
2. 优先查官方统计、监管与一手企业资料。
3. 把价值链映射到客户角色和信息流。
4. 用客户访谈验证行业常识在该企业是否成立。

## 边界与失败处理

- 注明来源、日期与地区；行业平均不能代替客户基线。
- 资料互相矛盾时呈现口径差异，不强行合成确定数字。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `industry-brief.md`。完成后核对：事实和推断分栏；每个关键结论有来源；列待验证问题。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
