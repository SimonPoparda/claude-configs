# Rules

Standing instructions that are always active — not modes to toggle, just how things are always done.

Imported in `CLAUDE.md` so they apply to every session in this repo.

## Rules

| Rule | Description |
|------|-------------|
| [project-setup](./project-setup.md) | Always use isolated environments (venv, local node_modules); never install globally |
| [plugin-activation](./plugin-activation.md) | "enable X" / "use X" auto-installs and activates the named plugin |

## Adding a Rule

1. Create `rules/<name>.md` with clear always/never instructions
2. Add a row to the table above
3. Add `@rules/<name>.md` to `CLAUDE.md`
