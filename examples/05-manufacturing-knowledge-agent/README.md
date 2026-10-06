# 制造业知识 Agent

**需求：** 维修班组需要快速找到正确设备版本的SOP和故障资料，避免遗漏安全警告。

这是合成教学案例。展示从业务证据到移交的完整链路和一个可复跑的确定性基线；没有声称真实客户收益、实际模型成绩或生产部署。

## Delivery chain

需求 → Discovery → Diagnosis → Solution → Architecture → Build → Eval → Deploy → Delivery

- [Discovery](artifacts/discovery.md)：现场观察维修员查手册全过程；记录设备型号、序列号、SOP版本、故障代码和停机时间。
- [Diagnosis](artifacts/diagnosis.md)：发现新旧手册并存，页间安全警告被切片丢失；版本和安全上下文比自然语言流畅度更关键。
- [Solution](artifacts/solution.md)：PoC只读检索设备手册；故障处置由授权维修员负责；不接PLC写接口。
- [Architecture](artifacts/architecture.md)：受限OT资料导入→按设备/版本解析→警告与步骤共同切片→权限检索→引用展示→人工判断。
- [Build](artifacts/build.md)：用P-100 E7验证设备词精确匹配、旧版隔离、警告完整；真实实现增加OCR和表格解析对照测试。
- [Eval](artifacts/eval.md)：冻结12条合成用例，覆盖正常、未知、租户、角色、注入、外发与风险转接。所有门禁必须通过；同时运行缺少控制的baseline，验证用例能够暴露失败。真实上线需客户代表性数据、性能与人工评审。
- [Deploy](artifacts/deploy.md)：部署在批准内网，断网验证无外发依赖；索引和手册版本绑定；回滚恢复前一份批准资料快照。
- [Delivery](artifacts/delivery.md)：设备工程师验收资料正确性，IT验收隔离与备份；维修班组独立查找一例SOP并演练升级。

## Run

从仓库根目录运行：

```bash
python scripts/run_example.py 05-manufacturing-knowledge-agent --output .fde/runs/05-manufacturing-knowledge-agent.json
python scripts/run_example.py 05-manufacturing-knowledge-agent --variant baseline
```

第二条命令预期返回1：未实施边界控制的基线应被负例拦截。此处输入和预期分离，响应实现位于 [reference_app.py](../../src/fde_skills/reference_app.py)。12个测试只证明合成场景契约，真实模型上线还需要客户标注集和环境测试。

## Substitute a real system

读取 [eval.jsonl](eval.jsonl) 的 request，调用经授权的候选系统，保存 JSONL：`{"id":"05-01","response":{"status":"answered","sources":["public-current"],"answer":"..."}}`。

```bash
python scripts/run_example.py 05-manufacturing-knowledge-agent --predictions captured-responses.jsonl
```

缺失响应判失败，重复或未知ID报错。不得将 expected 字段传给候选系统。真实认证必须在服务端生成 tenant/role；本地 fixture 身份仅用于隔离测试。用[行业 Pack](../../industries/manufacturing/README.md)扩充资料、指标和约束；用 [case.yaml](case.yaml) 编排各阶段 Skill。
