# FDE Delivery Framework

A Skill is a bounded delivery capability: a task, evidence contract, decision procedure, output, failure response and observable acceptance gate. The agent supplies reasoning and implementation; the customer supplies domain authority and acceptance ownership.

| Stage | Evidence required to enter | Exit artifact | Decision owner |
| --- | --- | --- | --- |
| Discovery | Authorized access, target task and stakeholders | Observed workflow, baseline and hypothesis register | Business owner |
| Diagnosis | Sources, failures and competing explanations | Problem tree, priorities and capability gaps | Business + FDE |
| Solution | Selected problem and feasibility constraints | PoC scope, PRD, options and success/stop criteria | Sponsor |
| Architecture | Functional and nonfunctional requirements | Data flow, trust boundaries, interfaces and ADRs | Technical owner |
| Build | Frozen task contract and development tests | Runnable increment with versioned dependencies | Engineering owner |
| Eval | Held-out data, baseline and pre-agreed thresholds | Slice metrics, failure analysis and go/no-go | Domain evaluator |
| Deploy | Passing gates, runbook, monitoring, recovery | Controlled rollout and verified rollback | Operations owner |
| Delivery | Production evidence, training and open issues | Acceptance, teach-back, ownership and support record | Customer signatory |

An earlier phase can be revisited. A missing owner, untestable hypothesis or data access gap should generate a bounded investigation, not a fictional completed deliverable. Use `ready`, `blocked`, `needs-review` as execution states; Skill metadata `status` describes authoring maturity separately.

## Evidence ledger

For each conclusion preserve source ID, observation date, allowed use, fact/assumption distinction, confidence and what would falsify it. Model-generated text is a proposal until checked against sources. Industry averages and synthetic examples never substitute for a customer's baseline.

## Execution and authorization

1. Select the primary Skill by its specific task and `when_to_use`.
2. Read its complete contract, obtain required inputs, and identify permissions already supplied by the user.
3. Apply an optional industry overlay; constraints are additive and cannot grant authority.
4. Execute the workflow, retaining the evidence named by each step.
5. Check every critical criterion and record failed/unknown results; do not average away a critical failure.
6. Produce the specified artifact and a next action with an owner. External writes remain subject to user authorization and system enforcement.

`dependencies` names prerequisite capabilities, not permission to execute them autonomously. Core Skills can consume existing prerequisite artifacts, so they generally do not force dependency chains. The case manifest defines a recommended sequence. Network, model and tool availability are environment capabilities; the library itself executes none of them.

## Reuse

Separate common contracts from client configuration, industry context and restricted evidence. Promote reusable knowledge only after removing customer identifiers and establishing permission. Review usefulness using realistic forward tests; structural validation alone cannot establish field readiness.
