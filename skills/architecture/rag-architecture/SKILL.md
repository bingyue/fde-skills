---
name: rag-architecture
display_name: RAG 架构设计 / RAG architecture
description: RAG 架构设计 / RAG architecture：需要带出处且受权限控制的企业问答。交付rag-design.md，包含证据、决策与失败处置。
version: 1.0.0
category: architecture
tags:
- architecture
- rag
scenario: 需要带出处且受权限控制的企业问答
goal: 交付可复验的 rag-design.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要带出处且受权限控制的企业问答
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 知识设计、查询集、权限策略、延迟成本目标
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: rag-design.md
  type: markdown
  description: RAG 架构设计 / RAG architecture的评审交付物
  required_fields:
  - 摄取
  - 解析
  - 索引
  - 检索
  - 重排
  - 生成
  - 引用
  - 拒答
workflow:
- id: step-1
  action: 先建立词法检索基线
  evidence: 记录本步骤的来源、判断和未决问题，写入 rag-design.md。
- id: step-2
  action: 设计解析、去重、元数据和版本更新链路
  evidence: 记录本步骤的来源、判断和未决问题，写入 rag-design.md。
- id: step-3
  action: 比较稀疏/稠密/混合与重排
  evidence: 记录本步骤的来源、判断和未决问题，写入 rag-design.md。
- id: step-4
  action: 在生成前按ACL和有效期过滤，缺证据转拒答
  evidence: 记录本步骤的来源、判断和未决问题，写入 rag-design.md。
constraints:
- 检索过滤前后都验证租户边界；引用必须来自实际返回上下文
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 设计含删除同步、来源冲突、空召回和超时策略
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
    criterion: 设计含删除同步、来源冲突、空召回和超时策略
    severity: critical
  - id: boundary-gate
    criterion: 检索过滤前后都验证租户边界；引用必须来自实际返回上下文
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# RAG 架构设计 / RAG architecture

需要带出处且受权限控制的企业问答。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 先建立词法检索基线。
2. 设计解析、去重、元数据和版本更新链路。
3. 比较稀疏/稠密/混合与重排。
4. 在生成前按ACL和有效期过滤，缺证据转拒答。

## 边界与失败处理

- 检索过滤前后都验证租户边界；引用必须来自实际返回上下文。
- 检索器不支持安全过滤时改为隔离索引，不能后置文本遮盖。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `rag-design.md`。完成后核对：设计含删除同步、来源冲突、空召回和超时策略。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
