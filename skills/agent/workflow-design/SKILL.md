---
name: workflow-design
display_name: 工作流设计 / Workflow design
description: 工作流设计 / Workflow design：稳定业务过程需要可重试、可恢复的自动化。交付workflow.md，包含证据、决策与失败处置。
version: 1.0.0
category: agent
tags:
- agent
- workflow
- design
scenario: 稳定业务过程需要可重试、可恢复的自动化
goal: 交付可复验的 workflow.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 稳定业务过程需要可重试、可恢复的自动化
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 现状流程、业务事件、接口副作用、人工步骤
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: workflow.md
  type: markdown
  description: 工作流设计 / Workflow design的评审交付物
  required_fields:
  - 状态
  - 转移条件
  - 事件
  - 幂等键
  - 超时
  - 补偿
workflow:
- id: step-1
  action: 建模状态与持久化事件
  evidence: 记录本步骤的来源、判断和未决问题，写入 workflow.md。
- id: step-2
  action: 区分可重试读操作与非幂等写操作
  evidence: 记录本步骤的来源、判断和未决问题，写入 workflow.md。
- id: step-3
  action: 为每条转移定义守卫和后置条件
  evidence: 记录本步骤的来源、判断和未决问题，写入 workflow.md。
- id: step-4
  action: 演练断点恢复、重复消息及人工取消
  evidence: 记录本步骤的来源、判断和未决问题，写入 workflow.md。
constraints:
- 不要将模型生成文本直接当状态转换指令
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 重复事件不会重复执行副作用；可从任一持久化状态恢复
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
    criterion: 重复事件不会重复执行副作用；可从任一持久化状态恢复
    severity: critical
  - id: boundary-gate
    criterion: 不要将模型生成文本直接当状态转换指令
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 工作流设计 / Workflow design

稳定业务过程需要可重试、可恢复的自动化。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 建模状态与持久化事件。
2. 区分可重试读操作与非幂等写操作。
3. 为每条转移定义守卫和后置条件。
4. 演练断点恢复、重复消息及人工取消。

## 边界与失败处理

- 不要将模型生成文本直接当状态转换指令。
- 预约API响应丢失时先查询状态，不能直接再次创建。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `workflow.md`。完成后核对：重复事件不会重复执行副作用；可从任一持久化状态恢复。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
