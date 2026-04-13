# Plugins

This directory tracks Claude Code plugins and reliables — reusable tools and extensions installed into Claude Code.

## Structure

Each plugin has its own subdirectory:

```
plugins/
└── <plugin-name>/
    └── README.md      # Source, install command, what it does, how to activate
```

The README serves as a quick-reference card so any plugin can be re-installed in seconds.

## Installed Plugins

| Plugin | Description | Install |
|--------|-------------|---------|
| [caveman](./caveman/) | ~75% token reduction, caveman-style responses | `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` |
| [karpathy-guidelines](./karpathy-guidelines/) | Coding behavior guidelines: think first, stay simple, surgical edits, verify goals | `claude plugin marketplace add forrestchang/andrej-karpathy-skills && claude plugin install andrej-karpathy-skills@karpathy-skills` |

## Adding a Plugin

1. Install it: `claude plugin marketplace add <source> && claude plugin install <name>`
2. Create `plugins/<name>/README.md` — include source URL, install command, description, and activation steps.
3. Add a row to the table above.
