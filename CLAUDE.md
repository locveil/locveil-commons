# locveil-commons — agent notes

The **Locveil umbrella repo** — the neutral, co-owned ground between the product repos
`../locveil-voice` (Irene, the voice assistant), `../locveil-bridge` (the smart-home
bridge), and `locveil-satellite` (pending, BUILD-22). The joint product: a fully local,
privacy-first, Russian-first voice-controlled smart home. Decision record:
`docs/design/productization.md` (D-1..D-12); initiative ledger: `board/BOARD.md`.

## Cross-repo sessions (D-4/D-5)

- **Cross-repo idea sessions run FROM this repo.** Load sibling context as needed — the
  products' `CLAUDE.md`, ledgers, and design docs live in `../locveil-voice` and
  `../locveil-bridge`. A cross-repo idea = a `PROD-N` task in `board/BOARD.md`; the
  deliverable is a design doc. Session notes go to `board/JOURNAL.md` (newest on top).
- **Placement rule:** a design defining a concept/contract both products consume lives in
  `docs/design/` here; a design whose primary artifact is one repo's code lives in that
  repo's `docs/design/`, even when the session ran here.
- **Board-as-outbox:** a completed PROD task delegates by committing the delegation text in
  its board entry; the receiving repo pulls it, verifies per its own
  `task-start-reconciliation`, files a local ID, and writes the ID back. The board lists
  delegated IDs but **never asserts their status** — per-repo ledgers own status.
- **The council (`/council`, PROD-12):** cross-repo topics with real stakes run as a
  moderated discussion — per-repo keeper subagents argue their repo's interests on a dossier
  artifact, the owner decides via the page's Copy-delta paste-back. Convention (normative):
  `process/council.md`. Decisions land exactly as terminal decisions would — on the board.
  **`hk-ids-from-the-board`:** a non-PROD-seeded topic gets the next free `HK-N` counted
  from the board ledgers (`**HK-N**` declarations in `BOARD.md` + `BOARD_DONE.md` — never
  journal headings or dossier files); HK entries are born-decided and file directly into
  `BOARD_DONE.md` (deferred → parks in `BOARD.md`). `ledger-discipline.md` §5.

## Layout & ownership regimes (D-2/D-3)

`board/` + `process/` + `site/` = regime 3 (commons owns process/product artifacts).
**Ledger discipline (HK-1/PROD-13, normative `process/ledger-discipline.md`):** `BOARD.md`
is the active ledger, completed entries MOVE to `BOARD_DONE.md`; scope-guard
(`packages/scope-guard/`, config `.scope-guard.toml`) enforces it — pre-commit hook
(`hooks/`, `core.hooksPath`) + `ledger-guard` CI, both `--check`-only; rotation only via
explicit `--rotate` in its own commit. Products vendor the script at `scope-vX` tags.
`eval/` + `packages/` = regime 2 (commons owns shared code; products pin versions; rule of
two for new extractions). `contracts/` = regime 1 (product-owned generated artifacts;
commons holds only pins). Packages version independently via prefixed tags — `eval-vX`,
`core-py-vX`, `ui-kit-vX` — each with its own `pyproject.toml`/`package.json`. **Never
publish a bare `locveil` package — always `locveil-*`.**

## Source-of-truth rules

- **The WebSocket wire protocol is defined by `../locveil-voice/docs/guides/websocket-api.md`**
  (that repo's `ws-protocol-doc-canonical` invariant). `eval/eval_commons/providers/
  ws_audio_provider.py` and any other WS client here IMPLEMENT that document — when provider
  behavior disagrees with it, the document wins; when the protocol gains a field (e.g.
  `wants_trace`, default `false`), this repo needs no change unless a test wants the new
  capability. Never reverse-engineer the protocol from server code or from this repo's own
  providers; read the document.
- **`contracts/` is a one-way inward pin owned by locveil-voice** (its re-pin tasks stamp
  `PIN.json`): a version-stamped copy of `../locveil-bridge`'s committed contract artifacts
  (catalog golden, STAMP, openapi) plus the co-owned `crossover_fixtures.json`. Never
  hand-edit the pin contents (`catalog.golden.json`, `openapi.json`, `STAMP.json`,
  `PIN.json`, `crossover_fixtures.json`) and never treat them as a source — they move via
  voice re-pin / fixture tasks; old repo names inside them are expected until the next
  re-pin. `contracts/README.md` is this repo's own documentation.

## The eval framework (`eval/`)

The shared, YAML-first test/eval framework (promptfoo providers, scorers, DeepSeek judge)
for both product repos. Consumers carry only YAML + a thin Makefile; **all execution logic
lives here** — behavior changes happen in this repo, not in the consumers. Distribution
`locveil-eval`; import package stays `eval_commons`; tag `eval-vX`.

- Consumers run suites via `make` from their own `eval/` directories (they wire the `uv`
  venv + global `promptfoo`) and reference this repo as `../../locveil-commons/eval/...`
  (`file://` paths) / `pip install -e ../locveil-commons/eval`.
- This repo's own tests:
  `cd eval && uv run --all-extras --with pytest --with jsonschema pytest tests/ -q`
  (the extras supply numpy/soxr for the audio-conform tests).
- promptfoo env references are `{{env.VAR}}`, not `${VAR}`.
- Tests parameterize over TARGET (local vs the WB7 controller) and CONFIG via the consumers'
  profile env files — never bake an endpoint or config into execution logic here.

## Shared blocks (pinned — `process/claude-md.md`; edit the sources in `process/claude-blocks/`, then re-pin)

<!-- locveil:begin shared-invariants scope-v3 -->
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
<!-- locveil:end shared-invariants -->

<!-- locveil:begin cross-repo-board scope-v3 -->
**Locveil cross-repo: the board.** The repos are SIBLINGS on disk — `../locveil-commons`
(umbrella: board, `process/`, shared packages), `../locveil-voice`, `../locveil-bridge`.
Cross-repo initiatives live at `../locveil-commons/board/BOARD.md` (`PROD-N`; council
topics `HK-N`; completed entries in `BOARD_DONE.md`). Delegations arrive as board-as-outbox
text committed inside a PROD entry: pull it, verify per `task-start-reconciliation`, file
it under a LOCAL task ID, execute locally, then write that ID back into the board entry.
The board never asserts a delegated task's status — this repo's ledger owns it. Direct
operational filings between product repos (bug reports, contract requests) stay
repo-to-repo and don't need the board. Cross-repo design sessions and the council run FROM
locveil-commons (convention: `../locveil-commons/process/council.md`); decisions land on
the board, never in chat.
<!-- locveil:end cross-repo-board -->
