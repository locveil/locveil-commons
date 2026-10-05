**Locveil contract triad** — digest; normative: `../locveil-commons/process/contracts.md`
(§2–§5; HK-5, HK-12, HK-13) + `process/ledger-discipline.md` §7. On disagreement those
files win. Never edit this block in place — edit in commons, then re-pin
(`process/claude-md.md` §3).

- **surface-with-the-artifact** — creating or bumping a versioned surface cuts its owned
  `contracts/<name>/` STAMP + tag + registry row in the SAME change. Every STAMP declares
  `artifacts` — what consumers pin AND what is byte-locked (empty only with a `guard`
  pointer; never a `README.md`); an enumerated file, or the STAMP itself, edited without
  a version move fails at commit.
- **three-level versions** — tags are `<family>-vX.Y.Z`: major = breaking, minor = the
  surface changed, patch = bytes only; runtime-served versions carry the major only.
- **pins-complete-and-verbatim** — a pin = exactly the owner's enumerated set at the tag,
  flat and byte-identical, + owner STAMP verbatim + strict PIN.json; only `PIN.json` and
  `README.md` in a pin folder are the consumer's. It moves ONLY by a deliberate re-pin
  ledger task (vendored repin derives the set from the owner's STAMP) — never
  hand-edits, never auto-fetch.
- **contracts-verdict** — every completion entry records `contracts: <what moved>` or
  `contracts: none — <why>`; "moved" = created, bumped, or FIRST CONSUMED a cross-repo
  surface; owner-side bumps add `re-pin owed: <consumers>`.
- **enforcement (§4–§5)** — contract-guard and repin run in the hook and on EVERY push,
  no path gate (the ledger guard keeps its own); layer-2 tests run when contracts move; pre-commit staleness only warns; push CI fails
  on a major gap or touch-the-family, release/dispatch gates on minor-or-major; the
  `.repin.toml` `[[tool]]` manifest pins vendored tools by tag + sha256.
