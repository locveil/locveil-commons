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
| [`scope`](scope/README.md) | cross-ref — artifact stays runnable at `../packages/scope-guard/scope_guard.py` (ledger discipline guard; drift-checked) | `scope/STAMP.json` + tag `scope-v7` (v1–v6 pre-stamp history) |
| [`contract-guard`](contract-guard/README.md) | cross-ref — artifact stays runnable at `../packages/contract-guard/contract_guard.py` (this very checker; drift-checked) | `contract-guard/STAMP.json` + tag `contract-guard-v3` (v1/v2 pre-stamp history) |
| [`ui-kit`](ui-kit/README.md) | package-style — the kit at `../packages/ui-kit/` at a tag (no byte-enumeration; HEAD advances between tags by design) | `ui-kit/STAMP.json` + tag `ui-kit-v1.2` |
| [`workbench`](workbench/README.md) | package-style — THE plugin contract (import-map singletons, peers, manifest fragment, runtime-config); machine schemas owed at next bump | `workbench/STAMP.json` + tag `workbench-v1.2` |

| [`docs-manifest`](docs-manifest/README.md) — INTERNAL: the user-facing docs tree, machine-readable (artifact `docs/manifest.json`) | `docs-manifest/STAMP.json` + `docs-manifest-v1`; coherence: `eval/tests/test_docs_manifest.py` |

The pinned CLAUDE.md blocks stay on the **block-pin lane** (`../process/claude-blocks/`,
sha256 rule in each consumer's `.scope-guard.toml` — `../process/contracts.md` §1); since
HK-12 the guard SCRIPTS themselves are stamped owned surfaces (rows above), and consumers
additionally track their vendored tags via their `.repin.toml` `[[tool]]` manifest.

Deliberately NOT contracts (HK-12 sweep, on record): the **eval framework** (live sibling
co-development is the designed asymmetry — revisit at its first hermetic gate), **brand**
(no second external consumer yet), the bridge's raw MQTT topic tree, pymotivaxmc2
(PyPI-pinned), `meta/locveil` (inside device-integration), satellite's internal
components.

## Consumed (pins)

| Pin | Owner | Stamped by | Notes |
|---|---|---|---|
| [`catalog`](pins/catalog/README.md) | locveil-bridge | **locveil-voice** (regime 1 — voice re-pin tasks stamp `PIN.json`; never hand-edit) | golden catalog + openapi + bridge STAMP |
| [`crossover-fixtures`](pins/crossover-fixtures/README.md) | co-owned voice/bridge | voice fixture tasks | `{utterance → canonical command}` fixtures bound to the pinned catalog; strict `PIN.json` arrives with the next fixtures task |

Guards: `../eval/tests/test_contracts_pin.py` + `../eval/tests/test_crossover_fixtures.py`
(layer-2 conformance) and the vendored contract-guard (layer-1 coherence, pre-commit + CI).
