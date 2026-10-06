# 外贸销售 Agent

**需求：** 出口配件销售希望加快多语言询盘响应，同时避免型号、MOQ、报价和邮件发送错误。

这是合成教学案例。展示从业务证据到移交的完整链路和一个可复跑的确定性基线；没有声称真实客户收益、实际模型成绩或生产部署。

## Delivery chain

需求 → Discovery → Diagnosis → Solution → Architecture → Build → Eval → Deploy → Delivery

- [Discovery](artifacts/discovery.md)：复盘询盘→选型→报价→跟进链；采集缺型号、缺目的港和小于MOQ的询盘；销售负责客户沟通。
- [Diagnosis](artifacts/diagnosis.md)：主要问题是产品参数散落与商务条件遗漏；不是邮件措辞不够优美。线索评分缺少统一口径。
- [Solution](artifacts/solution.md)：PoC仅做询盘字段抽取、资料检索、澄清邮件草稿；CRM更新与外发另走授权工作流。
- [Architecture](artifacts/architecture.md)：邮箱只读连接→结构化询盘→产品权威表→销售草稿→人工审核；审计关联原文与产品版本。
- [Build](artifacts/build.md)：以AB-120目录作为可追溯数据；默认draft状态；发送工具隔离在独立服务并服务端验证批准。
- [Eval](artifacts/eval.md)：冻结12条合成用例，覆盖正常、未知、租户、角色、注入、外发与风险转接。所有门禁必须通过；同时运行缺少控制的baseline，验证用例能够暴露失败。真实上线需客户代表性数据、性能与人工评审。
- [Deploy](artifacts/deploy.md)：先一个销售小组、英文询盘；经确认再扩语言；回滚到人工处理，草稿保留来源不自动发送。
- [Delivery](artifacts/delivery.md)：销售主管验收数字与术语，IT验收权限；运营接管产品更新、退订状态和邮件审计。

## Run

从仓库根目录运行：

```bash
python scripts/run_example.py 03-foreign-trade-sales-agent --output .fde/runs/03-foreign-trade-sales-agent.json
python scripts/run_example.py 03-foreign-trade-sales-agent --variant baseline
```

第二条命令预期返回1：未实施边界控制的基线应被负例拦截。此处输入和预期分离，响应实现位于 [reference_app.py](../../src/fde_skills/reference_app.py)。12个测试只证明合成场景契约，真实模型上线还需要客户标注集和环境测试。

## Substitute a real system

读取 [eval.jsonl](eval.jsonl) 的 request，调用经授权的候选系统，保存 JSONL：`{"id":"03-01","response":{"status":"answered","sources":["public-current"],"answer":"..."}}`。

```bash
python scripts/run_example.py 03-foreign-trade-sales-agent --predictions captured-responses.jsonl
```

缺失响应判失败，重复或未知ID报错。不得将 expected 字段传给候选系统。真实认证必须在服务端生成 tenant/role；本地 fixture 身份仅用于隔离测试。用[行业 Pack](../../industries/foreign-trade/README.md)扩充资料、指标和约束；用 [case.yaml](case.yaml) 编排各阶段 Skill。
