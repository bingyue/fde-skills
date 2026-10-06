# 企业 AI 诊断

**需求：** 客户希望建设全公司智能体平台；先判断客服知识检索是否值得投入。

这是合成教学案例。展示从业务证据到移交的完整链路和一个可复跑的确定性基线；没有声称真实客户收益、实际模型成绩或生产部署。

## Delivery chain

需求 → Discovery → Diagnosis → Solution → Architecture → Build → Eval → Deploy → Delivery

- [Discovery](artifacts/discovery.md)：访谈销售、客服、IT各一角色；脱敏20条近期工单；发现每次查规格要跨三个目录。
- [Diagnosis](artifacts/diagnosis.md)：问题树分知识过期、入口分散、权限未明确；基线来自合成样本，客户实际数据仍待取证。
- [Solution](artifacts/solution.md)：选择只读规格检索PoC；备选为统一目录搜索；平台采购暂缓。示例两周时间盒，业务owner负责验收。
- [Architecture](artifacts/architecture.md)：浏览器入口→授权服务→知识索引→证据回答；问题树和ROI模型作为版本化交付资产。
- [Build](artifacts/build.md)：先实现不调用模型的政策与资料查询基线；在确认价值后替换检索/生成组件，保留输入输出契约。
- [Eval](artifacts/eval.md)：冻结12条合成用例，覆盖正常、未知、租户、角色、注入、外发与风险转接。所有门禁必须通过；同时运行缺少控制的baseline，验证用例能够暴露失败。真实上线需客户代表性数据、性能与人工评审。
- [Deploy](artifacts/deploy.md)：试点只覆盖5名客服的只读场景；正式部署前需客户环境的身份接入、性能和恢复验证。
- [Delivery](artifacts/delivery.md)：交付诊断报告、首选PoC范围、预算假设和待验证项；业务主管与IT数据owner分别签收。

## Run

从仓库根目录运行：

```bash
python scripts/run_example.py 01-enterprise-ai-diagnosis --output .fde/runs/01-enterprise-ai-diagnosis.json
python scripts/run_example.py 01-enterprise-ai-diagnosis --variant baseline
```

第二条命令预期返回1：未实施边界控制的基线应被负例拦截。此处输入和预期分离，响应实现位于 [reference_app.py](../../src/fde_skills/reference_app.py)。12个测试只证明合成场景契约，真实模型上线还需要客户标注集和环境测试。

## Substitute a real system

读取 [eval.jsonl](eval.jsonl) 的 request，调用经授权的候选系统，保存 JSONL：`{"id":"01-01","response":{"status":"answered","sources":["public-current"],"answer":"..."}}`。

```bash
python scripts/run_example.py 01-enterprise-ai-diagnosis --predictions captured-responses.jsonl
```

缺失响应判失败，重复或未知ID报错。不得将 expected 字段传给候选系统。真实认证必须在服务端生成 tenant/role；本地 fixture 身份仅用于隔离测试。用[行业 Pack](../../industries/ecommerce/README.md)扩充资料、指标和约束；用 [case.yaml](case.yaml) 编排各阶段 Skill。
