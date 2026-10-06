# Agent adapters

The source of truth is `skills/<category>/<name>/SKILL.md`. Profiles under `adapters/` specify the destination; one shared compiler preserves behavior and supporting resources. Native files contain standard name, description, license and string-valued metadata; rich metadata remains in `references/fde-contract.yaml`.

| Agent | Project destination | Official specification checked 2026-10-06 |
| --- | --- | --- |
| Codex | `.agents/skills/<name>/SKILL.md` | [Skills](https://developers.openai.com/codex/skills/) |
| Claude Code | `.claude/skills/<name>/SKILL.md` | [Extend Claude with skills](https://code.claude.com/docs/en/skills) |
| Cursor | `.cursor/skills/<name>/SKILL.md` | [Agent Skills](https://cursor.com/docs/skills) |
| OpenCode | `.opencode/skills/<name>/SKILL.md` | [Agent Skills](https://opencode.ai/docs/skills/) |

All four currently accept native Skill directories. The portable layout follows the [Agent Skills specification](https://agentskills.io/specification). Rules and slash commands are separate platform interfaces: this release uses native Skills to avoid maintaining a second behavior definition or injecting all 60 Skills as always-on rules.

```bash
fde export cursor --skill rag-architecture --output ../client
fde export claude-code --industry foreign-trade --output ../client
```

Each exported Skill is self-contained. Its complete contract explicitly tells the agent to inspect required inputs and gates. Industry constraints are appended; they cannot remove core rules. Native tool permission fields are deliberately not inferred from capability descriptions.

Canonical exports declare `AGPL-3.0-only` and include the full `LICENSE` and project `NOTICE.md`. These notices also travel with the installed library and `fde init` scaffold. A separately licensed Skill must supply its own `LICENSE`, which is preserved during export; review its compatibility before distribution.

## Updates and conflicts

The exporter records file hashes in `.fde/exports/<agent>.json`. Repeating the same export is deterministic. Unmodified generated files update automatically. Edited generated files require `--force`; unmanaged conflicting files are rejected even with that option. All intended writes are checked before the first write. Unselected Skills are retained; use a fresh output directory for a clean distributable set. Keep the manifest if incremental updates are wanted.

Do not edit generated outputs as the primary source; change the canonical Skill and export again. No export executes a script or sends customer data. Restart or refresh your agent if required by its version and policy.

## Verification limits

CI verifies directory conventions, portable metadata, complete contracts, asset links, reproducibility and overwrite protection. This is file-format compatibility, not proof of behavior in proprietary agent runtimes. For a new agent version run a small real task with positive and negative inputs and record the runtime version and output before claiming behavioral compatibility.
