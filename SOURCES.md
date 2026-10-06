# Sources and attribution

New canonical Skills and industry examples are original editorial work for this release, informed by the delivery tasks requested for FDE Skills. All worked customer data is explicitly synthetic. Preserved historical material is documented in [the migration audit](docs/migration/README.md) and retains original terms under [NOTICE](NOTICE.md).

## Current platform specifications

Verified 2026-10-06:

- [Agent Skills specification](https://agentskills.io/specification): portable SKILL.md, naming and progressive disclosure.
- [Codex skills](https://developers.openai.com/codex/skills/): repository .agents/skills discovery.
- [Claude Code skills](https://code.claude.com/docs/en/skills): .claude/skills and native Skill invocation.
- [Cursor skills](https://cursor.com/docs/skills): .cursor/skills and .agents/skills discovery.
- [OpenCode skills](https://opencode.ai/docs/skills/): .opencode/skills and compatible Skill directories.

Adapters implement only the shared native Skill interface needed here. Platform-specific commands, always-on rules, model calls and tool permissions are outside the compilation contract.

## Historical sources

- [Original source guide](legacy/SOURCES.md)
- [External engineering imports](legacy/_catalog/external-skills-imported.md)
- [Consulting references](legacy/_catalog/consulting-references.md)
- [Original import lock](legacy/skills-lock.json)

These records establish historical provenance, not automatically a right to redistribute every imported file. New contributions require an explicit source and license review before import.
