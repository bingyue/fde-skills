---
name: retrieval-strategy
display_name: 检索策略 / Retrieval strategy
description: 检索策略 / Retrieval strategy：召回不足或噪声过高需要改进检索。交付retrieval-report.md，包含证据、决策与失败处置。
version: 1.0.0
category: knowledge
tags:
- knowledge
- retrieval
- strategy
scenario: 召回不足或噪声过高需要改进检索
goal: 交付可复验的 retrieval-report.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 召回不足或噪声过高需要改进检索
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 标注相关文档的查询集、索引、过滤规则
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: retrieval-report.md
  type: markdown
  description: 检索策略 / Retrieval strategy的评审交付物
  required_fields:
  - 查询类型
  - 基线
  - 候选
  - Recall@k
  - MRR
  - 延迟
  - 失败桶
workflow:
- id: step-1
  action: 划分精确标识、语义、时间与多跳查询
  evidence: 记录本步骤的来源、判断和未决问题，写入 retrieval-report.md。
- id: step-2
  action: 固定语料和相关性标注
  evidence: 记录本步骤的来源、判断和未决问题，写入 retrieval-report.md。
- id: step-3
  action: 对比BM25、向量、混合、重排和查询改写
  evidence: 记录本步骤的来源、判断和未决问题，写入 retrieval-report.md。
- id: step-4
  action: 逐类分析漏召回并选择预算内Pareto方案
  evidence: 记录本步骤的来源、判断和未决问题，写入 retrieval-report.md。
constraints:
- 不把测试集用于调参；查询改写不得移除权限或关键限定
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 报告k、分母、分层指标和p95延迟；低频型号单列
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
    criterion: 报告k、分母、分层指标和p95延迟；低频型号单列
    severity: critical
  - id: boundary-gate
    criterion: 不把测试集用于调参；查询改写不得移除权限或关键限定
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 检索策略 / Retrieval strategy

召回不足或噪声过高需要改进检索。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 划分精确标识、语义、时间与多跳查询。
2. 固定语料和相关性标注。
3. 对比BM25、向量、混合、重排和查询改写。
4. 逐类分析漏召回并选择预算内Pareto方案。

## 边界与失败处理

- 不把测试集用于调参；查询改写不得移除权限或关键限定。
- 无相关性标签时先小规模人工标注，不仅凭回答流畅度选型。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `retrieval-report.md`。完成后核对：报告k、分母、分层指标和p95延迟；低频型号单列。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
