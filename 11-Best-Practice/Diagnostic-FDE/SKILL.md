---
name: 诊断型FDE
description: "诊断型FDE（Field Discovery Engineer）——ToB产品解决方案架构师全流程Skill。当接到新行业B端客户需求时，按12步结构化流程完成：行业快速研究、竞品格局扫描、客户现状诊断、潜在需求挖掘与排序、需求-产品能力匹配（含腾讯云ADP/WorkBuddy/混元能力地图）、解决方案设计与产品优先级、Mermaid架构图生成、ROI商业价值测算、竞品差异化叙事(Why Us)、POC方案与落地路径、方案文档包(PPT+执行摘要+技术方案)、内部评审自检。输出完整的客户方案包，交付物包括架构图、能力覆盖矩阵、ROI测算、POC方案和汇报PPT。适用于售前方案设计、客户首次接触出方案、行业解决方案架构设计、竞品分析与差异化定位等场景。"
---

# 诊断型FDE — Field Discovery Engineer

> 从陌生行业到完整方案包，12步结构化交付。

面向腾讯云ToB产品架构师的全流程工作Skill。覆盖从接到新客户需求到输出完整方案包的全部环节，编排9个子skill协同工作，4个自研脚本补齐能力缺口。

---

## 触发条件

识别以下用户意图时激活此skill：

- "帮我分析XX行业/客户的需求"
- "出一套XX客户的解决方案"
- "做一下XX行业的竞品分析"
- "帮我设计XX场景的产品架构"
- "准备XX客户的方案汇报材料"
- 任何涉及：ToB方案设计、行业分析、能力匹配、架构图、POC方案的请求

---

## 全流程概览

```
输入：行业 + 客户名 + 初始需求描述

Phase 1: 情报收集（并行，1-2天）
  ① 行业快速研究        → 行业速览.md
  ② 竞品格局扫描        → 竞品分析.md
  ③ 客户现状诊断        → 客户诊断.md

Phase 2: 需求锁定（半天）
  ④ 需求挖掘+痛点排序   → 需求清单.md
  ⑤ 需求-能力匹配       → 能力匹配.md

Phase 3: 方案设计（1天）
  ⑥ 方案设计+产品优先级  → 解决方案.md
  ⑦ 架构图生成          → architecture.md (含Mermaid)
  ⑧ ROI商业价值测算      → ROI测算.md

Phase 4: 包装输出（半天）
  ⑨ 竞品差异化叙事      → Why-Us.md
  ⑩ POC方案+落地路径     → POC方案.md
  ⑪ 方案文档包          → PPT + 执行摘要 + 技术方案
  ⑫ 内部评审checklist    → 评审通过后提交

输出：完整客户方案包（8-12份文档）
```

---

## 子Skill与工具清单

### 子Skills（位于 `sub-skills/` 目录）

| 子Skill | 用途 | 主要调用步骤 |
|---------|------|------------|
| `competitive-teardown` | 竞品数据收集+12维评分+SWOT+Battle Card | ②⑨ |
| `research-summarizer` | 行业报告结构化摘要+多源对比 | ①⑨ |
| `product-discovery` | 假设映射+Discovery Sprint设计 | ③⑩ |
| `product-manager-toolkit` | RICE优先级+客户访谈分析+PRD模板 | ③④⑥ |
| `product-strategist` | OKR级联+战略分层(Growth/Retention/Revenue/Innovation/Operational) | ⑥ |
| `experiment-designer` | 假设→指标→样本量→停止规则 | ⑩ |
| `roadmap-communicator` | Now/Next/Later路线图+执行摘要 | ⑩⑪ |
| `product-analytics` | 指标框架(AARRR/North Star)+阶段判断 | ① |
| `ux-researcher-designer` | 用户画像生成+旅程图 | ③ |

### 自研脚本（位于 `scripts/` 目录）

| 脚本 | 用途 | 主要调用步骤 |
|------|------|------------|
| `capability_match.py` | 痛点→腾讯云产品能力语义匹配+覆盖矩阵 | ⑤ |
| `architecture_gen.py` | 方案→Mermaid架构图生成+语法修复 | ⑦ |
| `gap_analysis.py` | 需求×能力差距标记+缓解策略推荐 | ⑤ |
| `roi_calc.py` | 效率提升/收入增长/投资回报测算 | ⑧ |

### 核心参考文档（位于 `references/` 目录）

| 文档 | 内容 |
|------|------|
| `capability-map.md` | 腾讯云ADP/WorkBuddy/混元/数据产品全能力地图 |
| `trade-offs.md` | 8组腾讯云架构权衡决策对 |
| `architecture-patterns.md` | 6种行业通用解决方案架构模式 |
| `industry-glossary.yaml` | 行业术语→产品术语双向映射 |

### 模板文件（位于 `templates/` 目录）

| 模板 | 用途 |
|------|------|
| `poc-plan.md` | POC方案标准模板 |
| `evaluation-framework.md` | Demo/POC评测框架 |
| `case-study.md` | 案例沉淀标准模板 |

---

## 详细工作流

### Phase 1: 情报收集

> **执行策略**：①②③可并行执行。如有客户访谈记录优先处理③，否则先做①②。

---

#### ① 行业快速研究

**目标**：2小时内对陌生行业形成结构化认知。

**调用子skill**：`research-summarizer` + `product-analytics`

**执行步骤**：

1. 使用web搜索收集3-5篇该行业的权威报告/文章
2. 对每篇来源执行 `research-summarizer` 的 `/research:summarize` workflow：
   - 识别源类型（报告→executive summary结构）
   - 提取：Key Thesis / Key Findings / Methodology / Limitations / Actionable Takeaways
   - 评估质量：Credibility × Evidence × Recency × Objectivity 四维评分
3. 对所有来源执行 `/research:compare` workflow：
   - 构建对比矩阵（Central Thesis / Methodology / Key Finding / Credibility）
   - 输出：Consensus Findings / Contested Points / Gaps / Recommendation
4. 使用 `product-analytics` 的阶段判断框架，评估该行业数字化成熟度：
   - Pre-PMF（数字化起步）/ Growth（快速数字化）/ Mature（深度数字化）
5. 补充行业价值链梳理（从原材料/数据源到终端用户的完整链路）

**输出物**：`行业速览.md`

```markdown
# [行业名] 行业速览

## 行业概况
[1-2段核心摘要]

## 价值链
[从上游到下游的完整链路]

## 数字化成熟度：[Pre-PMF / Growth / Mature]
[判断依据]

## 核心痛点 TOP 5
1. [痛点] — [频率] — [影响]
...

## 关键趋势
- [趋势1]
- [趋势2]

## 信息来源质量评估
| 来源 | 可信度 | 证据强度 | 时效性 | 客观性 |
...

## 共识与争议
- 共识：...
- 争议：...
- 信息空白：...
```

**交付标准**：
- [ ] 至少3个独立来源
- [ ] 每个来源有四维质量评分
- [ ] 价值链完整（至少4个环节）
- [ ] 痛点排序有频率和影响支撑

---

#### ② 竞品格局扫描

**目标**：识别2-4个直接竞品，完成12维评分和SWOT。

**调用子skill**：`competitive-teardown`

**执行步骤**：

1. **定义竞品**：列出2-4个竞品（含客户当前使用的方案）
2. **数据收集**（按 `competitive-teardown` 的数据收集指南）：
   - 网站分析：定价/功能/CTA/案例/集成
   - 评论分析：好评/功能请求/BUG/UX投诉
   - 招聘信号：工程规模/技术栈/AI团队
   - SEO分析：Top关键词/域名权威/内容策略
   - 社交媒体：用户情绪/高频反馈
3. **12维评分**：Features/Pricing/UX/Performance/Docs/Support/Integrations/Security/Scalability/Brand/Community/Innovation — 每维1-5分+证据
4. **生成分析模板**：
   - Feature Comparison Matrix（行×功能，列×竞品，1-5评分）
   - Pricing Analysis（模型/价格区间/免费试用）
   - SWOT Analysis（每竞品3-5条/象限，锚定数据信号）
   - Positioning Map（2×2：简单↔复杂 × 低价值↔高价值）
5. **Action Items**：Quick wins (0-4周) / Medium-term (1-3月) / Strategic (3-12月)

**输出物**：`竞品分析.md`（含评分矩阵、SWOT、定位图、Action Items）

**交付标准**：
- [ ] 至少2个竞品完成完整分析
- [ ] 12维度均有评分和证据
- [ ] SWOT每象限至少3条，锚定数据
- [ ] 有明确的Action Items分层

---

#### ③ 客户现状诊断（AS-IS）

**目标**：理解客户当前的IT系统、数据资产、组织能力。

**调用子skill**：`product-discovery` + `product-manager-toolkit` + `ux-researcher-designer`

**执行步骤**：

1. **假设映射**（`product-discovery` Assumption Mapping）：
   - 列出对客户的所有假设
   - 按四象限分类：Desirability / Viability / Feasibility / Usability
   - 按 高风险×低确定性 排序→优先验证
2. **如有访谈记录**，执行 `product-manager-toolkit` 的Customer Interview Analyzer：
   ```bash
   python scripts/customer_interview_analyzer.py [transcript.txt]
   ```
   提取：Pain Points(含severity) / Feature Requests(含priority) / JTBD / Sentiment / Key Quotes
3. **生成关键人画像**（`ux-researcher-designer` Workflow 1）：
   - 至少3类画像：决策者(CxO) / 使用者(一线员工) / IT负责人(CTO/IT Director)
   - 每类含：Goals / Frustrations / Design Implications
4. **补充IT现状评估**（无子skill，按以下框架自行分析）：
   - 现有核心系统清单（ERP/CRM/WMS等）
   - 数据打通程度（孤岛/部分连通/全连通）
   - AI应用现状（无/试点/规模化）
   - IT团队规模和技术栈

**输出物**：`客户诊断.md`

**交付标准**：
- [ ] 假设清单≥10条，按四象限分类
- [ ] 高风险假设标注验证方式
- [ ] 至少3个关键人画像
- [ ] IT现状四维评估完整

---

### Phase 2: 需求锁定

---

#### ④ 潜在需求挖掘 + 痛点排序

**目标**：从Phase 1的三份文档中提炼结构化需求列表。

**调用子skill**：`product-manager-toolkit`（RICE排序）

**执行步骤**：

1. **MECE问题拆解**：
   - 将客户核心需求拆解为Issue Tree
   - 检查：不重叠(Mutually Exclusive) + 不遗漏(Collectively Exhaustive)
   - 拆解到可映射产品能力的粒度（通常3层）
2. **需求分类**：
   - 战略需求（改变商业模式/进入新市场）
   - 运营需求（提升效率/降低成本）
   - 技术需求（系统升级/数据打通）
3. **RICE优先级排序**（调用 `product-manager-toolkit`）：
   ```bash
   python scripts/rice_prioritizer.py needs.csv --capacity 15
   ```
   输入CSV格式：`name,reach,impact,confidence,effort,description`

   Impact映射：
   - massive = 改变客户商业模式
   - high = 显著提升核心指标
   - medium = 可衡量的效率提升
   - low = 微小改进

**输出物**：`需求清单.md`

```markdown
# [客户名] 需求清单

## Issue Tree
[Mermaid树状图]

## 需求分类
### 战略需求
1. ...
### 运营需求
1. ...
### 技术需求
1. ...

## RICE排序
| 排名 | 需求 | Reach | Impact | Confidence | Effort | RICE Score |
...

## 优先级建议
- Quick Wins: ...
- Big Bets: ...
- Not Now: ...
```

**交付标准**：
- [ ] Issue Tree ≥3层，通过MECE检查
- [ ] 需求总数 ≥ 8条
- [ ] RICE排序每条均有评分依据
- [ ] 明确标注Quick Wins / Big Bets / Not Now

---

#### ⑤ 需求-能力匹配

**目标**：每个需求对标腾讯云能力，标注覆盖度+差距。

**调用工具**：`scripts/capability_match.py` + `scripts/gap_analysis.py` + `references/capability-map.md` + `references/trade-offs.md`

**执行步骤**：

1. **加载能力地图**：读取 `references/capability-map.md`
2. **语义匹配**：对每个需求，运行 `capability_match.py`：
   ```bash
   python scripts/capability_match.py --needs needs.json --capability-map references/capability-map.md --output matched.json
   ```
   输出：每个需求匹配到的腾讯云能力 + 置信度评分(0-1)
3. **差距分析**：运行 `gap_analysis.py`：
   ```bash
   python scripts/gap_analysis.py --matched matched.json --output gap_report.md
   ```
   对每个需求标注：
   - ✅ 完全满足（产品能力直接覆盖，confidence ≥ 0.8）
   - ⚠️ 部分满足（需定制开发或配置，0.4 ≤ confidence < 0.8）
   - ❌ 不满足（需合作伙伴或产品路线图，confidence < 0.4）
4. **权衡决策**：对关键技术决策点，参考 `references/trade-offs.md` 列出：
   - 决策点描述
   - 方案A vs 方案B
   - Pros / Cons / 推荐

**输出物**：`能力匹配.md`

```markdown
# 能力覆盖矩阵

| # | 需求 | 匹配能力 | 覆盖度 | 置信度 | 缓解策略 |
|---|------|---------|:-----:|:-----:|---------|
| 1 | [需求] | ADP-XX + WorkBuddy-YY | ✅ | 0.92 | — |
| 2 | [需求] | 混元API + 向量DB | ⚠️ | 0.65 | 需定制Prompt模板 |
| 3 | [需求] | — | ❌ | 0.20 | 推荐合作伙伴XX |

## 覆盖度统计
- ✅ 完全满足：X/Y (Z%)
- ⚠️ 部分满足：X/Y (Z%)
- ❌ 不满足：X/Y (Z%)

## 关键权衡决策
### 决策1：[描述]
| 维度 | 方案A | 方案B |
...
推荐：[方案X]，原因：...
```

**交付标准**：
- [ ] 所有需求均完成匹配
- [ ] ✅覆盖率 ≥ 60%（否则需重新评估方案可行性）
- [ ] ❌项均有缓解策略
- [ ] 至少2个关键权衡决策有Pros/Cons分析

---

### Phase 3: 方案设计

---

#### ⑥ 解决方案设计 + 产品优先级

**目标**：基于能力匹配结果，设计产品组合方案并排优先级。

**调用子skill**：`product-strategist` + `product-manager-toolkit`

**执行步骤**：

1. **战略分层**（`product-strategist`）：
   根据客户需求性质选择策略类型：
   - Growth：客户要扩大业务规模
   - Retention：客户要降低流失/提升LTV
   - Revenue：客户要提升ARPU/新收入模式
   - Innovation：客户要差异化竞争力
   - Operational：客户要降本增效
2. **OKR级联**（`product-strategist`）：
   ```bash
   python scripts/okr_cascade_generator.py [strategy] --teams "模块A,模块B,模块C"
   ```
   从客户目标→产品目标→模块目标逐层拆解
3. **产品优先级**（`product-manager-toolkit` RICE）：
   对方案中的所有产品模块做RICE排序
4. **方案分阶段**：
   - Phase 1 (POC, 1-2月): Quick Wins，验证核心假设
   - Phase 2 (MVP, 3-6月): 核心功能上线
   - Phase 3 (Scale, 6-12月): 全量推广

**输出物**：`解决方案.md`

**交付标准**：
- [ ] 战略类型选择有依据
- [ ] OKR级联至少2层（客户目标→产品目标）
- [ ] 产品模块RICE排序完整
- [ ] 方案分3个阶段

---

#### ⑦ 架构图生成

**目标**：输出3张架构图（系统架构、数据流、部署架构）。

**调用工具**：`scripts/architecture_gen.py`

**执行步骤**：

1. **读取方案**：从`解决方案.md`提取模块列表和数据流关系
2. **生成Mermaid代码**：
   ```bash
   python scripts/architecture_gen.py --solution solution.json --type system --output architecture.md
   python scripts/architecture_gen.py --solution solution.json --type dataflow --output dataflow.md
   python scripts/architecture_gen.py --solution solution.json --type deployment --output deployment.md
   ```
3. **语法验证 + 修复**：脚本内置Mermaid语法检查，自动修复常见错误
4. **标注腾讯云产品**：每个模块标注对应的腾讯云产品名称

**输出物**：`architecture.md`（含3张Mermaid图）

**架构图规范**：
- 系统架构图：展示层→业务逻辑层→数据层→基础设施层
- 数据流图：数据采集→处理→存储→应用 的完整流转
- 部署架构图：VPC/子网/负载均衡/容器/数据库的物理部署

**交付标准**：
- [ ] 3张图均可正确渲染
- [ ] 每个模块标注腾讯云产品名
- [ ] 数据流方向清晰
- [ ] 部署架构包含安全边界

---

#### ⑧ ROI商业价值测算

**目标**：量化方案的3类商业价值。

**调用工具**：`scripts/roi_calc.py`

**执行步骤**：

1. **效率提升测算**：
   ```bash
   python scripts/roi_calc.py --type efficiency --current-cost [月人力成本] --time-saving [节省比例] --output roi.md
   ```
   公式：年节约 = 月人力成本 × 节省比例 × 12
2. **收入增长测算**：
   ```bash
   python scripts/roi_calc.py --type revenue --conversion-lift [提升比例] --avg-order-value [客单价] --monthly-traffic [月流量]
   ```
   公式：年增量收入 = 月流量 × 转化率提升 × 客单价 × 12
3. **投资回报期**：
   ```bash
   python scripts/roi_calc.py --type payback --investment [方案总成本] --annual-benefit [年收益]
   ```
   公式：回收月数 = 方案成本 ÷ (年收益÷12)
4. **敏感性分析**：对关键假设做±20%波动测试

**输出物**：`ROI测算.md`

**交付标准**：
- [ ] 3类测算至少完成2类
- [ ] 所有输入假设有来源标注
- [ ] 敏感性分析覆盖核心变量
- [ ] 有保守/基准/乐观三档

---

### Phase 4: 包装输出

---

#### ⑨ 竞品差异化叙事（Why Us）

**目标**：从②的竞品分析中提炼"为什么选腾讯云"。

**调用子skill**：`competitive-teardown`（Step 5-6）+ `research-summarizer`

**执行步骤**：

1. 从②的12维评分中，提取腾讯云得分 > 竞品得分的维度
2. 构建Stakeholder Presentation（`competitive-teardown` 7-slide模板）：
   - Slide 1: Executive Summary（威胁等级 + 核心优势 + 推荐行动）
   - Slide 2: 市场定位图（2×2 positioning）
   - Slide 3: 12维评分对比（雷达图/表格）
   - Slide 4: 定价分析
   - Slide 5: UX亮点（3条我们赢 vs 3条对手强）
   - Slide 6: 客户声音（top 3评论引用）
   - Slide 7: 行动计划
3. 匹配同行业成功案例（从案例库或web搜索）

**输出物**：`Why-Us.md`

**交付标准**：
- [ ] 至少3个差异化维度有数据支撑
- [ ] 不回避劣势，有坦诚的"where they are better"
- [ ] 至少1个同行业案例佐证

---

#### ⑩ POC方案 + 落地路径

**目标**：给出"下一步怎么做"。

**调用子skill**：`product-discovery` + `experiment-designer` + `roadmap-communicator`

**执行步骤**：

1. **POC范围界定**（`product-discovery` Discovery Sprint 10天结构）：
   - Day 1-2: Outcome + opportunity framing
   - Day 3-4: Assumption mapping + test design
   - Day 5-7: Problem and solution tests
   - Day 8-9: Evidence synthesis + decision options
   - Day 10: Stakeholder decision review
2. **成功指标定义**（`experiment-designer`）：
   - 写If/Then/Because假设：If [intervention], Then [metric change], Because [mechanism]
   - 定义Primary metric / Guardrail metrics / Secondary metrics
   - 估算样本量：
     ```bash
     python scripts/sample_size_calculator.py --baseline-rate [基线] --mde [最小可检测效应]
     ```
3. **路线图**（`roadmap-communicator` Now/Next/Later）：
   - Now (POC, 1-2月)：核心假设验证
   - Next (MVP, 3-6月)：核心功能上线
   - Later (Scale, 6-12月)：全量推广+持续优化
4. 填充 `templates/poc-plan.md` 模板

**输出物**：`POC方案.md`

**交付标准**：
- [ ] POC范围明确（做什么/不做什么）
- [ ] 成功指标≥3个（1 primary + 1 guardrail + 1 secondary）
- [ ] 时间线具体到周
- [ ] 资源需求明确（人/钱/环境）

---

#### ⑪ 方案文档包

**目标**：打包所有产出为可汇报、可传阅的文档。

**调用子skill**：`roadmap-communicator`

**执行步骤**：

1. **执行摘要**（`roadmap-communicator` Board/Executive模板）：
   - 1页纸，结果导向
   - 含：问题概述→方案概述→预期价值→投入→路线图→风险
2. **方案PPT**（使用WorkBuddy的pptx skill生成）：
   - Slide 1: 封面（客户名+项目名+日期）
   - Slide 2: 行业洞察（来自①）
   - Slide 3: 客户痛点（来自④）
   - Slide 4: 解决方案概览（来自⑥）
   - Slide 5: 系统架构（来自⑦）
   - Slide 6: 能力覆盖矩阵（来自⑤）
   - Slide 7: ROI测算（来自⑧）
   - Slide 8: Why Us（来自⑨）
   - Slide 9: POC方案（来自⑩）
   - Slide 10: 路线图+下一步
3. **技术方案文档**：整合①-⑩所有产出的完整技术版本

**输出物**：3份文档（执行摘要 + PPT + 技术方案）

**交付标准**：
- [ ] 执行摘要≤1页
- [ ] PPT ≤ 15页
- [ ] 所有数字可追溯到前序步骤

---

#### ⑫ 内部评审 Checklist

**目标**：提交客户前的自检。

在最终输出前，逐条检查：

**情报质量**：
- [ ] 行业来源≥3个，质量评分均≥Medium
- [ ] 竞品分析覆盖≥2个竞品，12维评分完整
- [ ] 客户假设清单≥10条

**方案质量**：
- [ ] 能力覆盖矩阵中✅率≥60%
- [ ] 所有❌项有缓解策略
- [ ] 架构图可正确渲染，产品标注准确
- [ ] ROI数字有假设来源，含敏感性分析

**叙事质量**：
- [ ] Why Us不回避劣势
- [ ] PPT叙事逻辑连贯（问题→方案→价值→How）
- [ ] 执行摘要可独立阅读

**落地可行性**：
- [ ] POC范围可2个月内完成
- [ ] 成功指标可量化可测量
- [ ] 资源需求在合理范围内

---

## 行为逻辑

### 启动行为

收到用户请求后：

1. **确认输入**：询问/确认行业、客户名、初始需求描述
2. **判断起点**：
   - 如果用户只给了行业→从①开始
   - 如果用户给了具体客户+需求→从①②③并行开始
   - 如果用户已有行业研究/竞品分析→跳过对应步骤
3. **按Phase顺序推进**：Phase 1→2→3→4，Phase内可并行
4. **每Phase结束时**：汇总该Phase产出，确认用户是否满意再进入下一Phase

### 中断恢复

如果用户说"continue"或"继续"：
- 检查已有产出文件，识别当前进度
- 从断点继续

### 单步执行

如果用户只需要某个步骤（如"帮我做竞品分析"）：
- 直接执行对应步骤
- 不强制执行全流程

### 输出规范

- 所有Markdown文档使用中文
- 架构图使用Mermaid（英文标签+中文注释）
- 数据表格对齐
- 每份文档开头有"最后更新时间"

---

## 相关Skills

- **mckinsey-consultant** — MECE拆解和PPT生成的方法论来源
- **ontology** (WorkBuddy内置) — 方案实体持久化和跨项目复用
- **pptx** (WorkBuddy内置) — 方案PPT生成
