---
name: tool-calling-evaluation
display_name: Tool Calling 评测 / Tool calling evaluation
description: Tool Calling 评测 / Tool calling evaluation：工具选择、参数、授权或重试可能错误。交付tool-eval-report.md，包含证据、决策与失败处置。
version: 1.0.0
category: evaluation
tags:
- evaluation
- tool
- calling
scenario: 工具选择、参数、授权或重试可能错误
goal: 交付可复验的 tool-eval-report.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 工具选择、参数、授权或重试可能错误
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 工具schema、任务样本、预期调用和系统状态
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: tool-eval-report.md
  type: markdown
  description: Tool Calling 评测 / Tool calling evaluation的评审交付物
  required_fields:
  - 选择
  - 参数
  - 顺序
  - 权限
  - 幂等
  - 超时
  - 后置条件
workflow:
- id: step-1
  action: 按任务定义允许与禁止调用
  evidence: 记录本步骤的来源、判断和未决问题，写入 tool-eval-report.md。
- id: step-2
  action: 测试边界参数和省略必要字段
  evidence: 记录本步骤的来源、判断和未决问题，写入 tool-eval-report.md。
- id: step-3
  action: 模拟超时、重复响应与部分成功
  evidence: 记录本步骤的来源、判断和未决问题，写入 tool-eval-report.md。
- id: step-4
  action: 同时验证调用轨迹与最终状态
  evidence: 记录本步骤的来源、判断和未决问题，写入 tool-eval-report.md。
constraints:
- 可解析参数不代表业务合法；生产副作用不能用于随意测试
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 错误参数被执行端拒绝；超时后不重复非幂等操作
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
    criterion: 错误参数被执行端拒绝；超时后不重复非幂等操作
    severity: critical
  - id: boundary-gate
    criterion: 可解析参数不代表业务合法；生产副作用不能用于随意测试
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Tool Calling 评测 / Tool calling evaluation

工具选择、参数、授权或重试可能错误。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按任务定义允许与禁止调用。
2. 测试边界参数和省略必要字段。
3. 模拟超时、重复响应与部分成功。
4. 同时验证调用轨迹与最终状态。

## 边界与失败处理

- 可解析参数不代表业务合法；生产副作用不能用于随意测试。
- 工具沙箱不模拟副作用时补状态模型，不能声称幂等测试通过。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `tool-eval-report.md`。完成后核对：错误参数被执行端拒绝；超时后不重复非幂等操作。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
