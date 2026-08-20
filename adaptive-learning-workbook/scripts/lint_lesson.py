#!/usr/bin/env python3
"""Validate an adaptive-learning Notion worksheet before it is created."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

EXACT_BLANK = "【\u3000\u3000】"
REQUIRED_HEADINGS = {
    "goal": re.compile(r"^# (?:今天的目标|本次目标|目标)\s*$", re.MULTILINE),
    "materials": re.compile(r"^# (?:学习材料|练习材料|材料)\s*$", re.MULTILINE),
    "steps": re.compile(r"^# (?:操作|练习步骤)\s*$", re.MULTILINE),
    "stop": re.compile(r"^# 停止规则\s*$", re.MULTILINE),
    "record": re.compile(r"^# 完成记录\s*$", re.MULTILINE),
}
TIME_RE = re.compile(r"总时限[：:]\s*\*{0,2}\s*(\d{1,3})\s*分钟")
BRACKET_RE = re.compile(r"【([^】]*)】")
PROHIBITED_PLACEHOLDERS = (
    "在这里填写",
    "在这里粘贴",
    "填写：",
    "填写:",
    "粘贴：",
    "粘贴:",
)
ANSWER_LEAK_MARKERS = ("正确答案", "参考答案", "答案是")
DECORATIVE_BLOCKS = ("<columns>", "<table ")


def _line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def lint_text(text: str, *, max_minutes: int = 60) -> list[str]:
    """Return actionable validation errors. An empty list means valid."""

    errors: list[str] = []

    for key, pattern in REQUIRED_HEADINGS.items():
        if not pattern.search(text):
            errors.append(f"missing required section: {key}")

    time_matches = TIME_RE.findall(text)
    if len(time_matches) != 1:
        errors.append("include exactly one visible '总时限：N 分钟'")
    else:
        minutes = int(time_matches[0])
        if minutes <= 0:
            errors.append("total time must be greater than 0 minutes")
        if minutes > max_minutes:
            errors.append(
                f"total time is {minutes} minutes; hard limit is {max_minutes}"
            )

    if text.count("【") != text.count("】"):
        errors.append("unmatched input bracket: every 【 needs a closing 】")

    bracket_matches = list(BRACKET_RE.finditer(text))
    if not bracket_matches:
        errors.append(f"include at least one empty input location: {EXACT_BLANK}")

    for match in bracket_matches:
        if match.group(0) != EXACT_BLANK:
            line = _line_number(text, match.start())
            errors.append(
                f"line {line}: input location must be exactly {EXACT_BLANK}"
            )

    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.count(EXACT_BLANK) > 1:
            errors.append(
                f"line {line_no}: one response line cannot contain multiple input locations"
            )
        if line.strip() == EXACT_BLANK:
            errors.append(
                f"line {line_no}: input location needs a clear label on the same line"
            )

    for phrase in PROHIBITED_PLACEHOLDERS:
        if phrase in text:
            errors.append(f"remove ambiguous placeholder phrase: {phrase}")

    for block in DECORATIVE_BLOCKS:
        if block in text:
            errors.append(
                f"remove low-editability decorative block from worksheet: {block}"
            )

    details_start = text.find("<details>")
    details_end = text.rfind("</details>")
    record_match = REQUIRED_HEADINGS["record"].search(text)

    if details_start == -1 or details_end == -1:
        errors.append("add a collapsed <details> answer section at the end")
        main_content = text
    else:
        main_content = text[:details_start]
        if details_end < details_start:
            errors.append("answer section closes before it opens")
        if text[details_end + len('</details>') :].strip():
            errors.append("answer section must be the final page block")
        if "<summary>完成后" not in text[details_start:details_end]:
            errors.append("answer toggle summary must begin with '完成后'")
        if record_match and details_start < record_match.start():
            errors.append("answer section must appear after the completion record")

    for marker in ANSWER_LEAK_MARKERS:
        if marker in main_content:
            errors.append(
                f"possible answer leakage before collapsed answer section: {marker}"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lint a Notion learning worksheet Markdown file."
    )
    parser.add_argument("path", type=Path, help="Markdown draft to validate")
    parser.add_argument(
        "--max-minutes",
        type=int,
        default=60,
        help="Hard time limit; defaults to 60",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Return machine-readable validation output",
    )
    args = parser.parse_args()

    if not args.path.is_file():
        message = f"file not found: {args.path}"
        if args.json:
            print(json.dumps({"valid": False, "errors": [message]}, ensure_ascii=False))
        else:
            print(f"ERROR: {message}", file=sys.stderr)
        return 2

    text = args.path.read_text(encoding="utf-8")
    errors = lint_text(text, max_minutes=args.max_minutes)

    if args.json:
        print(
            json.dumps(
                {"valid": not errors, "errors": errors},
                ensure_ascii=False,
                indent=2,
            )
        )
    elif errors:
        print(f"INVALID: {args.path}")
        for error in errors:
            print(f"- {error}")
    else:
        print(f"VALID: {args.path}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
