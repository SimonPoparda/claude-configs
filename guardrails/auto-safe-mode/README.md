# auto-safe-mode

Balanced autonomy guardrail. Claude operates freely within the project directory for normal work, but pauses and asks for explicit approval before any action that is hard to reverse or has broad impact.

## Activate

```
/auto-safe-mode
```

Or say: "enter auto-safe mode"

## Scope

All actions are constrained to the **current project directory**. Any operation that would affect files, processes, or systems outside the project root requires approval regardless of its risk level.

## Safe — no approval needed

These actions proceed automatically:

| Category | Examples |
|----------|---------|
| Read files | Reading any file within the project |
| Write / edit files | Creating or modifying files within the project |
| Run tests & linters | `npm test`, `pytest`, `eslint`, `tsc`, etc. |
| Build commands | `npm run build`, `make`, `cargo build`, etc. |
| Install dependencies | `npm install`, `pip install`, `cargo add`, etc. |
| Read-only git | `git status`, `git diff`, `git log`, `git branch` |
| Search & grep | Any read-only codebase exploration |

## Dangerous — approval required

Claude will describe the action and wait for a yes/no before proceeding:

| Category | Examples |
|----------|---------|
| Permanent deletion | `rm`, `rmdir`, deleting files or directories |
| Destructive git | `git reset --hard`, `git push --force`, `git checkout .`, `git clean` |
| Committing & pushing | `git commit`, `git push`, `git merge`, `git rebase` |
| Process management | Killing processes (`kill`, `pkill`) |
| Anything outside project root | Any path outside the working directory |
| External network calls | curl to external APIs, webhooks, etc. |
| Config / system changes | Modifying shell configs, environment variables, system settings |
| Database mutations | DROP, DELETE, TRUNCATE, or destructive migrations |

## Install

Copy the command to your project:

```bash
cp path/to/claude-configs/.claude/commands/auto-safe-mode.md .claude/commands/
```
