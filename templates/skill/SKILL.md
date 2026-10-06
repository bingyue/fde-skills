---
name: new-skill
display_name: 'TODO: human-readable capability'
description: 'TODO: state the concrete task and trigger'
version: 1.0.0
category: discovery
tags:
- discovery
scenario: 'TODO: customer task'
goal: 'TODO: measurable delivery outcome'
when_to_use:
- 'TODO: triggering condition'
when_not_to_use:
- 'TODO: neighboring task handled elsewhere'
inputs:
- name: context
  description: 'TODO: exact required evidence'
  required: true
  type: object
- name: constraints
  description: 'TODO: authorization, time and resource limits'
  required: true
  type: object
outputs:
- name: deliverable.md
  type: markdown
  description: 'TODO: decision or artifact'
  required_fields:
  - evidence
  - decision
  - next_action
workflow:
- id: collect
  action: 'TODO: collect evidence'
  evidence: 'TODO: source record'
- id: decide
  action: 'TODO: make task-specific decision'
  evidence: 'TODO: decision artifact'
constraints:
- 'TODO: concrete boundary'
quality_criteria:
- 'TODO: observable acceptance criterion'
tools:
- name: workspace-files
  purpose: 读取授权材料并保存交付物；不依赖特定厂商。
  required: true
dependencies: []
examples:
- name: worked-example
  path: examples/example.yaml
evaluation:
  method: 'TODO: realistic positive and negative case review'
  checks:
  - id: acceptance
    criterion: 'TODO: task-specific observable check'
    severity: critical
  regression_cases:
  - examples/example.yaml
license: AGPL-3.0-only
status: draft
---

# {{name}}

TODO: describe decisions, evidence and failure recovery.

Use the [output template](assets/output-template.md) and complete the [worked example](examples/example.yaml).
