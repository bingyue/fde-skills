---
name: value-difficulty-matrix
display_name: 价值 × 难度矩阵 / Value × Difficulty
description: 价值 × 难度矩阵 / Value × Difficulty：对场景组合做投资分组与讨论。交付value-difficulty.md，包含证据、决策与失败处置。
version: 1.0.0
category: business
tags:
- business
- value
- difficulty
- matrix
scenario: 对场景组合做投资分组与讨论
goal: 交付可复验的 value-difficulty.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 对场景组合做投资分组与讨论
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 收益与实施工作量估计、基线窗口、评分锚点
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: value-difficulty.md
  type: markdown
  description: 价值 × 难度矩阵 / Value × Difficulty的评审交付物
  required_fields:
  - 价值口径
  - 难度口径
  - 坐标
  - 置信区间
  - 象限动作
workflow:
- id: step-1
  action: 价值统一到同一周期的业务量或节省
  evidence: 记录本步骤的来源、判断和未决问题，写入 value-difficulty.md。
- id: step-2
  action: 难度拆成数据、集成、治理、运营
  evidence: 记录本步骤的来源、判断和未决问题，写入 value-difficulty.md。
- id: step-3
  action: 用参照案例定义1到5锚点
  evidence: 记录本步骤的来源、判断和未决问题，写入 value-difficulty.md。
- id: step-4
  action: 画四象限并对低置信度点标误差范围
  evidence: 记录本步骤的来源、判断和未决问题，写入 value-difficulty.md。
constraints:
- 不要跨部门混用收入增长和工时节省的未经归一分数
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个坐标有证据；低价值高难度项目有明确暂停条件
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
    criterion: 每个坐标有证据；低价值高难度项目有明确暂停条件
    severity: critical
  - id: boundary-gate
    criterion: 不要跨部门混用收入增长和工时节省的未经归一分数
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 价值 × 难度矩阵 / Value × Difficulty

对场景组合做投资分组与讨论。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 价值统一到同一周期的业务量或节省。
2. 难度拆成数据、集成、治理、运营。
3. 用参照案例定义1到5锚点。
4. 画四象限并对低置信度点标误差范围。

## 边界与失败处理

- 不要跨部门混用收入增长和工时节省的未经归一分数。
- 坐标来自主观投票时标为假设矩阵，安排估算验证。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `value-difficulty.md`。完成后核对：每个坐标有证据；低价值高难度项目有明确暂停条件。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
