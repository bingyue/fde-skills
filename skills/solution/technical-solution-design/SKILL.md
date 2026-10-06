---
name: technical-solution-design
display_name: 技术方案设计 / Technical solution
description: 技术方案设计 / Technical solution：业务验收已确定，需要可实施的技术路线。交付technical-design.md，包含证据、决策与失败处置。
version: 1.0.0
category: solution
tags:
- solution
- technical
- design
scenario: 业务验收已确定，需要可实施的技术路线
goal: 交付可复验的 technical-design.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 业务验收已确定，需要可实施的技术路线
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: PRD、数据契约、环境限制、评测要求
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: technical-design.md
  type: markdown
  description: 技术方案设计 / Technical solution的评审交付物
  required_fields:
  - 模块
  - 数据流
  - 接口
  - 技术取舍
  - 失败模式
  - 实施计划
workflow:
- id: step-1
  action: 将验收需求分配到模块与接口
  evidence: 记录本步骤的来源、判断和未决问题，写入 technical-design.md。
- id: step-2
  action: 比较最低可行技术路线
  evidence: 记录本步骤的来源、判断和未决问题，写入 technical-design.md。
- id: step-3
  action: 通过小实验验证最大技术风险
  evidence: 记录本步骤的来源、判断和未决问题，写入 technical-design.md。
- id: step-4
  action: 给出构建顺序、回滚点和运行成本
  evidence: 记录本步骤的来源、判断和未决问题，写入 technical-design.md。
constraints:
- 选型需标注版本和核验日期；不能以流行度替代约束匹配
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个must需求有负责组件；关键风险有验证结果或明确阻塞
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
    criterion: 每个must需求有负责组件；关键风险有验证结果或明确阻塞
    severity: critical
  - id: boundary-gate
    criterion: 选型需标注版本和核验日期；不能以流行度替代约束匹配
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 技术方案设计 / Technical solution

业务验收已确定，需要可实施的技术路线。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 将验收需求分配到模块与接口。
2. 比较最低可行技术路线。
3. 通过小实验验证最大技术风险。
4. 给出构建顺序、回滚点和运行成本。

## 边界与失败处理

- 选型需标注版本和核验日期；不能以流行度替代约束匹配。
- 硬件容量未知时先给容量实验，不承诺延迟SLA。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `technical-design.md`。完成后核对：每个must需求有负责组件；关键风险有验证结果或明确阻塞。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
