# claude-code adapter

Native output: `.claude/skills/<name>/SKILL.md`. Verified 2026-10-06 against [official documentation](https://code.claude.com/docs/en/skills).

```bash
fde export claude-code --skill enterprise-ai-diagnosis --output ./client-project
```

The adapter emits standard name/description/license and string-valued metadata; the complete FDE contract stays in references/fde-contract.yaml. Examples and assets are copied unchanged. No tools are automatically authorized. Restart or refresh the target agent as its documentation requires.

Generated files are tracked in `.fde/exports/claude-code.json`. Modified generated files require explicit `--force`; unmanaged files are never overwritten. Use a new output directory to produce a clean release. Export success verifies file compatibility, not proprietary agent runtime behavior.
