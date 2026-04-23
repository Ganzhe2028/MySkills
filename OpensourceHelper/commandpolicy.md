# OpenSource Release Guard — Command Policy

This file defines how the agent should use shell and Git commands while auditing and preparing a repository for open-source release.

The goal is not speed at all costs.  
The goal is safe, reviewable, minimal-scope execution.

---

## 0. Operating rule

Read first.  
Classify second.  
Plan third.  
Execute only the approved path.  
Re-check before publish.

---

## 1. Default mode

Start in **read-only audit mode**.

Until the audit report is finished, the agent must not:
- delete files
- move files
- edit tracked files
- change Git history
- sync branches
- push anything
- publish anything

The agent may inspect, search, classify, and prepare a plan.

---

## 2. Command safety levels

Every command falls into one of four levels.

### Level A — Read-only audit
Safe by default during audit.

Examples:
- file listing
- searching text
- reading config/docs/scripts
- inspecting Git status
- inspecting Git history
- checking ignore behavior
- generating a report

### Level B — Low-risk working tree preparation
Allowed only after the user approves the chosen cleanup path.

Examples:
- editing `.gitignore`
- adding `.gitkeep`
- creating `LICENSE`, `SECURITY.md`, `.env.example`
- sanitizing docs/tests/config
- adding hooks or CI config
- moving/removing current working-tree files
- `git rm --cached` on approved targets

### Level C — High-impact repo state changes
Require explicit user confirmation.

Examples:
- history rewrite
- branch reset
- remote changes
- rebase with publication impact
- merge intended to resolve remote divergence
- deleting ambiguous or high-value files

### Level D — Dangerous publication actions
Require explicit user confirmation every time.

Examples:
- any force push
- publishing to public remote
- remote replacement
- irreversible deletion with no clear recovery path

---

## 3. Allowed commands in audit mode

The agent may use commands like these during audit:

### File and text inspection
- `ls`
- `find`
- `rg`
- `grep`
- `cat`
- `sed -n`
- `head`
- `tail`

### Git inspection
- `git status --short`
- `git remote -v`
- `git branch -vv`
- `git log --oneline --graph --decorate -n <N>`
- `git log --name-only -- <path>`
- `git ls-files`
- `git diff --staged --name-only`
- `git diff --name-only`
- `git check-ignore -v <path>`
- `git reflog` for understanding state only

### Interpretation rule
Do not paste raw command output without explanation.  
Each command result must be interpreted in terms of release risk.

---

## 4. Allowed commands after cleanup path approval

Once the user approves a scoped plan, the agent may perform low-risk working-tree preparation.

Typical allowed actions:
- edit `.gitignore`
- add `.gitkeep`
- create safe template/example files
- sanitize docs/config/tests
- remove tracked private files from index
- create release support files
- add a pre-push hook or CI workflow

Typical commands may include:
- file creation/edit commands
- `mkdir -p`
- `mv`
- `cp`
- `rm` for clearly approved targets
- `git rm --cached <path>`
- `git add <approved paths>`

### Scope rule
Only touch files within approved scope.  
Do not refactor unrelated code.  
Do not “clean up while here.”

---

## 5. Commands requiring explicit confirmation

The agent must stop and get explicit approval before running commands in these categories.

### History rewrite
Examples:
- `git filter-repo`
- BFG Repo-Cleaner
- interactive rebase for cleanup
- orphan branch reconstruction meant to replace published history

### Branch state rewrite
Examples:
- `git reset --hard`
- destructive checkout operations
- resetting branch pointers to older commits

### Remote-impacting sync actions
Examples:
- `git push --force`
- `git push --force-with-lease`
- remote replacement or deletion
- pushing rewritten history
- pull/rebase/merge intended to resolve publish-state divergence

### Destructive deletion
Examples:
- deleting ambiguous directories
- deleting files the user may still need privately
- deleting media/data whose value is not obvious

---

## 6. Force-push policy

The agent must never treat force push as routine.

If force push is under consideration:
1. explain why it is needed
2. explain what commit range or branch state would be replaced
3. explain the risk to collaborators
4. prefer `--force-with-lease` over raw `--force`
5. require explicit approval before execution

If the repository is shared, also recommend a coordination note for collaborators.

---

## 7. Pull / rebase / merge policy

Never recommend blind sync commands.

Before suggesting `pull`, `rebase`, or `merge`, the agent must first inspect:
- current branch
- remote branch state
- local/remote divergence
- whether remote history was force-updated
- whether the user intends to align to remote or replace remote

### Required reasoning
The agent must state which of these strategies it is choosing:
- align local to remote
- overwrite remote with local
- merge histories
- postpone sync until cleanup is complete

### Forbidden behavior
Do not recommend `git pull --rebase` just because push was rejected.

---

## 8. `.gitignore` policy

The agent must never assume ignore rules are correct by appearance alone.

Required steps:
1. inspect ignore patterns
2. reason about whether patterns are root-anchored or broad
3. verify match behavior on important paths
4. distinguish ignored files from tracked files
5. explain whether example paths are accidentally excluded

### Key rule
Ignoring a file is not equivalent to making it safe.

If a sensitive file was already tracked, the agent must say so clearly and handle it as:
- index cleanup, and/or
- history cleanup

---

## 9. History-risk policy

If Git history contains real data, personal identifiers, or secrets, the repo must not be labeled safe for public release unless one of the following is true:

- the risky history is rewritten, or
- the repo will remain private, or
- the user explicitly accepts the risk and the agent clearly states that public release is blocked by history

### Required language
When this condition is met, the agent must classify the repo as either:
- **BLOCKED BY GIT HISTORY**
- **NOT READY TO OPEN-SOURCE**

Do not soften this into a vague caution.

---

## 10. Deletion policy

The agent should prefer these actions in order:

1. move private content out of the repo
2. replace with template/example
3. remove from Git index
4. delete from working tree only if clearly approved
5. rewrite history only if needed and approved

### Ambiguity rule
If a file may be sensitive but may also be valuable, do not delete it automatically.  
Surface it in the report and ask for a choice.

---

## 11. Artifact-generation policy

When preparing a repo for open-source release, the agent may generate artifacts such as:
- `.gitignore`
- `.gitkeep`
- `.env.example`
- `LICENSE`
- `SECURITY.md`
- `CONTRIBUTING.md`
- release checklist
- pre-push hook
- CI scan workflow

Rules:
- generate only artifacts relevant to the chosen release path
- keep content minimal and practical
- do not create ceremonial files with no actual use
- do not claim compliance guarantees the files cannot provide

---

## 12. Reporting policy

Every action-taking phase must be preceded by a decision-quality report.

The report must include:
- current verdict
- blockers
- ranked options
- recommended option
- exact proposed execution scope
- actions requiring explicit approval

After execution, the agent must provide:
- what changed
- why it changed
- what was intentionally left unchanged
- what still blocks publication, if anything
- final release verdict

---

## 13. Minimal approval protocol

Explicit confirmation is required before:
- rewriting history
- force pushing
- changing remotes
- destructive reset
- deleting ambiguous private data
- public publication

Valid confirmation should be tied to a concrete option or action set, for example:
- approve option 1
- approve history rewrite plan
- approve working-tree cleanup only
- approve force push with lease

Vague urgency is not approval.

---

## 14. Final gate rule

The agent must not say a repo is ready for public release unless all of the following are true:

- current tree is clean enough for publication
- history has no unresolved blocking exposure
- ignore behavior is correct
- examples are truly publishable
- remote strategy is explicit
- required destructive operations were approved
- final re-check was completed

If any of the above is false, publication is still blocked or conditional.

---

## 15. One-line summary

Inspect deeply, classify honestly, modify minimally, and never let convenience override publication safety.