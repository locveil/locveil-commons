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
matches the stamp, contract shape assertions. Layer 1: contract-guard (legacy `PIN.json`
until the next re-pin — BUILD-24 upgrades it to the strict shape with the `files` hash
map and `catalog-vN` tag reference).

Re-pin (until BUILD-24's `make repin` lands):

```bash
cp ../locveil-bridge/contracts/catalog/{catalog.golden.json,openapi.json,STAMP.json} contracts/pins/catalog/
# update PIN.json (contract, version, tag, owner_commit, files sha256s, pin_date), then:
cd eval && uv run --with pytest --with jsonschema pytest tests/test_contracts_pin.py -q
```
