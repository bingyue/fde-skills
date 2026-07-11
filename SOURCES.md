# Sources

FDE-Skills 内容来源与引用规范。

---

## 一、方法论来源（核心）

本库方法论为**国内 FDE 交付方法论**，自包含于各 Skill 的 README、workflow 与 `11-Best-Practice` 总纲，核心框架包括：

| 框架 | 说明 |
| --- | --- |
| Issue Tree + DIVE | 咨询式问题拆解与场景收敛 |
| EDD | 评估驱动开发，Golden Dataset 与回归门禁 |
| 三层 PoC | 开箱即用 → Vibe Coding → 工程化脚手架 |
| 周度 Demo | 项目节奏控制与预期校准 |
| AIBP 协作 | FDE 与业务双负责人机制 |
| 预期管理 | 概率性 AI 边界声明与人审策略 |
| 采纳增长 | 客户成功漏斗与续约指标 |
| 资产化 | 模板、评估集、Prompt、Skill 沉淀 |

详见 [`11-Best-Practice/China-FDE-Consulting-Pattern`](./11-Best-Practice/China-FDE-Consulting-Pattern/README.md)。

---

## 二、本地 Skill 扫描来源

仅扫描摘要，不移动原始 Skill：

| 目录 | 用途 |
| --- | --- |
| `~/.codex/skills` | 电商、增长、飞书、合规等交付相关 Skill |
| `~/.agents/skills` | 工程、安全、自动化流程类 Skill |
| `~/.cursor/skills-cursor` | 通用流程与审查类 Skill |

扫描结果：[`_catalog/local-skills-index.md`](./_catalog/local-skills-index.md)

---

## 三、外部 Skill 导入（skills.sh）

**策略**：不只记录链接，先下载到当前仓库再映射引用。

| 项 | 说明 |
| --- | --- |
| 落地目录 | `.agents/skills/` |
| 导入命令 | `npx skills add <repo>@<skill>` |
| 已导入 | 19 个（2026-07-11） |
| 编目 | [`_catalog/external-skills-imported.md`](./_catalog/external-skills-imported.md) |
| 映射 | [`_catalog/fde-skill-map.md`](./_catalog/fde-skill-map.md) |

**搜索记录**：[`_catalog/online-skills-search.md`](./_catalog/online-skills-search.md)

优先搜索 query：`fde`、`forward deployed engineer`、`enterprise ai`、`rag`、`agent`、`mcp`、`deployment`、`crm`、`customer service`、`supply chain`、`security`、`growth`

---

## 四、引用规范

1. 本库 Skill 引用外部 Skill 时，写清**本地路径**（如 `.agents/skills/langchain-rag/SKILL.md`），不只贴 skills.sh 链接。
2. 引用本库方法论时，指向具体 Skill 或 `11-Best-Practice` 章节，标注框架名称（如「DIVE 模型」「EDD 回归门禁」）。
3. 新增外部 Skill 必须在 `_catalog/external-skills-imported.md` 登记来源、路径、分类映射与状态。
4. 内容扩充脚本：`_catalog/scripts/expand_skills_data.py`（修改 Skill 定义后运行批量再生四件套）。

---

## 五、刻意不纳入的来源

- 纯营销获客类 Skill（Landing Page、Cold Email 等）— 已由 FDE-Adoption-Growth 覆盖企业采纳场景
- 海外 SaaS 托管部署（Vercel/Railway）— 已由 Private-Deployment-Gateway 覆盖国内私有化场景
- 按 CRM/ERP/MES 拆分的业务系统 Skill — 映射到 Discovery/Operations，不建顶层目录
