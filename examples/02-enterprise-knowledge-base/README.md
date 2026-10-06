# 企业知识库

**需求：** 300份员工知识文档跨部门分布，员工需要能引用来源且不过权的回答。

这是合成教学案例。展示从业务证据到移交的完整链路和一个可复跑的确定性基线；没有声称真实客户收益、实际模型成绩或生产部署。

## Delivery chain

需求 → Discovery → Diagnosis → Solution → Architecture → Build → Eval → Deploy → Delivery

- [Discovery](artifacts/discovery.md)：访谈新员工与HR；采集入职、报销、休假任务；明确哪些文档只对财务开放。
- [Diagnosis](artifacts/diagnosis.md)：发现旧政策混在当前目录，搜索依赖文件名；访问控制只有文件夹层，索引不得扩大权限。
- [Solution](artifacts/solution.md)：先治理权威来源和生效版本，再比较关键词与混合检索；不承诺回答所有制度问题。
- [Architecture](artifacts/architecture.md)：源文档→带ACL解析→有效期过滤→检索→引用核对→回答/拒答；删除与撤权事件同步缓存。
- [Build](artifacts/build.md)：离线基线用knowledge.json模拟文档索引，先证明权限和版本过滤；接入真实向量库时复用测试契约。
- [Eval](artifacts/eval.md)：冻结12条合成用例，覆盖正常、未知、租户、角色、注入、外发与风险转接。所有门禁必须通过；同时运行缺少控制的baseline，验证用例能够暴露失败。真实上线需客户代表性数据、性能与人工评审。
- [Deploy](artifacts/deploy.md)：先单部门Beta；监测空召回和拒答误差；发布绑定索引与文档快照，回滚能恢复对应版本。
- [Delivery](artifacts/delivery.md)：HR负责内容更新，IT负责权限和运行；接收人独立更新一条政策、撤权并确认检索变化。

## Run

从仓库根目录运行：

```bash
python scripts/run_example.py 02-enterprise-knowledge-base --output .fde/runs/02-enterprise-knowledge-base.json
python scripts/run_example.py 02-enterprise-knowledge-base --variant baseline
```

第二条命令预期返回1：未实施边界控制的基线应被负例拦截。此处输入和预期分离，响应实现位于 [reference_app.py](../../src/fde_skills/reference_app.py)。12个测试只证明合成场景契约，真实模型上线还需要客户标注集和环境测试。

## Substitute a real system

读取 [eval.jsonl](eval.jsonl) 的 request，调用经授权的候选系统，保存 JSONL：`{"id":"02-01","response":{"status":"answered","sources":["public-current"],"answer":"..."}}`。

```bash
python scripts/run_example.py 02-enterprise-knowledge-base --predictions captured-responses.jsonl
```

缺失响应判失败，重复或未知ID报错。不得将 expected 字段传给候选系统。真实认证必须在服务端生成 tenant/role；本地 fixture 身份仅用于隔离测试。用[行业 Pack](../../industries/ecommerce/README.md)扩充资料、指标和约束；用 [case.yaml](case.yaml) 编排各阶段 Skill。
