# 外贸 / Foreign trade

从询盘识别、产品知识到客户跟进的受控销售辅助。

[机器可读扩展](pack.yaml) 按 `extends` 引用通用 Skill；约束追加，指标与术语提供行业语境，禁止覆盖通用权限和证据门禁。

## 场景

- **inquiry-analysis**：抽取RFQ型号、数量、目的地与缺失条件；验收：缺失型号或币种标unknown，保留原文。
- **lead-qualification**：按客户授权评分规则分层销售线索；验收：来源与评分理由可审计，不编造购买意愿。
- **product-knowledge**：用版本化产品目录回答参数与认证；验收：认证只引用有效原件，型号精确匹配。
- **multilingual-service**：在多语言中保持规格、币种、单位和交期一致；验收：人工检查关键商务术语与数字。
- **email-drafting**：生成带来源的报价澄清或跟进邮件草稿；验收：发送由授权人员确认；不发明报价或承诺。
- **customer-follow-up**：按CRM状态建议下一步并记录已批准动作；验收：时区、同意状态与重复发送控制有效。

## 使用

```bash
fde show enterprise-ai-diagnosis --industry foreign-trade
fde export codex --industry foreign-trade --output ./client-project
```

只选择该 Pack 的 extends 及其显式依赖。示例指标需与业务 owner 确认，不能直接作为客户承诺。参见[行业案例](case.md)。
