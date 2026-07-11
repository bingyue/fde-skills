# Skill Template

新建 FDE-Skills 能力包时，复制本模板并填充。

---

## 元信息

| 字段 | 填写 |
| --- | --- |
| 名称 | |
| 分类 | `01-Foundation` ~ `11-Best-Practice` |
| 成熟度 | `draft` / `usable` / `validated` |
| 一句话 | |
| 关联方法论 | 如 DIVE、EDD、三层 PoC |

---

## 1. 适用场景

- 什么时候用：
- 谁应该用：
- 不适用场景：

## 2. 企业问题与目标

- 当前痛点：
- 交付目标：
- 业务指标（可量化）：

## 3. 输入 / 输出

### 输入

- 数据输入：
- 业务输入：
- 权限前提：

### 输出（交付物）

- 文档类：
- 决策类：
- 验收类：

## 4. 方法论框架

> 引用国内 FDE 交付方法论中的框架，如 Issue Tree、DIVE、EDD、周度 Demo 等。详见 `11-Best-Practice/China-FDE-Consulting-Pattern`。

1.
2.
3.

## 5. 执行步骤

### 准备阶段

1.
2.

### 执行阶段

1.
2.
3.

### 验收阶段

1.
2.

### 复盘阶段

1.

## 6. 常见误区

| 误区 | 正确做法 |
| --- | --- |
| | |

## 7. Prompt 模板

见 `prompt.md`。要求：分阶段多段，非 4 行 stub。

## 8. 工具与集成

- 可用工具：
- MCP / API：
- 外部系统：
- 本地参考：`.agents/skills/<name>/SKILL.md`

## 9. 权限与安全边界

- 访问边界：
- 敏感数据处理：
- 人工审核节点：

## 10. 验收与评估

见 `evaluation.md`，至少包含：

- 准确性 / 完整性
- 时效性
- 稳定性
- 风险控制
- 通过门槛与失败信号

## 11. 失败处理

- 常见失败模式：
- 降级策略：
- 回滚策略：

## 12. 与国内 FDE 生态的关联

- 对应交付阶段：
- 可组合的上下游 Skill：

---

## 文件清单

创建目录 `<category>/<skill-name>/` 并包含：

```text
README.md       # 本模板内容，150+ 行
prompt.md       # 分阶段 Prompt
checklist.md    # 准备/执行/验收/复盘
evaluation.md   # 指标矩阵
workflow.md     # 关键 Skill 建议增加
assets/         # 模板样例（可选）
```

创建后同步更新 `INDEX.md` 与 `_catalog/fde-skill-map.md`。
