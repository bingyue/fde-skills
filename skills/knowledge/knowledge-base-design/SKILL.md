---
name: knowledge-base-design
display_name: 知识库设计 / Knowledge base design
description: 知识库设计 / Knowledge base design：企业知识分散，需要可维护的权威知识体系。交付knowledge-design.md，包含证据、决策与失败处置。
version: 1.0.0
category: knowledge
tags:
- knowledge
- base
- design
scenario: 企业知识分散，需要可维护的权威知识体系
goal: 交付可复验的 knowledge-design.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 企业知识分散，需要可维护的权威知识体系
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 用户问题、资料、内容owner、版本与权限策略
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: knowledge-design.md
  type: markdown
  description: 知识库设计 / Knowledge base design的评审交付物
  required_fields:
  - 信息架构
  - 来源优先级
  - 元数据
  - 生命周期
  - 权限
  - 更新SOP
workflow:
- id: step-1
  action: 按用户任务设计知识类型和导航
  evidence: 记录本步骤的来源、判断和未决问题，写入 knowledge-design.md。
- id: step-2
  action: 定义文档ID、版本、生效期、owner和ACL
  evidence: 记录本步骤的来源、判断和未决问题，写入 knowledge-design.md。
- id: step-3
  action: 规定冲突解决、审核发布、撤销和删除
  evidence: 记录本步骤的来源、判断和未决问题，写入 knowledge-design.md。
- id: step-4
  action: 用过期知识和拒答场景走查维护闭环
  evidence: 记录本步骤的来源、判断和未决问题，写入 knowledge-design.md。
constraints:
- 检索可见性不能扩大原文权限
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 所有知识有权威源和失效机制；冲突不会静默合并
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
    criterion: 所有知识有权威源和失效机制；冲突不会静默合并
    severity: critical
  - id: boundary-gate
    criterion: 检索可见性不能扩大原文权限
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 知识库设计 / Knowledge base design

企业知识分散，需要可维护的权威知识体系。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按用户任务设计知识类型和导航。
2. 定义文档ID、版本、生效期、owner和ACL。
3. 规定冲突解决、审核发布、撤销和删除。
4. 用过期知识和拒答场景走查维护闭环。

## 边界与失败处理

- 检索可见性不能扩大原文权限。
- 无法确定有效版时拒绝给出确定参数并升级人工。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `knowledge-design.md`。完成后核对：所有知识有权威源和失效机制；冲突不会静默合并。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
