---
name: chunk-strategy
display_name: Chunk 策略 / Chunk strategy
description: Chunk 策略 / Chunk strategy：检索切片丢语义或上下文成本过高。交付chunk-experiment.md，包含证据、决策与失败处置。
version: 1.0.0
category: knowledge
tags:
- knowledge
- chunk
- strategy
scenario: 检索切片丢语义或上下文成本过高
goal: 交付可复验的 chunk-experiment.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 检索切片丢语义或上下文成本过高
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 代表文档、查询集、token预算、解析输出
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: chunk-experiment.md
  type: markdown
  description: Chunk 策略 / Chunk strategy的评审交付物
  required_fields:
  - 切分规则
  - 元数据继承
  - 对照配置
  - 召回
  - 成本
  - 选择
workflow:
- id: step-1
  action: 按标题、表格、列表和步骤识别结构
  evidence: 记录本步骤的来源、判断和未决问题，写入 chunk-experiment.md。
- id: step-2
  action: 比较结构切分与固定长度基线
  evidence: 记录本步骤的来源、判断和未决问题，写入 chunk-experiment.md。
- id: step-3
  action: 保留父文档ID、页码、版本和ACL
  evidence: 记录本步骤的来源、判断和未决问题，写入 chunk-experiment.md。
- id: step-4
  action: 在同一查询集测召回、答案完整性与token成本
  evidence: 记录本步骤的来源、判断和未决问题，写入 chunk-experiment.md。
constraints:
- 表头不能与数值分离；流程警告不能切掉
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 选型来自同一冻结集的对照；切片可追溯到原文
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
    criterion: 选型来自同一冻结集的对照；切片可追溯到原文
    severity: critical
  - id: boundary-gate
    criterion: 表头不能与数值分离；流程警告不能切掉
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Chunk 策略 / Chunk strategy

检索切片丢语义或上下文成本过高。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 按标题、表格、列表和步骤识别结构。
2. 比较结构切分与固定长度基线。
3. 保留父文档ID、页码、版本和ACL。
4. 在同一查询集测召回、答案完整性与token成本。

## 边界与失败处理

- 表头不能与数值分离；流程警告不能切掉。
- OCR阅读顺序错乱时先修解析，不用加大chunk掩盖错误。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `chunk-experiment.md`。完成后核对：选型来自同一冻结集的对照；切片可追溯到原文。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
