# Consulting References Imported

咨询方法论与 PPT 类外部 Skill，落地于 `11-Best-Practice/references/`。

导入日期：2026-07-12  
**不计入** 29 个核心 Skill 数量。

## 导入结果总览

- 已导入：6
- 落地路径：`11-Best-Practice/references/`

## 映射规则

| Reference | local_path | maps_to_core_skill | 用途 |
| --- | --- | --- | --- |
| MECE | `11-Best-Practice/references/MECE` | Consultative-Problem-Solving | MECE / 金字塔结构化输出 |
| McKinsey-Frameworks | `11-Best-Practice/references/McKinsey-Frameworks` | Diagnostic-FDE | SWOT/BCG/PEST 等框架速查 |
| McKinsey-Report | `11-Best-Practice/references/McKinsey-Report` | Executive-Communication-Framework | 行研报告与 PPT 故事线 |
| McKinsey-PPT-Design | `11-Best-Practice/references/McKinsey-PPT-Design` | Diagnostic-FDE | python-pptx 麦肯锡风 PPT |
| Elite-PPT-Pro | `11-Best-Practice/references/Elite-PPT-Pro` | Executive-Communication-Framework | 多咨询风 PPT 生成 |
| GE-Matrix-Analysis | `11-Best-Practice/references/GE-Matrix-Analysis` | McKinsey-Frameworks | GE/麦肯锡矩阵业务组合 |

## 明细

| slug | 目录名 | version | source | 触发词摘要 |
| --- | --- | --- | --- | --- |
| mece | MECE | 2.1.0 | skills.sh | 分析报告、结构化输出、决策建议 |
| mckinsey-frameworks | McKinsey-Frameworks | 1.0.0 | skills.sh | SWOT、BCG、PEST、安索夫、MECE |
| mckinsey-report | McKinsey-Report | 1.1.0 | skills.sh | 行研报告、咨询风格、PPT 大纲 |
| mck-ppt-design | McKinsey-PPT-Design | 2.0.0 | skills.sh | strategy deck、python-pptx、麦肯锡 PPT |
| elite-ppt-pro | Elite-PPT-Pro | 1.0.0 | skills.sh | 咨询 PPT、战略报告、工作汇报 |
| — | GE-Matrix-Analysis | — | 本地整理 | GE矩阵、麦肯锡矩阵、业务组合 |

## 与 `.agents/skills/` 的区别

| 路径 | 内容 |
| --- | --- |
| `.agents/skills/` | 工程/部署/RAG 等 19 个外部 Skill |
| `11-Best-Practice/references/` | 咨询方法论与 PPT 专项 Reference |

两者均**不单独建顶层目录**，通过 `_catalog/` 映射到本库核心 Skill。

## 维护

- 索引入口：[`11-Best-Practice/references/README.md`](../11-Best-Practice/references/README.md)
- 新增 Reference：去除版本号后缀目录名，更新本文件与 `INDEX.md` 第五节
- 已清理外部导入 Skill 中的个人邮箱与 SEO 推广文档；保留 Apache-2.0 上游来源一行说明
