# OpenSource Release Guard — Checklists

This file provides compact operational checklists for pre-release auditing, cleanup, execution, and final release gating.

---

## 0. Fast rule

Before a repo becomes public:

- check the current working tree
- check Git history
- check ignore rules
- check remote / branch strategy
- rank release options
- execute only the approved path
- re-check before publishing

---

## 1. Pre-audit checklist

Use this before making any cleanup changes.

### Repo state snapshot
- [ ] Confirm current branch
- [ ] Record `git status --short`
- [ ] Record `git remote -v`
- [ ] Record `git branch -vv`
- [ ] Record recent commit graph
- [ ] Note staged files
- [ ] Note untracked files
- [ ] Identify top-level directories relevant to publication

### Publication intent
- [ ] Is the repo intended for a public GitHub remote?
- [ ] Is the user asking for full open-source release or partial code release?
- [ ] Is the repo mixed with data, exports, logs, previews, or personal artifacts?
- [ ] Is there any sign the repo was originally private/local-first?

### Safety boundary
- [ ] Do not modify files yet
- [ ] Do not sync branches yet
- [ ] Do not publish yet
- [ ] Do not recommend force push or history rewrite yet

---

## 2. Current working tree audit checklist

Use this to evaluate what is unsafe **right now**.

### Privacy / identity
- [ ] Real username found?
- [ ] Personal email found?
- [ ] Phone number found?
- [ ] Absolute local paths found?
- [ ] Hostname / machine name found?
- [ ] School / company / team internal identifiers found?
- [ ] Screenshots or media with visible personal/internal info found?

### Secrets / credentials
- [ ] API key found?
- [ ] Token found?
- [ ] Password found?
- [ ] Cookie or session value found?
- [ ] Private key found?
- [ ] `.env` or secret config file present?
- [ ] Secret-looking values embedded in source or docs?

### Real data / derived data
- [ ] Raw data files present?
- [ ] JSONL / CSV / SQLite / DB / parquet present?
- [ ] Exported personal content present?
- [ ] Logs / analytics / previews / caches present?
- [ ] Embeddings or generated artifacts from real user content present?
- [ ] “examples” directory may still contain real data?

### Repo hygiene
- [ ] `.gitignore` exists?
- [ ] `.gitignore` rules look precise rather than broad/ambiguous?
- [ ] `.gitkeep` needed anywhere?
- [ ] Build artifacts tracked?
- [ ] Cache/temp files tracked?
- [ ] README mentions private local setup?
- [ ] Tests depend on non-public data?
- [ ] Scripts assume local-only private folders exist?

---

## 3. Git history audit checklist

Use this to evaluate whether the repo is safe to publish **historically**, not just currently.

### Sensitive history
- [ ] Previously committed real data?
- [ ] Previously committed exports or stores?
- [ ] Previously committed secrets?
- [ ] Previously committed personal identifiers?
- [ ] Previously committed screenshots/media with sensitive info?
- [ ] Sensitive files later deleted but still visible in history?

### Tracking confusion
- [ ] Files now ignored but historically tracked?
- [ ] Paths renamed to hide prior sensitive content?
- [ ] Example directories created after real data was already committed?
- [ ] Current tree appears clean only because risky files moved or were deleted?

### Publication blocker decision
- [ ] Does history contain material blocking risk?
- [ ] If yes, is history rewrite required before public release?
- [ ] If no, can cleanup remain limited to current tree?

---

## 4. Ignore rule checklist

Use this after inspecting `.gitignore`.

### Rule correctness
- [ ] Root-only directories use root-anchored rules when needed?
- [ ] Nested example directories are not accidentally ignored?
- [ ] Allow-rules are explicit when examples must remain committed?
- [ ] Ignore patterns are not overly broad?
- [ ] Ignore behavior has been verified, not assumed?

### Tracking reality
- [ ] Are dangerous files merely ignored, or actually untracked?
- [ ] Are already tracked files still in Git index?
- [ ] Do example files that should be committed remain visible to Git?

### Outcome
- [ ] Ignore rules protect real/private content
- [ ] Ignore rules do not hide intended public examples
- [ ] Ignore rules match actual repo layout

---

## 5. Remote / branch strategy checklist

Use this before any pull, rebase, merge, or push.

### Remote state
- [ ] Does the remote already contain commits?
- [ ] Is local ahead / behind / diverged?
- [ ] Is remote history known to have been force-updated?
- [ ] Is the current branch the correct publication branch?
- [ ] Is the user trying to replace a prior remote or first-publish a repo?

### Decision discipline
- [ ] Do not recommend blind `pull --rebase`
- [ ] Do not recommend blind force push
- [ ] Inspect graph before choosing strategy
- [ ] State clearly whether the plan is:
  - [ ] align to remote
  - [ ] overwrite remote
  - [ ] merge histories
  - [ ] keep private for now

### Approval boundary
- [ ] If force push is needed, require explicit approval
- [ ] If history rewrite is needed, require explicit approval
- [ ] If remote replacement is needed, require explicit approval

---

## 6. Release-readiness classification checklist

Choose exactly one.

- [ ] **READY TO PUBLISH**
- [ ] **READY AFTER CURRENT-TREE FIXES**
- [ ] **BLOCKED BY GIT HISTORY**
- [ ] **RECOMMEND SPLIT PUBLIC/PRIVATE REPO**
- [ ] **NOT READY TO OPEN-SOURCE**

Use the strongest justified classification.

---

## 7. Ranked options checklist

Every report must provide ranked options.

### Option quality
- [ ] Recommended option is listed first
- [ ] Each option explains why someone would choose it
- [ ] Each option explains tradeoffs
- [ ] Each option explains residual risk
- [ ] Each option states whether it blocks publication now

### Typical options
- [ ] Cleanup current tree, then publish
- [ ] Rewrite history, then publish
- [ ] Split into public/private repos
- [ ] Publish code only; remove data/examples
- [ ] Keep private for now

---

## 8. Execution planning checklist

Use this only after the audit report is complete.

### Can execute after user approval
- [ ] Update `.gitignore`
- [ ] Add `.gitkeep`
- [ ] Sanitize docs/tests/config/scripts
- [ ] Move/remove private files from working tree
- [ ] Replace real data with example templates
- [ ] Add release support files
- [ ] Add pre-push checks
- [ ] Add CI checks
- [ ] Remove tracked files from Git index

### Must require explicit confirmation
- [ ] Rewrite Git history
- [ ] Force push
- [ ] Change remotes
- [ ] Delete ambiguous files permanently
- [ ] Remove content whose value is unclear
- [ ] Publish the repository publicly

---

## 9. Cleanup execution checklist

Use this while implementing the chosen path.

### Working tree cleanup
- [ ] Remove or relocate real/private data
- [ ] Replace real data with sanitized examples or templates
- [ ] Remove personal identifiers from docs/tests/config
- [ ] Remove secrets from tracked files
- [ ] Fix `.gitignore`
- [ ] Add `.gitkeep` where empty structure should remain

### Release-prep artifacts
- [ ] Add or update `LICENSE`
- [ ] Add or update `SECURITY.md`
- [ ] Add or update `CONTRIBUTING.md`
- [ ] Add `.env.example` if relevant
- [ ] Add release checklist if useful
- [ ] Add privacy / release scanning hook or CI if useful

### Scope control
- [ ] Only make changes within approved scope
- [ ] Avoid unrelated refactors
- [ ] Prefer reversible edits
- [ ] Pause at major decision boundaries

---

## 10. Final re-check checklist

Run this after cleanup and before publishing.

### Current tree
- [ ] No blocking sensitive files remain
- [ ] No blocking secrets remain
- [ ] No blocking personal identifiers remain
- [ ] Example files are actually safe examples
- [ ] Staged files match intended publication surface

### History
- [ ] No unresolved history blocker remains for intended public release
- [ ] If history blocker remains, repo is not approved for public release
- [ ] If no history rewrite was done, explain why it is still acceptable

### Ignore behavior
- [ ] Ignore rules match intended behavior
- [ ] Protected paths stay untracked
- [ ] Intended public example paths remain tracked

### Remote strategy
- [ ] Push strategy is known
- [ ] No blind sync action remains
- [ ] Any force push need has explicit approval

### Verdict
- [ ] Final verdict issued
- [ ] Remaining blockers listed clearly
- [ ] User knows exact next step

---

## 11. Minimal publish gate

A repo must not be called publish-ready unless all are true:

- [ ] current tree has no blocking sensitive content
- [ ] Git history has no unresolved blocking exposure
- [ ] ignore rules behave correctly
- [ ] example data is actually safe
- [ ] release surface is understandable
- [ ] remote strategy is explicit
- [ ] required destructive actions were separately approved

If any of the above is false, do not label the repo ready for public release.