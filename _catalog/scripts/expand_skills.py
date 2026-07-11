#!/usr/bin/env python3
"""Generate rich deliverable content for all FDE-Skills."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 相邻 Skill 交叉引用（相对路径从各 Skill 目录出发）
CROSS_REFS = {
    "01-Foundation/FDE-Self-Assessment": [
        ("../FDE-Growth-Roadmap/README.md", "FDE-Growth-Roadmap", "成长路线与作品集绑定"),
        ("../Communication-Script-Library/README.md", "Communication-Script-Library", "沟通短板补齐"),
        ("../../11-Best-Practice/China-FDE-Consulting-Pattern/README.md", "China-FDE-Consulting-Pattern", "四角色能力地图"),
    ],
    "01-Foundation/FDE-Growth-Roadmap": [
        ("../FDE-Self-Assessment/README.md", "FDE-Self-Assessment", "能力基线输入"),
        ("../Communication-Script-Library/README.md", "Communication-Script-Library", "软技能成长路径"),
        ("../../11-Best-Practice/China-FDE-Consulting-Pattern/README.md", "China-FDE-Consulting-Pattern", "交付阶段对照"),
    ],
    "01-Foundation/Communication-Script-Library": [
        ("../../02-Discovery/Expectation-Management-Script/README.md", "Expectation-Management-Script", "AI 概率性边界话术"),
        ("../../02-Discovery/Executive-Communication-Framework/README.md", "Executive-Communication-Framework", "高层汇报话术"),
        ("../../02-Discovery/AIBP-Collaboration-Playbook/README.md", "AIBP-Collaboration-Playbook", "双负责人协作沟通"),
    ],
    "01-Foundation/Stakeholder-Mapping": [
        ("../SOW-Generator/README.md", "SOW-Generator", "Kickoff 后书面化范围"),
        ("../../02-Discovery/AIBP-Collaboration-Playbook/README.md", "AIBP-Collaboration-Playbook", "识别 AIBP 与业务 Owner"),
        ("../../02-Discovery/Business-Interview/README.md", "Business-Interview", "干系人深度访谈"),
    ],
    "01-Foundation/SOW-Generator": [
        ("../../10-Templates/SOW-Template/README.md", "SOW-Template", "标准模板基座"),
        ("../Stakeholder-Mapping/README.md", "Stakeholder-Mapping", "签约方与决策链"),
        ("../../02-Discovery/Consultative-Problem-Solving/README.md", "Consultative-Problem-Solving", "PoC 假设与范围来源"),
    ],
    "02-Discovery/Business-Interview": [
        ("../Consultative-Problem-Solving/README.md", "Consultative-Problem-Solving", "访谈输出喂给问题树"),
        ("../Process-Mapping/README.md", "Process-Mapping", "流程走查深化"),
        ("../../03-Solution-Design/PRD-Generator/README.md", "PRD-Generator", "需求规格化"),
    ],
    "02-Discovery/Process-Mapping": [
        ("../Business-Interview/README.md", "Business-Interview", "流程访谈输入"),
        ("../Consultative-Problem-Solving/README.md", "Consultative-Problem-Solving", "AI 介入点验证"),
        ("../../03-Solution-Design/PRD-Generator/README.md", "PRD-Generator", "流程写入 PRD"),
    ],
    "02-Discovery/Consultative-Problem-Solving": [
        ("../../11-Best-Practice/China-FDE-Consulting-Pattern/README.md", "China-FDE-Consulting-Pattern", "咨询式交付总纲"),
        ("../../11-Best-Practice/references/MECE/SKILL.md", "MECE", "问题树 MECE 校验"),
        ("../Process-Mapping/README.md", "Process-Mapping", "Embed 流程嵌入点"),
    ],
    "02-Discovery/Expectation-Management-Script": [
        ("../Executive-Communication-Framework/README.md", "Executive-Communication-Framework", "高层预期校准"),
        ("../../01-Foundation/Communication-Script-Library/README.md", "Communication-Script-Library", "分角色话术库"),
        ("../../07-Operations/FDE-Adoption-Growth/README.md", "FDE-Adoption-Growth", "采纳阶段预期管理"),
    ],
    "02-Discovery/Executive-Communication-Framework": [
        ("../../07-Operations/FDE-Adoption-Growth/README.md", "FDE-Adoption-Growth", "续约与价值播报"),
        ("../Expectation-Management-Script/README.md", "Expectation-Management-Script", "ROI 叙事中的边界声明"),
        ("../../11-Best-Practice/references/McKinsey-Report/SKILL.md", "McKinsey-Report", "行研报告与 Deck 故事线"),
    ],
    "02-Discovery/AIBP-Collaboration-Playbook": [
        ("../../01-Foundation/Stakeholder-Mapping/README.md", "Stakeholder-Mapping", "双负责人识别"),
        ("../../07-Operations/FDE-Adoption-Growth/README.md", "FDE-Adoption-Growth", "运营移交与采纳"),
        ("../../04-AI-Delivery/RAG-Evaluation/README.md", "RAG-Evaluation", "Ground Truth 共建"),
    ],
    "03-Solution-Design/PRD-Generator": [
        ("../../02-Discovery/Business-Interview/README.md", "Business-Interview", "需求来源"),
        ("../../02-Discovery/Process-Mapping/README.md", "Process-Mapping", "流程与介入点"),
        ("../../04-AI-Delivery/RAG-Evaluation/README.md", "RAG-Evaluation", "验收指标转评估集"),
    ],
    "03-Solution-Design/API-Design-Review": [
        ("../PRD-Generator/README.md", "PRD-Generator", "集成需求来源"),
        ("../../06-Integration/Feishu-Integration/README.md", "Feishu-Integration", "飞书/IM 集成契约"),
        ("../../04-AI-Delivery/Tool-Audit/README.md", "Tool-Audit", "Agent 工具契约"),
    ],
    "04-AI-Delivery/RAG-Evaluation": [
        ("../../02-Discovery/AIBP-Collaboration-Playbook/README.md", "AIBP-Collaboration-Playbook", "Ground Truth 样本"),
        ("../Tool-Audit/README.md", "Tool-Audit", "检索权限边界"),
        ("../../08-Security-Compliance/RBAC-Audit/README.md", "RBAC-Audit", "知识库权限审计"),
    ],
    "04-AI-Delivery/Tool-Audit": [
        ("../../03-Solution-Design/API-Design-Review/README.md", "API-Design-Review", "工具 API 契约"),
        ("../../08-Security-Compliance/RBAC-Audit/README.md", "RBAC-Audit", "最小权限与人审"),
        ("../RAG-Evaluation/README.md", "RAG-Evaluation", "上线回归门禁"),
    ],
    "05-Deployment/Private-Deployment-Gateway": [
        ("../../08-Security-Compliance/RBAC-Audit/README.md", "RBAC-Audit", "私有化权限与等保"),
        ("../Tool-Audit/README.md", "Tool-Audit", "Gateway 工具审计"),
        ("../../06-Integration/Feishu-Integration/README.md", "Feishu-Integration", "协同层集成"),
    ],
    "06-Integration/Feishu-Integration": [
        ("../../02-Discovery/AIBP-Collaboration-Playbook/README.md", "AIBP-Collaboration-Playbook", "周度 Demo 协同"),
        ("../../07-Operations/FDE-Adoption-Growth/README.md", "FDE-Adoption-Growth", "采纳嵌入协作流"),
        ("../../07-Operations/Customer-Service-Bot/README.md", "Customer-Service-Bot", "客服机器人入口"),
    ],
    "07-Operations/Customer-Service-Bot": [
        ("../../04-AI-Delivery/RAG-Evaluation/README.md", "RAG-Evaluation", "知识库评估"),
        ("../../06-Integration/Feishu-Integration/README.md", "Feishu-Integration", "工单与消息推送"),
        ("../FDE-Adoption-Growth/README.md", "FDE-Adoption-Growth", "客服采纳运营"),
    ],
    "07-Operations/FDE-Adoption-Growth": [
        ("../../02-Discovery/AIBP-Collaboration-Playbook/README.md", "AIBP-Collaboration-Playbook", "Champion 与双负责人"),
        ("../../02-Discovery/Executive-Communication-Framework/README.md", "Executive-Communication-Framework", "续约价值汇报"),
        ("../SQL-Dashboard-Brief/README.md", "SQL-Dashboard-Brief", "采纳看板指标"),
    ],
    "07-Operations/SQL-Dashboard-Brief": [
        ("../FDE-Adoption-Growth/README.md", "FDE-Adoption-Growth", "采纳漏斗 KPI"),
        ("../Customer-Service-Bot/README.md", "Customer-Service-Bot", "客服运营指标"),
        ("../../08-Security-Compliance/RBAC-Audit/README.md", "RBAC-Audit", "看板权限设计"),
    ],
    "08-Security-Compliance/RBAC-Audit": [
        ("../../04-AI-Delivery/Tool-Audit/README.md", "Tool-Audit", "Agent 工具权限"),
        ("../../05-Deployment/Private-Deployment-Gateway/README.md", "Private-Deployment-Gateway", "私有化部署合规"),
        ("../../04-AI-Delivery/RAG-Evaluation/README.md", "RAG-Evaluation", "检索过滤与脱敏"),
    ],
    "09-Industry/AI-Operations-Daily": [
        ("../../07-Operations/FDE-Adoption-Growth/README.md", "FDE-Adoption-Growth", "运营采纳模式"),
        ("../../07-Operations/SQL-Dashboard-Brief/README.md", "SQL-Dashboard-Brief", "日报指标看板"),
        ("../../07-Operations/Customer-Service-Bot/README.md", "Customer-Service-Bot", "舆情/客服联动"),
    ],
    "10-Templates/SOW-Template": [
        ("../../01-Foundation/SOW-Generator/README.md", "SOW-Generator", "模板填写与评审"),
        ("../../01-Foundation/Stakeholder-Mapping/README.md", "Stakeholder-Mapping", "签约方信息"),
    ],
    "11-Best-Practice/Palantir-FDE-Pattern": [
        ("../China-FDE-Consulting-Pattern/README.md", "China-FDE-Consulting-Pattern", "国内本土化对照"),
        ("../FDE-Full-Lifecycle/README.md", "FDE-Full-Lifecycle", "Audit→Evals→Deployment"),
    ],
    "11-Best-Practice/China-FDE-Consulting-Pattern": [
        ("../../02-Discovery/Consultative-Problem-Solving/README.md", "Consultative-Problem-Solving", "咨询环核心"),
        ("../FDE-Full-Lifecycle/README.md", "FDE-Full-Lifecycle", "构建与部署环"),
        ("../Diagnostic-FDE/README.md", "Diagnostic-FDE", "售前方案包"),
    ],
}

CASE_SNIPPETS = {
    "FDE-Self-Assessment": ("某金融客户 PoC 项目", "FDE 自评 L3 但沟通 L1，Beta 阶段业务方停止参加周度 Demo", "四角色评分暴露沟通阻塞短板，30 天计划绑定 Communication-Script + AIBP 共创场景卡", "60 天后周度 Demo 恢复，生产上线门禁一次通过"),
    "FDE-Growth-Roadmap": ("新人 FDE onboarding", "仅有课程学习记录，无可展示交付物", "路线图绑定场景卡、Golden Dataset、Demo 录像三件作品集", "90 天完成首个独立 PoC 主导"),
    "Communication-Script-Library": ("PoC 延期通报", "项目组用技术日志向业务 Owner 解释延期，引发信任危机", "选用「业务对象话术包」重述影响、选项与下一步", "业务 Owner 书面确认新里程碑"),
    "Stakeholder-Mapping": ("政企 AI 立项", "IT 支持但合规未入场，上线前被否决", "干系人矩阵识别隐形合规反对者，Kickoff 前拉齐", "合规评审前置 2 周完成"),
    "SOW-Generator": ("智能客服 PoC", "口头约定「做智能客服」，验收时争议准确率指标", "SOW 绑定 FAQ 场景、≥80% 准确率、20 条 Golden 样本", "PoC 4 周验收无追加纠纷"),
    "Business-Interview": ("制造业质检场景", "客户要求「上视觉 AI 平台」", "结构化访谈还原检验流程，获得 15 条真实缺陷样本", "PoC 范围收敛到单产线 AOI 辅助"),
    "Process-Mapping": ("财务报销自动化", "只画主路径，忽略退单/补件分支", "泳道图标异常分支与人审节点", "Beta 采纳率从 12% 提升到 58%"),
    "Consultative-Problem-Solving": ("智能体平台诉求", "客户要全公司统一 Agent 平台", "Issue Tree + DIVE 收敛到售后 FAQ PoC", "PoC 周期 12 周→4 周"),
    "Expectation-Management-Script": ("RAG Demo 后", "业务方认为「AI 应该 100% 准确」", "分角色话术讲清概率性、人审策略与迭代路径", "客户书面确认 Beta 阶段人工复核 100%"),
    "Executive-Communication-Framework": ("预算追加汇报", "FDE 讲 30 分钟架构细节，高管无决策", "一页纸：ROI + 风险 + 三选项，15 分钟汇报", "获得 Beta 扩展预算批准"),
    "AIBP-Collaboration-Playbook": ("PoC 组队", "FDE 独自定义验收，AIBP 未供 Ground Truth", "RACI + 场景卡双签 + 周度 Demo 机制", "Golden Dataset 20 条由 AIBP 确认"),
    "PRD-Generator": ("场景评审后", "开发与业务对「做什么」理解不一致", "场景卡扩展 PRD，验收标准可测试", "开发估时偏差从 40% 降到 10%"),
    "API-Design-Review": ("Agent 接 ERP", "工具无超时重试，一次故障导致工单重复创建", "API 评审补齐幂等、错误码、审计日志", "联调 3 天完成无 P0"),
    "RAG-Evaluation": ("知识库 PoC", "凭感觉调参，客户质疑效果", "EDD 五层指标 + 30 条 Golden Dataset + 回归门禁", "Beta 引用准确率 78% 达上线阈值"),
    "Tool-Audit": ("MCP 多工具 Agent", "工具权限过大，误删测试数据", "最小权限 + 人审 + 全链路日志", "生产上线 Tool-Audit 零 P0"),
    "Private-Deployment-Gateway": ("信创私有化", "PoC 用公有云 Demo，生产无法迁移", "三层路径选型 + AI Gateway 鉴权审计", "PoC→生产同架构迁移 2 周完成"),
    "Feishu-Integration": ("周度 Demo 协同", "AI 输出在独立页面，一线不用", "机器人嵌入现有审批/多维表格流程", "试点 5 人周活 100%"),
    "Customer-Service-Bot": ("售后客服 PoC", "Bot 能答但无人用，转人工率 90%", "分流规则 + 工单闭环 + 采纳看板", "Beta 首响降 35%，转人工 40%"),
    "FDE-Adoption-Growth": ("PoC 成功但续约难", "技术验收通过，WAU < 5%", "采纳漏斗诊断 + Champion 计划 + 价值播报", "续约前 WAU 达 32%"),
    "SQL-Dashboard-Brief": ("运营复盘无数据", "有 Agent 无指标，管理层看不到价值", "5 个 KPI 简报 + 权限矩阵", "采纳看板上线，周会引用数据决策"),
    "RBAC-Audit": ("政企上线门禁", "全员可检索全部知识库", "RBAC 审计 + 检索过滤 + 脱敏", "等保评审一次通过"),
    "AI-Operations-Daily": ("品牌跨境运营", "人盯 5 渠道舆情，日会无结构化输入", "日报 Agent + 分级预警 + 人审", "7 天稳定推送，捕获 2 次竞品异动"),
    "SOW-Template": ("新售前项目", "每次从零写 SOW，法务评审慢", "复制 11 章模板 + SOW-Generator 定制", "SOW 起草时间 3 天→4 小时"),
    "Palantir-FDE-Pattern": ("团队方法论设计", "只知国内案例，缺国际范式对照", "Palantir 模式本土化对照表", "采纳 3 项可落地实践（Ontology 轻量版等）"),
    "China-FDE-Consulting-Pattern": ("交付标准化", "各项目打法不一致，新人上手慢", "五环交付 + 会议地图 + 资产化清单", "团队统一 Kickoff→上线门禁节奏"),
}


def section(title, body):
    return f"\n## {title}\n\n{body}\n"


def gen_cross_refs(path_key, s):
    refs = CROSS_REFS.get(path_key, [])
    lines = []
    if refs:
        lines.append("### 推荐组合\n")
        for href, name, desc in refs:
            lines.append(f"- [{name}]({href}) — {desc}")
    ext = s.get("external_refs") or []
    if ext:
        lines.append("\n### 外部工程参考\n")
        for e in ext:
            lines.append(f"- `{e}`")
    if not lines:
        lines.append("- 见 `_catalog/fde-skill-map.md` 交付链路图")
    return "\n".join(lines)


def gen_scenario_deep(s):
    parts = []
    steps = s["steps"]
    pitfalls = s["pitfalls"]
    for i, sc in enumerate(s["scenes"]):
        step = steps[i] if i < len(steps) else steps[-1]
        pitfall = pitfalls[i % len(pitfalls)]
        parts.append(
            f"### 场景 {i + 1}：{sc}\n\n"
            f"**触发信号**：PoC/Beta/生产任一阶段出现「{sc}」相关诉求、阻塞或复盘需求。\n\n"
            f"**关键动作**：{step}\n\n"
            f"**FDE 注意**：避免 {pitfall}\n\n"
            f"**成功标志**：交付物清单勾选，evaluation.md 达标，AIBP/业务 Owner 书面确认。\n"
        )
    return "\n".join(parts)


def gen_faq(s):
    title = s["title"]
    pitfalls = s["pitfalls"]
    qs = [
        (f"执行【{title}】时如何避免「{pitfalls[0]}」？", f"按 README 方法论逐步执行，在周度 Demo 展示阶段性交付物；若 PoC 材料不齐，先输出「待验证清单」再推进。"),
        ("私有化/信创/等保环境下有哪些额外约束？", "在 prompt 约束段明确部署形态；涉及数据不出域、国产化组件、审计日志时同步引用 Private-Deployment-Gateway 与 RBAC-Audit。"),
        ("与 AIBP 分工边界不清怎么办？", "回到 AIBP-Collaboration-Playbook 更新 RACI；AIBP 负责 Ground Truth 与业务验收，FDE 负责可交付技术资产。"),
        ("PoC 通过后如何衔接到 Beta/生产？", "输出物中标注下一阶段 Skill（如 RAG-Evaluation→Private-Deployment-Gateway→FDE-Adoption-Growth），并在 checklist 触发上线门禁。"),
    ]
    return "\n".join(f"**Q{i + 1}：{q}**\n\nA：{a}\n" for i, (q, a) in enumerate(qs))


def gen_case_snippet(s):
    title = s["title"]
    bg, before, after, result = CASE_SNIPPETS.get(title, (
        "某制造企业 AI 项目",
        "团队按通用流程推进，范围漂移",
        f"按【{title}】方法论结构化交付",
        "PoC 周期缩短，业务 Owner 签字确认验收标准",
    ))
    return f"""> 以下为示意性片段，实际项目请替换为客户真实信息（数据脱敏）。

**背景**：{bg}。

**应用本 Skill 前**：{before}。

**应用本 Skill 后**：
1. 按【{title}】方法论输出核心交付物
2. 在周度 Demo 展示进展，AIBP 共审 Ground Truth/指标
3. 对照 evaluation.md 自评，触发上线门禁（如适用）

**结果**：{result}。"""


def gen_readme(cat, path_key, s):
    lines = [
        f"# {s['title']}",
        "",
        f"- **分类**：`{cat}`",
        f"- **成熟度**：`usable`",
        f"- **一句话**：{s['subtitle']}",
        "",
        "---",
        section("适用场景", "\n".join(f"- {x}" for x in s["scenes"])),
        section("问题定义", s["problem"]),
        section("方法论框架", s["methodology"]),
        section("输入 / 输出", f"""### 输入

{chr(10).join(f'- {x}' for x in s['inputs'])}

### 输出

{chr(10).join(f'- {x}' for x in s['outputs'])}"""),
        section("执行步骤", "\n".join(f"{i + 1}. {x}" for i, x in enumerate(s["steps"]))),
        section("常见误区", "\n".join(f"- ❌ {x}" for x in s["pitfalls"])),
        section("交付物清单", "\n".join(f"- [ ] {x}" for x in s["deliverables"])),
        section("与国内 FDE 生态关联", s["fde_ecosystem"]),
    ]
    lines.append(section("阶段门控", """| 阶段 | 进入条件 | 退出标准 |
| --- | --- | --- |
| PoC 准备 | 干系人识别、场景卡草稿、数据/权限前置条件确认 | 范围与验收指标书面确认 |
| PoC/Beta 执行 | 方法论对齐、AIBP 双签场景卡 | 核心交付物初稿 + 周度 Demo ≥1 次 |
| 生产门禁 | RBAC/评估/人审/日志检查通过 | evaluation.md 指标 ≥80% |
| 复盘资产化 | 阶段结束或里程碑完成 | 可复用模板/评估集沉淀至 `10-Templates` 或 `_catalog` |"""))
    lines.append(section("协作接口", """| 角色 | 本 Skill 中的职责 | 交接物 |
| --- | --- | --- |
| FDE | 主导本 Skill 执行与交付 | 过程文档 + 验收材料 |
| AIBP | 提供业务口径、Ground Truth、验收反馈 | 场景卡 / 样本 / 指标定义 |
| 业务 Owner | 决策优先级与范围 | 签字确认的范围与验收 |
| IT/安全 | 评审权限、部署、信创/等保边界 | 评审意见与整改清单 |"""))
    lines.append(section("关联 Skill", gen_cross_refs(path_key, s)))
    lines.append(section("场景深潜", gen_scenario_deep(s)))
    lines.append(section("术语表", """| 术语 | 含义 |
| --- | --- |
| FDE | Forward Deployed Engineer，嵌入客户现场的技术交付角色 |
| AIBP | AI Business Partner，业务效果与 Ground Truth 负责人 |
| PoC | Proof of Concept，验证核心假设的最小可运行版本 |
| Beta | 小范围试点，验证采纳与流程嵌入 |
| 信创 | 信息技术应用创新，国产化软硬件与合规要求 |
| EDD | Evaluation Driven Development，评估驱动开发 |
| Ground Truth | 业务真值样本，用于评估与验收 |
| 场景卡 | FDE 与 AIBP 对场景范围、指标、边界的共同协议 |
| 周度 Demo | 按周演示进展、收集反馈的项目节奏控制器 |
| 上线门禁 | 生产发布前对权限、评估、人审、日志的检查关卡 |"""))
    lines.append(section("常见问题 FAQ", gen_faq(s)))
    lines.append(section("案例片段（示意）", gen_case_snippet(s)))
    lines.append(section("版本记录", "| 版本 | 日期 | 变更 |\n| --- | --- | --- |\n| v1.1 | 2026-07-12 | FDE 场景增强：交叉引用、场景深潜、FAQ |\n| v1.0 | 2026-07-12 | 目录重组后首次充实版 |"))
    return "\n".join(lines) + "\n"


def gen_prompt(s):
    return f"""# {s['title']} — Prompt 模板

> 使用说明：将 `{{占位符}}` 替换为实际项目信息。建议分阶段调用，不要一次塞入全部上下文。

---

## 1. 角色设定

你是一位资深国内 FDE（Forward Deployed Engineer），熟悉企业 AI 落地、咨询式交付和国内私有化/信创生态。
你的任务：{s['prompt_focus']}

---

## 2. 上下文输入

```markdown
## 项目背景
{{项目名称}} / {{行业}} / {{阶段：PoC|Beta|生产}}

## 协作
- AIBP：{{姓名/职责}}
- 业务 Owner：{{姓名}}
- 部署：{{私有化|混合云|公有云}} / 信创：{{是|否}}

## 已知信息
{{粘贴已有文档、会议纪要、数据条件}}

## 约束
- 合规：{{等保|数据出境|行业监管}}
- 协同：{{飞书|企业微信|钉钉}}
- 时间：{{里程碑日期}}
```

---

## 3. 主任务 Prompt

```
请基于以上上下文，执行【{s['title']}】：

1. 先用 5 句话重述问题定义，确认理解无误
2. 按方法论框架逐步推进（见 README 方法论章节）
3. 输出完整交付物，格式为 Markdown
4. 列出 3 个最大风险和缓解动作
5. 给出下一步建议（含关联 Skill 相对路径）

要求：
- 不编造客户未提供的数据
- 对概率性 AI 能力明确标注不确定性
- 涉及权限/合规/信创时主动提示人工审核节点
- PoC 产出须标注如何衔接到 Beta/生产与采纳运营
```

---

## 4. 分阶段 Prompt

### 4.1 准备阶段

```
请为【{s['title']}】生成准备清单：
- 需要谁参与（FDE/AIBP/IT/合规）、需要什么输入材料
- Kickoff 或场景评审议程（如适用）
- PoC 第一周工作计划与飞书协同方式
```

### 4.2 执行阶段

```
请基于当前进展，输出本 Skill 的核心交付物草稿。
标注：已完成 / 进行中 / 阻塞（含阻塞原因）
如涉及私有化或信创，单独列出环境与组件约束。
```

### 4.3 验收阶段

```
请对照 evaluation.md 标准做自评：
- 逐项给出达标/未达标判断和证据
- 未达标项给出 7 天内可完成的补救计划
- Beta/生产阶段须确认 RBAC、评估回归、人审策略
```

### 4.4 复盘阶段

```
请总结本 Skill 执行复盘：
- 3 个做得好的点
- 3 个改进点
- 可沉淀到 10-Templates / _catalog 的资产建议
- 采纳运营（FDE-Adoption-Growth）需跟进的项
```

---

## 5. 输出格式约束

- 标题层级不超过 3 级
- 表格用于对比和清单
- 决策项用「建议 + 理由 + 风险」三段式
- 中文为主，技术术语保留英文缩写

---

## 6. FDE 交付约束（国内场景）

- **阶段链路**：PoC 验证假设 → Beta 验证采纳与流程嵌入 → 生产过上线门禁
- **双负责人**：关键验收与 Ground Truth 须 AIBP 确认，FDE 不独自签字
- **私有化/信创**：数据不出域、审计日志、国产化组件兼容须 upfront 声明
- **采纳**：技术验收 ≠ 业务成功，PoC 输出须含采纳/培训/看板建议
"""


def gen_checklist(s):
    phases = s["checklist_phases"]
    out = [f"# {s['title']} — 执行清单\n"]
    for phase, items in phases.items():
        out.append(f"\n## {phase}\n")
        for item in items:
            out.append(f"- [ ] {item}")
    out.append("""

## FDE 阶段门禁

- [ ] PoC：场景卡双签、验收指标可量化、数据/权限前置条件满足
- [ ] Beta：周度 Demo 节奏建立、采纳看板或埋点就绪、失败样本入库
- [ ] 生产：RBAC-Audit + 评估回归 + 人审策略 + 运维 Runbook 过门禁
- [ ] 信创/私有化（如适用）：部署架构与 Gateway 审计项已确认

## 阻塞升级

- [ ] 阻塞超过 2 个工作日 → 升级 AIBP / 项目负责人
- [ ] 涉及安全合规/等保 → 同步 08-Security-Compliance/RBAC-Audit
- [ ] 范围变更 → 重走 SOW-Generator / 场景卡确认
""")
    return "\n".join(out) + "\n"


def gen_evaluation(s):
    metrics = s["eval_metrics"]
    rows = "\n".join(f"| {m[0]} | {m[1]} | {m[2]} | {m[3]} |" for m in metrics)
    return f"""# {s['title']} — 评估标准

## 1. 通过门槛

全部「必达指标」达到 **≥80%** 方可标记本 Skill 交付完成。

## 2. 指标矩阵

| 维度 | 必达标准 | 失败信号 | 验收证据 |
| --- | --- | --- | --- |
{rows}

## 3. 分项验收细则

### 3.1 交付物完整性

- 检查 README 交付物清单是否全部产出
- 交付物需有版本号和日期
- 关键文档需 AIBP 或业务 Owner 确认（邮件/飞书纪要）

### 3.2 质量门禁

- 无编造数据或虚假指标
- 风险与边界写清楚，尤其 AI 概率性输出
- 与国内私有化/信创/等保场景一致

### 3.3 可复用性

- 至少 1 项输出可迁入 `10-Templates` 或项目资产库
- prompt.md 模板可在下一个 PoC 项目直接复用

### 3.4 FDE 阶段对齐

| 阶段 | 额外验收 |
| --- | --- |
| PoC | 场景卡双签、指标可采集 |
| Beta | 采纳数据或看板就绪 |
| 生产 | RBAC + 评估回归 + 人审过门禁 |

## 4. 样品验收标准（示例）

```
Given 项目阶段 = PoC
When 执行本 Skill 全部步骤
Then:
  - 核心交付物 ≥ 1 份经 AIBP/业务 Owner 确认的 Markdown 文档
  - checklist.md 准备+执行项完成率 ≥ 90%
  - 无 P0 阻塞项未升级
  - 输出含 Beta/生产衔接建议（如适用）
```

## 5. 不通过处置

| 级别 | 条件 | 动作 |
| --- | --- | --- |
| P0 | 缺失核心交付物 | 停止下游依赖，3 天内补齐 |
| P1 | 指标未达标但有改进路径 | 开补救 sprint，周度 Demo 跟踪 |
| P2 | 文档质量不达标 | 同行评审后修订 |
"""

if __name__ == "__main__":
    print("Run expand_skills_data.py instead")
