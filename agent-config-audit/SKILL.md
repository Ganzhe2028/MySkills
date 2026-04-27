---
name: agent-config-audit
description: Audit local Hermes Agent, OpenCode, and Codex state without changing models, tokens, permissions, MCP, gateway, or skills.
---

# Agent Config Audit

Use this skill before changing local agent configuration. It produces a current-state report and does not repair anything.

## Run

From this skill directory:

```bash
python3 scripts/audit_agent_config.py
python3 scripts/audit_agent_config.py --json
```

## What to report

- Hermes Agent: version, default model/provider, gateway status, configured messaging platforms, memory setting, skill count.
- OpenCode: version, default model, plugin list, Chrome MCP configured/connected status, skill count, active config roots.
- Codex: version, model/reasoning effort, enabled MCP servers, enabled plugins, skill counts for `.agents` and `.codex`.

## Safety rules

- Redact API keys, bearer tokens, auth headers, passwords, and secret values.
- Do not print raw config files.
- Do not run setup, model switching, gateway start/stop, install, update, or doctor fix commands.
- If a read-only command fails, report the failure and continue with file-based evidence.
