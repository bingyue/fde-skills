# Diagnostic-FDE

- **分类**：`11-Best-Practice`
- **成熟度**：`usable`
- **版本**：`1.0.0`
- **一句话**：诊断型 FDE——从陌生行业到完整 ToB 客户方案包的 12 步结构化交付

---

## 适用场景

- 接到新行业 B 端客户需求，需快速出完整方案包
- 售前方案设计、客户首次接触出方案
- 行业解决方案架构设计、竞品分析与差异化定位
- 能力覆盖矩阵、架构图、ROI、POC 方案一体化输出

## 问题定义

ToB AI 售前常面临「行业陌生 + 时间紧 + 交付物多」：需在 3–5 天内输出行业速览、竞品分析、客户诊断、需求排序、能力匹配、架构图、ROI、Why Us、POC 与汇报材料。本 Skill 将这一过程结构化为 **12 步四阶段工作流**，并编排 9 个子 Skill 与 4 个自研脚本协同执行。

## 方法论框架

### 四阶段十二步

```text
Phase 1 情报收集（①②③ 可并行）
  ① 行业快速研究 → 行业速览.md
  ② 竞品格局扫描 → 竞品分析.md
  ③ 客户现状诊断 → 客户诊断.md

Phase 2 需求锁定
  ④ 需求挖掘+痛点排序 → 需求清单.md
  ⑤ 需求-能力匹配 → 能力匹配.md

Phase 3 方案设计
  ⑥ 解决方案+产品优先级 → 解决方案.md
  ⑦ 架构图生成 → architecture.md（Mermaid）
  ⑧ ROI 商业价值测算 → ROI测算.md

Phase 4 包装输出
  ⑨ 竞品差异化叙事 → Why-Us.md
  ⑩ POC方案+落地路径 → POC方案.md
  ⑪ 方案文档包 → 执行摘要 + PPT + 技术方案
  ⑫ 内部评审 Checklist → 通过后提交客户
```

### 子 Skill 编排（`sub-skills/`）

| 子 Skill | 主要步骤 |
| --- | --- |
| competitive-teardown | ②⑨ 竞品拆解与 Battle Card |
| research-summarizer | ①⑨ 行业报告摘要与对比 |
| product-discovery | ③⑩ 假设映射与 Discovery Sprint |
| product-manager-toolkit | ③④⑥ RICE、访谈分析、PRD |
| product-strategist | ⑥ OKR 级联与战略分层 |
| experiment-designer | ⑩ 假设验证与样本量 |
| roadmap-communicator | ⑩⑪ 路线图与执行摘要 |
| product-analytics | ① 数字化成熟度判断 |
| ux-researcher-designer | ③ 用户画像与旅程 |

### 自研脚本（`scripts/`）

| 脚本 | 用途 |
| --- | --- |
| `capability_match.py` | 需求→产品能力语义匹配 |
| `gap_analysis.py` | 能力差距与缓解策略 |
| `architecture_gen.py` | 方案→Mermaid 架构图 |
| `roi_calc.py` | 效率/收入/投资回报测算 |

## 输入 / 输出

### 输入

- 行业名称
- 客户名称
- 初始需求描述
- （可选）访谈记录、已有行业研究

### 输出

完整客户方案包（8–12 份文档）：

- 行业速览、竞品分析、客户诊断
- 需求清单（Issue Tree + RICE）
- 能力覆盖矩阵、解决方案、架构图
- ROI 测算、Why Us、POC 方案
- 执行摘要、汇报 PPT 大纲、技术方案

## 执行步骤

1. **确认输入**：行业、客户、需求；判断起点（全量或单步）
2. **Phase 1**：并行执行 ①②③，汇总情报质量
3. **Phase 2**：MECE 拆解 + RICE 排序 + 能力匹配（✅ 覆盖率目标 ≥ 60%）
4. **Phase 3**：方案设计、三张架构图、ROI 三档测算
5. **Phase 4**：差异化叙事、POC 计划、文档包、⑫ 自检
6. **断点恢复**：检查已有产出，从断点继续

## 捆绑资源

| 资源 | 路径 |
| --- | --- |
| 完整 12 步工作流 | `SKILL.md` |
| 能力地图 | `references/capability-map.md` |
| 架构模式 | `references/architecture-patterns.md` |
| 权衡决策 | `references/trade-offs.md` |
| 行业术语映射 | `references/industry-glossary.yaml` |
| POC 模板 | `templates/poc-plan.md` |
| 评估框架 | `templates/evaluation-framework.md` |
| 案例模板 | `templates/case-study.md` |

## 常见误区

- ❌ 跳过 Phase 1 直接写方案
- ❌ 能力匹配无缓解策略的 ❌ 项
- ❌ 架构图不可渲染或产品标注错误
- ❌ ROI 数字无假设来源
- ❌ Why Us 只讲优势回避劣势

## 交付物清单

- [ ] 行业速览（≥3 独立来源）
- [ ] 竞品分析（≥2 竞品，12 维评分）
- [ ] 客户诊断（≥10 条假设，3 类画像）
- [ ] 需求清单（MECE + RICE）
- [ ] 能力匹配（✅ 率 ≥ 60%）
- [ ] 架构图 3 张可渲染
- [ ] ROI 含敏感性分析
- [ ] POC 方案（指标可量化）
- [ ] ⑫ 内部评审全部通过

## 与国内 FDE 生态关联

- 上游：`02-Discovery/Consultative-Problem-Solving`、`02-Discovery/Executive-Communication-Framework`
- 并行：`11-Best-Practice/FDE-Full-Lifecycle`
- 下游：`03-Solution-Design/PRD-Generator`、`10-Templates/SOW-Template`

## 关联 Skill

- `FDE-Customer-Product-Bridge` — 客户现场转产品/研发
- `China-FDE-Consulting-Pattern` — 国内交付总纲

## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.0.0 | 2026-07-12 | 从 `diagnostic-fde-1.0.0` 迁移至 FDE-Skills 标准结构 |
