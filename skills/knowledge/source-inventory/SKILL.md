---
name: source-inventory
display_name: 数据源盘点 / Source inventory
description: 数据源盘点 / Source inventory：知识或Agent项目启动前确认可用数据。交付source-register.md，包含证据、决策与失败处置。
version: 1.0.0
category: knowledge
tags:
- knowledge
- source
- inventory
scenario: 知识或Agent项目启动前确认可用数据
goal: 交付可复验的 source-register.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 知识或Agent项目启动前确认可用数据
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 系统清单、数据owner、授权、更新记录
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: source-register.md
  type: markdown
  description: 数据源盘点 / Source inventory的评审交付物
  required_fields:
  - 来源
  - owner
  - 权限
  - 格式
  - 更新
  - 保留期
  - 用途
workflow:
- id: step-1
  action: 从真实用户任务反推所需数据
  evidence: 记录本步骤的来源、判断和未决问题，写入 source-register.md。
- id: step-2
  action: 抽样验证访问与格式
  evidence: 记录本步骤的来源、判断和未决问题，写入 source-register.md。
- id: step-3
  action: 记录权威来源和重复冲突源
  evidence: 记录本步骤的来源、判断和未决问题，写入 source-register.md。
- id: step-4
  action: 评估增量同步、删除传播和退役流程
  evidence: 记录本步骤的来源、判断和未决问题，写入 source-register.md。
constraints:
- 持有导出文件不等于有权用于训练或索引
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个接入源有用途、owner和授权范围；未知项进入阻塞清单
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
    criterion: 每个接入源有用途、owner和授权范围；未知项进入阻塞清单
    severity: critical
  - id: boundary-gate
    criterion: 持有导出文件不等于有权用于训练或索引
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 数据源盘点 / Source inventory

知识或Agent项目启动前确认可用数据。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 从真实用户任务反推所需数据。
2. 抽样验证访问与格式。
3. 记录权威来源和重复冲突源。
4. 评估增量同步、删除传播和退役流程。

## 边界与失败处理

- 持有导出文件不等于有权用于训练或索引。
- 来源无owner时不索引，保留调查项。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `source-register.md`。完成后核对：每个接入源有用途、owner和授权范围；未知项进入阻塞清单。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
