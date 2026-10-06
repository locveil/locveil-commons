# crossover-fixtures — the bidirectional test fixtures (consumed, co-owned)

`crossover_fixtures.json`: `{utterance → expected canonical command}` fixtures bound to
the pinned catalog (`../catalog/`). Voice's producer tests assert the *emitted* command
matches; the bridge's consumer tests (VWB-16) replay the *expected* command against its
native layer — so device ids and capabilities cannot drift apart between the two suites.

Co-owned: voice-authored, moved by voice fixture tasks; never hand-edited here. Strict
`PIN.json` (hash map, per `process/contracts.md` §2) arrives with the next fixtures task —
until then contract-guard reports the pending pin as a warning by design.

Guard (layer 2): `eval/tests/test_crossover_fixtures.py` — every fixture binds to real
catalog entities and the fixtures' `catalog_version` must equal the pin's.

## Moves (newest first)

- **2026-10-06 — voice TEST-24:** F82–F86 added, the AC louvers (QUAL-82, board PROD-18
  round 1) — tier 1, `bedroom_hvac`: F82 «заслонка в положение три» → `vane.set{pos_3}`,
  F83 «заслонка на авто» → `vane.set{auto}`, F84 «качай заслонку» → `vane.set{swing}`,
  F85 «направь заслонку влево» → `widevane.set{left}`, F86 «заслонка в центр» →
  `widevane.set{center}`. Catalog binding unchanged (`5622ba7a1a78102a`).
