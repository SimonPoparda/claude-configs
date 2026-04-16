Activate all plugins, guardrails, and rules for this session. Work through each step below in order and confirm when done.

## 1. Plugins

Run `claude plugin list` and check which of these are installed:

- `caveman@caveman`
- `andrej-karpathy-skills@karpathy-skills`

For any that are missing, install them:
- Caveman: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman`
- Karpathy: `claude plugin marketplace add forrestchang/andrej-karpathy-skills && claude plugin install andrej-karpathy-skills@karpathy-skills`

### Caveman
Caveman is now active. Reduce output tokens ~75%. Use terse, fragment-based responses. Drop articles and filler.

### Karpathy Guidelines
Fetch the latest version of both files and apply them for this session:
- https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
- https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/EXAMPLES.md

## 2. Guardrails

@.claude/commands/auto-safe-mode.md

## 3. Rules

@rules/project-setup.md

## 4. Confirm

After completing all steps, print a short status summary:

```
/enable-all complete.
✔ caveman        — active
✔ karpathy       — active (latest from repo)
✔ auto-safe-mode — active
✔ project-setup  — active
```

If any step failed, show ✘ and the reason.
