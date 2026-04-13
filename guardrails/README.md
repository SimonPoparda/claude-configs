# Guardrails

This directory contains behavioral modes that control how Claude operates — scoping its autonomy, defining what requires approval, and setting safety boundaries.

## Structure

```
guardrails/
└── <mode-name>/
    ├── README.md        # What it does, how to activate, safe vs dangerous action list
    └── <mode-name>.md   # The actual rules Claude follows when the mode is active
```

## Available Modes

| Mode | Description | Activate |
|------|-------------|----------|
| [auto-safe-mode](./auto-safe-mode/) | Full autonomy within project scope; approval required for destructive actions | `/auto-safe-mode` |

## Adding a Guardrail

1. Create `guardrails/<mode-name>/`
2. Write `<mode-name>.md` — define the rules clearly: what's allowed, what requires approval, and what's forbidden
3. Add `.claude/commands/<mode-name>.md` to expose it as a slash command
4. Add a row to the table above
