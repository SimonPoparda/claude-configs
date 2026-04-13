# Plugin Activation

When the user says anything like **"enable X"**, **"use X"**, **"activate X"**, or **"turn on X"** where X matches a known plugin name, follow this procedure:

## Steps

1. **Check if installed**
   ```bash
   claude plugin list
   ```
   Look for the plugin name in the output.

2. **If not installed** — find the install command in `plugins/<name>/README.md` and run it automatically. Do not ask for permission first; installing a plugin is a safe action.

3. **Activate** — once installed, apply the plugin's behavior for this session by reading `plugins/<name>/<name>.md` and following its instructions.

4. **Confirm** — tell the user the plugin is active and briefly describe what changed.

## Known plugins

| Trigger names | Directory | Behavior file |
|---------------|-----------|---------------|
| caveman, cave, unga | `plugins/caveman/` | Loaded automatically by the plugin system after install |
| karpathy, karpathy-guidelines, coding guidelines | `plugins/karpathy-guidelines/` | Fetch latest from repo (see below) |

## Example

User: "use caveman"
→ Run `claude plugin list`, check for "caveman"
→ If missing: run `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman`
→ Confirm: "Caveman mode active. Tok cut ~75%. Talk like caveman now."

## Plugin-specific activation

### karpathy-guidelines

Do **not** rely on the installed plugin snapshot. Always fetch the latest version directly from the source repo:

- Guidelines: `https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md`
- Examples: `https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/EXAMPLES.md`

Fetch both files, read their contents, and apply them for the session. This ensures you always use the most up-to-date version of the guidelines and examples.

## Adding a plugin to this list

When a new plugin is added to `plugins/`, add a row to the Known plugins table above with its trigger names and behavior file path.
