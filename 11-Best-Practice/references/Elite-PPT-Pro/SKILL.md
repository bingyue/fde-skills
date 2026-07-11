---
name: elite-ppt-pro
description: >-
  顶级咨询风格 PPT 生成器。融合麦肯锡/BCG/贝恩/埃森哲等七大咨询风格，
  提供 38 种幻灯片版式，支持从数据研究到 PPTX+HTML 双输出的完整工作流。
  适用场景：(1) 制作战略规划/市场分析/竞争格局等咨询报告 PPT，
  (2) 年度总结/工作汇报/团队复盘，(3) 数字化转型/商业模型分析，
  (4) KPI仪表板/数据分析报告，(5) 消费者洞察/市场研究。
  触发词：做PPT、生成PPT、咨询PPT、战略报告、工作汇报PPT、
  市场分析PPT、行业分析PPT、商业报告、investor presentation。
---

# Elite PPT Pro — 顶级咨询PPT融合技能

> **FDE 用途**：Diagnostic-FDE / Executive-Communication 的 PPT 交付物；先 McKinsey-Report 出故事线再出片。  
> **详细配色 → [references/themes.md](references/themes.md)**
> **代码模板 → [references/code-templates.md](references/code-templates.md)**
> **版式库(38种) → [references/slide-types.md](references/slide-types.md)**
> **QA清单 → [references/qa-checklist.md](references/qa-checklist.md)**


## 核心设计理念

| 维度 | 原则 |
|------|------|
| **数据优先** | 先研究收集15+数据点，再动手做PPT |
| **标题即结论** | 每页标题直接写结论，不写话题 |
| **信息密度最大** | 每页至少4个内容区域，数据+图表+分析并存 |
| **颜色克制** | 每页最多2个强调色 |
| **来源标注** | 每个数据点必须有来源，页面底部统一引用 |
| **双输出** | PPTX（可编辑交付）+ HTML（高保真预览） |

---

## 工作流（严格按顺序执行）

### Step 1：研究阶段 — 绝不跳过

先收集数据，再设计。最低标准：
- ≥15个具体数据点（带数字）
- ≥5个不同来源
- 每张内容幻灯片均有对应数据
- 至少1组历史趋势数据
- 竞争对比数据
- 所有引用标注来源名称和日期

数据来源优先级：Tier1官方数据 > Tier2顶级研究机构 > Tier3行业报告 > Tier4权威媒体 > Tier5公司官网

### Step 2：策划幻灯片结构

默认10页结构：封面 → 核心洞察摘要 → 6页内容页 → 执行建议 → 附录。典型8-15页。

### Step 3：选择风格

| 风格 | 主色 | 适用场景 |
|------|------|----------|
| A 咨询青绿 | `#00A69C` | 战略规划、市场分析、投资人汇报 |
| B 职场紫 | `#7B5EA7` | 年度总结、工作汇报、团队复盘 |
| C 商业绿 | `#2D8A6A` | 商业框架、策略分析、产品管理 |
| D 贝恩红 | `#C41E3A` | 消费者洞察、市场研究 |
| E 埃森哲蓝 | `#0369A1` | 数字化转型、战略布局 |
| F 消费者橙 | `#E65100` | 消费者行为研究 |
| G 数据蓝 | `#1A237E` | KPI仪表板、数据报告 |
| 麦肯锡 | `#0B1F3A` | 严肃正式汇报 |

> 完整配色代码见 **[references/themes.md](references/themes.md)**

### Step 4：选择版式（38种）

详见 **[references/slide-types.md](references/slide-types.md)**，按数据类型推荐：

| 数据类型 | 推荐版式 |
|----------|----------|
| 市场增长趋势 | A5数据看板 / G3阶梯增长 |
| 竞争格局 | A3竞争矩阵 / C11波特三角 |
| 战略路径 | A2战略箭头 / A6流程步骤 |
| 用户分析 | C9客户旅程 / F1消费者旅程 |
| 业务框架 | C10商业画布 / C1SWOT |
| KPI汇报 | G1KPI仪表板 / B5增长箭头 |

### Step 5：生成PPTX代码

使用 pptxgenjs。每页结构模板和所有辅助函数（`addEliteHeader`, `addKPICard`, `addBulletPoints`, `addDataCard`, `addDataSource`, `addPageBadge`）见 **[references/code-templates.md](references/code-templates.md)**。

### Step 6：HTML预览版（可选但推荐）

生成对应HTML版本用于浏览器演示和在线分享。

### Step 7：QA检查

详见 **[references/qa-checklist.md](references/qa-checklist.md)**，强制检查项：
- 标题是结论，不是话题
- 每个数据点有来源标注
- 每页≥4个内容区域
- 全文最多2个强调色
- 文字无截断（wrap: true）
- 布局不超出幻灯片边界

---

## 技术规范速查

### 必须遵守

| 规范 | 要求 |
|------|------|
| 颜色 | 6字符hex，无#前缀 |
| 字体 | 中文 Microsoft YaHei，英文 Arial |
| 背景 | 内容页强制白色 `FFFFFF` |
| 形状 | 用字符串 `"rect"` / `"oval"` / `"line"` |
| 边界 | x+w ≤ 10，y+h ≤ 5.625 |
| wrap | 多行文本必须 `wrap: true` |

### 明确禁止

| 禁止 | 替代 |
|------|------|
| 颜色带 `#` 前缀 | 直接写6字符hex |
| 无来源的数据声明 | 标注来源机构+日期 |
| 标题写话题而非结论 | 改为"数据显示XX领先" |
| 单页超过2个强调色 | 合并为主题色 |
| 空洞的定性描述 | 替换为具体数字 |

---

## 快速开始

```javascript
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
// 主题从 references/themes.md 中选择
const theme = { /* 风格A */ primary:"1A1A2E", secondary:"2D6A6A", accent:"00A69C", light:"E8F7F6", bg:"FFFFFF", darkText:"333333", midText:"666666", border:"DDDDDD" };

// 封面页
const cover = pres.addSlide();
cover.background = { color: theme.primary };
cover.addText("AI行业竞争格局深度分析", {
  x: 1, y: 1.6, w: 8, h: 1.2, fontSize: 40, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", wrap: true
});

// 内容页 — 完整辅助函数见 references/code-templates.md
// ... 使用 addEliteHeader, addKPICard, addBulletPoints, addDataSource, addPageBadge

pres.writeFile({ fileName: "output.pptx" });
```
