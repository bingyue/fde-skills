---
name: rag-evaluation
display_name: RAG 评测 / RAG evaluation
description: RAG 评测 / RAG evaluation：检索问答需要区分召回、引用和答案错误。交付rag-eval-report.md，包含证据、决策与失败处置。
version: 1.0.0
category: evaluation
tags:
- evaluation
- rag
scenario: 检索问答需要区分召回、引用和答案错误
goal: 交付可复验的 rag-eval-report.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 检索问答需要区分召回、引用和答案错误
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 冻结查询集、相关文档标签、回答与上下文、ACL样本
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: rag-eval-report.md
  type: markdown
  description: RAG 评测 / RAG evaluation的评审交付物
  required_fields:
  - Recall@k
  - 引用有效率
  - groundedness
  - 拒答
  - 切片
  - 延迟
workflow:
- id: step-1
  action: 固定语料、索引、模型和prompt版本
  evidence: 记录本步骤的来源、判断和未决问题，写入 rag-eval-report.md。
- id: step-2
  action: 先测检索再测生成与引用支持
  evidence: 记录本步骤的来源、判断和未决问题，写入 rag-eval-report.md。
- id: step-3
  action: 独立测试权限、空知识和过期冲突
  evidence: 记录本步骤的来源、判断和未决问题，写入 rag-eval-report.md。
- id: step-4
  action: 按失败桶提出最小修复并在保留集复测
  evidence: 记录本步骤的来源、判断和未决问题，写入 rag-eval-report.md。
constraints:
- 流畅回答不等于正确；LLM裁判需抽样人工校准
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个指标有公式、分母和切片；权限泄露为硬失败
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
    criterion: 每个指标有公式、分母和切片；权限泄露为硬失败
    severity: critical
  - id: boundary-gate
    criterion: 流畅回答不等于正确；LLM裁判需抽样人工校准
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# RAG 评测 / RAG evaluation

检索问答需要区分召回、引用和答案错误。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 固定语料、索引、模型和prompt版本。
2. 先测检索再测生成与引用支持。
3. 独立测试权限、空知识和过期冲突。
4. 按失败桶提出最小修复并在保留集复测。

## 边界与失败处理

- 流畅回答不等于正确；LLM裁判需抽样人工校准。
- 相关性标签不足时先标注，不能仅用端到端评分归因检索。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `rag-eval-report.md`。完成后核对：每个指标有公式、分母和切片；权限泄露为硬失败。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
