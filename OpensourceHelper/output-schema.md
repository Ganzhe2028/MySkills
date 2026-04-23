# OpenSource Release Guard — Output Schema

This file defines the exact output structure the agent should use when running the skill.

The goal is consistency.  
The agent should not improvise the report shape on every run.

---

## 0. General rule

Every run must produce one of these output types:

- `audit_report`
- `execution_plan`
- `execution_update`
- `final_verdict`

The agent may also include a short `clarification_needed` output only when a real blocking ambiguity prevents safe execution.

Do not mix all output types together unless the phase genuinely requires it.

---

## 1. Shared field rules

These fields may appear in multiple output types.

### `verdict_label`
Must be one of:

- `READY TO PUBLISH`
- `READY AFTER CURRENT-TREE FIXES`
- `BLOCKED BY GIT HISTORY`
- `RECOMMEND SPLIT PUBLIC/PRIVATE REPO`
- `NOT READY TO OPEN-SOURCE`

### `risk_level`
Must be one of:

- `low`
- `medium`
- `high`
- `critical`

### `status`
Must be one of:

- `ok`
- `warning`
- `blocked`
- `needs_approval`
- `done`
- `partial`

### `blocking`
Boolean:
- `true`
- `false`

### `confidence`
Must be one of:

- `high`
- `medium`
- `low`

Use lower confidence when:
- rights/licensing boundaries are unclear
- history visibility is not fully verified
- the repo is only partially accessible
- the examples may still contain real data
- remote strategy is not fully known

---

## 2. Output type: `audit_report`

Use this after the initial repository audit and before any destructive or high-impact action.

### Required structure

```json
{
  "output_type": "audit_report",
  "repo_summary": {
    "name": "string",
    "publication_intent": "public_github | private_cleanup | undecided | partial_open_source",
    "current_branch": "string",
    "has_git_history": true,
    "has_remote": true,
    "remote_state_summary": "string"
  },
  "executive_summary": {
    "verdict_label": "BLOCKED BY GIT HISTORY",
    "risk_level": "high",
    "top_blocker": "string",
    "recommended_option_id": "option_1",
    "summary": "string"
  },
  "findings": [
    {
      "id": "finding_1",
      "category": "privacy | secrets | real_data | git_history | ignore_rules | repo_hygiene | compliance | remote_strategy",
      "title": "string",
      "severity": "low | medium | high | critical",
      "blocking": true,
      "why_it_matters": "string",
      "evidence": [
        {
          "type": "path | pattern | git_history | command_result | structural_inference",
          "value": "string"
        }
      ],
      "recommended_action": "string"
    }
  ],
  "release_options": [
    {
      "id": "option_1",
      "rank": 1,
      "title": "string",
      "recommended": true,
      "summary": "string",
      "why_choose_this": "string",
      "tradeoffs": [
        "string"
      ],
      "residual_risks": [
        "string"
      ],
      "requires": [
        "working_tree_cleanup",
        "history_rewrite",
        "force_push",
        "repo_split",
        "release_artifact_generation"
      ],
      "publication_status_if_chosen": "ready_after_fixes | blocked_until_history_rewrite | private_only | not_recommended"
    }
  ],
  "proposed_execution_scope": {
    "will_change": [
      "string"
    ],
    "will_not_change": [
      "string"
    ],
    "needs_explicit_approval": [
      "string"
    ]
  },
  "next_step": {
    "type": "choose_option | clarify_boundary | approve_scope",
    "message": "string"
  }
}
````

---

## 3. Finding category definitions

Use exactly one primary category per finding.

### `privacy`

Personal identifiers, local paths, screenshots, usernames, emails, internal names.

### `secrets`

API keys, passwords, session values, private keys, embedded credentials.

### `real_data`

Actual datasets, exports, logs, caches, previews, analytics outputs, derived personal content.

### `git_history`

Sensitive or blocking content in commit history, even if absent now.

### `ignore_rules`

Incorrect, ambiguous, or misleading `.gitignore` behavior.

### `repo_hygiene`

Build artifacts, tracked temp files, missing release files, broken examples, local-only docs/scripts.

### `compliance`

Redistribution, license, asset-rights, or publication-rights uncertainty.

### `remote_strategy`

Remote divergence, publish flow confusion, push/pull/rebase risk.

---

## 4. Severity rules

### `low`

Non-blocking issue. Good to fix before release, but not a real gate by itself.

### `medium`

Important issue. Could create confusion or minor leakage risk. Usually should be fixed before release.

### `high`

Serious issue. Publication should generally pause until resolved.

### `critical`

Direct blocker. Example:

* real sensitive data in current tree
* history contains blocking private content
* secrets exposed
* remote strategy likely to corrupt intended publish state

---

## 5. Output type: `execution_plan`

Use this after the user chooses an option and before making changes.

### Required structure

```json
{
  "output_type": "execution_plan",
  "selected_option_id": "option_1",
  "goal": "string",
  "execution_scope": {
    "in_scope": [
      "string"
    ],
    "out_of_scope": [
      "string"
    ]
  },
  "planned_actions": [
    {
      "id": "action_1",
      "title": "string",
      "category": "working_tree_cleanup | ignore_fix | docs_sanitization | example_generation | release_artifact_generation | git_index_cleanup | history_rewrite_prep | remote_strategy_prep",
      "status": "needs_approval",
      "reason": "string",
      "expected_effect": "string",
      "reversible": true
    }
  ],
  "approval_required": [
    {
      "id": "approval_1",
      "action": "string",
      "why_approval_is_required": "string",
      "risk_if_done": "string"
    }
  ],
  "pre_execution_notes": [
    "string"
  ]
}
```

### Rule

If the chosen option includes history rewrite, force push, or remote replacement, those actions must appear under `approval_required`.

---

## 6. Output type: `execution_update`

Use this after some approved changes have been made, especially when pausing mid-way.

### Required structure

```json
{
  "output_type": "execution_update",
  "goal": "string",
  "progress_status": "partial | done",
  "completed_actions": [
    {
      "id": "action_1",
      "title": "string",
      "status": "done",
      "what_changed": [
        "string"
      ],
      "why": "string"
    }
  ],
  "remaining_actions": [
    {
      "id": "action_2",
      "title": "string",
      "status": "needs_approval | ok",
      "blocked_by": "string"
    }
  ],
  "open_decisions": [
    {
      "id": "decision_1",
      "question": "string",
      "options": [
        "string"
      ],
      "recommended": "string"
    }
  ],
  "current_risk_snapshot": {
    "risk_level": "medium",
    "top_remaining_blocker": "string"
  }
}
```

### Rule

Do not claim the repo is safe to publish from an `execution_update` unless a full final re-check has been completed.

---

## 7. Output type: `final_verdict`

Use this only after re-checking the repo following cleanup or after concluding no further safe progress can be made.

### Required structure

```json
{
  "output_type": "final_verdict",
  "verdict_label": "READY AFTER CURRENT-TREE FIXES",
  "risk_level": "medium",
  "final_summary": "string",
  "checks": {
    "current_tree_safe": {
      "status": "ok | warning | blocked",
      "note": "string"
    },
    "git_history_safe_for_public_release": {
      "status": "ok | warning | blocked",
      "note": "string"
    },
    "ignore_rules_correct": {
      "status": "ok | warning | blocked",
      "note": "string"
    },
    "examples_publishable": {
      "status": "ok | warning | blocked",
      "note": "string"
    },
    "remote_strategy_explicit": {
      "status": "ok | warning | blocked",
      "note": "string"
    }
  },
  "remaining_blockers": [
    "string"
  ],
  "approved_next_actions": [
    "string"
  ],
  "publish_recommendation": {
    "can_publish_publicly_now": false,
    "can_publish_privately_now": true,
    "recommended_next_step": "string"
  }
}
```

---

## 8. Output type: `clarification_needed`

Use this sparingly.
Only use it when a real ambiguity blocks safe judgment or safe execution.

### Allowed cases

* cannot tell whether example data is sanitized or real
* cannot tell whether a directory is intended to remain public
* cannot tell whether remote should be aligned or replaced
* cannot tell whether deletion would destroy valuable project assets

### Required structure

```json
{
  "output_type": "clarification_needed",
  "blocking_question": "string",
  "why_it_blocks_safe_progress": "string",
  "best_current_guess": "string",
  "safe_default_if_no_answer": "string"
}
```

### Rule

Do not ask broad, lazy questions.
Ask only when a specific ambiguity changes the safe action boundary.

---

## 9. Narrative rendering rules

Even if the agent internally follows the JSON-like schema above, the user-facing report should be rendered as readable prose.

### User-facing order for `audit_report`

1. Executive summary
2. Critical findings
3. Release options
4. Proposed execution scope
5. Approval-required actions
6. Next step

### User-facing order for `execution_plan`

1. Goal
2. Planned actions
3. What will not be touched
4. Approval-required actions
5. Execution boundary

### User-facing order for `execution_update`

1. What changed
2. Why it changed
3. What remains
4. What decision is still needed

### User-facing order for `final_verdict`

1. Final verdict
2. Gate results
3. Remaining blockers if any
4. Exact next step

---

## 10. Required honesty rules

The agent must not:

* label the repo publish-ready when Git history still blocks public release
* claim examples are safe without checking or stating uncertainty
* treat `.gitignore` cleanup as equivalent to history cleanup
* hide uncertainty about licensing or redistribution
* imply force push is harmless
* say “safe” when it only means “current working tree looks clean”

---

## 11. Minimal audit completeness rule

An `audit_report` is incomplete unless it includes all of these:

* at least one working-tree assessment
* at least one Git-history assessment
* at least one ignore-rule assessment
* at least one publish-strategy assessment
* a ranked options section
* one recommended option
* one explicit next step

If any of these is missing, the audit is not complete.

---

## 12. Minimal final-verdict rule

A `final_verdict` must not use `READY TO PUBLISH` unless all are true:

* current tree is safe enough for publication
* Git history has no unresolved blocking exposure
* ignore rules are correct
* example paths are publishable
* remote strategy is explicit
* required destructive actions were approved and completed

Otherwise use one of the weaker verdict labels.

---

## 13. Compact templates

### Compact audit template

```json
{
  "output_type": "audit_report",
  "executive_summary": {
    "verdict_label": "BLOCKED BY GIT HISTORY",
    "risk_level": "high",
    "top_blocker": "Real data was removed from the current tree but remains in Git history.",
    "recommended_option_id": "option_1",
    "summary": "The repo should not be made public yet. The current tree can likely be cleaned, but history remains a blocking exposure."
  },
  "findings": [],
  "release_options": [],
  "proposed_execution_scope": {
    "will_change": [],
    "will_not_change": [],
    "needs_explicit_approval": []
  },
  "next_step": {
    "type": "choose_option",
    "message": "Choose option 1 if you want me to prepare a history-rewrite-safe release path."
  }
}
```

### Compact final verdict template

```json
{
  "output_type": "final_verdict",
  "verdict_label": "READY AFTER CURRENT-TREE FIXES",
  "risk_level": "medium",
  "final_summary": "The current tree is clean enough after the approved fixes, but public release is still blocked until history is handled.",
  "checks": {
    "current_tree_safe": {
      "status": "ok",
      "note": "No blocking private files remain in the working tree."
    },
    "git_history_safe_for_public_release": {
      "status": "blocked",
      "note": "Sensitive historical commits still exist."
    },
    "ignore_rules_correct": {
      "status": "ok",
      "note": "Ignore behavior matches intended public/private boundaries."
    },
    "examples_publishable": {
      "status": "ok",
      "note": "Examples appear sanitized."
    },
    "remote_strategy_explicit": {
      "status": "warning",
      "note": "Publish strategy is known, but force-push approval is still pending."
    }
  },
  "remaining_blockers": [
    "Git history still contains blocking exposure."
  ],
  "approved_next_actions": [
    "Prepare a history rewrite plan.",
    "Review force-push approval before public release."
  ],
  "publish_recommendation": {
    "can_publish_publicly_now": false,
    "can_publish_privately_now": true,
    "recommended_next_step": "Keep the repo private until history is rewritten or the release plan changes."
  }
}
```

---

## 14. One-line schema rule

Always produce a verdict, evidence-backed findings, ranked options, an explicit execution boundary, and a final publish decision.
