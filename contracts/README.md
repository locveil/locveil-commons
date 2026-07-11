# The Irene ↔ bridge contract pin (consumer copy)

A **pinned, one-way-inward copy** of the `locveil-bridge` contract artifacts — the shared
boundary both repos test against without the other running (`locveil-voice`
`docs/design/mqtt_integration.md` §14). The bridge is the *generator and source of truth*;
it commits its reference artifacts in **its own** repo (`locveil-bridge/contracts/`) and
never writes here. The **voice side owns this copy**: it re-pins (plain file copy + updated
`PIN.json`) whenever it starts coding against a newer bridge build.

## Files

| File | Origin | What it is |
|---|---|---|
| `catalog.golden.json` | bridge (byte-identical) | The golden catalog — the full house as `GET /system/catalog` serves it: rooms + aliases, devices (aggregates, scenario managers), capabilities with typed param descriptors (`unit`, `values` triplets, `options_from`) |
| `openapi.json` | bridge (byte-identical) | The API schema of record — `CatalogResponse`, `CatalogParam`, and the canonical action request/response shapes under `components/schemas` |
| `STAMP.json` | bridge (byte-identical) | The bridge's own build stamp (generating commit + catalog content-hash) |
| `PIN.json` | **this repo** | The pin record: which bridge commit/patch level the voice side coded against, and when it was pinned |
| `crossover_fixtures.json` | **this repo** (voice-authored) | The bidirectional test fixtures: `{utterance → expected canonical command}` bound to the pinned catalog. Irene's producer tests assert the *emitted* command matches; the bridge's consumer tests (VWB-16) replay the *expected* command against its native layer |

## Guarantees (tested)

`tests/test_contracts_pin.py` keeps the pin honest:

- the golden catalog **validates against the pinned `openapi.json`'s `CatalogResponse` schema** —
  the two halves of the pin can never disagree with each other;
- `STAMP.json`'s catalog hash matches the golden's `version`, and `PIN.json` matches the stamp;
- v1.1 shape assertions (aliases present, localized enum labels, units on params,
  `values`-XOR-`options_from`) — so an accidental re-pin of a pre-patch artifact fails loudly.

`tests/test_crossover_fixtures.py` keeps the fixtures honest the same way: every fixture's
expected command must bind to real catalog entities (device ids, capabilities, actions,
param ranges/enums, rooms, semantic groups, sensor fields), and the fixtures'
`catalog_version` must equal the pin's. After a re-pin, a failing fixture guard points at
exactly which fixtures need re-authoring.

## Re-pinning

```bash
cp ../locveil-bridge/contracts/{catalog.golden.json,openapi.json,STAMP.json} contracts/
# update PIN.json (bridge commit, catalog version, date), then:
pytest tests/test_contracts_pin.py
```

Consumers: the voice repo's device-command contract tests (its TEST-18 / the
`device_command` capture provider) and the bridge's consumer-half tests (VWB-16) both read
**this** copy, so device ids and capabilities cannot drift apart between the two suites.
A real WB7 catalog dump will join the golden as a realism check once the bridge is deployed
on the controller (pending its `ops/` cutover).
