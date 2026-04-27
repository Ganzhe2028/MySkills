#!/usr/bin/env python3
"""Read-only local audit for Hermes Agent, OpenCode, and Codex."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None  # type: ignore[assignment]


HOME = Path.home()
SECRET_RE = re.compile(
    r"(?i)(api[_-]?key|token|secret|password|authorization|bearer)\s*[:=]\s*[^,\s]+"
)
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def redact(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: redact(v) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    if isinstance(value, str):
        value = ANSI_RE.sub("", value)
        value = SECRET_RE.sub(lambda m: m.group(0).split(":", 1)[0].split("=", 1)[0] + ": ***REDACTED***", value)
        value = re.sub(r"sk-[A-Za-z0-9_-]{8,}", "sk-***REDACTED***", value)
        return value
    return value


def run_cmd(args: list[str], timeout: int = 8) -> dict[str, Any]:
    binary = shutil.which(args[0])
    if not binary:
        return {"ok": False, "error": f"{args[0]} not found"}
    try:
        proc = subprocess.run(
            [binary, *args[1:]],
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": redact(str(exc))}
    return {
        "ok": proc.returncode == 0,
        "code": proc.returncode,
        "stdout": redact(proc.stdout.strip()),
        "stderr": redact(proc.stderr.strip()),
    }


def read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        return {"_error": str(exc)}


def read_toml(path: Path) -> dict[str, Any]:
    if not path.is_file() or tomllib is None:
        return {}
    try:
        return tomllib.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        return {"_error": str(exc)}


def parse_simple_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]
    for raw_line in path.read_text(errors="replace").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        key, value = raw_line.strip().split(":", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value == "":
            child: dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            lowered = value.lower()
            if lowered in {"true", "false"}:
                parsed: Any = lowered == "true"
            else:
                parsed = value
            parent[key] = redact(parsed)
    return root


def count_skills(path: Path) -> int:
    if not path.is_dir():
        return 0
    return sum(1 for _ in path.glob("*/SKILL.md"))


def parse_hermes_status(output: str) -> dict[str, Any]:
    status: dict[str, Any] = {}
    current_section = ""
    platforms: dict[str, str] = {}
    for line in output.splitlines():
        text = line.strip()
        if text.startswith("◆ "):
            current_section = text[2:].strip()
        if current_section == "Gateway Service" and text.startswith("Status:"):
            status["gateway_status"] = text.split("Status:", 1)[1].strip()
        if current_section == "Messaging Platforms" and ("✓ configured" in text or "✗ not configured" in text):
            parts = text.split()
            if parts:
                platforms[parts[0]] = "configured" if "✓ configured" in text else "not configured"
        if current_section == "Sessions" and text.startswith("Active:"):
            status["active_sessions"] = text.split("Active:", 1)[1].strip()
    if platforms:
        status["platforms"] = platforms
    return status


def audit_hermes() -> dict[str, Any]:
    config_path = HOME / ".hermes/config.yaml"
    config = parse_simple_yaml(config_path)
    status_cmd = run_cmd(["hermes", "status"], timeout=12)
    version_cmd = run_cmd(["hermes", "--version"], timeout=20)
    gateway_state = read_json(HOME / ".hermes/gateway_state.json")
    return {
        "binary": shutil.which("hermes"),
        "version": (version_cmd.get("stdout") or "").splitlines()[0] if version_cmd.get("ok") else version_cmd,
        "config_path": str(config_path),
        "model": config.get("model", {}),
        "memory": config.get("memory", {}),
        "status": parse_hermes_status(status_cmd.get("stdout", "")) if status_cmd.get("ok") else status_cmd,
        "gateway_state_file": redact(gateway_state),
        "skill_count": count_skills(HOME / ".hermes/skills"),
    }


def audit_opencode() -> dict[str, Any]:
    primary = HOME / ".config/opencode/opencode.json"
    secondary = HOME / ".opencode/opencode.json"
    primary_config = read_json(primary)
    secondary_config = read_json(secondary)
    mcp_cmd = run_cmd(["opencode", "mcp", "list"], timeout=15)
    mcp_stdout = str(mcp_cmd.get("stdout", ""))
    chrome_connected = "chrome" in mcp_stdout and "connected" in mcp_stdout
    mcp_error = None if mcp_cmd.get("ok") else (mcp_cmd.get("stderr") or mcp_cmd.get("error"))
    return {
        "binary": shutil.which("opencode"),
        "version": run_cmd(["opencode", "--version"], timeout=8),
        "primary_config": str(primary),
        "secondary_config": str(secondary),
        "model": primary_config.get("model"),
        "plugins": primary_config.get("plugin", []),
        "chrome_mcp_configured": "chrome" in (primary_config.get("mcp") or {}),
        "chrome_mcp_connected": chrome_connected,
        "mcp_check": {"ok": mcp_cmd.get("ok"), "error": mcp_error},
        "skill_count": count_skills(HOME / ".config/opencode/skills"),
        "secondary_skill_paths": (secondary_config.get("skills") or {}).get("paths", []),
    }


def audit_codex() -> dict[str, Any]:
    config_path = HOME / ".codex/config.toml"
    config = read_toml(config_path)
    enabled_plugins = [
        name for name, data in (config.get("plugins") or {}).items() if isinstance(data, dict) and data.get("enabled")
    ]
    return {
        "binary": shutil.which("codex"),
        "version": run_cmd(["codex", "--version"], timeout=8),
        "config_path": str(config_path),
        "model": config.get("model"),
        "reasoning_effort": config.get("model_reasoning_effort"),
        "features": config.get("features", {}),
        "mcp_servers": sorted((config.get("mcp_servers") or {}).keys()),
        "enabled_plugins": sorted(enabled_plugins),
        "agents_skill_count": count_skills(HOME / ".agents/skills"),
        "codex_skill_count": count_skills(HOME / ".codex/skills"),
    }


def build_report() -> dict[str, Any]:
    return {
        "changed_configuration": False,
        "hermes": audit_hermes(),
        "opencode": audit_opencode(),
        "codex": audit_codex(),
    }


def print_markdown(report: dict[str, Any]) -> None:
    hermes = report["hermes"]
    opencode = report["opencode"]
    codex = report["codex"]
    print("# Agent Config Audit")
    print()
    print("No configuration was changed.")
    print()
    print("## Hermes Agent")
    print(f"- Version: {hermes.get('version')}")
    print(f"- Model: {(hermes.get('model') or {}).get('default')} via {(hermes.get('model') or {}).get('provider')}")
    print(f"- Gateway: {(hermes.get('status') or {}).get('gateway_status', 'unknown')}")
    print(f"- Gateway state file: {(hermes.get('gateway_state_file') or {}).get('gateway_state', 'unknown')}")
    print(f"- Skills: {hermes.get('skill_count')}")
    print()
    print("## OpenCode")
    version = opencode.get("version", {})
    print(f"- Version: {version.get('stdout') if isinstance(version, dict) else version}")
    print(f"- Model: {opencode.get('model')}")
    print(f"- Chrome MCP configured: {opencode.get('chrome_mcp_configured')}")
    print(f"- Chrome MCP connected: {opencode.get('chrome_mcp_connected')}")
    print(f"- Skills: {opencode.get('skill_count')}")
    print()
    print("## Codex")
    cversion = codex.get("version", {})
    print(f"- Version: {cversion.get('stdout') if isinstance(cversion, dict) else cversion}")
    print(f"- Model: {codex.get('model')} ({codex.get('reasoning_effort')})")
    print(f"- MCP servers: {', '.join(codex.get('mcp_servers') or [])}")
    print(f"- Skills: .agents={codex.get('agents_skill_count')}, .codex={codex.get('codex_skill_count')}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only audit for local agent configuration.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown.")
    args = parser.parse_args()
    report = redact(build_report())
    if args.json:
        json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
        print()
    else:
        print_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
