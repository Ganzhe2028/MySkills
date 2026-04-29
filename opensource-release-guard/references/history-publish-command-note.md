# History Publish Command Note

This file used to contain only:

```bash
git push -f -u origin main
```

Treat that command as a high-impact publication action, not a reusable script.

Run a force push only after:

- the audit has identified why rewritten history must replace the remote
- the exact branch and commit range are understood
- collaborators and existing remote state have been considered
- the user has explicitly approved the action

Prefer `--force-with-lease` over raw `--force` when force push is approved.
