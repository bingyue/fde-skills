---
name: production-acceptance
display_name: 生产验收 / Production acceptance
description: 生产验收 / Production acceptance：系统部署后需证明真实环境满足运行要求。交付production-acceptance.md，包含证据、决策与失败处置。
version: 1.0.0
category: deployment
tags:
- deployment
- production
- acceptance
scenario: 系统部署后需证明真实环境满足运行要求
goal: 交付可复验的 production-acceptance.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 系统部署后需证明真实环境满足运行要求
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 发布基线、SLO、负载模型、恢复目标、灰度日志
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: production-acceptance.md
  type: markdown
  description: 生产验收 / Production acceptance的评审交付物
  required_fields:
  - 环境
  - 负载
  - 安全
  - 恢复
  - 缺陷
  - 结论
workflow:
- id: step-1
  action: 核对实际部署与批准版本
  evidence: 记录本步骤的来源、判断和未决问题，写入 production-acceptance.md。
- id: step-2
  action: 执行授权用户旅程和跨租户负例
  evidence: 记录本步骤的来源、判断和未决问题，写入 production-acceptance.md。
- id: step-3
  action: 验证峰值负载、依赖故障与恢复
  evidence: 记录本步骤的来源、判断和未决问题，写入 production-acceptance.md。
- id: step-4
  action: 按观察窗口记录SLO和未决缺陷
  evidence: 记录本步骤的来源、判断和未决问题，写入 production-acceptance.md。
constraints:
- 测试环境成绩不能直接代替生产证据；破坏性实验需受控
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 版本和环境可追溯；关键用户旅程与恢复目标达标
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
    criterion: 版本和环境可追溯；关键用户旅程与恢复目标达标
    severity: critical
  - id: boundary-gate
    criterion: 测试环境成绩不能直接代替生产证据；破坏性实验需受控
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 生产验收 / Production acceptance

系统部署后需证明真实环境满足运行要求。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 核对实际部署与批准版本。
2. 执行授权用户旅程和跨租户负例。
3. 验证峰值负载、依赖故障与恢复。
4. 按观察窗口记录SLO和未决缺陷。

## 边界与失败处理

- 测试环境成绩不能直接代替生产证据；破坏性实验需受控。
- 观察样本不足时标有条件验收和观察期，不声称全面达标。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `production-acceptance.md`。完成后核对：版本和环境可追溯；关键用户旅程与恢复目标达标。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
