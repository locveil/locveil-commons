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

## Dev setup & gates

- Python ≥ 3.11, [`uv`](https://github.com/astral-sh/uv). Eval framework tests:
  `cd eval && uv run --all-extras --with pytest --with jsonschema pytest tests/ -q`.
- Hooks: `git config core.hooksPath hooks` — runs scope-guard + contract-guard,
  `--check` only. CI mirrors them (`ledger-guard`, `contract-guard`), path-gated.
- Shared tooling changes (`packages/scope-guard/`, `packages/contract-guard/`) are
  released by prefixed tag (`scope-vN`, `contract-guard-vN`); consumers move only by
  re-pin — never patch a vendored copy in a product repo.

## Shared packages the products vendor

| Package | Distribution | Tags |
|---|---|---|
| [`packages/scope-guard/`](packages/scope-guard/README.md) | `locveil-scope-guard` | `scope-vN` |
| [`packages/contract-guard/`](packages/contract-guard/README.md) | `locveil-contract-guard` | `contract-guard-vN` |
| [`eval/`](eval/README.md) | `locveil-eval` | `eval-vN` |
