# Ledger & journal discipline — normative convention (HK-1 / PROD-13)

Decided by the first council session (HK-1, 2026-07-11; dossier ephemeral, this file and
`board/BOARD.md` are the record). Applies to **every Locveil repo**: locveil-voice,
locveil-bridge, locveil-commons, and locveil-satellite when it exists. Per-repo CLAUDE.md
invariant text implements this convention; where they disagree, this file wins (until the
PROD-5 drift guard automates the alignment).

## 1. The ledger triad

Every repo keeps:

1. **Active ledger + DONE ledger** (`single-task-ledger`): one logical ledger in two
   files — active (open `[ ]` / in-progress `[>]` / paused `[~]` tasks) and DONE (completed
   `[x]`). Every task ID is declared in **exactly one** file. Completion **moves** the
   entry to DONE in the same change as its journal entry — never flips `[x]` in place.
   Where the ledger uses workstream sections, a task's prefix must match its section and
   IDs ascend within a section (sorted insert, never append).
2. **One active journal** (`one-active-journal`): newest-on-top dated sections; frozen
   archives under an archive directory with a pointer in the journal header. Archives are
   history — never re-edited.
3. **Record-at-completion**: every ID newly moved to DONE has a journal entry mentioning
   it, in the same change.

## 2. Rotation (journal AND DONE ledger)

- **Watermarks** (lines; per-repo config, these are the defaults):
  journal **high ~1500 / low ~1000 / hard ceiling ~2000**;
  DONE ledger **high ~3000 / low ~2000 / hard ceiling ~4000**.
- Journal rotation freezes the **oldest whole dated sections** (never split a day) into
  `<archive_dir>/<first-date>_<last-date>.md` until at or under low-water, and updates the
  header pointer. DONE-ledger rotation moves the **lowest-numbered completed entries per
  workstream section** into a sequential archive file the same way.
- **ID-resolution guarantee (hard rule):** rotated ledger archives remain part of the
  checker's known-ID set — scope-guard scans the ledger archive directory for declarations.
  A rotation that makes old IDs unresolvable (false ORPHANs, broken
  `task-start-reconciliation`) is a defect.
- Rotation is executed **only** by an explicit `scope_guard.py --rotate` run, deterministic,
  in its own commit. Hooks and CI never mutate the tree.

## 3. The shared tool: scope-guard

- Lives at `packages/scope-guard/` in locveil-commons (regime 2). Distribution
  **`locveil-scope-guard`**, single stdlib-only file `scope_guard.py`, tags **`scope-vX`**.
- Consumption is **pinned**: each product repo vendors `scope_guard.py` at a tagged version
  (the version stamp is in the file) plus its own `.scope-guard.toml`. A rule change in
  commons never moves a consumer until it re-pins. Behavior changes happen here, never in
  the consumers (eval-framework precedent).
- **Rule set = the union** of the historical voice + bridge checkers, config-toggled:
  DUPLICATE id · MISPLACED status (two-directional) · ORPHAN finding · DEAD evidence link
  (with voice's evidence-index `[x]` exists-marker semantics) · ALIAS phantom · MISFILED
  task · OUT-OF-ORDER id · UNINDEXED review · tombstone handling — plus the HK-1 additions:
  journal & DONE watermark checks · archive-pointer integrity · completion-journal
  cross-check · required-task-tags (per-repo list) · board rule pack (commons).
- Everything repo-specific is config: file paths, prefixes, status chars, section style,
  optional rules. **File naming stays as-is per repo** — a rename is a config edit, and
  none is required (HK-1 q6: drop).

## 4. Enforcement

- **Pre-commit hook** in every repo runs `scope_guard.py --check` (stdlib-only,
  sub-second). Hook distribution: committed `hooks/` directory + one-time
  `git config core.hooksPath hooks`.
- **CI**: a path-gated `ledger-guard` job (docs/ledger paths + the vendored script + config)
  runs `--check`. Over journal/DONE **high-water → warning**; over **hard ceiling → fail**.
  All other rule violations fail.
- **CI convention (HK-2):** the job is named exactly `ledger-guard`; path filters cover the
  ledger/journal/docs paths, `CLAUDE.md` (the pinned blocks), the vendored
  `scope_guard.py`, `.scope-guard.toml`, and the workflow file itself. Template:
  `process/new-repo-template/ledger-guard.yml` — new repos copy, never reinvent.
- Cutover proof (per repo, before deleting its local checker): the vendored scope-guard
  runs green against the repo's current tree.

## 5. Board specifics (commons)

- The board ledger is `board/BOARD.md` (active) + `board/BOARD_DONE.md` (completed
  entries moved on close). Prefixes: `PROD` (cross-repo initiatives), `HK`
  (housekeeping/council topics), and `IMPL` (implementation work genuinely on commons —
  regime-2/3 code under `packages/`, `site/`, `eval/` — that is not itself a cross-repo
  initiative; decided HK-10, 2026-07-14). **Entries live under per-prefix sections**
  (`## PROD — …`, `## HK — …`), sorted-insert within — the same shape as the product
  ledgers; a flat interleaved list is not acceptable (owner finding 2026-07-11; commons
  config runs `require_sections` + `sections_required_for_all` accordingly).
- **HK-N**: a council topic gets an HK id at seed time (unless seeded from a PROD entry),
  is journaled, and — being born-decided — its entry is filed **directly into
  `BOARD_DONE.md`** when the council lands. A deferred council parks the HK entry in the
  active board.
- Board rule pack (machine-checked subset): the triad checks, plus — a closed entry whose
  text contains a `Delegation →` block must carry a written-back local ID. The wider rule
  — **the board never asserts a delegated task's status** — remains prose (per-repo
  ledgers own status).

## 6. Evidence anchoring (design + review docs) — HK-10

- **Every design doc and every review doc must be referenced by at least one ledger
  entry** (active or DONE) — an unreferenced evidence doc is forgotten scope (owner
  ruling, 2026-07-14). Sharper form: a doc whose scope is **not fully executed** must be
  referenced by an **open** task; a fully-executed doc is anchored by the completion
  entries that cite it (a record, not work).
- The rule is org-wide. The product repos already run pieces of it (voice's evidence
  index with `[x]` exists-markers, bridge's path-scan dead-link checks) — but those
  guard the ledger→doc direction. The missing direction — **a doc ON DISK that no
  ledger entry references** — becomes a scope-guard check (`UNREFERENCED evidence`,
  config-toggled) at the next `scope-vX` cut (commons **IMPL-2**); consumers adopt it
  when they re-pin, per §3 pinned-consumption rules.
- Evidence directories are config (`[evidence] dirs`); commons scans `docs/design/` +
  `docs/review/`.
