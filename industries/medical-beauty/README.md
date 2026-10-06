# 医美 / Medical beauty

项目咨询、客服、预约、到店和知识运营的非临床辅助。

[机器可读扩展](pack.yaml) 按 `extends` 引用通用 Skill；约束追加，指标与术语提供行业语境，禁止覆盖通用权限和证据门禁。

## 场景

- **service-consultation**：提供已审核的服务流程与准备事项；验收：不诊断、不个性化推荐治疗、不保证效果。
- **customer-service**：识别问题并检索批准的项目介绍；验收：资料有审核人和有效期；未知内容转人工。
- **appointment**：按授权时段创建或修改预约请求；验收：确认项目、门店、时间与联系授权，幂等防重复。
- **arrival-follow-up**：在客户同意范围内生成到店提醒草稿；验收：禁止越过同意范围发送或营销施压。
- **knowledge-governance**：维护项目知识、禁用表达和审核版本；验收：临床及宣传内容由机构指定合格人员审核。
- **compliance-routing**：将症状、不良反应和禁忌问题升级给专业人员；验收：风险咨询不进入自动转化流程。

## 使用

```bash
fde show enterprise-ai-diagnosis --industry medical-beauty
fde export codex --industry medical-beauty --output ./client-project
```

只选择该 Pack 的 extends 及其显式依赖。示例指标需与业务 owner 确认，不能直接作为客户承诺。参见[行业案例](case.md)。
