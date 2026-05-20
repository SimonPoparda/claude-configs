Sandbox mode YT: https://www.youtube.com/watch?v=Qc-Q4lXMbE4&t=150s

settings.json
{
    "sandbox": {
        "enabled": true
    },
    "permissions": {
        "autoAllow": ["Bash(sandboxed)"],
        "excludedCommands": ["docker *"]
    },
    "network": {
        "allowLocalPortBinding": true
    },
    "deny": [
        "Read(**/.env)",
        "Read(**/.credentials*)",
        "Read(**/.secrets*)"
    ]
}
