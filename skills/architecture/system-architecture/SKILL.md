---
name: system-architecture
display_name: 系统架构 / System architecture
description: 系统架构 / System architecture：跨服务AI应用需要清晰边界与可靠性设计。交付architecture.md，包含证据、决策与失败处置。
version: 1.0.0
category: architecture
tags:
- architecture
- system
scenario: 跨服务AI应用需要清晰边界与可靠性设计
goal: 交付可复验的 architecture.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 跨服务AI应用需要清晰边界与可靠性设计
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 技术方案、用户规模、数据分类、可用性目标
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: architecture.md
  type: markdown
  description: 系统架构 / System architecture的评审交付物
  required_fields:
  - 上下文
  - 容器
  - 信任边界
  - 数据流
  - 故障隔离
  - ADR
workflow:
- id: step-1
  action: 画系统上下文与外部依赖
  evidence: 记录本步骤的来源、判断和未决问题，写入 architecture.md。
- id: step-2
  action: 标记认证、授权、数据驻留和队列边界
  evidence: 记录本步骤的来源、判断和未决问题，写入 architecture.md。
- id: step-3
  action: 跟踪正常/超时/重试路径
  evidence: 记录本步骤的来源、判断和未决问题，写入 architecture.md。
- id: step-4
  action: 用单点故障与容量场景检验方案
  evidence: 记录本步骤的来源、判断和未决问题，写入 architecture.md。
constraints:
- 图中每条跨边界调用都要定义身份和失败策略
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 架构图、接口与部署拓扑一致；无无限重试链
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
    criterion: 架构图、接口与部署拓扑一致；无无限重试链
    severity: critical
  - id: boundary-gate
    criterion: 图中每条跨边界调用都要定义身份和失败策略
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 系统架构 / System architecture

跨服务AI应用需要清晰边界与可靠性设计。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 画系统上下文与外部依赖。
2. 标记认证、授权、数据驻留和队列边界。
3. 跟踪正常/超时/重试路径。
4. 用单点故障与容量场景检验方案。

## 边界与失败处理

- 图中每条跨边界调用都要定义身份和失败策略。
- 没有并发估计时以明确假设做负载试验，记录容量未知。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `architecture.md`。完成后核对：架构图、接口与部署拓扑一致；无无限重试链。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
