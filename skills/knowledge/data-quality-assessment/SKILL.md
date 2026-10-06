---
name: data-quality-assessment
display_name: 数据质量评估 / Data quality
description: 数据质量评估 / Data quality：输入数据可能导致检索或业务决策失真。交付data-quality.md，包含证据、决策与失败处置。
version: 1.0.0
category: knowledge
tags:
- knowledge
- data
- quality
- assessment
scenario: 输入数据可能导致检索或业务决策失真
goal: 交付可复验的 data-quality.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 输入数据可能导致检索或业务决策失真
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 带字段说明的样本、主键、业务规则、时间窗口
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: data-quality.md
  type: markdown
  description: 数据质量评估 / Data quality的评审交付物
  required_fields:
  - 完整性
  - 唯一性
  - 一致性
  - 时效
  - 分层结果
  - 修复计划
workflow:
- id: step-1
  action: 按业务来源和时间分层抽样
  evidence: 记录本步骤的来源、判断和未决问题，写入 data-quality.md。
- id: step-2
  action: 定义非空、唯一、范围和跨表规则
  evidence: 记录本步骤的来源、判断和未决问题，写入 data-quality.md。
- id: step-3
  action: 统计违规分母并追踪业务影响
  evidence: 记录本步骤的来源、判断和未决问题，写入 data-quality.md。
- id: step-4
  action: 区分源头修复、管道校验和人工隔离
  evidence: 记录本步骤的来源、判断和未决问题，写入 data-quality.md。
constraints:
- 不静默填充关键业务字段；保留原值与修正证据
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每条规则可复跑；关键失败样本可定位；修复有owner
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
    criterion: 每条规则可复跑；关键失败样本可定位；修复有owner
    severity: critical
  - id: boundary-gate
    criterion: 不静默填充关键业务字段；保留原值与修正证据
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 数据质量评估 / Data quality

输入数据可能导致检索或业务决策失真。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按业务来源和时间分层抽样。
2. 定义非空、唯一、范围和跨表规则。
3. 统计违规分母并追踪业务影响。
4. 区分源头修复、管道校验和人工隔离。

## 边界与失败处理

- 不静默填充关键业务字段；保留原值与修正证据。
- 无字段含义时暂停语义清洗，先补数据字典。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `data-quality.md`。完成后核对：每条规则可复跑；关键失败样本可定位；修复有owner。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
