---
name: ai-security-testing
display_name: AI 安全测试 / AI security testing
description: AI 安全测试 / AI security testing：上线前验证提示注入、越权、数据泄露与工具滥用。交付security-report.md，包含证据、决策与失败处置。
version: 1.0.0
category: evaluation
tags:
- evaluation
- ai
- security
- testing
scenario: 上线前验证提示注入、越权、数据泄露与工具滥用
goal: 交付可复验的 security-report.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 上线前验证提示注入、越权、数据泄露与工具滥用
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 授权范围、威胁模型、隔离环境、测试账户
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: security-report.md
  type: markdown
  description: AI 安全测试 / AI security testing的评审交付物
  required_fields:
  - 威胁
  - 测试用例
  - 复现
  - 影响
  - 修复
  - 复测
workflow:
- id: step-1
  action: 明确允许测试的资产与数据
  evidence: 记录本步骤的来源、判断和未决问题，写入 security-report.md。
- id: step-2
  action: 在合成和脱敏环境测试直接/间接注入
  evidence: 记录本步骤的来源、判断和未决问题，写入 security-report.md。
- id: step-3
  action: 覆盖跨租户检索、工具权限、日志泄露与资源耗尽
  evidence: 记录本步骤的来源、判断和未决问题，写入 security-report.md。
- id: step-4
  action: 按影响分级并验证修复
  evidence: 记录本步骤的来源、判断和未决问题，写入 security-report.md。
constraints:
- 不越出授权资产；不向真实外部地址发送敏感数据
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每个高风险路径有负例；未修复关键漏洞阻断上线
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
    criterion: 每个高风险路径有负例；未修复关键漏洞阻断上线
    severity: critical
  - id: boundary-gate
    criterion: 不越出授权资产；不向真实外部地址发送敏感数据
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# AI 安全测试 / AI security testing

上线前验证提示注入、越权、数据泄露与工具滥用。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 明确允许测试的资产与数据。
2. 在合成和脱敏环境测试直接/间接注入。
3. 覆盖跨租户检索、工具权限、日志泄露与资源耗尽。
4. 按影响分级并验证修复。

## 边界与失败处理

- 不越出授权资产；不向真实外部地址发送敏感数据。
- 无法隔离副作用时先建立测试替身，不在生产试探。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `security-report.md`。完成后核对：每个高风险路径有负例；未修复关键漏洞阻断上线。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
