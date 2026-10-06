# 电商 / Ecommerce

商品知识、售前售后与订单履约的AI辅助。

[机器可读扩展](pack.yaml) 按 `extends` 引用通用 Skill；约束追加，指标与术语提供行业语境，禁止覆盖通用权限和证据门禁。

## 场景

- **product-qa**：用SKU与有效商品版本回答材质、尺寸和适用问题；验收：规格结论能回指有效SKU资料。
- **order-support**：查询授权客户自己的订单与物流；验收：订单归属校验通过且不泄露支付信息。
- **returns-triage**：依据实际订单与当期退换政策分流；验收：政策来源、例外和人审队列完整。
- **review-insights**：从脱敏评价提炼问题并回链原文；验收：区分频率、严重性和样本偏差。
- **inventory-assist**：解释库存可售状态并提示补货；验收：库存时间戳与仓库范围明确。
- **service-eval**：测试过期促销、越权订单和无依据承诺；验收：不承诺未批准退款、优惠或到货日。

## 使用

```bash
fde show enterprise-ai-diagnosis --industry ecommerce
fde export codex --industry ecommerce --output ./client-project
```

只选择该 Pack 的 extends 及其显式依赖。示例指标需与业务 owner 确认，不能直接作为客户承诺。参见[行业案例](case.md)。
