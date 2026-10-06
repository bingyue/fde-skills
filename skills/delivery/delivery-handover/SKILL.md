---
name: delivery-handover
display_name: 交付移交 / Delivery handover
description: 交付移交 / Delivery handover：交付团队退出前客户需要独立运营、恢复和更新系统。交付handover.md，包含证据、决策与失败处置。
version: 1.0.0
category: delivery
tags:
- delivery
- handover
scenario: 交付团队退出前客户需要独立运营、恢复和更新系统
goal: 交付可复验的 handover.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 交付团队退出前客户需要独立运营、恢复和更新系统
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 发布版本、验收、运行手册、权限、培训、支持约定
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: handover.md
  type: markdown
  description: 交付移交 / Delivery handover的评审交付物
  required_fields:
  - 资产清单
  - 责任转移
  - 演练
  - 访问
  - 培训
  - 支持
  - 未决项
workflow:
- id: step-1
  action: 清点代码、镜像、数据契约、评测与运维资产
  evidence: 记录本步骤的来源、判断和未决问题，写入 handover.md。
- id: step-2
  action: 由接收团队独立执行部署、告警处理和回滚
  evidence: 记录本步骤的来源、判断和未决问题，写入 handover.md。
- id: step-3
  action: 通过安全渠道转移账户责任并撤销临时访问
  evidence: 记录本步骤的来源、判断和未决问题，写入 handover.md。
- id: step-4
  action: 记录签收、支持窗口和剩余问题
  evidence: 记录本步骤的来源、判断和未决问题，写入 handover.md。
constraints:
- 密钥不写入交付文档；演示给客户看不等于客户会操作
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 接收人完成teach-back与恢复演练；临时访问清理；每个未决项有owner
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
    criterion: 接收人完成teach-back与恢复演练；临时访问清理；每个未决项有owner
    severity: critical
  - id: boundary-gate
    criterion: 密钥不写入交付文档；演示给客户看不等于客户会操作
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 交付移交 / Delivery handover

交付团队退出前客户需要独立运营、恢复和更新系统。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 清点代码、镜像、数据契约、评测与运维资产。
2. 由接收团队独立执行部署、告警处理和回滚。
3. 通过安全渠道转移账户责任并撤销临时访问。
4. 记录签收、支持窗口和剩余问题。

## 边界与失败处理

- 密钥不写入交付文档；演示给客户看不等于客户会操作。
- 接收团队无人负责时延期移交并明确过渡支持责任。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `handover.md`。完成后核对：接收人完成teach-back与恢复演练；临时访问清理；每个未决项有owner。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
