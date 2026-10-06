---
name: human-in-the-loop
display_name: 人工介入设计 / Human in the loop
description: 人工介入设计 / Human in the loop：自动化存在高影响决策或低置信度例外。交付hitl-design.md，包含证据、决策与失败处置。
version: 1.0.0
category: agent
tags:
- agent
- human
- in
- the
- loop
scenario: 自动化存在高影响决策或低置信度例外
goal: 交付可复验的 hitl-design.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 自动化存在高影响决策或低置信度例外
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 风险分类、任务状态、审批角色、响应时限
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: hitl-design.md
  type: markdown
  description: 人工介入设计 / Human in the loop的评审交付物
  required_fields:
  - 触发
  - 队列
  - 审核证据
  - 授权
  - 超时
  - 恢复
workflow:
- id: step-1
  action: 按不可逆影响和证据不足定义触发
  evidence: 记录本步骤的来源、判断和未决问题，写入 hitl-design.md。
- id: step-2
  action: 为审核者呈现来源、差异与可选动作
  evidence: 记录本步骤的来源、判断和未决问题，写入 hitl-design.md。
- id: step-3
  action: 绑定一次性批准到具体参数和版本
  evidence: 记录本步骤的来源、判断和未决问题，写入 hitl-design.md。
- id: step-4
  action: 定义超时、拒绝、撤销和恢复
  evidence: 记录本步骤的来源、判断和未决问题，写入 hitl-design.md。
constraints:
- 不能把沉默视为批准；修改参数后旧批准失效
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 无人处理时进入安全等待或取消；批准有主体和审计证据
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
    criterion: 无人处理时进入安全等待或取消；批准有主体和审计证据
    severity: critical
  - id: boundary-gate
    criterion: 不能把沉默视为批准；修改参数后旧批准失效
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 人工介入设计 / Human in the loop

自动化存在高影响决策或低置信度例外。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按不可逆影响和证据不足定义触发。
2. 为审核者呈现来源、差异与可选动作。
3. 绑定一次性批准到具体参数和版本。
4. 定义超时、拒绝、撤销和恢复。

## 边界与失败处理

- 不能把沉默视为批准；修改参数后旧批准失效。
- 审核队列超时不能自动通过，应升级或取消。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `hitl-design.md`。完成后核对：无人处理时进入安全等待或取消；批准有主体和审计证据。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
