---
name: permission-model
display_name: 权限模型 / Permission model
description: 权限模型 / Permission model：企业AI跨数据与工具执行需要最小权限。交付permission-model.md，包含证据、决策与失败处置。
version: 1.0.0
category: architecture
tags:
- architecture
- permission
- model
scenario: 企业AI跨数据与工具执行需要最小权限
goal: 交付可复验的 permission-model.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 企业AI跨数据与工具执行需要最小权限
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 角色、资源、动作、租户与属性、服务身份
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: permission-model.md
  type: markdown
  description: 权限模型 / Permission model的评审交付物
  required_fields:
  - 主体
  - 资源
  - 动作
  - 策略
  - 拒绝规则
  - 审计
  - 测试矩阵
workflow:
- id: step-1
  action: 枚举用户和服务主体
  evidence: 记录本步骤的来源、判断和未决问题，写入 permission-model.md。
- id: step-2
  action: 按角色与属性定义读写范围
  evidence: 记录本步骤的来源、判断和未决问题，写入 permission-model.md。
- id: step-3
  action: 在检索与工具执行端实施强制校验
  evidence: 记录本步骤的来源、判断和未决问题，写入 permission-model.md。
- id: step-4
  action: 覆盖跨租户、权限撤销、继承和管理员例外
  evidence: 记录本步骤的来源、判断和未决问题，写入 permission-model.md。
constraints:
- 默认拒绝；不能依赖模型自觉遵守ACL
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每项允许有对应拒绝测试；撤权后缓存和索引不泄露
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
    criterion: 每项允许有对应拒绝测试；撤权后缓存和索引不泄露
    severity: critical
  - id: boundary-gate
    criterion: 默认拒绝；不能依赖模型自觉遵守ACL
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 权限模型 / Permission model

企业AI跨数据与工具执行需要最小权限。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 枚举用户和服务主体。
2. 按角色与属性定义读写范围。
3. 在检索与工具执行端实施强制校验。
4. 覆盖跨租户、权限撤销、继承和管理员例外。

## 边界与失败处理

- 默认拒绝；不能依赖模型自觉遵守ACL。
- 服务账号权限宽于用户时必须下传用户范围或收窄服务权限。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `permission-model.md`。完成后核对：每项允许有对应拒绝测试；撤权后缓存和索引不泄露。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
