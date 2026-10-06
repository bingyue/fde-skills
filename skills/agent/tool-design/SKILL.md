---
name: tool-design
display_name: 工具设计 / Tool design
description: 工具设计 / Tool design：Agent需要访问企业系统的安全API契约。交付tool-contract.md，包含证据、决策与失败处置。
version: 1.0.0
category: agent
tags:
- agent
- tool
- design
scenario: Agent需要访问企业系统的安全API契约
goal: 交付可复验的 tool-contract.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- Agent需要访问企业系统的安全API契约
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 系统接口、任务需求、权限、错误与审计要求
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: tool-contract.md
  type: markdown
  description: 工具设计 / Tool design的评审交付物
  required_fields:
  - 名称
  - 参数schema
  - 权限
  - 副作用
  - 幂等
  - 错误
  - 结果schema
workflow:
- id: step-1
  action: 按单一业务动作定义工具
  evidence: 记录本步骤的来源、判断和未决问题，写入 tool-contract.md。
- id: step-2
  action: 使用有界参数与明确结果结构
  evidence: 记录本步骤的来源、判断和未决问题，写入 tool-contract.md。
- id: step-3
  action: 服务端校验身份和对象级权限
  evidence: 记录本步骤的来源、判断和未决问题，写入 tool-contract.md。
- id: step-4
  action: 定义超时、重试、幂等键与审计并做契约测试
  evidence: 记录本步骤的来源、判断和未决问题，写入 tool-contract.md。
constraints:
- 工具描述不是授权凭据；业务校验必须在执行端
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 越权、重复提交、无效参数和超时都有可验证结果
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
    criterion: 越权、重复提交、无效参数和超时都有可验证结果
    severity: critical
  - id: boundary-gate
    criterion: 工具描述不是授权凭据；业务校验必须在执行端
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 工具设计 / Tool design

Agent需要访问企业系统的安全API契约。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按单一业务动作定义工具。
2. 使用有界参数与明确结果结构。
3. 服务端校验身份和对象级权限。
4. 定义超时、重试、幂等键与审计并做契约测试。

## 边界与失败处理

- 工具描述不是授权凭据；业务校验必须在执行端。
- 参数包含任意SQL或shell命令时缩小为白名单业务操作。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `tool-contract.md`。完成后核对：越权、重复提交、无效参数和超时都有可验证结果。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
