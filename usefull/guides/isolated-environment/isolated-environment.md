YT reference: https://www.youtube.com/watch?v=8dqqa0dLpGU

# Setting Up an Isolated Environment for Claude Code (YOLO Mode)

Running Claude Code in YOLO mode (`--dangerously-skip-permissions`) allows the agent to work without manual approval at each step, but comes with risks — such as accidental file deletion or malicious command injection. To protect your system, use Docker Dev Containers as an isolation layer.

## 1. Required Software

Before you begin, install the following tools:

- **Docker Desktop** — download from [docker.com](https://www.docker.com)
- **Dev Containers Extension** — available for VS Code and Cursor

## 2. Prepare the Repository

1. Clone the official Claude Code repository (link mentioned in the video above).
2. Navigate into the folder: `cd claude-code`
3. Remove unnecessary files — the only folder you need to create the environment is the hidden `.devcontainer` folder. You can delete the rest to keep things clean.

## 3. Configure the Container (Key Changes)

Open the folder in your editor and make the following changes to the configuration file inside `.devcontainer`:

- **Persistent authentication** — change the volume mount method so you don't have to log in to Claude every time the container starts.
- **Port forwarding** — if you plan to build web apps (e.g., with Next.js), add port forwarding (e.g., port 3000) so you can access the app from your host machine's browser.

## 4. Launch the Environment

1. Press `Ctrl + Shift + P` (Windows/Linux) or `Cmd + Shift + P` (Mac) in your editor.
2. Select: **Dev Containers: Open Folder in Container**
3. Choose the `claude-code` folder and wait for Docker to build the image (first run may take a few minutes).

## 5. Initial Setup and Login

Once the container has loaded:

1. In the container's terminal, run: `claude`
2. Log in with your Anthropic account.
3. Accept the recommended settings and trust the files in the folder.
4. **Restart** — close the container and reopen it via **Reopen in Container** to confirm that authentication was saved correctly.

## 6. Activating YOLO Mode (Autopilot)

You can now safely let Claude work autonomously inside the container. To run it without permission prompts, use:

```bash
claude --dangerously-skip-permissions
```
