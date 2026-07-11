# New-repo template (HK-2 / PROD-5 — `process/claude-md.md` §5)

The canonical starting point for a new Locveil repo's process scaffolding. The
bootstrapping task (satellite: voice BUILD-22) INSTANTIATES this — never freehands.
Discipline is seeded, not retrofitted.

## Instantiation checklist

1. Copy `CLAUDE.md` to the repo root; fill every `{{PLACEHOLDER}}`; write the repo-local
   LAW sections (never inside the marker blocks).
2. Copy `docs/` skeletons (`LEDGER.md`, `LEDGER_DONE.md`, `JOURNAL.md`) — rename freely
   (naming is config), keep the shapes.
3. Vendor the guard at the current tag and copy the config + hook:
   ```
   git -C ../locveil-commons show scope-v3:packages/scope-guard/scope_guard.py > scripts/scope_guard.py
   cp scope-guard.toml ../<new-repo>/.scope-guard.toml     # then edit paths/prefixes
   cp hooks/pre-commit ../<new-repo>/hooks/pre-commit && chmod +x
   git config core.hooksPath hooks
   ```
4. Set the block hashes: `python3 scripts/scope_guard.py --hash-blocks` → paste into
   `.scope-guard.toml` `[claude]`.
5. Copy `ledger-guard.yml` into `.github/workflows/` and adjust the path filters to the
   chosen file names (convention: `ledger-discipline.md` §4).
6. First commit must pass the hook. If it doesn't, the instantiation is wrong — fix it,
   don't bypass.
