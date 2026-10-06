---
name: ai-scenario-prioritization
display_name: AI 场景优先级 / AI scenario prioritization
description: AI 场景优先级 / AI scenario prioritization：候选场景多，需要决定先投哪个PoC。交付prioritized-backlog.md，包含证据、决策与失败处置。
version: 1.0.0
category: business
tags:
- business
- ai
- scenario
- prioritization
scenario: 候选场景多，需要决定先投哪个PoC
goal: 交付可复验的 prioritized-backlog.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 候选场景多，需要决定先投哪个PoC
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 场景卡、收益区间、数据可用性、风险和资源约束
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: prioritized-backlog.md
  type: markdown
  description: AI 场景优先级 / AI scenario prioritization的评审交付物
  required_fields:
  - 候选
  - 硬门槛
  - 评分依据
  - 排序
  - 敏感性
  - 下一动作
workflow:
- id: step-1
  action: 先淘汰无合法数据权限或无owner的场景
  evidence: 记录本步骤的来源、判断和未决问题，写入 prioritized-backlog.md。
- id: step-2
  action: 共同设定收益、可行性、风险与学习价值权重
  evidence: 记录本步骤的来源、判断和未决问题，写入 prioritized-backlog.md。
- id: step-3
  action: 保留区间分数并进行权重敏感性分析
  evidence: 记录本步骤的来源、判断和未决问题，写入 prioritized-backlog.md。
- id: step-4
  action: 为首选与备选写明确进入和退出条件
  evidence: 记录本步骤的来源、判断和未决问题，写入 prioritized-backlog.md。
constraints:
- 不能用高收益抵消不可接受的安全边界
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 排序可复算；前两名差距不稳时安排证据实验
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
    criterion: 排序可复算；前两名差距不稳时安排证据实验
    severity: critical
  - id: boundary-gate
    criterion: 不能用高收益抵消不可接受的安全边界
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# AI 场景优先级 / AI scenario prioritization

候选场景多，需要决定先投哪个PoC。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 先淘汰无合法数据权限或无owner的场景。
2. 共同设定收益、可行性、风险与学习价值权重。
3. 保留区间分数并进行权重敏感性分析。
4. 为首选与备选写明确进入和退出条件。

## 边界与失败处理

- 不能用高收益抵消不可接受的安全边界。
- 权重变化使冠军翻转时报告不确定排序并先补证据。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `prioritized-backlog.md`。完成后核对：排序可复算；前两名差距不稳时安排证据实验。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
