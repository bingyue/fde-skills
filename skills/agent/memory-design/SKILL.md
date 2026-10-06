---
name: memory-design
display_name: 记忆设计 / Memory design
description: 记忆设计 / Memory design：跨会话需要保存业务状态与可撤销偏好。交付memory-design.md，包含证据、决策与失败处置。
version: 1.0.0
category: agent
tags:
- agent
- memory
- design
scenario: 跨会话需要保存业务状态与可撤销偏好
goal: 交付可复验的 memory-design.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 跨会话需要保存业务状态与可撤销偏好
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 记忆用途、用户身份、保留期、删除与纠错要求
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: memory-design.md
  type: markdown
  description: 记忆设计 / Memory design的评审交付物
  required_fields:
  - 短期长期
  - 键与隔离
  - 写入条件
  - 有效期
  - 纠错
  - 删除
workflow:
- id: step-1
  action: 区分任务状态、用户偏好与事实证据
  evidence: 记录本步骤的来源、判断和未决问题，写入 memory-design.md。
- id: step-2
  action: 定义tenant/user/session键
  evidence: 记录本步骤的来源、判断和未决问题，写入 memory-design.md。
- id: step-3
  action: 设置确认、来源、有效期及冲突处理
  evidence: 记录本步骤的来源、判断和未决问题，写入 memory-design.md。
- id: step-4
  action: 验证删除、用户切换和错误记忆修复
  evidence: 记录本步骤的来源、判断和未决问题，写入 memory-design.md。
constraints:
- 未经授权不存敏感资料；检索记忆不能替代当前授权
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 跨租户隔离与删除传播通过；旧记忆不覆盖新确认事实
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
    criterion: 跨租户隔离与删除传播通过；旧记忆不覆盖新确认事实
    severity: critical
  - id: boundary-gate
    criterion: 未经授权不存敏感资料；检索记忆不能替代当前授权
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 记忆设计 / Memory design

跨会话需要保存业务状态与可撤销偏好。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 区分任务状态、用户偏好与事实证据。
2. 定义tenant/user/session键。
3. 设置确认、来源、有效期及冲突处理。
4. 验证删除、用户切换和错误记忆修复。

## 边界与失败处理

- 未经授权不存敏感资料；检索记忆不能替代当前授权。
- 用户请求删除后缓存仍命中时停止使用并修复删除链路。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `memory-design.md`。完成后核对：跨租户隔离与删除传播通过；旧记忆不覆盖新确认事实。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
