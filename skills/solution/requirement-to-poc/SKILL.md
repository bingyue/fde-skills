---
name: requirement-to-poc
display_name: 需求到 PoC / Requirement to PoC
description: 需求到 PoC / Requirement to PoC：客户愿望需要转为可构建、可判定的短周期实验。交付requirement-to-poc.md，包含证据、决策与失败处置。
version: 1.0.0
category: solution
tags:
- solution
- requirement
- to
- poc
scenario: 客户愿望需要转为可构建、可判定的短周期实验
goal: 交付可复验的 requirement-to-poc.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 客户愿望需要转为可构建、可判定的短周期实验
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 发现报告、优先场景、数据样本、资源约束
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: requirement-to-poc.md
  type: markdown
  description: 需求到 PoC / Requirement to PoC的评审交付物
  required_fields:
  - 假设
  - 追溯
  - 构建切片
  - 数据集
  - 门槛
  - 演示
  - 决策
workflow:
- id: step-1
  action: 把业务结果转成可测假设
  evidence: 记录本步骤的来源、判断和未决问题，写入 requirement-to-poc.md。
- id: step-2
  action: 冻结一个纵向切片与非AI基线
  evidence: 记录本步骤的来源、判断和未决问题，写入 requirement-to-poc.md。
- id: step-3
  action: 先建评测和失败例再实现最小链路
  evidence: 记录本步骤的来源、判断和未决问题，写入 requirement-to-poc.md。
- id: step-4
  action: 用盲测与业务反馈决定继续/调整/停止
  evidence: 记录本步骤的来源、判断和未决问题，写入 requirement-to-poc.md。
constraints:
- PoC要验证核心风险，不可仅挑容易展示样本
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 需求→测试→实现→结果逐项可追溯；退出决定有证据
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
    criterion: 需求→测试→实现→结果逐项可追溯；退出决定有证据
    severity: critical
  - id: boundary-gate
    criterion: PoC要验证核心风险，不可仅挑容易展示样本
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 需求到 PoC / Requirement to PoC

客户愿望需要转为可构建、可判定的短周期实验。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 把业务结果转成可测假设。
2. 冻结一个纵向切片与非AI基线。
3. 先建评测和失败例再实现最小链路。
4. 用盲测与业务反馈决定继续/调整/停止。

## 边界与失败处理

- PoC要验证核心风险，不可仅挑容易展示样本。
- 关键资料缺失时先验证数据准备可行性，不做无依据生成Demo。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `requirement-to-poc.md`。完成后核对：需求→测试→实现→结果逐项可追溯；退出决定有证据。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
