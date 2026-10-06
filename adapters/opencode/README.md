# opencode adapter

Native output: `.opencode/skills/<name>/SKILL.md`. Verified 2026-10-06 against [official documentation](https://opencode.ai/docs/skills/).

```bash
fde export opencode --skill enterprise-ai-diagnosis --output ./client-project
```

The adapter emits standard name/description/license and string-valued metadata; the complete FDE contract stays in references/fde-contract.yaml. Examples and assets are copied unchanged. No tools are automatically authorized. Restart or refresh the target agent as its documentation requires.

Generated files are tracked in `.fde/exports/opencode.json`. Modified generated files require explicit `--force`; unmanaged files are never overwritten. Use a new output directory to produce a clean release. Export success verifies file compatibility, not proprietary agent runtime behavior.
