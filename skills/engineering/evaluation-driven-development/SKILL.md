---
name: evaluation-driven-development
display_name: 评测驱动开发 / Evaluation-driven development
description: 评测驱动开发 / Evaluation-driven development：AI需求不稳定，需要用可复现评测指导构建迭代。交付edd-plan.md，包含证据、决策与失败处置。
version: 1.0.0
category: engineering
tags:
- engineering
- evaluation
- driven
- development
scenario: AI需求不稳定，需要用可复现评测指导构建迭代
goal: 交付可复验的 edd-plan.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- AI需求不稳定，需要用可复现评测指导构建迭代
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 验收标准、真实与合成失败例、基线系统
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: edd-plan.md
  type: markdown
  description: 评测驱动开发 / Evaluation-driven development的评审交付物
  required_fields:
  - 任务契约
  - 数据切分
  - 基线
  - 实验日志
  - 门禁
  - 回归
workflow:
- id: step-1
  action: 先定义系统后置条件和质量/成本预算
  evidence: 记录本步骤的来源、判断和未决问题，写入 edd-plan.md。
- id: step-2
  action: 建立开发集与保留验收集
  evidence: 记录本步骤的来源、判断和未决问题，写入 edd-plan.md。
- id: step-3
  action: 一次改变一个可解释因素并记录版本
  evidence: 记录本步骤的来源、判断和未决问题，写入 edd-plan.md。
- id: step-4
  action: 将失败加入开发回归，保留集按规则轮换
  evidence: 记录本步骤的来源、判断和未决问题，写入 edd-plan.md。
constraints:
- 不在看到结果后降低门槛；测试集不能反复充当调参集
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 每次实验记录输入版本、变更、分层结果与决定
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
    criterion: 每次实验记录输入版本、变更、分层结果与决定
    severity: critical
  - id: boundary-gate
    criterion: 不在看到结果后降低门槛；测试集不能反复充当调参集
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 评测驱动开发 / Evaluation-driven development

AI需求不稳定，需要用可复现评测指导构建迭代。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 先定义系统后置条件和质量/成本预算。
2. 建立开发集与保留验收集。
3. 一次改变一个可解释因素并记录版本。
4. 将失败加入开发回归，保留集按规则轮换。

## 边界与失败处理

- 不在看到结果后降低门槛；测试集不能反复充当调参集。
- 失败样本来自保留集时登记泄漏并替换下一版本保留集。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `edd-plan.md`。完成后核对：每次实验记录输入版本、变更、分层结果与决定。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
