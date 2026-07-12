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
| `STAMP.json` | bridge (byte-identical) | The bridge's build stamp (generating commit + catalog content-hash) |
| `PIN.json` | **voice-stamped** | The pin record: which bridge commit/contract version voice coded against, and when |

Guards (layer 2): `eval/tests/test_contracts_pin.py` — golden validates against the
pinned openapi's `CatalogResponse`, STAMP hash matches the golden's `version`, PIN
matches the stamp, contract shape assertions. Layer 1: contract-guard (strict `PIN.json`
since the `catalog-v1.5` re-pin — `files` sha256 map + family tag, BUILD-24).

Re-pin (scripted, BUILD-24 — from `../locveil-voice/eval`):

```bash
make repin CONTRACT=catalog          # newest bridge catalog-vN tag (or TAG=catalog-v1.6)
make repin-check                     # release-time staleness gate across all pins
cd ../../locveil-commons/eval && uv run --with pytest --with jsonschema pytest tests/test_contracts_pin.py -q
```
