# claude-configs

A lean repository of reusable guidelines and commands for Claude Code. Copy what you need into your projects.

## Quick start

To use these guidelines in a project:

1. **Copy rules** — Copy `rules/*.md` into your project's `.claude/` folder or reference them in your own `CLAUDE.md`
2. **Activate plugins** — Use the install commands in `plugins/` to add caveman or karpathy-guidelines
3. **Use commands** — Copy `.claude/commands/` files into your project's `.claude/` folder

## What's included

### Rules (always-on guidelines)
- **`rules/project-setup.md`** — Enforce dependency isolation (venv, local node_modules, never global installs)
- **`rules/plugin-activation.md`** — Auto-install and activate plugins when user says "enable X"

### Plugins (external tools)
- **`plugins/caveman.md`** — ~75% token reduction, terse responses
- **`plugins/karpathy-guidelines.md`** — Behavioral guidelines: think first, stay simple, surgical edits, verify goals

### Commands (slash commands / skills)
- **`.claude/commands/auto-safe-mode.md`** — Balanced autonomy: full access within project, approval required for destructive/broad actions
- **`.claude/commands/enable-all.md`** — Activate everything at once

## Structure

```
.
├── CLAUDE.md                (root config)
├── README.md                (this file)
├── rules/
│   ├── project-setup.md
│   └── plugin-activation.md
├── plugins/
│   ├── caveman.md
│   └── karpathy-guidelines.md
└── .claude/
    └── commands/
        ├── auto-safe-mode.md
        └── enable-all.md
```
