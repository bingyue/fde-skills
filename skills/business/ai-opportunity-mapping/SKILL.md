---
name: ai-opportunity-mapping
display_name: AI 机会地图 / AI opportunity mapping
description: AI 机会地图 / AI opportunity mapping：需要跨部门识别可复用、可投资的AI机会组合。交付opportunity-map.md，包含证据、决策与失败处置。
version: 1.0.0
category: business
tags:
- business
- ai
- opportunity
- mapping
scenario: 需要跨部门识别可复用、可投资的AI机会组合
goal: 交付可复验的 opportunity-map.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要跨部门识别可复用、可投资的AI机会组合
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 价值链、流程、场景卡、数据资产、组织约束
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: opportunity-map.md
  type: markdown
  description: AI 机会地图 / AI opportunity mapping的评审交付物
  required_fields:
  - 价值链
  - 机会
  - 共享能力
  - 依赖
  - 风险
  - 投资序列
workflow:
- id: step-1
  action: 沿价值链寻找信息与决策瓶颈
  evidence: 记录本步骤的来源、判断和未决问题，写入 opportunity-map.md。
- id: step-2
  action: 区分单点场景和共用数据能力
  evidence: 记录本步骤的来源、判断和未决问题，写入 opportunity-map.md。
- id: step-3
  action: 将候选映射到价值/可行性与组织owner
  evidence: 记录本步骤的来源、判断和未决问题，写入 opportunity-map.md。
- id: step-4
  action: 排序先解锁依赖的实验，形成组合路线图
  evidence: 记录本步骤的来源、判断和未决问题，写入 opportunity-map.md。
constraints:
- 不把所有场景都归为一个大Agent；保留非AI路径
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个机会有业务结果、前提、owner；共享依赖避免重复投资
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
    criterion: 每个机会有业务结果、前提、owner；共享依赖避免重复投资
    severity: critical
  - id: boundary-gate
    criterion: 不把所有场景都归为一个大Agent；保留非AI路径
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# AI 机会地图 / AI opportunity mapping

需要跨部门识别可复用、可投资的AI机会组合。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 沿价值链寻找信息与决策瓶颈。
2. 区分单点场景和共用数据能力。
3. 将候选映射到价值/可行性与组织owner。
4. 排序先解锁依赖的实验，形成组合路线图。

## 边界与失败处理

- 不把所有场景都归为一个大Agent；保留非AI路径。
- 缺共享owner时先明确治理责任，不强行合并不同权限数据。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `opportunity-map.md`。完成后核对：每个机会有业务结果、前提、owner；共享依赖避免重复投资。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
