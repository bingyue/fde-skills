---
name: ontology-design
display_name: Ontology 设计 / Ontology design
description: Ontology 设计 / Ontology design：多系统同名对象含义不同，需要统一业务实体与动作。交付ontology.md，包含证据、决策与失败处置。
version: 1.0.0
category: ontology
tags:
- ontology
- design
scenario: 多系统同名对象含义不同，需要统一业务实体与动作
goal: 交付可复验的 ontology.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 多系统同名对象含义不同，需要统一业务实体与动作
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 业务术语、对象样本、系统主键、生命周期、权限
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: ontology.md
  type: markdown
  description: Ontology 设计 / Ontology design的评审交付物
  required_fields:
  - 实体
  - 属性
  - 关系
  - 标识
  - 状态
  - 动作
  - 来源映射
workflow:
- id: step-1
  action: 从真实决策所需对象建模
  evidence: 记录本步骤的来源、判断和未决问题，写入 ontology.md。
- id: step-2
  action: 定义实体标识、基数和时间语义
  evidence: 记录本步骤的来源、判断和未决问题，写入 ontology.md。
- id: step-3
  action: 映射源系统键与冲突解决
  evidence: 记录本步骤的来源、判断和未决问题，写入 ontology.md。
- id: step-4
  action: 把动作前置条件、权限与审计挂到对象
  evidence: 记录本步骤的来源、判断和未决问题，写入 ontology.md。
constraints:
- 不要把所有表直接变成实体；区分概念、数据实例与操作权限
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 模型能解释两个系统冲突样本；动作有前置与后置条件
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
    criterion: 模型能解释两个系统冲突样本；动作有前置与后置条件
    severity: critical
  - id: boundary-gate
    criterion: 不要把所有表直接变成实体；区分概念、数据实例与操作权限
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Ontology 设计 / Ontology design

多系统同名对象含义不同，需要统一业务实体与动作。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 从真实决策所需对象建模。
2. 定义实体标识、基数和时间语义。
3. 映射源系统键与冲突解决。
4. 把动作前置条件、权限与审计挂到对象。

## 边界与失败处理

- 不要把所有表直接变成实体；区分概念、数据实例与操作权限。
- 标识无法可靠关联时保留未解析关系，不自动合并同名客户。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `ontology.md`。完成后核对：模型能解释两个系统冲突样本；动作有前置与后置条件。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
