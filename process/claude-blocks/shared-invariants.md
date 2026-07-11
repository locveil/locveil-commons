**Locveil shared process invariants** — digest; normative source: `../locveil-commons/process/`
(`ledger-discipline.md`, `claude-md.md`). On disagreement the process files win. Never edit
this block in place — edit in commons, then re-pin (`process/claude-md.md` §3).

- **ledger triad** — active ledger + DONE ledger + one rotating journal; completion MOVES
  the entry to DONE and journals it in the same change; rotation only via an explicit
  `scope_guard.py --rotate` in its own commit; watermarks + mechanics:
  `process/ledger-discipline.md`.
- **every-task-in-the-ledger** — no work without a ledger ID; a doc finding becomes scope
  only when a ledger task declares it.
- **task-start-reconciliation** — before executing any task, verify its claims against repo
  reality; narrow or redefine at intake rather than executing stale text.
- **design-then-implement** — non-trivial changes get a reviewed design doc before code.
- **review-then-remediate** — review findings become ledger tasks before they get fixed.
- **Enforcement** — vendored `scope_guard.py` at a pinned `scope-vX` tag + committed
  pre-commit hook + path-gated `ledger-guard` CI job; hooks and CI run `--check` only.
