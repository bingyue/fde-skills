---
name: multi-agent-design
display_name: 多 Agent 设计 / Multi-Agent design
description: 多 Agent 设计 / Multi-Agent design：单Agent存在可测瓶颈，考虑协作分工。交付multi-agent-design.md，包含证据、决策与失败处置。
version: 1.0.0
category: agent
tags:
- agent
- multi
- design
scenario: 单Agent存在可测瓶颈，考虑协作分工
goal: 交付可复验的 multi-agent-design.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 单Agent存在可测瓶颈，考虑协作分工
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 单Agent基线、可分解任务、共享状态与预算
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: multi-agent-design.md
  type: markdown
  description: 多 Agent 设计 / Multi-Agent design的评审交付物
  required_fields:
  - 角色
  - 消息契约
  - 调度
  - 仲裁
  - 预算
  - 对照结果
workflow:
- id: step-1
  action: 先记录单Agent错误与延迟
  evidence: 记录本步骤的来源、判断和未决问题，写入 multi-agent-design.md。
- id: step-2
  action: 仅将独立任务拆给专业角色
  evidence: 记录本步骤的来源、判断和未决问题，写入 multi-agent-design.md。
- id: step-3
  action: 定义消息结构、版本、超时与冲突仲裁
  evidence: 记录本步骤的来源、判断和未决问题，写入 multi-agent-design.md。
- id: step-4
  action: 测并行收益、重复成本和合并错误后决定是否采用
  evidence: 记录本步骤的来源、判断和未决问题，写入 multi-agent-design.md。
constraints:
- 不能因多Agent流行而拆分；共享写操作需串行或事务保护
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 多Agent对照改善约定指标；合并失败有确定处理
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
    criterion: 多Agent对照改善约定指标；合并失败有确定处理
    severity: critical
  - id: boundary-gate
    criterion: 不能因多Agent流行而拆分；共享写操作需串行或事务保护
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 多 Agent 设计 / Multi-Agent design

单Agent存在可测瓶颈，考虑协作分工。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 先记录单Agent错误与延迟。
2. 仅将独立任务拆给专业角色。
3. 定义消息结构、版本、超时与冲突仲裁。
4. 测并行收益、重复成本和合并错误后决定是否采用。

## 边界与失败处理

- 不能因多Agent流行而拆分；共享写操作需串行或事务保护。
- 结论冲突时列证据差异，不能投票代替事实核验。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `multi-agent-design.md`。完成后核对：多Agent对照改善约定指标；合并失败有确定处理。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
