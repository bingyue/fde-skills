---
name: customer-discovery
display_name: 客户发现 / Customer discovery
description: 客户发现 / Customer discovery：正式开发前需要确认问题、采购、采纳与交付条件。交付discovery-report.md，包含证据、决策与失败处置。
version: 1.0.0
category: discovery
tags:
- discovery
- customer
scenario: 正式开发前需要确认问题、采购、采纳与交付条件
goal: 交付可复验的 discovery-report.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 正式开发前需要确认问题、采购、采纳与交付条件
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 客户诉求、组织背景、访谈和观察入口
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: discovery-report.md
  type: markdown
  description: 客户发现 / Customer discovery的评审交付物
  required_fields:
  - 问题证据
  - 业务基线
  - 决策链
  - 数据条件
  - 购买采纳
  - 下一实验
workflow:
- id: step-1
  action: 建立关键假设清单
  evidence: 记录本步骤的来源、判断和未决问题，写入 discovery-report.md。
- id: step-2
  action: 组合访谈与现场观察核验任务
  evidence: 记录本步骤的来源、判断和未决问题，写入 discovery-report.md。
- id: step-3
  action: 确认预算、数据owner、使用者与验收人
  evidence: 记录本步骤的来源、判断和未决问题，写入 discovery-report.md。
- id: step-4
  action: 用最小实验验证价值与交付可行性
  evidence: 记录本步骤的来源、判断和未决问题，写入 discovery-report.md。
constraints:
- 访谈认可不能等同采购意愿或采用承诺
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个核心假设有支持/反证；下一步含停止条件
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
    criterion: 每个核心假设有支持/反证；下一步含停止条件
    severity: critical
  - id: boundary-gate
    criterion: 访谈认可不能等同采购意愿或采用承诺
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 客户发现 / Customer discovery

正式开发前需要确认问题、采购、采纳与交付条件。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 建立关键假设清单。
2. 组合访谈与现场观察核验任务。
3. 确认预算、数据owner、使用者与验收人。
4. 用最小实验验证价值与交付可行性。

## 边界与失败处理

- 访谈认可不能等同采购意愿或采用承诺。
- 没有实际使用者参与时暂缓需求冻结，继续发现。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `discovery-report.md`。完成后核对：每个核心假设有支持/反证；下一步含停止条件。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
