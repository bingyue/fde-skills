---
name: enterprise-ai-pricing
display_name: 企业 AI 方案报价 / Enterprise AI pricing
description: 企业 AI 方案报价 / Enterprise AI pricing：客户要求可交付且有边界的AI项目报价。交付proposal-pricing.md，包含证据、决策与失败处置。
version: 1.0.0
category: business
tags:
- business
- enterprise
- ai
- pricing
scenario: 客户要求可交付且有边界的AI项目报价
goal: 交付可复验的 proposal-pricing.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 客户要求可交付且有边界的AI项目报价
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 范围、工作量、成本、风险、付款与维护要求
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: proposal-pricing.md
  type: markdown
  description: 企业 AI 方案报价 / Enterprise AI pricing的评审交付物
  required_fields:
  - 工作包
  - 假设
  - 价格区间
  - 里程碑
  - 排除项
  - 变更
  - 维护
workflow:
- id: step-1
  action: 按可验收工作包拆分发现/开发/评测/部署/移交
  evidence: 记录本步骤的来源、判断和未决问题，写入 proposal-pricing.md。
- id: step-2
  action: 估算角色工日和外部费用
  evidence: 记录本步骤的来源、判断和未决问题，写入 proposal-pricing.md。
- id: step-3
  action: 按数据、集成与合规不确定性列备选
  evidence: 记录本步骤的来源、判断和未决问题，写入 proposal-pricing.md。
- id: step-4
  action: 把付款条件与交付验收而非夸大收益绑定
  evidence: 记录本步骤的来源、判断和未决问题，写入 proposal-pricing.md。
constraints:
- 报价是商业建议需授权人员确认；币种税费与有效期写清
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每项费用能追溯范围和工期；持续运维不隐藏在一次开发费内
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
    criterion: 每项费用能追溯范围和工期；持续运维不隐藏在一次开发费内
    severity: critical
  - id: boundary-gate
    criterion: 报价是商业建议需授权人员确认；币种税费与有效期写清
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 企业 AI 方案报价 / Enterprise AI pricing

客户要求可交付且有边界的AI项目报价。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按可验收工作包拆分发现/开发/评测/部署/移交。
2. 估算角色工日和外部费用。
3. 按数据、集成与合规不确定性列备选。
4. 把付款条件与交付验收而非夸大收益绑定。

## 边界与失败处理

- 报价是商业建议需授权人员确认；币种税费与有效期写清。
- 客户要求无限修改时定义变更预算和验收边界再出固定价。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `proposal-pricing.md`。完成后核对：每项费用能追溯范围和工期；持续运维不隐藏在一次开发费内。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
