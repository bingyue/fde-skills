---
name: prd-generation
display_name: PRD 生成 / PRD generation
description: PRD 生成 / PRD generation：已确认业务场景需要转为开发验收契约。交付prd.md，包含证据、决策与失败处置。
version: 1.0.0
category: solution
tags:
- solution
- prd
- generation
scenario: 已确认业务场景需要转为开发验收契约
goal: 交付可复验的 prd.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 已确认业务场景需要转为开发验收契约
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 场景卡、流程、用户角色、失败样本、约束
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: prd.md
  type: markdown
  description: PRD 生成 / PRD generation的评审交付物
  required_fields:
  - 问题
  - 用户故事
  - 功能非功能
  - 状态
  - 验收用例
  - 追溯表
workflow:
- id: step-1
  action: 定义用户任务和不解决的问题
  evidence: 记录本步骤的来源、判断和未决问题，写入 prd.md。
- id: step-2
  action: 拆出正常、拒绝、异常、人工接管状态
  evidence: 记录本步骤的来源、判断和未决问题，写入 prd.md。
- id: step-3
  action: 为每条需求编写Given/When/Then
  evidence: 记录本步骤的来源、判断和未决问题，写入 prd.md。
- id: step-4
  action: 把需求ID连到接口、评测和交付证据
  evidence: 记录本步骤的来源、判断和未决问题，写入 prd.md。
constraints:
- 不能用模型准确率替代用户任务完成定义
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每条must需求有测试；权限和超时行为可验证
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
    criterion: 每条must需求有测试；权限和超时行为可验证
    severity: critical
  - id: boundary-gate
    criterion: 不能用模型准确率替代用户任务完成定义
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# PRD 生成 / PRD generation

已确认业务场景需要转为开发验收契约。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 定义用户任务和不解决的问题。
2. 拆出正常、拒绝、异常、人工接管状态。
3. 为每条需求编写Given/When/Then。
4. 把需求ID连到接口、评测和交付证据。

## 边界与失败处理

- 不能用模型准确率替代用户任务完成定义。
- 用户故事无owner时标记待确认，不代替业务签字。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `prd.md`。完成后核对：每条must需求有测试；权限和超时行为可验证。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
