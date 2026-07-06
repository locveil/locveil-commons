# eval-commons — agent notes

The shared, YAML-first test/eval framework (promptfoo providers, scorers, DeepSeek judge) for
the sibling repos `../wb-mqtt-voice` (Irene, the voice assistant) and `../wb-mqtt-bridge` (the
smart-home bridge). Consumers carry only YAML + a thin Makefile; **all execution logic lives
here** — behavior changes happen in this repo, not in the consumers.

## Source-of-truth rules

- **The WebSocket wire protocol is defined by `../wb-mqtt-voice/docs/guides/websocket-api.md`**
  (that repo's `ws-protocol-doc-canonical` invariant). `eval_commons/providers/ws_audio_provider.py`
  and any other WS client here IMPLEMENT that document — when provider behavior disagrees with
  it, the document wins; when the protocol gains a field (e.g. `wants_trace`, default `false`),
  this repo needs no change unless a test wants the new capability. Never reverse-engineer the
  protocol from server code or from this repo's own providers; read the document.
- **`contracts/` is a one-way inward pin owned by wb-mqtt-voice** (its re-pin tasks stamp
  `PIN.json`): a version-stamped copy of `../wb-mqtt-bridge`'s committed contract artifacts
  (catalog golden, STAMP, openapi). Never hand-edit anything under `contracts/` and never treat
  it as a source — it is re-pinned from the bridge when the bridge's artifact moves.

## Working notes

- Consumers run suites via `make` from their own `eval/` directories (they wire the `uv` venv +
  global `promptfoo`); this repo's own tests run with `uv run --with pytest pytest tests/ -q`.
- promptfoo env references are `{{env.VAR}}`, not `${VAR}`.
- Tests parameterize over TARGET (local vs the WB7 controller) and CONFIG via the consumers'
  profile env files — never bake an endpoint or config into execution logic here.
