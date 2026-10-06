---
name: docker-deployment
display_name: Docker 部署 / Docker deployment
description: Docker 部署 / Docker deployment：AI服务需要可重复构建和受控运行。交付docker-release.md，包含证据、决策与失败处置。
version: 1.0.0
category: deployment
tags:
- deployment
- docker
scenario: AI服务需要可重复构建和受控运行
goal: 交付可复验的 docker-release.md，支持客户对当前阶段作出有证据的决定。
when_to_use:
- AI服务需要可重复构建和受控运行
when_not_to_use:
- 只需一般知识解释且没有具体交付任务
- 缺少关键输入且无法取得证据时，仅执行缺口识别，不宣布完成
inputs:
- name: context
  description: 应用入口、依赖锁、配置契约、健康检查
  required: true
  type: object
- name: constraints
  description: 客户授权范围、数据边界、预算、期限与输出语言。
  required: true
  type: object
outputs:
- name: docker-release.md
  type: markdown
  description: Docker 部署 / Docker deployment的评审交付物
  required_fields:
  - 镜像digest
  - 构建
  - 用户
  - 配置
  - 健康
  - 资源
  - 回滚
workflow:
- id: step-1
  action: 固定基础镜像与依赖并多阶段构建
  evidence: 记录本步骤的来源、判断和未决问题，写入 docker-release.md。
- id: step-2
  action: 以非root用户运行且密钥从运行环境注入
  evidence: 记录本步骤的来源、判断和未决问题，写入 docker-release.md。
- id: step-3
  action: 定义健康、就绪、资源和优雅退出
  evidence: 记录本步骤的来源、判断和未决问题，写入 docker-release.md。
- id: step-4
  action: 验证重启、持久化与旧digest回滚
  evidence: 记录本步骤的来源、判断和未决问题，写入 docker-release.md。
constraints:
- 不得把密钥或客户数据打入镜像；不使用latest作为发布标识
- 事实、假设和模拟数据分别标注；外部操作遵循用户授权及目标环境权限。
quality_criteria:
- 干净环境可构建；非root启动；恢复和回滚有记录
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
    criterion: 干净环境可构建；非root启动；恢复和回滚有记录
    severity: critical
  - id: boundary-gate
    criterion: 不得把密钥或客户数据打入镜像；不使用latest作为发布标识
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: ready
---

# Docker 部署 / Docker deployment

AI服务需要可重复构建和受控运行。优先读取客户实际材料，按契约执行；输出语言遵循客户要求。

## 执行

1. 固定基础镜像与依赖并多阶段构建。
2. 以非root用户运行且密钥从运行环境注入。
3. 定义健康、就绪、资源和优雅退出。
4. 验证重启、持久化与旧digest回滚。

## 边界与失败处理

- 不得把密钥或客户数据打入镜像；不使用latest作为发布标识。
- 依赖下载失败时终止构建，不静默退回未锁定版本。
- 输出状态使用 `ready`、`blocked` 或 `needs-review`，列出来源、待确认项与负责人。

## 交付与评审

使用 [交付模板](assets/output-template.md) 组织 `docker-release.md`。完成后核对：干净环境可构建；非root启动；恢复和回滚有记录。

读取 [工作示例与反例](examples/example.yaml) 后再应用到真实客户；这些数据为教学模拟，不代表生产评测成绩。
