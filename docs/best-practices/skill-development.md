# Developing useful FDE Skills

Start from a recurring customer decision. State what evidence changes that decision, what artifact must exist afterwards, and what should happen if the evidence is missing. A prompt can help execute a Skill but is not its acceptance contract.

## Design sequence

1. Search the registry and identify the smallest reusable task.
2. Record a representative request and a neighboring request that should route elsewhere.
3. Define typed inputs and output fields, including provenance and unknowns.
4. Write steps that resolve actual uncertainty; include at least one meaningful failure branch.
5. Define review checks before drafting the example result.
6. Add synthetic or authorized anonymized data and label its provenance.
7. Review whether an agent can execute without undisclosed local files or secrets.

Use references for long domain material, assets for generated-output templates, and scripts only when deterministic automation reduces repeated work. Put necessary instructions in SKILL.md and link supporting files. Avoid duplicating an entire industry workflow: put domain-specific knowledge and metrics in a Pack.

## Evidence-driven review

A schema-valid Skill can still be ineffective. Give a reviewer the task and raw input without the expected answer. Inspect whether they seek missing evidence, preserve permissions, produce the required artifact and catch the negative case. Record limitations and improve the narrow defect. Only promote to `field-validated` with authorized field evidence.

Numerical targets need a denominator, observation window, slice and business owner. A refusal or escalation can be a successful outcome on a negative case. Do not reward tool calls, fluent text or the number of generated documents as a substitute for task success.
