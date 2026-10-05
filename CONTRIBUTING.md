# Contributing to locveil-commons

The umbrella repo of the Locveil org — the neutral, co-owned ground between
`locveil-voice`, `locveil-bridge`, and `locveil-satellite`. Contributions here are
mostly *process and shared machinery*; product code belongs in the product repos.

## Orientation

- **What lives where:** `board/` — the cross-repo initiative ledger (PROD/HK) and
  journal; `process/` — the normative org conventions; `packages/` — shared tooling the
  products vendor at pinned tags; `contracts/` — the contract registry (owned surfaces +
  consumed pins); `eval/` — the shared test/eval framework; `site/` — the future landing
  page.
- **The repos are siblings on disk.** Cross-repo work flows through the board
  (board-as-outbox), never through direct writes into a sibling's tree.

## The rules that bind every change

- **Ledger discipline** — no work without a ledger ID; completions move to the DONE
  ledger with a journal entry in the same change, carrying a `docs:` verdict line.
  Normative: [`process/ledger-discipline.md`](process/ledger-discipline.md).
- **Contracts** — uniform layout, complete pins, two-layer enforcement. Normative:
  [`process/contracts.md`](process/contracts.md); registry:
  [`contracts/README.md`](contracts/README.md). Never hand-edit a pin.
- **User-facing docs** — the manifest ([`docs/manifest.json`](docs/manifest.json)) is
  the scope of record; style + rule: [`process/user-docs.md`](process/user-docs.md).
- **The council** — cross-repo decisions with real stakes:
  [`process/council.md`](process/council.md).
- **Sprints** — planning in owner-session capacity with the shippable-at-sprint-end
  invariant; the sprint file (`board/sprints/`) lists IDs and never asserts status.
  Normative: [`process/sprints.md`](process/sprints.md).
- **Python layout & naming** — src-layout, config/docker at root, locveil_* backend
  imports: [`process/python-layout.md`](process/python-layout.md) (binds product repos
  and new packages; the eval framework and single-file guards are ruled exempt).

## Dev setup & gates

- Python ≥ 3.11, [`uv`](https://github.com/astral-sh/uv). Eval framework tests:
  `cd eval && uv run --extra record --extra dev pytest tests/ -q`; tool suites:
  `cd packages/contract-guard && uv run --no-project --with pytest python -m pytest tests -q`
  (same for `packages/repin`).
- Hooks: `git config core.hooksPath hooks` — runs scope-guard + contract-guard
  (`--check` only) and a warn-only `repin --check`. CI: `ledger-guard` (path-gated) and
  `contract-guard`, which runs on EVERY push with no path gate — layer 1 (guard strict +
  repin staleness with touch-the-family) and layer 2 (the eval suite and both tool
  suites). A contract edit that skips its version move, or a pin that trails while you
  touch it, fails there.
- Cutting a contract (`process/contracts.md` §2–§3): artifact + `STAMP.json` (three-part
  version, `artifacts` declared) + registry row in ONE commit, then tag that commit
  `<family>-vX.Y.Z` and push commit and tag together.
- Shared tooling changes (`packages/scope-guard/`, `packages/contract-guard/`,
  `packages/repin/`) are released by prefixed tag; consumers move only by re-vendor
  (`repin.py tool <name>`) — never patch a vendored copy in a product repo.

## Shared packages the products vendor

| Package | Distribution | Tags |
|---|---|---|
| [`packages/scope-guard/`](packages/scope-guard/README.md) | `locveil-scope-guard` | `scope-vX.Y.Z` |
| [`packages/contract-guard/`](packages/contract-guard/README.md) | `locveil-contract-guard` | `contract-guard-vX.Y.Z` |
| [`packages/repin/`](packages/repin/README.md) | `locveil-repin` | `repin-vX.Y.Z` |
| [`eval/`](eval/README.md) | `locveil-eval` | `eval-vN` |
