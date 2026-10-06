---
name: poc-scope
display_name: PoC 范围定义 / PoC scope
description: PoC 范围定义 / PoC scope：在限定预算与时间内验证一个业务假设。交付poc-charter.md，包含证据、决策与失败处置。
version: 1.0.0
category: solution
tags:
- solution
- poc
- scope
scenario: 在限定预算与时间内验证一个业务假设
goal: 交付可复验的 poc-charter.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 在限定预算与时间内验证一个业务假设
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 场景卡、资源上限、样本与权限、业务指标
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: poc-charter.md
  type: markdown
  description: PoC 范围定义 / PoC scope的评审交付物
  required_fields:
  - 假设
  - 范围内外
  - 时间盒
  - 基线
  - 成功门槛
  - 停止条件
workflow:
- id: step-1
  action: 选择一个用户任务和风险可控数据切片
  evidence: 记录本步骤的来源、判断和未决问题，写入 poc-charter.md。
- id: step-2
  action: 写清范围外需求与依赖
  evidence: 记录本步骤的来源、判断和未决问题，写入 poc-charter.md。
- id: step-3
  action: 先约定基线、数据冻结和指标分母
  evidence: 记录本步骤的来源、判断和未决问题，写入 poc-charter.md。
- id: step-4
  action: 按验证价值安排时间盒和退出评审
  evidence: 记录本步骤的来源、判断和未决问题，写入 poc-charter.md。
constraints:
- PoC未通过不自动扩大范围；门槛须在跑分前确定
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 范围能映射到测试；成功与失败均有下一步决策
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
    criterion: 范围能映射到测试；成功与失败均有下一步决策
    severity: critical
  - id: boundary-gate
    criterion: PoC未通过不自动扩大范围；门槛须在跑分前确定
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# PoC 范围定义 / PoC scope

在限定预算与时间内验证一个业务假设。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 选择一个用户任务和风险可控数据切片。
2. 写清范围外需求与依赖。
3. 先约定基线、数据冻结和指标分母。
4. 按验证价值安排时间盒和退出评审。

## 边界与失败处理

- PoC未通过不自动扩大范围；门槛须在跑分前确定。
- 数据晚交一周时重新时间盒，不压缩评测或暗改门槛。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `poc-charter.md`。完成后核对：范围能映射到测试；成功与失败均有下一步决策。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
