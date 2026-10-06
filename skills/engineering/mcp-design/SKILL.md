---
name: mcp-design
display_name: MCP 设计 / MCP design
description: MCP 设计 / MCP design：把企业工具作为MCP能力暴露给不同Agent。交付mcp-design.md，包含证据、决策与失败处置。
version: 1.0.0
category: engineering
tags:
- engineering
- mcp
- design
scenario: 把企业工具作为MCP能力暴露给不同Agent
goal: 交付可复验的 mcp-design.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 把企业工具作为MCP能力暴露给不同Agent
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 工具契约、客户端、传输与身份需求
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: mcp-design.md
  type: markdown
  description: MCP 设计 / MCP design的评审交付物
  required_fields:
  - 能力目录
  - 传输
  - 身份
  - 权限
  - 工具schema
  - 错误
  - 测试
workflow:
- id: step-1
  action: 核验当前MCP官方协议与客户端能力
  evidence: 记录本步骤的来源、判断和未决问题，写入 mcp-design.md。
- id: step-2
  action: 区分tools、resources、prompts
  evidence: 记录本步骤的来源、判断和未决问题，写入 mcp-design.md。
- id: step-3
  action: 把工具契约映射到受控server实现
  evidence: 记录本步骤的来源、判断和未决问题，写入 mcp-design.md。
- id: step-4
  action: 验证初始化、schema、认证、超时和客户端兼容
  evidence: 记录本步骤的来源、判断和未决问题，写入 mcp-design.md。
constraints:
- 工具元数据不授予权限；禁止把客户端密钥写入示例
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 列出协议版本与验证日期；在目标客户端完成契约测试
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
    criterion: 列出协议版本与验证日期；在目标客户端完成契约测试
    severity: critical
  - id: boundary-gate
    criterion: 工具元数据不授予权限；禁止把客户端密钥写入示例
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# MCP 设计 / MCP design

把企业工具作为MCP能力暴露给不同Agent。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 核验当前MCP官方协议与客户端能力。
2. 区分tools、resources、prompts。
3. 把工具契约映射到受控server实现。
4. 验证初始化、schema、认证、超时和客户端兼容。

## 边界与失败处理

- 工具元数据不授予权限；禁止把客户端密钥写入示例。
- 客户端协议不兼容时返回明确错误并提供受控HTTP替代。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `mcp-design.md`。完成后核对：列出协议版本与验证日期；在目标客户端完成契约测试。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
