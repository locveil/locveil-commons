**Locveil contract triad** — digest; normative: `../locveil-commons/process/contracts.md`
(§2–§5) + `process/ledger-discipline.md` §7 (HK-12). On disagreement those files win.
Never edit this block in place — edit in commons, then re-pin (`process/claude-md.md` §3).

- **surface-with-the-artifact** — creating or bumping a versioned surface cuts its owned
  `contracts/<name>/` STAMP + `<family>-vN` tag + registry row in the SAME change; new
  stamps enumerate `artifacts`; an enumerated artifact edited without a version move
  fails at commit (contract-guard v3 CONTENT-DRIFT/ORPHAN-TAG).
- **pins-complete-and-verbatim** — a pin = the owner's full tagged artifact set,
  byte-identical + owner STAMP verbatim + strict PIN.json; it moves ONLY by a deliberate
  re-pin ledger task (the vendored repin tool) — never hand-edits, never auto-fetch.
- **contracts-verdict** — every completion entry records `contracts: <what moved>` or
  `contracts: none — <why>`; "moved" = created, bumped, or FIRST CONSUMED a cross-repo
  surface; owner-side bumps add `re-pin owed: <consumers>`.
- **staleness ladder (§5)** — pre-commit `repin --check` warns (offline-safe, tokenless
  remote-first); push CI fails only on touch-the-family / release workflows / major-gap
  (per-repo config); the `.repin.toml` `[[tool]]` manifest watches vendored guard tags.
