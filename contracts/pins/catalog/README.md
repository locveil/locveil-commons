# catalog — the Irene ↔ bridge contract pin (consumed)

A **pinned, one-way-inward copy** of the `locveil-bridge` catalog contract artifacts —
the shared boundary both repos test against without the other running. The bridge is the
generator and source of truth (its own `contracts/catalog/` after the PROD-16 cut); it
never writes here. **The voice side owns this copy** (regime 1): its re-pin tasks copy
the files and stamp `PIN.json`. Never hand-edit any file in this folder.

| File | Origin | What it is |
|---|---|---|
| `catalog.golden.json` | bridge (byte-identical) | The golden catalog — rooms + aliases, devices, capabilities with typed param descriptors |
| `openapi.json` | bridge (byte-identical) | The API schema of record — `CatalogResponse`, `CatalogParam`, canonical action shapes |
| `catalog-contract.md` | bridge (byte-identical) | The normative guide — parameter semantics and the versioning rule (enumerated since the bridge's guide/README split, HK-13) |
| `STAMP.json` | bridge (byte-identical) | The bridge's build stamp (generating commit + catalog content-hash) |
| `PIN.json` | **voice-stamped** | The pin record: which bridge commit/contract version voice coded against, and when |

The file set is not chosen here: it is exactly the `artifacts` the bridge's STAMP
enumerates at the pinned tag, plus the STAMP (repin v2, HK-13) — `PIN.json` and this
README are the only files in the folder that are not the owner's bytes.

Guards (layer 2): `eval/tests/test_contracts_pin.py` — golden validates against the
pinned openapi's `CatalogResponse`, STAMP hash matches the golden's `version`, PIN
matches the stamp, contract shape assertions. Layer 1: contract-guard (strict `PIN.json`
with the `files` sha256 map; pin completeness against the carried STAMP).

Re-pin (scripted — from `../locveil-voice`; voice's multi-dest run stamps its own copy
and this one at the same tag, so they never diverge):

```bash
python3 scripts/repin.py catalog     # newest bridge catalog tag (or --tag catalog-vX.Y.Z)
make -C eval repin-check             # release-time staleness gate across all pins
cd ../locveil-commons/eval && uv run --extra record --extra dev pytest tests/test_contracts_pin.py -q
```
