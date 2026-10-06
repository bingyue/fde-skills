---
name: private-deployment
display_name: 私有化部署 / Private deployment
description: 私有化部署 / Private deployment：企业要求内网、离线或受限出域部署。交付private-deployment.md，包含证据、决策与失败处置。
version: 1.0.0
category: deployment
tags:
- deployment
- private
scenario: 企业要求内网、离线或受限出域部署
goal: 交付可复验的 private-deployment.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- 企业要求内网、离线或受限出域部署
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 环境清单、网络策略、硬件、模型许可、数据驻留
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: private-deployment.md
  type: markdown
  description: 私有化部署 / Private deployment的评审交付物
  required_fields:
  - 拓扑
  - 离线物料
  - 身份
  - 网络
  - 容量
  - 更新
  - 恢复
workflow:
- id: step-1
  action: 确认每条模型与遥测出站依赖
  evidence: 记录本步骤的来源、判断和未决问题，写入 private-deployment.md。
- id: step-2
  action: 准备带校验和的离线安装物料
  evidence: 记录本步骤的来源、判断和未决问题，写入 private-deployment.md。
- id: step-3
  action: 核验硬件、模型许可与性能
  evidence: 记录本步骤的来源、判断和未决问题，写入 private-deployment.md。
- id: step-4
  action: 演练无互联网运行、备份恢复、升级和回滚
  evidence: 记录本步骤的来源、判断和未决问题，写入 private-deployment.md。
constraints:
- 私有网络不等于满足全部合规要求；例外出域需业务确认
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 出站依赖清单完整；断网仍满足约定功能；恢复可复现
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
    criterion: 出站依赖清单完整；断网仍满足约定功能；恢复可复现
    severity: critical
  - id: boundary-gate
    criterion: 私有网络不等于满足全部合规要求；例外出域需业务确认
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# 私有化部署 / Private deployment

企业要求内网、离线或受限出域部署。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 确认每条模型与遥测出站依赖。
2. 准备带校验和的离线安装物料。
3. 核验硬件、模型许可与性能。
4. 演练无互联网运行、备份恢复、升级和回滚。

## 边界与失败处理

- 私有网络不等于满足全部合规要求；例外出域需业务确认。
- 模型无法装载时降低配置或更换方案，不私自切到外部API。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `private-deployment.md`。完成后核对：出站依赖清单完整；断网仍满足约定功能；恢复可复现。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
