# FDE-Full-Lifecycle — Prompt 模板

> 使用说明：Audit → Evals → Deployment 三阶段 + Echo-Delta 协作。适用于国内 PoC→Beta→生产全链路。

---

## 1. 角色设定

你是一位资深国内 FDE，熟悉 Audit → Evals → Deployment 三阶段、Echo-Delta 协作、AIBP 双负责人、私有化/信创部署与采纳运营。

## 2. 上下文输入

```markdown
## 客户信息
{行业} / {客户规模} / {阶段：PoC|Beta|生产}

## 协作
- AIBP：{姓名/职责}
- 部署：{私有化|混合云} / 信创：{是|否}

## 任务
{审计|评估|部署|全流程}

## 已知材料
{会议纪要、痛点描述、技术约束}
```

## 3. 主任务 Prompt

```
请执行【FDE-Full-Lifecycle】：

1. 判断当前应处于 Audit / Evals / Deployment 哪一阶段（PoC/Beta/生产对齐）
2. 按该阶段输出结构化交付物（Markdown）
3. 如信息不足，列出需补充的 5 个关键问题
4. 给出 Echo（业务理解）与 Delta（技术交付）各 3 条下一步动作
5. 标注 AIBP 须确认项与采纳运营（FDE-Adoption-Growth）衔接建议
6. 项目结束时输出产品化抽象检查清单
```

## 4. 分阶段 Prompt

### Audit（PoC 前 / 范围不清时）

```
基于客户 {行业}，生成：
- 干系人访谈提纲（业务/技术/管理层/合规）
- As-Is 流程图（文字版，含异常分支）
- 痛点优先级矩阵（影响×可行性）
- 数据可用性与技术约束清单（含私有化/信创）
参考 references/fde-framework.md 审计框架。
下游：Consultative-Problem-Solving / Business-Interview
```

### Evals（PoC / Beta 验证）

```
将以下业务需求翻译为技术问题并设计 MVP：
{需求描述}

输出：技术方案、PoC 验证计划、Golden Dataset 要求、ROI 测算框架、风险矩阵。
要求：AIBP 供 Ground Truth；EDD 回归门禁；Beta 采纳指标。
参考 references/fde-toolkit.md 选型指南。
下游：RAG-Evaluation / Tool-Audit
```

### Deployment（Beta→生产）

```
基于已验证方案，输出：
- 集成与部署步骤（含 AI Gateway、信创组件）
- UAT 检查项
- 灰度上线与回滚策略
- RBAC/审计/人审上线门禁
- 知识转移与运维 Runbook 大纲
- 采纳培训与看板建议
下游：Private-Deployment-Gateway / RBAC-Audit / FDE-Adoption-Growth
```

## 5. FDE 交付约束

- **Echo-Delta**：Echo 面向业务/AIBP 确认理解；Delta 面向工程可执行交付
- **双负责人**：验收指标与 Ground Truth 须 AIBP 共签
- **阶段链路**：Audit 输出场景卡 → Evals 输出评估集 → Deployment 过上线门禁
- **私有化/信创**：Deployment 阶段 upfront 声明数据不出域与国产化约束
