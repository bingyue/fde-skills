# 企业知识库 — Build

状态：教学模拟，未进行客户生产验收。

## 决策与产物

离线基线用knowledge.json模拟文档索引，先证明权限和版本过滤；接入真实向量库时复用测试契约。

## 证据

需求见[案例说明](../README.md)，输入见[知识快照](../knowledge.json)，门禁见[冻结用例](../eval.jsonl)。

## 责任与下一步

FDE维护方案与实现；业务owner核验场景和标签；IT核验身份、运行和恢复。使用 `evaluation-driven-development` 执行本阶段，输出通过/失败及来源，不将模拟结果作为客户签收。
