---
name: guardrail-design
display_name: Guardrail 设计 / Guardrail design
description: Guardrail 设计 / Guardrail design：需要阻止越权、无证据结论和危险工具动作。交付guardrail-design.md，包含证据、决策与失败处置。
version: 1.0.0
category: agent
tags:
- agent
- guardrail
- design
scenario: 需要阻止越权、无证据结论和危险工具动作
goal: 交付可复验的 guardrail-design.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要阻止越权、无证据结论和危险工具动作
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 威胁模型、业务禁区、输出规则、误拦成本
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: guardrail-design.md
  type: markdown
  description: Guardrail 设计 / Guardrail design的评审交付物
  required_fields:
  - 规则
  - 执行层
  - 检测
  - 动作
  - 误报漏报
  - 回归集
workflow:
- id: step-1
  action: 按输入、检索、生成、工具分层识别风险
  evidence: 记录本步骤的来源、判断和未决问题，写入 guardrail-design.md。
- id: step-2
  action: 将确定性规则放服务端
  evidence: 记录本步骤的来源、判断和未决问题，写入 guardrail-design.md。
- id: step-3
  action: 用对抗和正常样本测误拦与漏检
  evidence: 记录本步骤的来源、判断和未决问题，写入 guardrail-design.md。
- id: step-4
  action: 定义拒绝、降级、人审及记录策略
  evidence: 记录本步骤的来源、判断和未决问题，写入 guardrail-design.md。
constraints:
- 关键词过滤或模型自评不能作为唯一边界
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 关键禁止动作有确定性控制；每条规则有绕过测试
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
    criterion: 关键禁止动作有确定性控制；每条规则有绕过测试
    severity: critical
  - id: boundary-gate
    criterion: 关键词过滤或模型自评不能作为唯一边界
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Guardrail 设计 / Guardrail design

需要阻止越权、无证据结论和危险工具动作。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按输入、检索、生成、工具分层识别风险。
2. 将确定性规则放服务端。
3. 用对抗和正常样本测误拦与漏检。
4. 定义拒绝、降级、人审及记录策略。

## 边界与失败处理

- 关键词过滤或模型自评不能作为唯一边界。
- 检测服务不可用时高风险写操作失败关闭，普通只读按既定降级。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `guardrail-design.md`。完成后核对：关键禁止动作有确定性控制；每条规则有绕过测试。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
