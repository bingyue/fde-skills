---
name: fde-issue-tree-analysis
description: Use when diagnosing ambiguous customer-site FDE problems with Issue Tree, MECE, hypothesis-driven analysis, and evidence loops. Helps turn vague complaints such as poor AI knowledge-base quality, unstable agents, low workflow adoption, unclear PoC ROI, permissions blockers, or data-quality issues into verifiable hypotheses, experiments, action plans, and stage-gate decisions.
metadata:
  short-description: FDE issue tree diagnosis and evidence loop
---

# FDE Issue Tree Analysis

Use this skill when the user needs to structure and diagnose a complex enterprise delivery problem before jumping into implementation.

## When To Use

- The customer says an AI system, knowledge base, agent, automation, or PoC "does not work well" but the root cause is unclear.
- The user needs an Issue Tree, MECE check, root-cause hypotheses, evidence plan, or validation experiments.
- The team is preparing for PoC review, Beta blocker diagnosis, production incident review, or delivery retrospective.
- The problem spans business goals, data, technical chain, process embedding, permissions, security, adoption, or ownership.

## How To Use

1. Read `README.md` for the ISSUE-FDE framework and delivery gates.
2. Use `prompt.md` for general diagnosis, RAG diagnosis, interview evidence gathering, or MECE self-check.
3. Use `checklist.md` to verify the tree, hypotheses, evidence plan, and action loop.
4. Use `evaluation.md` to assess whether the diagnosis is review-ready.
5. Use examples in `examples/` when the problem resembles an AI knowledge-base diagnosis.

## Output Expectations

Produce a structured diagnosis that includes:

- Problem statement, scope boundary, impact object, and current-stage risk.
- Level 1 to Level 3 Issue Tree with MECE checks.
- Top hypotheses prioritized by impact, evidence availability, and validation cost.
- Evidence requirements and validation experiments.
- FDE action plan with owner, dependency, deliverable, timeline, and regression metric.
- Stage-gate conclusion for PoC, Beta, production, or retrospective.

Do not treat symptoms as root causes. Every leaf node should be testable with data, samples, logs, interviews, or metrics.
