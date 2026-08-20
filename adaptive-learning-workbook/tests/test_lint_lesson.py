from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "lint_lesson.py"
SPEC = importlib.util.spec_from_file_location("lint_lesson", SCRIPT)
assert SPEC and SPEC.loader
LINT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LINT)


class LessonLintTests(unittest.TestCase):
    def test_all_page_templates_are_valid(self) -> None:
        for name in (
            "diagnostic-page.md",
            "micro-practice-page.md",
            "transfer-page.md",
        ):
            with self.subTest(name=name):
                text = (ROOT / "assets" / name).read_text(encoding="utf-8")
                self.assertEqual([], LINT.lint_text(text))

    def test_regression_fixtures_fail_for_expected_reason(self) -> None:
        cases = {
            "invalid-bracket-spacing.md": "input location must be exactly",
            "invalid-overlong.md": "hard limit is 60",
            "invalid-placeholder.md": "ambiguous placeholder phrase",
            "invalid-answer-leak.md": "possible answer leakage",
            "invalid-unlabelled-input.md": "needs a clear label",
            "invalid-missing-stop-rule.md": "missing required section: stop",
            "invalid-two-inputs-one-line.md": "cannot contain multiple",
        }
        for name, expected in cases.items():
            with self.subTest(name=name):
                text = (ROOT / "tests" / "fixtures" / name).read_text(
                    encoding="utf-8"
                )
                errors = LINT.lint_text(text)
                self.assertTrue(
                    any(expected in error for error in errors),
                    f"{name} did not produce expected error; got {errors}",
                )

    def test_skill_pack_has_required_references(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: adaptive-learning-workbook", skill)
        for relative_path in (
            "references/learner-contract.md",
            "references/learning-method.md",
            "references/notion-page-contract.md",
            "references/ielts-reading-adapter.md",
        ):
            self.assertTrue((ROOT / relative_path).is_file())
            self.assertIn(relative_path, skill)

    def test_chinese_wording_review_is_required(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        contract = (ROOT / "references" / "notion-page-contract.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("natural-chinese-writing", skill)
        self.assertIn("natural-chinese-writing", contract)
        self.assertIn("look at what / do what / write what", contract)
        self.assertIn("worksheet friction", contract)

    def test_attempt_state_and_reflection_rules_are_required(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        method = (ROOT / "references" / "learning-method.md").read_text(
            encoding="utf-8"
        )
        contract = (ROOT / "references" / "notion-page-contract.md").read_text(
            encoding="utf-8"
        )
        triggers = (ROOT / "tests" / "trigger-cases.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("first response", skill)
        self.assertIn("earliest broken conversion", skill)
        self.assertIn("Attempt-state audit", method)
        self.assertIn("emerging control", method)
        self.assertIn("Curriculum progress and scaffold fading", method)
        self.assertIn("Completion and reflection fields", contract)
        self.assertIn("blank reflection field", contract)
        self.assertIn("sign-to-interval conversion", triggers)
        self.assertIn("submission order", skill)
        self.assertIn("submission-and-correction order", contract)
        self.assertIn("separate correction", triggers)


if __name__ == "__main__":
    unittest.main()
