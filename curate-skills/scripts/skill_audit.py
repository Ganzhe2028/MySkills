#!/usr/bin/env python3
"""Audit a skills directory and emit inventory plus action hints."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

SKIP_PARTS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    "dist",
    "build",
}

TOKEN_STOP_WORDS = {
    "a",
    "an",
    "and",
    "agent",
    "agents",
    "any",
    "are",
    "asks",
    "authentication",
    "build",
    "checks",
    "codex",
    "conventions",
    "create",
    "creating",
    "data",
    "dependencies",
    "deployment",
    "deploy",
    "deploys",
    "do",
    "does",
    "edit",
    "editing",
    "environment",
    "existing",
    "for",
    "from",
    "guide",
    "guidance",
    "help",
    "helps",
    "host",
    "how",
    "into",
    "install",
    "its",
    "model",
    "missing",
    "need",
    "needs",
    "new",
    "output",
    "or",
    "perform",
    "preview",
    "prerequisites",
    "production",
    "project",
    "projects",
    "provides",
    "publish",
    "quick",
    "skill",
    "skills",
    "start",
    "support",
    "tasks",
    "that",
    "the",
    "their",
    "them",
    "this",
    "use",
    "used",
    "user",
    "users",
    "using",
    "when",
    "with",
    "workflow",
    "workflows",
    "work",
}

WEAK_DESCRIPTION_TOKENS = {
    "help",
    "guidance",
    "tasks",
    "workflows",
    "capabilities",
    "support",
}


@dataclass
class SkillRecord:
    path: str
    folder_name: str
    name: str | None
    description: str | None
    line_count: int
    word_count: int
    heading_count: int
    headings: list[str] = field(default_factory=list)
    scripts: int = 0
    references: int = 0
    assets: int = 0
    has_openai_yaml: bool = False
    frontmatter_valid: bool = False
    frontmatter_error: str | None = None
    issues: list[str] = field(default_factory=list)
    action_hints: list[str] = field(default_factory=list)
    primary_hint: str = "keep"
    tokens: list[str] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit a skill directory and emit inventory plus action hints.",
    )
    parser.add_argument("target", help="Skill folder or skills root to audit")
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="Output format",
    )
    parser.add_argument(
        "--min-similarity",
        type=float,
        default=0.28,
        help="Minimum overlap score for merge candidates",
    )
    return parser.parse_args()


def should_skip(path: Path) -> bool:
    return any(part in SKIP_PARTS or part.startswith(".") for part in path.parts)


def find_skill_dirs(target: Path) -> list[Path]:
    if (target / "SKILL.md").exists():
        return [target.resolve()]

    skill_dirs: list[Path] = []
    for candidate in target.rglob("SKILL.md"):
        if should_skip(candidate.relative_to(target)):
            continue
        skill_dirs.append(candidate.parent.resolve())
    return sorted(set(skill_dirs))


def split_frontmatter(content: str) -> tuple[str | None, str, str | None]:
    if not content.startswith("---\n"):
        return None, content, "missing YAML frontmatter"

    marker = "\n---\n"
    end = content.find(marker, 4)
    if end == -1:
        if content.endswith("\n---"):
            end = len(content) - 4
            body = ""
        else:
            return None, content, "unterminated YAML frontmatter"
    else:
        body = content[end + len(marker) :]

    frontmatter = content[4:end]
    return frontmatter, body, None


def parse_frontmatter(frontmatter_text: str | None) -> tuple[dict[str, object], str | None]:
    if frontmatter_text is None:
        return {}, None

    if yaml is not None:
        try:
            parsed = yaml.safe_load(frontmatter_text) or {}
        except Exception as exc:  # pragma: no cover - parser-specific errors
            return {}, str(exc)
        if not isinstance(parsed, dict):
            return {}, "frontmatter is not a YAML mapping"
        return parsed, None

    parsed: dict[str, object] = {}
    for raw_line in frontmatter_text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        parsed[key.strip()] = value.strip().strip("\"'")
    return parsed, None


def count_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for child in path.rglob("*") if child.is_file() and not should_skip(child.relative_to(path)))


def extract_headings(body: str) -> list[str]:
    headings = []
    for line in body.splitlines():
        match = re.match(r"^#{1,3}\s+(.+?)\s*$", line)
        if match:
            headings.append(match.group(1))
    return headings


def tokenize(*chunks: str | None) -> list[str]:
    tokens: set[str] = set()
    for chunk in chunks:
        if not chunk:
            continue
        for token in re.findall(r"[a-z0-9][a-z0-9-]{1,}", chunk.lower().replace("_", "-")):
            normalized = token.strip("-")
            if len(normalized) < 3 or normalized in TOKEN_STOP_WORDS:
                continue
            tokens.add(normalized)
    return sorted(tokens)


def description_has_trigger(description: str | None) -> bool:
    if not description:
        return False
    lowered = description.lower()
    return "use when" in lowered or "trigger" in lowered or "when codex needs" in lowered


def description_is_generic(description: str | None) -> bool:
    if not description:
        return True
    lowered = description.lower()
    if "[todo" in lowered:
        return True
    meaningful = tokenize(description)
    if len(meaningful) < 5:
        return True
    weak_count = sum(1 for token in meaningful if token in WEAK_DESCRIPTION_TOKENS)
    return weak_count >= 2 and not description_has_trigger(description)


def score_similarity(left: SkillRecord, right: SkillRecord) -> tuple[float, list[str]]:
    left_tokens = set(left.tokens)
    right_tokens = set(right.tokens)
    shared = sorted(left_tokens & right_tokens)
    token_score = 0.0
    overlap_score = 0.0
    if left_tokens and right_tokens:
        token_score = len(shared) / len(left_tokens | right_tokens)
        overlap_score = len(shared) / min(len(left_tokens), len(right_tokens))
    text_score = SequenceMatcher(
        None,
        (left.description or "")[:400].lower(),
        (right.description or "")[:400].lower(),
    ).ratio()
    name_score = SequenceMatcher(
        None,
        left.folder_name.lower(),
        right.folder_name.lower(),
    ).ratio()
    score = (0.4 * token_score) + (0.2 * overlap_score) + (0.2 * text_score) + (0.2 * name_score)
    return round(score, 3), shared[:8]


def ordered_unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def primary_hint(hints: list[str]) -> str:
    priority = [
        "replace-candidate",
        "merge-candidate",
        "split-candidate",
        "tighten",
        "keep",
    ]
    for label in priority:
        if label in hints:
            return label
    return "keep"


def inspect_skill(skill_dir: Path) -> SkillRecord:
    content = (skill_dir / "SKILL.md").read_text()
    frontmatter_text, body, frontmatter_boundary_error = split_frontmatter(content)
    frontmatter, frontmatter_parse_error = parse_frontmatter(frontmatter_text)

    name = frontmatter.get("name") if isinstance(frontmatter.get("name"), str) else None
    description = (
        frontmatter.get("description")
        if isinstance(frontmatter.get("description"), str)
        else None
    )

    headings = extract_headings(body)
    record = SkillRecord(
        path=str(skill_dir),
        folder_name=skill_dir.name,
        name=name.strip() if name else None,
        description=description.strip() if description else None,
        line_count=len(content.splitlines()),
        word_count=len(re.findall(r"\S+", content)),
        heading_count=len(headings),
        headings=headings[:8],
        scripts=count_files(skill_dir / "scripts"),
        references=count_files(skill_dir / "references"),
        assets=count_files(skill_dir / "assets"),
        has_openai_yaml=(skill_dir / "agents" / "openai.yaml").exists(),
        frontmatter_valid=frontmatter_boundary_error is None and frontmatter_parse_error is None,
        frontmatter_error=frontmatter_boundary_error or frontmatter_parse_error,
    )

    issues: list[str] = []
    hints: list[str] = []

    if record.frontmatter_error:
        issues.append(record.frontmatter_error)
        hints.append("tighten")
    if not record.name:
        issues.append("missing name")
        hints.append("tighten")
    if not record.description:
        issues.append("missing description")
        hints.append("tighten")
    elif description_is_generic(record.description):
        issues.append("weak trigger surface")
        hints.append("tighten")
    if record.name and record.folder_name != record.name:
        issues.append("folder name does not match frontmatter name")
        hints.append("tighten")
    if not record.has_openai_yaml:
        issues.append("missing agents/openai.yaml")
        hints.append("tighten")
    if record.line_count > 180 or record.word_count > 1400 or (
        record.line_count > 140 and record.heading_count > 12
    ):
        issues.append("large skill surface")
        hints.append("split-candidate")
    if (record.scripts + record.references + record.assets) == 0 and description_is_generic(record.description):
        issues.append("thin wrapper risk")
        hints.append("replace-candidate")

    record.issues = ordered_unique(issues)
    record.action_hints = ordered_unique(hints) or ["keep"]
    record.primary_hint = primary_hint(record.action_hints)
    record.tokens = tokenize(
        record.folder_name,
        record.name,
        record.description,
        " ".join(record.headings),
    )
    return record


def build_overlap_report(
    skills: list[SkillRecord],
    min_similarity: float,
) -> tuple[list[dict[str, object]], dict[str, list[str]]]:
    overlaps: list[dict[str, object]] = []
    pair_map: dict[str, list[str]] = {skill.path: [] for skill in skills}

    for left, right in combinations(skills, 2):
        score, shared = score_similarity(left, right)
        if score < min_similarity or (not shared and score < 0.55):
            continue
        overlaps.append(
            {
                "left": left.folder_name,
                "right": right.folder_name,
                "score": score,
                "shared_tokens": shared,
            }
        )
        pair_map[left.path].append(right.folder_name)
        pair_map[right.path].append(left.folder_name)

    overlaps.sort(key=lambda item: item["score"], reverse=True)
    return overlaps, pair_map


def enrich_with_overlap(skills: list[SkillRecord], pair_map: dict[str, list[str]]) -> None:
    for skill in skills:
        peers = pair_map.get(skill.path, [])
        if peers:
            skill.issues.append("overlap with " + ", ".join(peers[:3]))
            skill.action_hints = ordered_unique(skill.action_hints + ["merge-candidate"])
            skill.primary_hint = primary_hint(skill.action_hints)


def render_markdown(
    target: Path,
    skills: list[SkillRecord],
    overlaps: list[dict[str, object]],
) -> str:
    lines = [
        "# Skill Audit",
        "",
        f"- Target: `{target}`",
        f"- Skills discovered: {len(skills)}",
        "",
        "## Summary",
        "",
        "| Skill | Hint | Scripts | Refs | Assets | Lines | Issues |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]

    for skill in skills:
        issues = "; ".join(skill.issues[:3]) if skill.issues else "none"
        lines.append(
            f"| `{skill.folder_name}` | `{skill.primary_hint}` | {skill.scripts} | "
            f"{skill.references} | {skill.assets} | {skill.line_count} | {issues} |"
        )

    lines.extend(["", "## Overlap Candidates", ""])
    if overlaps:
        lines.extend(
            [
                "| Left | Right | Score | Shared Tokens |",
                "| --- | --- | ---: | --- |",
            ]
        )
        for overlap in overlaps[:20]:
            shared = ", ".join(overlap["shared_tokens"])
            lines.append(
                f"| `{overlap['left']}` | `{overlap['right']}` | {overlap['score']:.3f} | {shared} |"
            )
    else:
        lines.append("No high-overlap pairs detected.")

    lines.extend(["", "## Details", ""])
    for skill in skills:
        lines.append(f"### `{skill.folder_name}`")
        lines.append(f"- Path: `{skill.path}`")
        lines.append(f"- Name: `{skill.name or '(missing)'}`")
        lines.append(f"- Description: `{skill.description or '(missing)'}`")
        lines.append(f"- Action hints: `{', '.join(skill.action_hints)}`")
        lines.append(
            f"- Resources: scripts={skill.scripts}, references={skill.references}, assets={skill.assets}, openai_yaml={'yes' if skill.has_openai_yaml else 'no'}"
        )
        lines.append(f"- Headings: {', '.join(skill.headings) if skill.headings else '(none)'}")
        lines.append(f"- Issues: {', '.join(skill.issues) if skill.issues else 'none'}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def render_json(
    target: Path,
    skills: list[SkillRecord],
    overlaps: list[dict[str, object]],
) -> str:
    payload = {
        "target": str(target),
        "skill_count": len(skills),
        "skills": [asdict(skill) for skill in skills],
        "overlaps": overlaps,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    args = parse_args()
    target = Path(args.target).expanduser().resolve()
    if not target.exists():
        print(f"Target not found: {target}", file=sys.stderr)
        return 1

    skill_dirs = find_skill_dirs(target)
    if not skill_dirs:
        print(f"No skills found under: {target}", file=sys.stderr)
        return 1

    skills = [inspect_skill(skill_dir) for skill_dir in skill_dirs]
    overlaps, pair_map = build_overlap_report(skills, args.min_similarity)
    enrich_with_overlap(skills, pair_map)
    skills.sort(key=lambda item: (item.primary_hint != "keep", item.folder_name))

    if args.format == "markdown":
        sys.stdout.write(render_markdown(target, skills, overlaps))
    else:
        sys.stdout.write(render_json(target, skills, overlaps))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
