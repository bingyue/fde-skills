# 动态技术栈候选目录

> 这是搜索起点，不是固定推荐。每次执行必须重新核验版本、许可证、维护状态、国内可用性、数据政策和目标环境兼容。

## 1. 国内模型与 API

运行时检索：

- 阿里云百炼 / 通义千问
- 火山引擎方舟 / 豆包
- 腾讯云混元
- 百度智能云千帆
- DeepSeek
- 智谱 GLM
- Moonshot / Kimi
- MiniMax
- 硅基流动等聚合推理服务
- ModelScope 上的开源模型

核验：

- 当期模型名称和发布日期；
- 上下文、结构化输出、工具调用、多模态；
- 地域、数据留存、是否用于训练、日志和删除策略；
- API 兼容、限流、SLA、内容安全和价格；
- 企业合同与发票；
- 是否允许目标行业和数据等级。

不要在 Skill 中静态写“当前最强模型”。

---

## 2. 开源 AI 应用与 RAG 平台

| 候选 | 核心定位 | PoC 重点核验 | 官方入口 |
| --- | --- | --- | --- |
| Dify | 工作流、Agent、RAG、模型管理 | 社区/企业能力边界、插件、迁移 | [官网](https://dify.ai/zh) / [GitHub](https://github.com/langgenius/dify) |
| RAGFlow | 深度文档理解与 RAG | 解析质量、资源需求、权限 | [GitHub](https://github.com/infiniflow/ragflow) |
| FastGPT | 知识库与可视化工作流 | 部署、API、复杂文档能力 | [GitHub](https://github.com/labring/FastGPT) |
| MaxKB | 企业知识库问答 | 中文场景、集成、版本许可 | [GitHub](https://github.com/1Panel-dev/MaxKB) |
| Coze Studio | Agent/工作流开发 | 开源版与云版差异、私有化 | [GitHub](https://github.com/coze-dev/coze-studio) |
| n8n | 通用自动化与 AI 工作流 | 许可证、连接器、AI 状态治理 | [官网](https://n8n.io/) / [GitHub](https://github.com/n8n-io/n8n) |

平台能力变化快，必须用当期官方资料确认 SSO、RBAC、审计、MCP、离线安装等。

---

## 3. 文档解析与 OCR

| 候选 | 用途 | 重点核验 |
| --- | --- | --- |
| MinerU | PDF 转结构化内容 | 中文复杂版面、公式/表格、硬件 |
| PaddleOCR | 中文 OCR 与文档识别 | 扫描件、表格、部署环境 |
| Docling | 多格式文档解析 | 中文与复杂版式效果 |
| Unstructured | 文档抽取与分块 | 格式覆盖、部署与许可 |
| PyMuPDF | 轻量 PDF 处理 | 许可、文本层质量 |

解析选型必须基于客户代表文档 bake-off，不得只看官方 Demo。

---

## 4. Agent 与编排

| 候选方向 | 适用 | 不适用 |
| --- | --- | --- |
| 普通 Python/TypeScript + 模型 SDK | 单轮、确定性流程 | 复杂持久状态 |
| PydanticAI 类轻量框架 | 类型安全、结构化输出、测试 | 大型状态图 |
| LangGraph | 状态、循环、分支、恢复、人审 | 简单调用 |
| OpenAI Agents SDK / Google ADK 等 | 对应生态与轻量 Agent | 强模型中立要求时需评估 |
| LlamaIndex Workflows/Haystack | Retrieval-heavy 工作流 | 与现有栈重复时 |
| MCP SDK/FastMCP | 标准化工具接入 | 工具很少且接口稳定时 |

核验官方资料：

- 持久化、重试、幂等、人审、MCP；
- 模型中立程度；
- Trace、测试和结构化输出；
- License、Release 和 breaking changes。

---

## 5. 数据与检索

| 方向 | 默认使用条件 |
| --- | --- |
| PostgreSQL + pgvector | 已有 PostgreSQL、PoC 规模有限 |
| Elasticsearch/OpenSearch | 已有搜索栈、需要关键词+向量 |
| Milvus | 独立向量服务、规模和生态需求明确 |
| Qdrant | 轻量独立向量服务与过滤需求 |
| Redis | 已有 Redis 且只需轻量缓存/向量能力 |

必须验证：

- 混合检索和过滤；
- 备份、迁移、租户和权限；
- 中文分词与字段检索；
- 团队是否已有运维经验。

---

## 6. 评估与可观测

| 候选 | 用途 |
| --- | --- |
| Ragas | RAG 评估辅助 |
| DeepEval | LLM/RAG 测试 |
| promptfoo | Prompt/模型回归和安全测试 |
| Langfuse | 自托管/云端 Trace 与评估 |
| Phoenix | LLM 可观测与评估 |
| OpenTelemetry | 标准化 Trace/Metrics/Logs |

强制配套：

- 客户业务 Golden Dataset；
- 失败类型标签；
- 模型/Prompt/数据版本；
- 延迟、成本、Token 和人工反馈；
- 业务 Owner/AIBP 验收。

---

## 7. 模型推理与私有化

| 候选 | 常见用途 | 核验重点 |
| --- | --- | --- |
| vLLM | 通用 GPU 高吞吐服务 | 模型/量化/硬件兼容 |
| SGLang | 复杂生成、前缀复用、Agent 场景 | 稳定性与团队经验 |
| Xinference | 多模型/多引擎统一管理 | 后端、模型和集群支持 |
| LMDeploy | 国内开源模型与多硬件方向 | 官方兼容矩阵 |
| MindIE | 昇腾推理 | CANN/硬件/模型版本 |
| MindSpore/vLLM-MindSpore | 昇腾/MindSpore 生态 | 官方部署文档 |
| Ollama/llama.cpp | 开发机和轻量试验 | 不默认用于企业生产 |

官方参考：

- [MindIE-LLM](https://github.com/Ascend/MindIE-LLM)
- [MindSpore Transformers 部署文档](https://www.mindspore.cn/mindformers/docs/zh-CN/stable/guide/deployment.html)
- [vLLM](https://github.com/vllm-project/vllm)
- [SGLang](https://github.com/sgl-project/sglang)
- [Xinference](https://github.com/xorbitsai/inference)
- [LMDeploy](https://github.com/InternLM/lmdeploy)

公开 benchmark 只能用于形成候选。最终必须在客户硬件上复测。

---

## 8. Vibe Coding 工具

### 国际/通用

- Cursor
- Claude Code
- OpenAI Codex
- GitHub Copilot
- Cline / Roo Code
- OpenCode
- Aider

### 国内

- Trae
- 腾讯 CodeBuddy（插件/IDE/CLI）
- 通义灵码
- Qoder
- 百度 Comate
- 华为 CodeArts 相关 AI 编码能力

官方示例：

- [腾讯云 CodeBuddy 产品文档](https://cloud.tencent.com.cn/document/product/1749/104236)

每次选型重点检查：

- 企业版和个人版数据政策是否不同；
- Prompt/代码是否保留、用于训练或跨境；
- 是否支持自定义模型/国内模型/VPC；
- Agent 可执行的终端、文件和网络权限；
- 审计、团队策略、MCP、测试与 Review；
- 当前定价和可用区域。

---

## 9. PoC 默认脚手架候选

### Python 路径

```text
FastAPI
Pydantic / pydantic-settings
pytest
httpx
ruff / mypy（按团队要求）
OpenTelemetry
Docker Compose
```

### TypeScript 路径

```text
Next.js
TypeScript
shadcn/ui（或客户设计系统）
Zod
Vitest / Playwright
OpenTelemetry
Docker Compose
```

不是强制全选。只加入验证核心假设所需组件。

---

## 10. 国内企业 PoC 额外检查

- 数据分类分级、个人信息与跨境；
- 生成式 AI、深度合成、算法与内容安全适用性；
- 模型/云服务采购、发票、合同和 SLA；
- 内网镜像、离线包、软件源和漏洞库；
- 国产 CPU/GPU/NPU、OS、数据库、中间件兼容；
- 等保、日志留存、账号、审批和审计；
- 飞书、企业微信、钉钉、OA、ERP/CRM 等现有入口；
- 客户是否允许 AI Coding 工具访问代码仓库。

合规解释应由客户法务、安全和合规负责人确认，本 Skill 不作法律结论。

---

## 11. 搜索结果更新规则

在以下任一条件发生时重新执行完整检索：

- 距上次决策超过 30 天；
- 关键模型、平台或许可证升级；
- 部署环境/硬件变化；
- 数据等级或供应商审批变化；
- PoC 进入 Beta/生产；
- 关键依赖出现安全事件、维护停滞或不兼容。
