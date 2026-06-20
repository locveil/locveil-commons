# eval-commons — Architecture

A reusable, **declarative (YAML-first)** test & evaluation framework shared across
multiple projects. It covers two test surfaces today and a third on the roadmap:

1. **System tests** — deterministic, assertion-based (transports: WebSocket, MQTT, HTTP).
2. **User/UX tests** — judged by an LLM acting as a human (judge model: **DeepSeek**).
3. **UI-interaction simulation** *(Phase 2)* — goal-driven browser agent.

The governing constraint: **code lives here, once; every consuming project carries
only YAML.** The only bespoke code is the set of transport/scoring providers in this
package — written once, reused everywhere.

---

## 1. Why this shape (decision record)

This design is the output of a multi-source, fact-checked research pass (2025–2026).
The load-bearing, independently-verified findings:

| Finding | Verdict |
|---|---|
| **promptfoo** has a built-in **WebSocket provider** (`messageTemplate`, streaming) | confirmed (3-0) |
| promptfoo has **no built-in MQTT** provider | confirmed |
| promptfoo supports a **custom OpenAI-compatible judge** (→ DeepSeek is config, not code) | confirmed (3-0) |
| promptfoo has two declarative judge assertions: **`llm-rubric`** and model-graded **`g-eval`** | confirmed (3-0) |
| promptfoo supports **custom Python providers referenced declaratively from YAML** | confirmed (3-0) |
| promptfoo supports **modular configs** (split/share YAML) | confirmed (3-0) |
| promptfoo has **no first-class "ship config as an npm package"** story | confirmed (3-0) |
| cross-project config reuse via shared config | weak (2-1) — works via `file://` refs, not a packaged install |
| **Tavern** does declarative **MQTT in YAML** but **no general WebSocket** | confirmed (3-0) |
| **DeepEval** `G-Eval` accepts a custom judge `model=`; ships a `ConversationSimulator` for multi-turn | confirmed (3-0) |
| DeepSeek-V3 used as a baseline LLM-as-judge | confirmed (3-0) |
| **No** tool in scope has built-in WER/CER — `jiwer` is bespoke | confirmed (open gap) |
| DeepSeek **Russian** grading reliability | **unestablished** — must be calibrated |

**Decision.** Standardize on **promptfoo** as the single declarative runner. The two
things it can't do declaratively for our stack (drive a stateful streaming WebSocket /
MQTT, score WER) and the things no tool does (goal-driven UI) become **shared custom
providers** in this package. promptfoo's verified ability to call **Python providers by
path** lets the Python voice ecosystem (`websockets`, `paho-mqtt`, `jiwer`, later
`playwright` and DeepEval) live behind a YAML interface — one runner, one shared package,
projects stay YAML-only.

### Alternatives rejected
- **Tavern + promptfoo (two tools).** Tavern gives zero-code native MQTT YAML, but every
  project then carries *both* an npm and a pip test stack — a heavier common-dependency
  footprint. Rejected: we already need custom providers for the streaming WS protocol and
  for UI simulation, so a custom MQTT provider is zero marginal architectural cost.
  Single-tool wins.
- **DeepEval as the primary runner.** Python-native, excellent `ConversationSimulator`,
  but its tests are pytest code, not declarative YAML — violates the YAML-first constraint.
  Retained as an *optional* shared provider for richer agent-as-human simulation (Phase 1.5).

---

## 2. Component model

```
┌─ promptfoo (the only test runner — common npm dep in every project) ──────────┐
│  reads per-project YAML  →  test cases + endpoint vars only. NO project code.  │
└────────────────────────────────────────────────────────────────────────────────┘
            │ references providers & judge declaratively, by file:// path
            ▼
┌─ eval-commons  (THIS package — written once, versioned, reused) ───────────────┐
│                                                                                 │
│  eval_commons/providers/                                                        │
│    ws_audio_provider.py   → drives a stateful streaming-ASR WebSocket           │
│                              (register → PCM16 frames → end → partial/final)     │
│    mqtt_provider.py        → generic MQTT publish/subscribe assert (paho)        │
│    sim_user_provider.py    → DeepEval ConversationSimulator wrapper  (Phase 1.5) │
│    ui_provider.py          → Playwright goal-driven browser agent    (Phase 2)   │
│                                                                                 │
│  eval_commons/assertions/                                                       │
│    wer_scorer.py           → jiwer WER/CER as a promptfoo python assertion       │
│                                                                                 │
│  eval_commons/audio/       → WAV → PCM16 frame helpers                           │
│                                                                                 │
│  shared/                                                                         │
│    deepseek-judge.yaml     → the judge provider, defined ONCE                    │
│    promptfooconfig.base.yaml → shared defaults projects extend via file://       │
│    rubrics/ru-ux.yaml      → calibrated Russian UX rubrics                        │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### The provider contract (promptfoo Python provider)

Every transport provider exposes the promptfoo Python-provider entrypoint:

```python
def call_api(prompt: str, options: dict, context: dict) -> dict:
    config = options.get("config", {})   # the YAML `config:` block for this provider
    ...                                   # do the I/O (connect, stream, collect)
    return {"output": <str>}             # what assertions/judge see
```

- `prompt` — the test case input (for us: a path/key to an audio fixture, or an utterance).
- `config` — per-test endpoint wiring (`ws_url`, `mqtt_host`, `return_mode`, …) from YAML.
- `output` — a string. Its **shape is controlled by `return_mode`** so the same provider
  serves both deterministic and UX assertions (see §4).

### The assertion contract (promptfoo Python assertion)

```python
def get_assert(output: str, context: dict) -> dict:
    reference = context["vars"]["reference"]
    ...
    return {"pass": bool, "score": float, "reason": str}
```

---

## 3. Cross-project reuse strategy

promptfoo has **no packaged-config install** (verified). So reuse travels two ways:

1. **Providers & assertions** — referenced from a project's YAML by relative `file://`
   path into a **pinned checkout** of this repo (git submodule, or a sibling clone with a
   pinned tag). The Python files are importable and path-referenceable as-is; `pip install
   -e .` is optional and only buys clean intra-package imports.
2. **Shared YAML** (`deepseek-judge.yaml`, `rubrics/*`, `promptfooconfig.base.yaml`) —
   pulled into a project config via `file://` references and YAML composition.

**Recommended layout across projects** (sibling clones under one parent dir):

```
development/
  eval-commons/                 # this package, pinned to a tag
  wb-mqtt-voice/
    eval/promptfooconfig.yaml   # pure YAML; file://../../eval-commons/...
  wb-mqtt-bridge/
    eval/promptfooconfig.yaml   # pure YAML; reuses mqtt_provider.py
```

Pin the eval-commons version per project (submodule SHA or tag) so a provider change is an
explicit, reviewed bump — never a silent break across N projects.

---

## 4. The `return_mode` pattern (one run, multiple assertion shapes)

A single audio utterance yields three things we assert on: the **recognized transcript**
(for WER), the **intent metadata** (deterministic), and the **user-facing reply** (for the
UX judge). promptfoo assertions evaluate the provider's `output` string, and an `llm-rubric`
judge should see *only the reply*, not a JSON blob. So the provider exposes `return_mode`:

| `return_mode` | `output` is… | used by |
|---|---|---|
| `full` (default) | JSON: `{transcript, response_text, intent_name, success, partials, latency_ms}` | python assertions (WER, intent) |
| `transcript` | the recognized text only | WER, exact-match |
| `response_text` | the assistant's reply only | `llm-rubric` / `g-eval` (DeepSeek judge) |

For the PoC we run the utterance once per mode (simple, explicit). **Optimization later:**
a single run that fans its result to all assertions (cache by fixture hash). This is called
out so the duplication is a known trade-off, not an accident.

---

## 5. DeepSeek as the judge

Defined **once** in `shared/deepseek-judge.yaml`, referenced by every UX assertion:

```yaml
id: openai:chat:deepseek-chat
config:
  apiBaseUrl: https://api.deepseek.com/v1
  apiKeyEnvar: DEEPSEEK_API_KEY
  temperature: 0
```

DeepSeek is OpenAI-compatible, so promptfoo's `openai:chat:*` provider drives it with only
a base-URL + key swap. The same model id feeds DeepEval's `model=` in Phase 1.5.

---

## 6. Phased roadmap

- **Phase 1 (now).** promptfoo runner · WS-audio provider · WER scorer · DeepSeek
  `llm-rubric` UX judging · promptfoo built-in multi-turn for conversational UX ·
  MQTT provider available for `wb-mqtt-bridge`.
- **Phase 1.5 (if persona depth is insufficient).** Drop DeepEval `ConversationSimulator`
  into `sim_user_provider.py`, behind the same YAML interface — no project changes.
- **Phase 2 (UI simulation).** `ui_provider.py` (Playwright goal-driven agent) slots into
  the *existing* shared-provider boundary. The UX judge machinery (rubric + DeepSeek) is
  reused verbatim — "talks" becomes "clicks," scoring is unchanged. Touches no existing
  project.

The shared-provider boundary is drawn precisely so each phase is a change *here*, never a
rewrite *there*.

---

## 7. Risks & gotchas

1. **DeepSeek-as-judge on Russian is unproven (highest risk).** Sources confirm DeepSeek is
   used as a baseline judge but establish **nothing** about Russian grading quality.
   Mitigation (non-negotiable): maintain a small **human-scored Russian calibration set**;
   measure judge↔human agreement before trusting scores; periodically audit with a stronger
   model. See `shared/rubrics/ru-ux.yaml` and `examples/` for where calibration data lives.
2. **No packaged-config reuse in promptfoo.** Reuse is `file://` refs into a *pinned*
   checkout, not `npm install`. Pin per project; treat provider edits as a versioned bump.
3. **MQTT + WER + UI are the only bespoke code — by design.** Isolated here, never
   per-project. The streaming WS protocol is bespoke too (stateful binary handshake).
4. **Per-mode re-runs.** The `return_mode` PoC runs audio more than once per utterance;
   acceptable for now, flagged for a single-run fan-out optimization (§4).
5. **Localization discipline.** Judge user-facing CHOICE/response values in Russian; never
   ask the judge to grade translated technical identifiers (model/driver/service names are
   canonical and self-matchable).

---

## 8. How a project consumes this (in one screen)

```yaml
# wb-mqtt-voice/eval/promptfooconfig.yaml  — PURE YAML, no project code
providers:
  - id: file://../../eval-commons/eval_commons/providers/ws_audio_provider.py
    config: { ws_url: ws://localhost:6000/ws/audio, return_mode: full }

defaultTest:
  options:
    provider:                       # the DeepSeek judge, for llm-rubric/g-eval
      file://../../eval-commons/shared/deepseek-judge.yaml

tests: file://tests/*.yaml          # the per-project cases live here, as YAML
```

That's the whole contract: install promptfoo, point at the shared providers + judge,
write YAML cases. Everything else is in this package.
