# locveil-commons — contract registry

The direction-labeled index required by `../process/contracts.md` §2. Every contract this
repo OWNS and every pin it CONSUMES, one line each; details live in the per-contract
READMEs. Layout is the uniform org shape: `contracts/<name>/` owned,
`contracts/pins/<name>/` consumed.

## Owned

| Contract | Where | Version authority |
|---|---|---|
| [`report-protocol`](report-protocol/README.md) | `report-protocol/` (machine core; prose spec: `../process/problem-reports.md`) | `report-protocol/STAMP.json` + tag `report-protocol-v1.0.1` |
| [`core-py`](core-py/README.md) | cross-ref — artifact stays importable at `../packages/core-py/entry_point_loader.py` (vendored RUNTIME code; strict pin + byte-identity test consumer-side) | `core-py/STAMP.json` + tag `core-py-v1.1` (v1 tree predates the STAMP — packaging correction, artifact unchanged) |
| [`repin`](repin/README.md) | cross-ref — artifact stays runnable at `../packages/repin/repin.py` (HK-12 re-pin + staleness tool; consumers vendor + own `.repin.toml`) | `repin/STAMP.json` + tag `repin-v2.0.0` |
| [`scope`](scope/README.md) | cross-ref — artifact stays runnable at `../packages/scope-guard/scope_guard.py` (ledger discipline guard; drift-checked); scope tags also ship the pinned blocks (HK-2 single-pin) | `scope/STAMP.json` + tag `scope-v7.3.1` (v1–v6 pre-stamp history) |
| [`contract-guard`](contract-guard/README.md) | cross-ref — artifact stays runnable at `../packages/contract-guard/contract_guard.py` (this very checker; drift-checked) | `contract-guard/STAMP.json` + tag `contract-guard-v4.0.0` (v1/v2 pre-stamp history) |
| [`ui-kit`](ui-kit/README.md) | package-style — the kit at `../packages/ui-kit/` at a tag (`artifacts: []` by declaration: HEAD advances between tags by design) | `ui-kit/STAMP.json` + tag `ui-kit-v1.3.0`; guard `eval/tests/test_ui_kit_tokens.py` |
| [`workbench`](workbench/README.md) | THE plugin contract — enumerated: the contract types (`../packages/workbench/src/contract.ts`) + the manifest-fragment and runtime-config schemas (`../packages/workbench/schemas/`); import-map singletons and peers semantics stay prose | `workbench/STAMP.json` + tag `workbench-v1.3.0`; guard `eval/tests/test_workbench_schemas.py` |
| [`docs-manifest-schema`](docs-manifest-schema/README.md) | cross-ref — artifact stays at `../process/user-docs/manifest.schema.json` (the org-wide docs-manifest vocabulary; per-repo `docs/manifest.json` files are instance data, not contracts — HK-13) | `docs-manifest-schema/STAMP.json` + tag `docs-manifest-schema-v1.0.0`; guard `eval/tests/test_docs_manifest.py` |

The pinned CLAUDE.md blocks stay on the **block-pin lane** (`../process/claude-blocks/`,
sha256 rule in each consumer's `.scope-guard.toml` — `../process/contracts.md` §1); since
HK-12 the guard SCRIPTS themselves are stamped owned surfaces (rows above), and consumers
additionally track their vendored tags via their `.repin.toml` `[[tool]]` manifest.

Deliberately NOT contracts (HK-12 sweep, on record): the **eval framework** as an OWNED
surface (live sibling co-development is the designed asymmetry — revisit at its first
hermetic gate; what eval CONSUMES is pinned — `ws-protocol` since IMPL-19), **brand**
(no second external consumer yet), the bridge's raw MQTT topic tree, pymotivaxmc2
(PyPI-pinned), `meta/locveil` (inside device-integration), satellite's internal
components.

## Consumed (pins)

| Pin | Owner | Stamped by | Notes |
|---|---|---|---|
| [`catalog`](pins/catalog/README.md) | locveil-bridge | **locveil-voice** (regime 1 — voice re-pin tasks stamp `PIN.json`; never hand-edit) | golden catalog + openapi + bridge STAMP |
| [`ws-protocol`](pins/ws-protocol/) | locveil-voice | commons (repin) | the WS wire protocol — the document + its machine core (golden frames, transcripts, schema); the eval WS provider implements it |
| [`crossover-fixtures`](pins/crossover-fixtures/README.md) | co-owned voice/bridge | voice fixture tasks | `{utterance → canonical command}` fixtures bound to the pinned catalog; strict `PIN.json` arrives with the next fixtures task |

Guards: `../eval/tests/test_contracts_pin.py` + `../eval/tests/test_crossover_fixtures.py` +
`../eval/tests/test_ws_protocol_pin.py` (layer-2 conformance) and the vendored contract-guard (layer-1 coherence, pre-commit + CI).
