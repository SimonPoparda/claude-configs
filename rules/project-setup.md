# Project Setup Rules

Always follow these practices when setting up or working in a project.

## Dependency isolation

- **Python**: Always create and activate a `venv` before installing anything.
  ```bash
  python -m venv .venv && source .venv/bin/activate
  ```
  Never run `pip install` outside of an active virtual environment. If no `.venv` exists, create one first.

- **Node**: Use the project's local `node_modules` only. Never use `-g` / `--global` flags.

- **Other runtimes**: Apply the same principle — use the project-local scope (e.g. `bundle install --path vendor/bundle` for Ruby, project-level `go.mod` for Go).

## Before installing any dependency

1. Check if a lockfile or manifest already exists (`requirements.txt`, `pyproject.toml`, `package.json`, etc.)
2. Confirm the correct environment is active (venv sourced, correct Node version, etc.)
3. Install into the project scope only

## Never

- `pip install <package>` without an active venv
- `npm install -g <package>`
- Any install command that writes to a global or user-level package store
