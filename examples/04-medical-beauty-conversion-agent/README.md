# 医美咨询与预约 Agent

**需求：** 机构需要提高服务咨询与预约处理效率；临床问题和疗效判断必须交专业人员。

这是合成教学案例。展示从业务证据到移交的完整链路和一个可复跑的确定性基线；没有声称真实客户收益、实际模型成绩或生产部署。

## Delivery chain

需求 → Discovery → Diagnosis → Solution → Architecture → Build → Eval → Deploy → Delivery

- [Discovery](artifacts/discovery.md)：采集行政咨询与风险咨询类型；确认机构审核人、预约owner和专业转接渠道。
- [Diagnosis](artifacts/diagnosis.md)：客服知识版本不统一，预约与风险咨询混流；转化率不能覆盖专业转接门槛。
- [Solution](artifacts/solution.md)：只回答批准服务信息和生成预约请求；临床或不良反应先转接，不能用转化目标推动自动治疗预约。
- [Architecture](artifacts/architecture.md)：咨询入口→风险分流→批准知识→预约草稿→确认队列；健康资料单独授权隔离。
- [Build](artifacts/build.md)：离线基线演示高风险关键词转接和预约资料检索；真实部署需专业人员扩充表达变体和人工值守。
- [Eval](artifacts/eval.md)：冻结12条合成用例，覆盖正常、未知、租户、角色、注入、外发与风险转接。所有门禁必须通过；同时运行缺少控制的baseline，验证用例能够暴露失败。真实上线需客户代表性数据、性能与人工评审。
- [Deploy](artifacts/deploy.md)：先行政咨询影子运行；验证转接可用、预约不重复、同意记录有效；可一键回到纯人工服务。
- [Delivery](artifacts/delivery.md)：机构指定专业人员签知识边界，客服负责人验收队列；真实上线前需当地政策与机构流程复核。

## Run

从仓库根目录运行：

```bash
python scripts/run_example.py 04-medical-beauty-conversion-agent --output .fde/runs/04-medical-beauty-conversion-agent.json
python scripts/run_example.py 04-medical-beauty-conversion-agent --variant baseline
```

第二条命令预期返回1：未实施边界控制的基线应被负例拦截。此处输入和预期分离，响应实现位于 [reference_app.py](../../src/fde_skills/reference_app.py)。12个测试只证明合成场景契约，真实模型上线还需要客户标注集和环境测试。

## Substitute a real system

读取 [eval.jsonl](eval.jsonl) 的 request，调用经授权的候选系统，保存 JSONL：`{"id":"04-01","response":{"status":"answered","sources":["public-current"],"answer":"..."}}`。

```bash
python scripts/run_example.py 04-medical-beauty-conversion-agent --predictions captured-responses.jsonl
```

缺失响应判失败，重复或未知ID报错。不得将 expected 字段传给候选系统。真实认证必须在服务端生成 tenant/role；本地 fixture 身份仅用于隔离测试。用[行业 Pack](../../industries/medical-beauty/README.md)扩充资料、指标和约束；用 [case.yaml](case.yaml) 编排各阶段 Skill。
