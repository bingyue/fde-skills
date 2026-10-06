---
name: eval-dataset-generation
display_name: Eval Dataset 生成 / Eval dataset generation
description: Eval Dataset 生成 / Eval dataset generation：需要覆盖真实任务的开发评测样本。交付eval-dataset.jsonl，包含证据、决策与失败处置。
version: 1.0.0
category: evaluation
tags:
- evaluation
- eval
- dataset
- generation
scenario: 需要覆盖真实任务的开发评测样本
goal: 交付可复验的 eval-dataset.jsonl，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要覆盖真实任务的开发评测样本
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 脱敏任务日志、风险分类、标注规范、数据用途授权
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: eval-dataset.jsonl
  type: jsonl
  description: Eval Dataset 生成 / Eval dataset generation的评审交付物
  required_fields:
  - case_id
  - task
  - slice
  - expected
  - source
  - split
workflow:
- id: step-1
  action: 从真实任务分层抽样并补充稀有失败
  evidence: 记录本步骤的来源、判断和未决问题，写入 eval-dataset.jsonl。
- id: step-2
  action: 明确标注可接受输出与禁止行为
  evidence: 记录本步骤的来源、判断和未决问题，写入 eval-dataset.jsonl。
- id: step-3
  action: 合成样本单独标记并人工复核
  evidence: 记录本步骤的来源、判断和未决问题，写入 eval-dataset.jsonl。
- id: step-4
  action: 去重后按客户/时间/实体分组切分
  evidence: 记录本步骤的来源、判断和未决问题，写入 eval-dataset.jsonl。
constraints:
- 合成题不能冒充真实用户频率；避免开发测试泄漏
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每例有来源与期望；标签争议有裁决；切分不存在同实体泄漏
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
    criterion: 每例有来源与期望；标签争议有裁决；切分不存在同实体泄漏
    severity: critical
  - id: boundary-gate
    criterion: 合成题不能冒充真实用户频率；避免开发测试泄漏
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Eval Dataset 生成 / Eval dataset generation

需要覆盖真实任务的开发评测样本。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 从真实任务分层抽样并补充稀有失败。
2. 明确标注可接受输出与禁止行为。
3. 合成样本单独标记并人工复核。
4. 去重后按客户/时间/实体分组切分。

## 边界与失败处理

- 合成题不能冒充真实用户频率；避免开发测试泄漏。
- 无授权日志时使用明示合成样本且不声称线上代表性。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `eval-dataset.jsonl`。完成后核对：每例有来源与期望；标签争议有裁决；切分不存在同实体泄漏。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。

查看[三条实际 JSONL 样本](examples/dataset.jsonl)，在交付时按客户任务扩充并按实体分组切分。
