---
name: enterprise-ai-diagnosis
display_name: 企业 AI 诊断 / Enterprise AI diagnosis
description: 企业 AI 诊断 / Enterprise AI diagnosis：企业提出宽泛AI转型目标，需要形成证据驱动的进入方案。交付diagnosis-report.md，包含证据、决策与失败处置。
version: 1.0.0
category: diagnosis
tags:
- diagnosis
- enterprise
- ai
scenario: 企业提出宽泛AI转型目标，需要形成证据驱动的进入方案
goal: 交付可复验的 diagnosis-report.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 企业提出宽泛AI转型目标，需要形成证据驱动的进入方案
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 客户目标、业务基线、流程、数据、组织和运行约束
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: diagnosis-report.md
  type: markdown
  description: 企业 AI 诊断 / Enterprise AI diagnosis的评审交付物
  required_fields:
  - 问题树
  - 证据
  - 成熟度
  - 机会
  - 优先级
  - PoC建议
  - 停止项
workflow:
- id: step-1
  action: 重述目标并区分症状与业务结果
  evidence: 记录本步骤的来源、判断和未决问题，写入 diagnosis-report.md。
- id: step-2
  action: 联合访谈、观察、数据盘点构建问题树
  evidence: 记录本步骤的来源、判断和未决问题，写入 diagnosis-report.md。
- id: step-3
  action: 评估AI与流程/规则替代并识别阻塞
  evidence: 记录本步骤的来源、判断和未决问题，写入 diagnosis-report.md。
- id: step-4
  action: 给出一个首选PoC、备选和不做清单
  evidence: 记录本步骤的来源、判断和未决问题，写入 diagnosis-report.md。
constraints:
- 证据不足必须标假设；不得把售前建议当生产承诺
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 结论可追溯原始证据；首选有owner、范围、评测、预算与退出条件
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
    criterion: 结论可追溯原始证据；首选有owner、范围、评测、预算与退出条件
    severity: critical
  - id: boundary-gate
    criterion: 证据不足必须标假设；不得把售前建议当生产承诺
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 企业 AI 诊断 / Enterprise AI diagnosis

企业提出宽泛AI转型目标，需要形成证据驱动的进入方案。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 重述目标并区分症状与业务结果。
2. 联合访谈、观察、数据盘点构建问题树。
3. 评估AI与流程/规则替代并识别阻塞。
4. 给出一个首选PoC、备选和不做清单。

## 边界与失败处理

- 证据不足必须标假设；不得把售前建议当生产承诺。
- 没有业务基线时输出诊断缺口与取证计划，不虚构ROI。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `diagnosis-report.md`。完成后核对：结论可追溯原始证据；首选有owner、范围、评测、预算与退出条件。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
