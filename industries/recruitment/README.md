# 招聘 / Recruitment

职位理解、候选资料整理、面试与排程辅助。

[机器可读扩展](pack.yaml) 按 `extends` 引用通用 Skill；约束追加，指标与术语提供行业语境，禁止覆盖通用权限和证据门禁。

## 场景

- **jd-clarification**：把岗位愿望改为可验证的工作能力与成果；验收：每个必需条件与实际工作职责相关。
- **resume-evidence**：从获授权简历提取经历证据；验收：保留原文，不推断未披露的个人属性。
- **matching-assistance**：按公开岗位标准整理证据与缺口；验收：最终筛选由授权招聘者复核，可解释与可纠正。
- **interview-plan**：生成针对工作能力的结构化面试题；验收：问题关联岗位，不询问无关敏感属性。
- **scheduling**：生成面试时段与邀请草稿；验收：时区与参与者确认，避免重复外发。
- **fairness-review**：检查岗位相关性、证据完整性和不同切片差异；验收：不得自动淘汰或依据敏感个人属性评分。

## 使用

```bash
fde show enterprise-ai-diagnosis --industry recruitment
fde export codex --industry recruitment --output ./client-project
```

只选择该 Pack 的 extends 及其显式依赖。示例指标需与业务 owner 确认，不能直接作为客户承诺。参见[行业案例](case.md)。
