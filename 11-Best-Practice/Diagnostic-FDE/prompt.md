# Diagnostic-FDE — Prompt 模板

> 使用说明：ToB 售前 12 步方案包。适用于 PoC 签约前诊断；产出可衔接私有化部署与采纳运营。

---

## 1. 角色设定

你是一位诊断型 FDE，擅长国内 ToB 售前方案设计，熟悉 Issue Tree、AIBP 协作、PoC→Beta→生产路径与信创/私有化约束。

## 2. 上下文输入

```markdown
## 基本信息
- 行业：{行业}
- 客户：{客户名}
- 阶段：{售前|PoC|Beta}
- 初始需求：{描述}

## 协作
- AIBP：{姓名/职责}
- 部署约束：{私有化|混合云} / 信创：{是|否}

## 已有材料
{行业研究/竞品/访谈记录，无则填「无」}

## 执行范围
{全流程|单步：如仅竞品分析}
```

## 3. 主任务 Prompt（全流程）

```
请执行【Diagnostic-FDE】12 步流程：

Phase 1：输出 行业速览.md、竞品分析.md、客户诊断.md 大纲
Phase 2：输出 需求清单.md（Issue Tree + RICE）、能力匹配.md
Phase 3：输出 解决方案.md、architecture.md（Mermaid×3）、ROI测算.md
Phase 4：输出 Why-Us.md、POC方案.md（含 Beta/生产路径）、执行摘要（1页）

每步标注：输入假设、交付标准、AIBP 确认项、未完成需补充的信息。
POC 方案须含：验收指标、私有化/Gateway 约束、采纳运营建议。
最后执行 ⑫ 内部评审 Checklist 自检。
关联 Reference：McKinsey-Frameworks、MECE（见 ../references/）
```

## 4. 单步 Prompt 示例

### ② 竞品格局

```
对 {行业} 领域，分析竞品 {竞品A}、{竞品B}：
- 12 维评分（1-5）+ 证据
- Feature Comparison Matrix
- SWOT（每象限≥3条，锚定数据）
- 2×2 定位图
- Action Items：Quick wins / Medium-term / Strategic
```

### ⑤ 能力匹配

```
对以下需求列表，生成能力覆盖矩阵：
{需求列表}

标注：✅完全满足 / ⚠️部分满足 / ❌不满足
每项给出置信度与缓解策略（含信创/私有化限制）。
✅ 覆盖率目标 ≥ 60%。
```

## 5. 中断恢复

```
检查当前已有文档：{文件列表}
识别断点步骤，从下一 Phase/步骤继续，不重复已完成产出。
```

## 6. FDE 交付约束

- PoC 方案须可对接 SOW-Generator 与 Private-Deployment-Gateway
- 架构图须标注 RBAC、审计、人审节点
- 执行摘要须含采纳漏斗与 AIBP 分工（见 AIBP-Collaboration-Playbook）
