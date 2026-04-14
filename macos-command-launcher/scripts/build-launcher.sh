#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  build-launcher.sh --name NAME [--output-dir DIR] [--mode terminal|silent] \
    --service "absolute command line" "pgrep match" [--service ...]

Examples:
  build-launcher.sh \
    --name "My Launcher" \
    --output-dir "$HOME/Applications" \
    --mode terminal \
    --service "/Users/mac/bin/service-a start" "service-a start" \
    --service "/Users/mac/bin/service-b --flag" "service-b --flag"
EOF
}

die() {
  printf 'error: %s\n' "$1" >&2
  exit 1
}

escape_applescript_string() {
  local value=$1
  value=${value//\\/\\\\}
  value=${value//\"/\"\"}
  printf '%s' "$value"
}

name=""
output_dir="$HOME/Applications"
mode="terminal"
declare -a service_commands=()
declare -a service_matches=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --name)
      [[ $# -ge 2 ]] || die "--name needs a value"
      name=$2
      shift 2
      ;;
    --output-dir)
      [[ $# -ge 2 ]] || die "--output-dir needs a value"
      output_dir=$2
      shift 2
      ;;
    --mode)
      [[ $# -ge 2 ]] || die "--mode needs a value"
      mode=$2
      shift 2
      ;;
    --service)
      [[ $# -ge 3 ]] || die "--service needs a command and a match string"
      service_commands+=("$2")
      service_matches+=("$3")
      shift 3
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
done

[[ -n "$name" ]] || die "--name is required"
[[ ${#service_commands[@]} -gt 0 ]] || die "at least one --service pair is required"
[[ "$mode" == "terminal" || "$mode" == "silent" ]] || die "--mode must be terminal or silent"

mkdir -p "$output_dir"

app_path="$output_dir/$name.app"
tmp_dir=$(mktemp -d)
trap 'rm -rf "$tmp_dir"' EXIT

apple_script="$tmp_dir/launcher.applescript"

{
  printf 'on run\n'
  printf '  set services to {'
  for i in "${!service_commands[@]}"; do
    if [[ $i -gt 0 ]]; then
      printf ', '
    fi
    printf '{"%s", "%s"}' \
      "$(escape_applescript_string "${service_commands[$i]}")" \
      "$(escape_applescript_string "${service_matches[$i]}")"
  done
  printf '}\n'
  printf '  set serviceIndex to 0\n'
  printf '  repeat with service in services\n'
  printf '    set serviceIndex to serviceIndex + 1\n'
  printf '    set commandText to item 1 of service\n'
  printf '    set matchText to item 2 of service\n'
  printf '    set runningFlag to do shell script "/bin/sh -lc " & quoted form of ("if /usr/bin/pgrep -f -- " & quoted form of matchText & " >/dev/null; then echo 1; else echo 0; fi")\n'
  printf '    if runningFlag is "0" then\n'
  printf '      if "%s" is "terminal" then\n' "$mode"
  printf '        if serviceIndex > 1 then delay 0.3\n'
  printf '        tell application "Terminal"\n'
  printf '          activate\n'
  printf '          do script commandText\n'
  printf '        end tell\n'
  printf '      else\n'
  printf '        set shellCommand to "nohup " & commandText & " >/dev/null 2>&1 &"\n'
  printf '        do shell script "/bin/sh -lc " & quoted form of shellCommand\n'
  printf '      end if\n'
  printf '    end if\n'
  printf '  end repeat\n'
  printf 'end run\n'
} > "$apple_script"

/usr/bin/osacompile -o "$app_path" "$apple_script"

[[ -d "$app_path" ]] || die "bundle not created: $app_path"
[[ -f "$app_path/Contents/Info.plist" ]] || die "missing Info.plist in bundle: $app_path"

printf 'created: %s\n' "$app_path"
printf 'next: open it once, then confirm processes with /usr/bin/pgrep -f\n'
