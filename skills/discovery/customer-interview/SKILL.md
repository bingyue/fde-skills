---
name: customer-interview
display_name: 客户需求访谈 / Customer interview
description: 客户需求访谈 / Customer interview：客户描述需求含糊，需要还原具体工作事件。交付interview-notes.md，包含证据、决策与失败处置。
version: 1.0.0
category: discovery
tags:
- discovery
- customer
- interview
scenario: 客户描述需求含糊，需要还原具体工作事件
goal: 交付可复验的 interview-notes.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 客户描述需求含糊，需要还原具体工作事件
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 最近三次业务事件、受访角色、访谈许可
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: interview-notes.md
  type: markdown
  description: 客户需求访谈 / Customer interview的评审交付物
  required_fields:
  - 角色
  - 事件时间线
  - 原话证据
  - 假设
  - 待核实问题
workflow:
- id: step-1
  action: 按决策者、操作者、IT分别取样，记录缺席角色
  evidence: 记录本步骤的来源、判断和未决问题，写入 interview-notes.md。
- id: step-2
  action: 让受访者复盘最近一次任务的触发、步骤、耗时和结果
  evidence: 记录本步骤的来源、判断和未决问题，写入 interview-notes.md。
- id: step-3
  action: 用实际工单核对口述与观察差异
  evidence: 记录本步骤的来源、判断和未决问题，写入 interview-notes.md。
- id: step-4
  action: 将原话、事实、推断分栏，回访确认冲突
  evidence: 记录本步骤的来源、判断和未决问题，写入 interview-notes.md。
constraints:
- 不要把客户提出的工具名称当成已验证需求
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每项需求能追溯到事件和角色；矛盾有责任人与验证动作
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
    criterion: 每项需求能追溯到事件和角色；矛盾有责任人与验证动作
    severity: critical
  - id: boundary-gate
    criterion: 不要把客户提出的工具名称当成已验证需求
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 客户需求访谈 / Customer interview

客户描述需求含糊，需要还原具体工作事件。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按决策者、操作者、IT分别取样，记录缺席角色。
2. 让受访者复盘最近一次任务的触发、步骤、耗时和结果。
3. 用实际工单核对口述与观察差异。
4. 将原话、事实、推断分栏，回访确认冲突。

## 边界与失败处理

- 不要把客户提出的工具名称当成已验证需求。
- 只有管理层意见时，标记一线证据缺失，安排观察再定范围。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `interview-notes.md`。完成后核对：每项需求能追溯到事件和角色；矛盾有责任人与验证动作。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
