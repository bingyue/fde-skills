---
name: ai-scenario-discovery
display_name: AI 场景发现 / AI scenario discovery
description: AI 场景发现 / AI scenario discovery：从业务流程形成可验证的AI候选场景。交付scenario-cards.md，包含证据、决策与失败处置。
version: 1.0.0
category: discovery
tags:
- discovery
- ai
- scenario
scenario: 从业务流程形成可验证的AI候选场景
goal: 交付可复验的 scenario-cards.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 从业务流程形成可验证的AI候选场景
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 流程节点、重复决策、输入资料、风险边界
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: scenario-cards.md
  type: markdown
  description: AI 场景发现 / AI scenario discovery的评审交付物
  required_fields:
  - 用户任务
  - 基线
  - AI动作
  - 非AI替代
  - 验证指标
workflow:
- id: step-1
  action: 找高频阅读、检索、分类、生成、执行节点
  evidence: 记录本步骤的来源、判断和未决问题，写入 scenario-cards.md。
- id: step-2
  action: 为每个节点写真实用户任务
  evidence: 记录本步骤的来源、判断和未决问题，写入 scenario-cards.md。
- id: step-3
  action: 比较规则、搜索和流程改造等基线
  evidence: 记录本步骤的来源、判断和未决问题，写入 scenario-cards.md。
- id: step-4
  action: 定义最小离线实验和人工复核方式
  evidence: 记录本步骤的来源、判断和未决问题，写入 scenario-cards.md。
constraints:
- 不得把平台建设或聊天窗口本身当业务场景
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每张卡都有用户、触发、结果、非AI对照和可测收益
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
    criterion: 每张卡都有用户、触发、结果、非AI对照和可测收益
    severity: critical
  - id: boundary-gate
    criterion: 不得把平台建设或聊天窗口本身当业务场景
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# AI 场景发现 / AI scenario discovery

从业务流程形成可验证的AI候选场景。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 找高频阅读、检索、分类、生成、执行节点。
2. 为每个节点写真实用户任务。
3. 比较规则、搜索和流程改造等基线。
4. 定义最小离线实验和人工复核方式。

## 边界与失败处理

- 不得把平台建设或聊天窗口本身当业务场景。
- 没有任务量时先做观察采样，不报告预计ROI。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `scenario-cards.md`。完成后核对：每张卡都有用户、触发、结果、非AI对照和可测收益。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
