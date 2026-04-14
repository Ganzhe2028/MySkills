---
name: macos-command-launcher
description: Build reusable macOS command launcher apps and choose the right packaging route. Use when the user wants a Spotlight-launchable manual starter, a Terminal-visible wrapper, a silent background launcher, a LaunchAgent, or a native app for Mac commands or services.
user-invocable: true
---

## What this skill does

Create simple, reliable macOS launchers with explicit absolute paths, no PATH dependence, duplicate-start protection via a separate running precheck, and an `osacompile`-based manual `.app` workflow.

For Spotlight-startable manual launchers, prefer a `.app` placed in `~/Applications`.

## Route table

| Need | Use | Why | Notes |
| --- | --- | --- | --- |
| Manual starter that should launch from Spotlight | `.app` | Spotlight indexes app bundles well | Put it in `~/Applications` |
| Quick Finder double-click shell wrapper | `.command` | Fastest terminal wrapper | Not ideal for Spotlight |
| Always-on background service at login | LaunchAgent | Starts automatically without user action | Best for daemons and sync jobs |
| Real UI, menus, settings, or app lifecycle | Native app | Proper macOS application model | Do this only when the launcher is no longer enough |

## Default workflow

1. Choose the smallest route that fits the job.
2. Use absolute executable paths only.
3. Precheck each service with a separate `/usr/bin/pgrep -f` running flag before starting.
4. Keep Terminal-visible mode simple: reliability over tab choreography.
5. If Spotlight matters, place the bundle in `~/Applications`.
6. Verify the bundle exists, then verify launch and process state.

## Helper script

Use `scripts/build-launcher.sh` to compile a manual `.app` launcher from explicit inputs with repeated `--service <command> <match>` pairs. It does not build LaunchAgents or native apps.

The second `--service` value is a `pgrep -f` match string. Keep it specific and stable; broad, empty, or changing matches can skip the wrong process or fail to guard duplicates.

`silent` mode is only a manual background start. It does not manage login startup or restarts; use LaunchAgent for start-at-login or keep-alive behavior.

Example:

```bash
./scripts/build-launcher.sh \
  --name "My Launcher" \
  --output-dir "$HOME/Applications" \
  --mode terminal \
  --service "/Users/mac/bin/service-a start" "service-a start" \
  --service "/Users/mac/bin/service-b --flag" "service-b --flag"
```

## Failure modes

- PATH-dependent commands fail after login or from Spotlight.
- Duplicate launches happen when the `pgrep` match is too broad or missing.
- Terminal-visible launchers become fragile when they try to manage tabs/windows too much.
- Spotlight does not find the launcher if the app bundle is not in `~/Applications`.

## Verification checklist

- Bundle/applet exists at the expected path.
- `Info.plist` exists inside the bundle.
- GUI launch path works from Finder or Spotlight.
- Confirm each service process appears with `pgrep -f`.
- Confirm a second launch does not spawn duplicates.
