# Board journal — newest on top

## 2026-07-11 — BUILD-21 commons bootstrap (PROD-2 restructure + PROD-3 board)

Owner had completed the rename chain (GitHub org `locveil`, repos `locveil-commons` /
`locveil-voice` / `locveil-bridge`, local dirs + remotes) and, earlier the same day, the
PROD-1 name lock (Locveil; .com/.ru registered, org claimed, .io dropped, .eu pending ID
verification). This session executed the commons side of voice BUILD-21:

- **D-2 restructure**: eval framework moved to `eval/` via `git mv` (package `eval_commons`,
  `shared/`, `examples/`, `tests/`, pyproject, uv.lock, ARCHITECTURE.md, its README);
  `board/`, `process/`, `packages/`, `site/` created. `contracts/` and `docs/design/` stay
  at root. Distribution renamed `eval-commons` → `locveil-eval` (import name unchanged);
  uv.lock regenerated; test `contracts/` anchors repointed (`parents[2]`). Suite green from
  the new home: 40 passed (`cd eval && uv run --all-extras --with pytest --with jsonschema
  pytest tests/ -q`).
- **Name sweep** of repo-owned files (code comments, examples, shared YAML, docs,
  contracts/README). NOT swept, by design: the pinned artifacts + `PIN.json` +
  `crossover_fixtures.json` (new names arrive with the next re-pin / fixture re-author) and
  the dated records (`productization_roadmap.md`, body of the migrated decision record).
- **PROD-3 board bootstrap**: `BOARD.md` (conventions + §3 seed backlog as PROD-1..11),
  this journal, new commons CLAUDE.md (session discipline, ownership regimes, tag scheme),
  root README rewritten as the umbrella; old README/ARCHITECTURE live on under `eval/`.
- **Decision record migrated**: `docs/design/productization.md` copied verbatim from
  `locveil-voice@92d1abd` with a migration + name-lock header; the voice-side pointer swap
  is delegated in PROD-2.

Open tails: PROD-2 delegations to voice (BUILD-21 tail: eval-ref re-point + pointer swap)
and bridge (first board-as-outbox delegation, ID pending write-back); `locveil.eu` owner
action in PROD-1.
