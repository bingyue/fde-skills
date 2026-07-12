# 咨询方法论 Reference 库

> **定位**：外部导入的咨询/PPT 方法论 Skill，供本库核心 Skill **按需引用**，不计入 29 个核心 Skill 数量。
> **路径**：`11-Best-Practice/references/`

---

## 与核心 Skill 的区别

| 维度 | 核心 Skill（`11-Best-Practice/<Name>/`） | Reference（本目录） |
| --- | --- | --- |
| 结构 | README + prompt + checklist + evaluation | 以 `SKILL.md` + 资产为主 |
| 用途 | FDE 交付主线能力 | 咨询框架、报告写作、PPT 生成等专项增强 |
| 索引 | 计入 `INDEX.md` 核心 Skill 数 | 计入 `_catalog/consulting-references.md` |
| 激活 | 按交付阶段直接选用 | 与核心 Skill 组合加载 |

---

## Reference 一览

| Reference | 原导入名 | 版本 | 一句话 | 推荐组合 |
| --- | --- | --- | --- | --- |
| [MECE](./MECE/) | `mece` | 2.1.0 | 金字塔原理 + MECE 结构化输出 | Consultative-Problem-Solving、Executive-Communication-Framework |
| [McKinsey-Frameworks](./McKinsey-Frameworks/) | `mckinsey-frameworks` | 1.0.0 | 30+ 经典战略/组织/营销框架速查 | Diagnostic-FDE、Consultative-Problem-Solving |
| [McKinsey-Report](./McKinsey-Report/) | `mckinsey-report` | 1.1.0 | 素材→麦肯锡风格行研报告 + PPT 故事线 | Executive-Communication-Framework、Diagnostic-FDE |
| [McKinsey-PPT-Design](./McKinsey-PPT-Design/) | `mck-ppt-design` | 2.0.0 | python-pptx 麦肯锡风 70 版式 PPT 生成 | McKinsey-Report、Diagnostic-FDE |
| [Elite-PPT-Pro](./Elite-PPT-Pro/) | `elite-ppt-pro` | 1.0.0 | 七大咨询风 38 版式 PPTX+HTML 双输出 | McKinsey-Report、Executive-Communication-Framework |
| [GE-Matrix-Analysis](./GE-Matrix-Analysis/) | — | — | GE/麦肯锡矩阵业务组合分析 | McKinsey-Frameworks、Diagnostic-FDE |

---

## 按交付场景选用

```text
问题拆解 / 结构化表达
  → MECE + Consultative-Problem-Solving

高层汇报 / 决策材料
  → Executive-Communication-Framework + McKinsey-Report

售前方案包 / 行业诊断
  → Diagnostic-FDE + McKinsey-Frameworks + MECE

PPT 交付物
  → McKinsey-Report（故事线）→ McKinsey-PPT-Design 或 Elite-PPT-Pro（出片）

业务组合 / 投资优先级
  → GE-Matrix-Analysis + McKinsey-Frameworks（BCG 对照）
```

---

## 加载方式

1. **Agent 会话**：将对应 `SKILL.md` 路径告知 Agent，或与核心 Skill 的 `prompt.md` 一并加载
2. **按需深读**：各 Reference 的 `references/` 子目录含框架详解、版式库、配色等，执行时再加载
3. **编目登记**：新增 Reference 须更新 [`_catalog/consulting-references.md`](../../_catalog/consulting-references.md)

---

## 目录结构

```text
references/
├── README.md                 # 本索引
├── MECE/
├── McKinsey-Frameworks/
├── McKinsey-Report/
├── McKinsey-PPT-Design/
├── Elite-PPT-Pro/
└── GE-Matrix-Analysis/
```

---

## 变更记录

| 日期 | 变更 |
| --- | --- |
| 2026-07-12 | 从 `11-Best-Practice/` 根目录迁入 `references/`，去除版本号后缀 |
| 2026-07-12 | 清理外部 Reference 作者邮箱与 SEO-PLAN；补充 FDE 组合选用说明 |
