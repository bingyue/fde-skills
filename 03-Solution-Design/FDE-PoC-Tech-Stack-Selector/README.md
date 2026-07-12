# FDE-PoC-Tech-Stack-Selector

- **分类**：`03-Solution-Design`
- **成熟度**：`usable`
- **一句话**：强制检索最新国内 AI 实践，输出明确、可执行、可回退的 PoC 技术栈与构建蓝图

---

## 为什么需要独立 Skill

现有能力分别解决：

- `Diagnostic-FDE`：售前方案与商业价值；
- `Private-Deployment-Gateway`：私有化部署和网关；
- `RAG-Evaluation`：RAG 评估；
- `Tool-Audit`：Agent/MCP 工具审计；
- `PRD-Generator`：定义做什么。

但 PoC 开工前仍缺一个统一决策环节：**在时间、数据、团队和国内环境约束下，究竟用什么模型、框架、平台、数据库、评估工具和 Vibe Coding 工具，为什么选，以及失败时怎么切换。**

本 Skill 填补 Discovery 与 AI-Delivery 之间的技术决策缺口。

---

## 适用场景

- 需要在 48 小时内输出 AI PoC 技术方案；
- 需要在 Dify、RAGFlow、FastGPT、MaxKB、自研之间做决定；
- 需要选择国产模型 API、开源模型或私有化推理；
- 需要选择 LangGraph、PydanticAI、Agent SDK、MCP 或普通工作流；
- 希望使用 Cursor、Trae、CodeBuddy、Qoder、Claude Code、Codex 等加速 PoC；
- 客户有数据不出域、信创、国产算力或内网隔离要求；
- PoC 已有 Demo，但无法说明如何进入 Beta/生产；
- 技术选型会议只有工具偏好，没有统一决策证据。

不适用于：

- 场景与验收指标尚未定义；
- 只想采购全公司 AI 中台；
- 已进入生产性能调优和容量规划；
- 希望绕过客户安全、法务或采购流程。

---

## 核心原则

### 1. 先验证假设，不先建设平台

技术栈必须服务于一个可证伪的业务假设。PoC 的目标不是展示技术数量，也不是提前实现完整生产架构。

### 2. 路径优先于产品

先判断 L1/L2/L3，再选择工具：

| 路径 | 适用 | 典型形态 | 主要风险 |
| --- | --- | --- | --- |
| L1 开箱即用 | 标准知识库、简单工作流、快速演示 | Dify、RAGFlow、FastGPT、MaxKB、Coze Studio 等 | 定制和迁移边界 |
| L2 Vibe Coding | 定制 UI/API/业务逻辑，2–4 周 | AI IDE/CLI + FastAPI/Next.js/Streamlit | 生成代码质量与数据泄露 |
| L3 工程化 | 复杂状态、权限、集成、核心算法 | SDK/框架 + 数据层 + 评估/追踪 | 过度设计、周期失控 |

### 3. 开源优先，但不排斥国产云

默认策略：

- 主方案优先选择许可证清晰、可本地部署、社区仍维护的开源能力；
- 当国产云在模型质量、合规、区域、算力或交付周期上更适合时，给出云替代；
- API 层采用兼容协议或自有 Adapter，降低模型供应商锁定；
- 不因“国产”或“开源”标签自动判定安全、兼容或可商用。

### 4. 每次都重新搜索

AI 工具迭代极快。静态目录只提供候选，最终推荐必须在执行当天搜索官方文档、Release、许可证、部署说明和国内实践。

---

## STACK-POC 方法

## S — Scope：把场景收敛为技术假设

### 最小场景卡

```text
用户：谁会使用？
流程：AI 插入哪个步骤？
输入：数据格式、规模、敏感性？
输出：回答、结构化数据、动作还是决策建议？
指标：准确率、召回、时延、采纳或业务结果？
边界：AI 不做什么？谁负责人工兜底？
周期：几天/几周？
环境：公有云、私有化、离线、信创？
```

### 场景路由

| 场景 | 先验证什么 | 常见最小路径 |
| --- | --- | --- |
| 知识库/RAG | 文档解析、召回、引用正确性 | RAG 平台或轻量代码 |
| Agent/工作流 | 工具可靠性、状态、失败恢复 | 确定性工作流优先 |
| 文档智能 | OCR、版面、字段准确率 | 专用解析/OCR + 结构化输出 |
| 数据分析 | 语义层、SQL 安全、可解释性 | 受控查询 + 人审 |
| 多模态 | 媒体质量、模型能力、成本 | API 优先验证 |
| 自动化集成 | API 可用性、权限、幂等 | n8n/工作流或轻量服务 |

---

## T — Timely Research：强制最新技术检索

### 搜索包

每次执行至少搜索以下组合：

```text
{场景} 2026 最新 开源 AI POC 中国 企业 实践
{候选工具} official docs latest release license self-host
{候选模型} 官方 API 地域 数据处理 SLA 上下文 结构化输出
{推理框架} official supported models hardware benchmark release
{Vibe工具} 企业版 数据保留 隐私 私有化 官方
{候选工具A} vs {候选工具B} migration production issue
```

年份必须使用执行当天的年份，不能固定复制“2026”。

### 证据优先级

1. 官方文档、官方 GitHub/Gitee/ModelScope、Release；
2. 云厂商官方产品文档与客户案例；
3. 有复现步骤的工程团队实践；
4. 高质量社区对比；
5. 聚合文章仅用于发现候选，不作为关键结论唯一证据。

### 检索证据表

| 候选 | 来源 | 检索日期 | 版本/发布日期 | 许可证 | 国内可用/部署 | 关键证据 |
| --- | --- | --- | --- | --- | --- | --- |

以下判断无证据时不得写入最终结论：

- “最新”“最强”“生产级”“完全开源”；
- “支持私有化/信创/国产 GPU”；
- “兼容某模型、MCP、SSO、RBAC”；
- “企业数据不会被训练或保留”。

---

## A — Architecture：选择最小技术路径

### 模型层

#### API 优先条件

- 数据允许进入已批准区域和供应商；
- PoC 目标是验证业务/产品假设而非推理设施；
- 周期短、并发低、模型尚未稳定；
- 需要快速比较多模型或多模态能力。

运行时检索国内候选，如阿里云百炼/通义、火山方舟/豆包、腾讯混元、百度千帆、智谱、DeepSeek、Moonshot、MiniMax、硅基流动等；**不得依赖静态模型名称**。

#### 自部署触发条件

- 数据不得出域或完全离线；
- 目标硬件/信创为核心验证项；
- 有明确吞吐、时延或成本假设；
- 团队具备模型服务与 GPU 运维能力。

候选方向：

- 统一服务/管理：Xinference 等；
- NVIDIA/通用 GPU：vLLM、SGLang；
- 量化与轻量试验：llama.cpp、Ollama（仅开发验证）；
- 国内生态与多硬件：LMDeploy；
- 昇腾：MindIE、MindSpore/vLLM-MindSpore 等官方适配路径。

最终选择必须核对目标模型、目标硬件和版本兼容矩阵。

### 应用与编排层

| 需求 | 首选方向 |
| --- | --- |
| 简单问答/工作流 | Dify/FastGPT/MaxKB 等快速路径 |
| 复杂文档解析与 RAG | RAGFlow、MinerU/Docling/PaddleOCR 等组合验证 |
| 业务自动化连接 | n8n 或现有流程平台 |
| 简单工具调用 | 模型 SDK + 普通代码 |
| 类型安全、结构化 Agent | PydanticAI 等轻量框架 |
| 持久状态、分支、恢复、人审 | LangGraph 等图编排 |
| 标准化工具接入 | MCP，但先验证权限与工具质量 |

**反模式**：能用确定性流程解决时，不使用多 Agent。

### 数据与检索层

| 现状/需求 | 默认选择 |
| --- | --- |
| 已有 PostgreSQL，规模有限 | pgvector |
| 已有 Elasticsearch/OpenSearch | 复用其关键词+向量混合检索 |
| 需要独立向量服务或较大规模 | 比较 Milvus、Qdrant 等 |
| 复杂中文 PDF/表格/扫描件 | 先做解析 bake-off，再选 RAG 平台 |
| PoC 数据量很小 | 不为了“未来规模”提前增加组件 |

### UI 与 API

- 内部 Demo：平台内置 UI、Streamlit、Gradio；
- 需要业务体验验证：Next.js/React + 组件库；
- Python 服务：FastAPI；
- 企业集成：API Adapter + 客户现有网关；
- PoC 不默认建设微服务、Kubernetes 或复杂事件总线。

### 评估与可观测性

必须包含：

- 业务 Golden Dataset；
- 版本化 Prompt/配置；
- 模型输入输出、时延、Token/成本记录；
- 失败分类与人工反馈；
- 最小回归测试。

候选工具：

- RAG：Ragas、DeepEval 等；
- Prompt/模型回归：promptfoo 等；
- Trace：Langfuse、Phoenix、OpenTelemetry 或平台内置追踪；
- 业务验收：本库 `RAG-Evaluation` 和客户 Ground Truth。

工具评分不能替代业务 Owner/AIBP 验收。

---

## C — Compare：从候选到唯一主方案

### 第一步：硬门禁

任一不通过即淘汰：

1. 数据/代码流向无法获批；
2. 许可证与商业用途不清；
3. 目标网络、硬件或部署不兼容；
4. 无法在 PoC 时间内验证 Primary Metric；
5. 团队无法调试、接管或回退；
6. 核心依赖已停止维护或存在不可接受风险。

### 第二步：加权评分

| 维度 | 权重 | 核心问题 |
| --- | ---: | --- |
| 场景匹配 | 20 | 是否直接验证核心假设？ |
| 首个 Demo 速度 | 20 | 几天能获得可测结果？ |
| 安全/私有化/信创 | 15 | 数据、网络、硬件是否满足？ |
| 团队可维护 | 15 | 当前团队是否能改、查、接管？ |
| 评估与调试 | 10 | 能否复现失败并做回归？ |
| 升级路径 | 10 | PoC 资产能否进入 Beta？ |
| 成本 | 5 | 人力、API、算力是否合理？ |
| 生态/锁定 | 5 | 维护活跃、替换成本如何？ |

评分只是决策辅助；硬门禁和核心假设优先于总分。

### 第三步：明确结论

最终必须写：

```text
主方案：选择 A，因为……
降级方案：若 X 在 D3 前失败，切换 B……
淘汰 C：因为……
淘汰 D：因为……
Beta 升级：保留……；重构……；新增……
```

---

## K — Kickoff：10 日 PoC 蓝图

| 时间 | 动作 | 交付物 | 门禁 |
| --- | --- | --- | --- |
| D0 | 场景、数据、安全、指标确认 | 场景卡、数据清单 | AIBP/IT 双确认 |
| D1 | 最新检索与候选 bake-off | 证据表、TDR 草稿 | 硬门禁通过 |
| D2 | 最小架构与环境 | 可运行骨架 | 密钥/日志合规 |
| D3–4 | 关键链路实现 | Demo v0 | 主路径可跑通 |
| D5 | Golden Dataset 首轮 | 基线报告 | 有可重复指标 |
| D6–7 | 最高优先级改进 | Demo v1 | Primary Metric 改善 |
| D8 | 业务流程与人工兜底 | 用户测试 | 风险可控 |
| D9 | 回归、降级与成本 | 评估报告 | 无 P0 阻塞 |
| D10 | Go/No-Go 评审 | 决策包 | 书面结论 |

---

## Vibe Coding 技术栈

### 工具类型

| 类型 | 候选方向 | 适用 |
| --- | --- | --- |
| AI 原生 IDE | Cursor、Trae、CodeBuddy IDE、Qoder 等 | 快速跨文件构建 |
| IDE 插件 | 通义灵码、CodeBuddy、Comate、Copilot、Cline/Roo Code | 保留现有 IDE |
| Agent CLI | Claude Code、Codex、CodeBuddy Code、OpenCode、Aider 等 | 自动化任务与终端工作流 |
| UI/脚手架 | v0/组件生成、shadcn/ui、模板仓库 | 快速体验原型 |

名单会变化，必须运行时搜索。

### Spec-first 工作包

在让 Agent 编码前准备：

```text
requirements.md   场景、范围、用户故事、验收指标
architecture.md   组件、数据流、权限、依赖与回退
tasks.md          可独立验收的小任务
tests/            Golden Dataset、API 与关键路径测试
.env.example      变量名，不含真实密钥
```

### 企业安全红线

- 未批准工具不得接触客户代码、数据、密钥和内部文档；
- 禁止把生产凭证放入 Prompt、代码或截图；
- 检查企业版的数据保留、模型训练、区域和审计策略；
- 生成依赖必须锁版本并做许可证/漏洞检查；
- 权限、SQL、文件系统、网络调用、删除操作必须人工评审；
- AI 不能自行批准合并、部署或执行破坏性操作。

---

## 标准输出

1. **一句话决策**：唯一主方案；
2. **PoC 假设与约束**；
3. **最新技术检索证据表**；
4. **L1/L2/L3 路径判断**；
5. **候选门禁与评分表**；
6. **分层技术栈**：模型、编排、RAG、数据、UI、评估、部署、Vibe Coding；
7. **架构与数据流**；
8. **降级与淘汰方案**；
9. **10 日构建计划**；
10. **Golden Dataset 与 Go/No-Go**；
11. **成本、风险、回退**；
12. **PoC→Beta/生产升级清单**；
13. **技术决策记录（TDR/ADR）**。

---

## 常见误区

- ❌ 按 Star 数或热度直接选型；
- ❌ 把“支持某能力”误写为“适合本场景”；
- ❌ 同时引入两个 Agent 框架、两个向量库和多个工作流平台；
- ❌ 为 PoC 提前建设 Kubernetes、微服务和全量治理平台；
- ❌ 不做 Golden Dataset，只凭 Demo 观感验收；
- ❌ 使用国外 Vibe Coding SaaS 处理未批准客户代码；
- ❌ 低代码 PoC 直接进入生产；
- ❌ 用本地小模型掩盖数据、检索或流程问题；
- ❌ 没有降级路径，关键工具一旦失败项目停摆；
- ❌ 静态技术目录长期不更新。

---

## 关联 Skill

### 上游

- [Consultative-Problem-Solving](../../02-Discovery/Consultative-Problem-Solving/README.md)
- [FDE-Issue-Tree-Analysis](../../02-Discovery/FDE-Issue-Tree-Analysis/README.md)
- [Sidecar-AI-Transformation](../../02-Discovery/Sidecar-AI-Transformation/README.md)
- [SOW-Generator](../../01-Foundation/SOW-Generator/README.md)

### 并行

- [PRD-Generator](../PRD-Generator/README.md)
- [API-Design-Review](../API-Design-Review/README.md)
- [Private-Deployment-Gateway](../../05-Deployment/Private-Deployment-Gateway/README.md)

### 下游

- [RAG-Evaluation](../../04-AI-Delivery/RAG-Evaluation/README.md)
- [Tool-Audit](../../04-AI-Delivery/Tool-Audit/README.md)
- [RBAC-Audit](../../08-Security-Compliance/RBAC-Audit/README.md)
- [FDE-Adoption-Growth](../../07-Operations/FDE-Adoption-Growth/README.md)

---

## 文件导航

- [Agent 执行指令](SKILL.md)
- [Prompt 模板](prompt.md)
- [执行清单](checklist.md)
- [评分与验收](evaluation.md)
- [工作流](workflow.md)
- [动态技术资料目录](references.md)
- [技术决策记录模板](templates/tech-decision-record.md)
- [PoC 构建计划模板](templates/poc-build-plan.md)
- [知识库 PoC 示例](examples/knowledge-base-poc.md)

---

## 版本记录

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v1.0 | 2026-07-12 | 新增强制最新检索、开源优先/国产云替代、Vibe Coding 与明确技术决策流程 |
