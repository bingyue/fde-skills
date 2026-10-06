---
name: business-process-mapping
display_name: 业务流程梳理 / Business process mapping
description: 业务流程梳理 / Business process mapping：需要识别AI应该嵌入的具体流程节点。交付process-map.md，包含证据、决策与失败处置。
version: 1.0.0
category: discovery
tags:
- discovery
- business
- process
- mapping
scenario: 需要识别AI应该嵌入的具体流程节点
goal: 交付可复验的 process-map.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 需要识别AI应该嵌入的具体流程节点
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 真实订单或工单轨迹、角色、系统事件、例外流程
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: process-map.md
  type: markdown
  description: 业务流程梳理 / Business process mapping的评审交付物
  required_fields:
  - 触发
  - 步骤
  - 输入输出
  - 系统
  - 等待时间
  - 异常路径
workflow:
- id: step-1
  action: 跟踪正常、失败、返工各一条案例
  evidence: 记录本步骤的来源、判断和未决问题，写入 process-map.md。
- id: step-2
  action: 画泳道和系统交接而非理想流程
  evidence: 记录本步骤的来源、判断和未决问题，写入 process-map.md。
- id: step-3
  action: 区分处理时间与排队等待
  evidence: 记录本步骤的来源、判断和未决问题，写入 process-map.md。
- id: step-4
  action: 标记AI介入点、人工兜底与现有基线
  evidence: 记录本步骤的来源、判断和未决问题，写入 process-map.md。
constraints:
- 流程优化建议与现状事实分别记录
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个节点有角色、输入、输出；异常路径闭环；时长注明样本窗口
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
    criterion: 每个节点有角色、输入、输出；异常路径闭环；时长注明样本窗口
    severity: critical
  - id: boundary-gate
    criterion: 流程优化建议与现状事实分别记录
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 业务流程梳理 / Business process mapping

需要识别AI应该嵌入的具体流程节点。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 跟踪正常、失败、返工各一条案例。
2. 画泳道和系统交接而非理想流程。
3. 区分处理时间与排队等待。
4. 标记AI介入点、人工兜底与现有基线。

## 边界与失败处理

- 流程优化建议与现状事实分别记录。
- 缺少异常案例时保留未验证分支并补采样。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `process-map.md`。完成后核对：每个节点有角色、输入、输出；异常路径闭环；时长注明样本窗口。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
