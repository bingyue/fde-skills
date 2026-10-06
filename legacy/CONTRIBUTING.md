# Contributing

## 新增 Skill 的最小要求

每个 Skill 至少包含：

- `README.md`（150+ 行：适用场景、问题定义、方法论、输入输出、步骤、误区、交付物、国内 FDE 生态关联）
- `prompt.md`（分阶段多段 Prompt，非 stub）
- `checklist.md`（准备 / 执行 / 验收 / 复盘）
- `evaluation.md`（指标矩阵、通过门槛、验收样例）

关键 Skill 建议增加 `workflow.md` 或 `case-study.md`。

## 命名规范

- 目录使用 `Pascal-Case` 或 `Kebab-Case`，避免空格。
- 以**企业交付场景**命名，不以工具或业务系统命名。

示例：

- `02-Discovery/Business-Interview`
- `04-AI-Delivery/Tool-Audit`

## 目录归类（11 目录体系）

| 目录 | 归类原则 |
| --- | --- |
| `01-Foundation` | 立项、干系人、SOW、自评、成长、通用话术 |
| `02-Discovery` | 访谈、流程、咨询式拆解、预期、沟通、AIBP |
| `03-Solution-Design` | PRD、场景卡、API/架构轻量设计 |
| `04-AI-Delivery` | RAG、评估、Agent、MCP 审计 |
| `05-Deployment` | 私有化、Gateway、部署模式 |
| `06-Integration` | 飞书、企业 IM、系统协同 |
| `07-Operations` | 客服、采纳、看板、运营自动化 |
| `08-Security-Compliance` | RBAC、合规、安全评审 |
| `09-Industry` | 高价值行业示例，保持精简 |
| `10-Templates` | 可复用交付模板 |
| `11-Best-Practice` | 方法论总纲、国际对照 |

**咨询 Reference** 放 `11-Best-Practice/references/`，不计入核心 Skill，须在 `_catalog/consulting-references.md` 登记。

**不要**按 CRM/ERP/MES 等业务系统拆顶层目录。行业能力放 `09-Industry`，每次新增需证明跨客户复用价值。

## 质量标准

- 明确输入、输出、执行步骤。
- 有权限与安全边界描述。
- 有验收指标与失败处理。
- 可映射到实际客户交付场景。
- 引用 `.agents/skills/` 或本库其他 Skill 时写清关联，不只贴链接。

## 内容扩充

- 批量扩充脚本：`_catalog/scripts/expand_skills_data.py`
- 修改 Skill 定义后运行：`python3 _catalog/scripts/expand_skills_data.py`
- 同步更新 `INDEX.md` 与 `_catalog/fde-skill-map.md`

## 外部 Skill（skills.sh）规范

- 不只记录链接，必须先下载到 `.agents/skills/`。
- 默认：`npx skills add <repo>@<skill>`
- 导入后在 `_catalog/external-skills-imported.md` 登记来源、路径、**新 taxonomy 映射**与状态。
- 咨询/PPT 类导入放 `11-Best-Practice/references/`，在 `_catalog/consulting-references.md` 登记，目录名去掉版本号后缀。
