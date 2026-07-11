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
