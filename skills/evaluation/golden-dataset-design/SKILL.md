---
name: golden-dataset-design
display_name: Golden Dataset 设计 / Golden dataset
description: Golden Dataset 设计 / Golden dataset：需要稳定且不可被调参污染的验收基准。交付golden-dataset.md，包含证据、决策与失败处置。
version: 1.0.0
category: evaluation
tags:
- evaluation
- golden
- dataset
- design
scenario: 需要稳定且不可被调参污染的验收基准
goal: 交付可复验的 golden-dataset.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要稳定且不可被调参污染的验收基准
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 业务验收标准、专家标签、来源版本、保留测试集
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: golden-dataset.md
  type: markdown
  description: Golden Dataset 设计 / Golden dataset的评审交付物
  required_fields:
  - 范围
  - 标注协议
  - 仲裁
  - 冻结版本
  - 泄漏检查
  - 更新策略
workflow:
- id: step-1
  action: 选定高价值和高风险任务切片
  evidence: 记录本步骤的来源、判断和未决问题，写入 golden-dataset.md。
- id: step-2
  action: 双人标注关键样本并裁决分歧
  evidence: 记录本步骤的来源、判断和未决问题，写入 golden-dataset.md。
- id: step-3
  action: 冻结输入、标签、语料版本与哈希
  evidence: 记录本步骤的来源、判断和未决问题，写入 golden-dataset.md。
- id: step-4
  action: 制定退役和增补规则并保留历史分数
  evidence: 记录本步骤的来源、判断和未决问题，写入 golden-dataset.md。
constraints:
- 测试答案不进入prompt或开发调参；不得事后删除难例
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 冻结manifest可复现；分歧率与仲裁记录可查
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
    criterion: 冻结manifest可复现；分歧率与仲裁记录可查
    severity: critical
  - id: boundary-gate
    criterion: 测试答案不进入prompt或开发调参；不得事后删除难例
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Golden Dataset 设计 / Golden dataset

需要稳定且不可被调参污染的验收基准。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 选定高价值和高风险任务切片。
2. 双人标注关键样本并裁决分歧。
3. 冻结输入、标签、语料版本与哈希。
4. 制定退役和增补规则并保留历史分数。

## 边界与失败处理

- 测试答案不进入prompt或开发调参；不得事后删除难例。
- 业务政策变化时新建版本，不能改旧标签仍报同一测试集。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `golden-dataset.md`。完成后核对：冻结manifest可复现；分歧率与仲裁记录可查。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
