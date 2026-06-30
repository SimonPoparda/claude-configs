# Project Isolation & Initialization Rules

## 1. The Containment Rule (Strict)
- **NO GLOBAL INSTALLS:** Never install dependencies in the global scope. If a global installation is absolutely necessary, ask the user first and provide a clear justification.
- **Venv Enforcement:** Always create and use a local virtual environment (`.venv`) for Python projects. Do not run scripts outside of the isolated environment.
- **Scope Check:** Before executing any installation command, explicitly verify that the current working directory is the project root.

## 2. Scaffolding Checklist
When initializing a new project or module, always ensure the following files are present:
- `.gitignore`: Must include `.venv`, `__pycache__`, `.env`, node_modules, and OS-specific files (e.g., `.DS_Store`). And other files if that's necessary.
- `.env.example`: Provide a template file showcasing the required environment variables.
- `.env`: Store secrets locally here. **NEVER** commit the actual `.env` file to version control. Use Azure Key Vault, Databricks Secret Scopes, or equivalent cloud providers for production secrets.

## 3. Tool Selection
- **Python:** Prefer `uv` for fast package management if available; otherwise, use standard `pip` within the virtual environment.
- **Node.js:** Prefer `npm` or the project's existing package manager (`yarn`, `pnpm`).
- **Audit:** Always check for an existing `requirements.txt`, `pyproject.toml`, or `package.json` before proposing or installing new libraries.

## 4. Execution Flow
1. **Detect:** Identify the project technology stack (Python, JavaScript/TypeScript, Go, etc.).
2. **Isolate:** Create the local environment configuration (e.g., `uv venv` or `npm init`).
3. **Verify:** Run a local version check (e.g., `which python` or `get-command python`) to ensure the local, isolated tool is being used instead of the global one.