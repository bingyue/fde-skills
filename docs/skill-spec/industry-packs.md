# Industry Skill Packs

A pack is `industries/<name>/pack.yaml`, validated by [industry.schema.json](../../schemas/industry.schema.json). It contains name, display_name, version, description, extends, knowledge, constraints, metrics, terminology, scenarios and cases.

- `extends`: names of existing core Skills. The core definition stays unchanged.
- `knowledge`: topic, guidance, source. Real engagements replace generic source descriptions with customer-approved references.
- `constraints`: additive domain rules; they never remove a core constraint or grant authority.
- `metrics`: name, definition, target. A suggested target is not a customer commitment.
- `terminology`: term and definition scoped to this industry.
- `scenarios`: task, reused Skill names and an acceptance statement.
- `cases`: pack-relative examples.

Composition is a pair of contracts, not a destructive dictionary override: core AND industry. If two rules conflict, record the conflict for review and follow the narrower existing authorization until resolved. An industry metric cannot hide an individual critical failure. Packs do not execute workflows, send messages or embed live credentials.

```bash
fde show enterprise-ai-diagnosis --industry manufacturing --json
fde export opencode --industry manufacturing --output ./factory-project
```

Without `--skill`, export selects the Pack's `extends` set. An explicitly selected Skill outside that set is rejected. Add a reference deliberately if appropriate; do not silently ignore the overlay.

To add a Pack, define the business tasks first, reuse existing Skills, supply knowledge boundaries, test key negative cases, and run `fde validate`. The [five examples](../../README_EN.md#industry-packs-and-delivery-examples) show implementation patterns. Medical beauty and recruitment Packs cover administrative assistance, review and escalation; customers must validate local professional and regulatory requirements before production.
