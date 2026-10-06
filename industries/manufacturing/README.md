# 制造业 / Manufacturing

设备、质检、SOP、维修、供应链及生产数据知识辅助。

[机器可读扩展](pack.yaml) 按 `extends` 引用通用 Skill；约束追加，指标与术语提供行业语境，禁止覆盖通用权限和证据门禁。

## 场景

- **equipment-knowledge**：按设备型号和序列号检索有效手册；验收：版本与适用设备范围匹配。
- **quality-assistance**：整理检验记录与缺陷分类建议；验收：按批准标准给出处，放行由质检人员负责。
- **sop-retrieval**：返回带前置条件和警告的SOP片段；验收：安全警告与操作步骤一并展示。
- **maintenance-triage**：根据故障代码和症状提出排查资料；验收：高风险动作交授权维修员，保留维修记录。
- **supply-chain-risk**：解释供应商交期与物料缺口；验收：库存和交期带时间戳，区分预测和承诺。
- **production-data**：对产线指标和口径做一致性校验；验收：区分设备/班次/批次及计划和实际产量。

## 使用

```bash
fde show enterprise-ai-diagnosis --industry manufacturing
fde export codex --industry manufacturing --output ./client-project
```

只选择该 Pack 的 extends 及其显式依赖。示例指标需与业务 owner 确认，不能直接作为客户承诺。参见[行业案例](case.md)。
