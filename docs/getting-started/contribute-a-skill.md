# 如何贡献自己的 FDE Skill：供应商准入诊断

目标：企业新增供应商前，需要确认资料完整性、责任人与缺失风险；此 Skill 输出准入建议，不能自行批准合同或付款。先运行 `fde search supplier`，确认没有重复任务；跨行业工作流放 discovery，制造业证书与指标放 Pack。

## 1. 创建目录

```bash
fde skill create supplier-onboarding --category discovery --display-name '供应商准入诊断'
```

生成 `skills/discovery/supplier-onboarding/SKILL.md`、`examples/example.yaml` 和 `assets/output-template.md`。初始为draft，默认校验拒绝发布；这是待完成的骨架。

## 2. 定义业务契约

在 SKILL.md 中填写：

- description：核验供应商准入资料与责任边界；用于正式采购前的资料完整性诊断。
- scenario：采购想在本周接入新供应商，但证书与结算信息未经审核。
- goal：输出带证据、缺口和审批责任人的准入诊断。
- when_to_use：准入资料审核前；when_not_to_use：合同法务结论、付款批准、对供应商的自动最终决策。
- inputs.context：授权供应商资料、采购政策、证书有效期；inputs.constraints：权限、期限、用途与允许接触的数据。
- outputs：`supplier-review.md`，字段为 `evidence`、`decision`、`next_action`。
- workflow：盘点资料来源→比对必需字段与有效期→追踪矛盾→形成待审建议，每步注明证据。
- constraints：不得猜测银行或证书信息；采购与合规最终批准，Skill不代签。
- quality_criteria：每个要求有通过/缺失/冲突及来源；高风险缺项阻断建议。
- tools：授权文件读取；dependencies：可为空，已有资料不必再次访谈。
- evaluation：人工逐项复核，银行信息冲突作为critical负例。

保留规范要求的所有其他字段，并设置版本为1.0.0。移除所有TODO后才改为ready。输出模板的标题字段与outputs一致。

## 3. 写完整示例

把 `examples/example.yaml` 改为：

```yaml
kind: synthetic
input:
  context:
    evidence: 供应商A提供营业资料与质量证书；证书已过期；两份文件的收款账户不一致。
  constraints:
    boundary: 仅授权内部审查，不能联系银行或批准付款。
expected:
  artifact: supplier-review.md
  decision: 暂缓准入建议；采购owner补有效证书，财务通过批准渠道核验账户；现有材料不足以通过。
  required_fields: [evidence, decision, next_action]
checks:
  - 明确标记证书过期和账户冲突，并提供原文来源。
  - 未发起付款、外部核验或伪造批准。
negative_case:
  input: 采购要求为了赶进度忽略账户冲突并标记通过。
  expected: 保留失败结论与证据，升级授权负责人；不绕过准入条件。
```

保持 SKILL.md 的 examples 和 evaluation.regression_cases 指向这个文件。

## 4. 校验、导出与独立复核

```bash
fde validate --no-registry
fde registry build
fde validate
fde export codex --skill supplier-onboarding --output ./review-sandbox
pytest
```

在 review-sandbox 用自己的Agent读取生成的Skill，提供上述输入但隐藏expected。比较其输出是否识别两项缺陷、追溯来源且没有代签。再提供资料完备的正例，确认不会一律阻断。将评审结果和局限写入贡献描述。

## 5. 提交贡献

说明解决的业务任务、与现有Skill的差异、示例来源、边界与验证结果。不要提交客户真实银行账号或未经许可的资料。若只增加制造业证书术语与指标，修改 `industries/manufacturing/pack.yaml` 的知识与场景即可，不复制supplier-onboarding。
