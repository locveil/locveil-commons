# locveil-commons — contract registry

The direction-labeled index required by `../process/contracts.md` §2. Every contract this
repo OWNS and every pin it CONSUMES, one line each; details live in the per-contract
READMEs. Layout is the uniform org shape: `contracts/<name>/` owned,
`contracts/pins/<name>/` consumed.

## Owned

| Contract | Where | Version authority |
|---|---|---|
| [`report-protocol`](report-protocol/README.md) | `report-protocol/` (machine core; prose spec: `../process/problem-reports.md`) | `report-protocol/STAMP.json` + tag `report-protocol-v1` |
| [`core-py`](core-py/README.md) | cross-ref — artifact stays importable at `../packages/core-py/entry_point_loader.py` (vendored RUNTIME code; strict pin + byte-identity test consumer-side) | `core-py/STAMP.json` + tag `core-py-v1` |
| [`repin`](repin/README.md) | cross-ref — artifact stays runnable at `../packages/repin/repin.py` (HK-12 re-pin + staleness tool; consumers vendor + own `.repin.toml`) | `repin/STAMP.json` + tag `repin-v1` |

| [`docs-manifest`](docs-manifest/README.md) — INTERNAL: the user-facing docs tree, machine-readable (artifact `docs/manifest.json`) | `docs-manifest/STAMP.json` + `docs-manifest-v1`; coherence: `eval/tests/test_docs_manifest.py` |

Cross-references (owned process contracts on the **block-pin lane**, not relocated —
`../process/contracts.md` §1):

- **scope kit** (`scope-vN`) — `../packages/scope-guard/` + `../process/claude-blocks/`;
  enforced by the sha256 block rule in each consumer's `.scope-guard.toml`.
- **contract-guard** (`contract-guard-vN`) — `../packages/contract-guard/`; the layer-1
  coherence checker itself, vendored by consumers like the scope kit.

## Consumed (pins)

| Pin | Owner | Stamped by | Notes |
|---|---|---|---|
| [`catalog`](pins/catalog/README.md) | locveil-bridge | **locveil-voice** (regime 1 — voice re-pin tasks stamp `PIN.json`; never hand-edit) | golden catalog + openapi + bridge STAMP |
| [`crossover-fixtures`](pins/crossover-fixtures/README.md) | co-owned voice/bridge | voice fixture tasks | `{utterance → canonical command}` fixtures bound to the pinned catalog; strict `PIN.json` arrives with the next fixtures task |

Guards: `../eval/tests/test_contracts_pin.py` + `../eval/tests/test_crossover_fixtures.py`
(layer-2 conformance) and the vendored contract-guard (layer-1 coherence, pre-commit + CI).
