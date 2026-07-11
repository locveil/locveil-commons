# locveil-commons

The umbrella repo of **Locveil** — a fully local, privacy-first, Russian-first
voice-controlled smart home. Two products, valuable standalone and contract-coupled (the
canonical `DeviceCommand` boundary), plus a hardware satellite on the way:

| Repo | Product |
|---|---|
| [`locveil-voice`](https://github.com/locveil/locveil-voice) | Irene — the voice assistant (wake word, ASR, NLU, TTS) |
| [`locveil-bridge`](https://github.com/locveil/locveil-bridge) | The smart-home bridge (device catalog, canonical command API, MQTT/Wirenboard) |
| `locveil-satellite` *(pending)* | The ESP32 room satellite (PCB + firmware + enclosure) |

This repo is the neutral ground both products share — no product code lives here.

## Layout

```
board/            cross-repo initiative ledger (PROD-N) + journal
process/          normative specs: ops, shared CLAUDE.md invariants, report policy
docs/design/      cross-repo design docs (incl. the productization decision record)
eval/             the shared YAML-first test/eval framework (locveil-eval, tag eval-vX)
packages/         co-owned runtime code: core-py, ui-kit (rule of two; own tags each)
contracts/        pinned product-owned contract artifacts + crossover fixtures
site/             the landing page (GitHub Pages → locveil.com)
```

Three ownership regimes keep one repo safe: product-owned **pins** (`contracts/`),
co-owned **shared code** products consume by version (`eval/`, `packages/`), and
commons-owned **process/product artifacts** (`board/`, `process/`, `site/`). Details:
`docs/design/productization.md`.

## The eval framework

Shared, declarative test & evaluation providers (promptfoo) consumed by both product repos
— system/CLI/UX/UI test surfaces, WER scoring, an LLM judge. See
[`eval/README.md`](eval/README.md) and [`eval/ARCHITECTURE.md`](eval/ARCHITECTURE.md).
