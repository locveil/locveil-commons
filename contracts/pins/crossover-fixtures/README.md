# crossover-fixtures — the bidirectional test fixtures (consumed pin)

A **strict pin** of the `locveil-voice`-owned `crossover-fixtures` family (PROD-29,
2026-10-12): `{utterance → expected canonical command}` fixtures in two tiers and four
expect kinds, bound to the bridge catalog by CONTENT HASH (`catalog_version` in the owner's
STAMP, mirrored into `PIN.json`). Owner surface: `locveil-voice/contracts/crossover-fixtures/`
(STAMP + guard there). Moves ONLY by `python3 packages/repin/repin.py crossover-fixtures` —
never hand-edited here. Until PROD-29 this folder was a co-owned file voice wrote into
directly; that posture, and the standing `PIN-PENDING` warning, ended with the first pin.

Consumers in this repo: `eval/eval_commons/fixtures_to_tests.py` (generates the products'
device-test YAML from it), `eval/eval_commons/assertions/device_command_assert.py`, and
the layer-2 guard `eval/tests/test_crossover_fixtures.py` — every fixture binds to real
catalog surfaces of the catalog pin beside it, and the two pins' catalog hashes must agree
(`test_pin_agreement`): a catalog re-pin at voice is followed by a fixtures minor and a
commons re-pin (the accepted cost). The bridge pins the same family when its consumer
contract test (VWB-16) lands.
