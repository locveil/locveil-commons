# locveil-commons — Architecture

A reusable, **declarative (YAML-first)** test & evaluation framework shared across
multiple projects. It covers two test surfaces today and a third on the roadmap:

1. **System tests** — deterministic, assertion-based (transports: WebSocket, MQTT, HTTP).
2. **CLI tests** — deterministic, assertion-based over local `argparse` console scripts
   (stdout / JSON / exit code). This is the dominant test surface for both projects.
3. **User/UX tests** — judged by an LLM acting as a human (judge model: **DeepSeek**).
4. **UI-interaction simulation** *(Phase 2)* — goal-driven browser agent.

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
┌─ locveil-commons  (THIS package — written once, versioned, reused) ───────────────┐
│                                                                                 │
│  eval_commons/providers/                                                        │
│    ws_audio_provider.py   → drives a stateful streaming-ASR WebSocket           │
│                              (register → PCM16 frames → end → partial/final)     │
│    mqtt_provider.py        → generic MQTT publish/subscribe assert (paho)        │
│    cli_provider.py         → single-shot subprocess CLI (argv → stdout/json/exit)│
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
│    rubrics/{ru,en}/*.txt   → calibrated UX rubrics (one file per rubric)          │
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
  locveil-commons/                 # this package, pinned to a tag
  locveil-voice/
    eval/promptfooconfig.yaml   # pure YAML; file://../../locveil-commons/...
  locveil-bridge/
    eval/promptfooconfig.yaml   # pure YAML; reuses mqtt_provider.py
```

Pin the locveil-commons version per project (submodule SHA or tag) so a provider change is an
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

## 5. CLI testing (the `cli_provider`)

Both projects expose most of their testable behaviour as **`argparse` console scripts**, not
network endpoints — e.g. `irene-config-validate`, `irene-build-analyze`,
`irene-dependency-validate`, `irene-replay-trace`; `wb-openapi`, `broadlink-cli --convert`,
`broadlink-discovery`, `device-test <id> <command>`. They share one shape: **argv in →
stdout/stderr + (often) a `--json` blob + a meaningful exit code (0/1/2)**. promptfoo has no
built-in provider that spawns a local process, so this is a shared custom provider — written
once, same YAML-only contract as the transports.

`cli_provider.py` runs a single subprocess (no shell, argv passed verbatim) and shapes its
output via the same `return_mode` switch as §4:

| `return_mode` | `output` is… | used by |
|---|---|---|
| `full` (default) | JSON `{stdout, stderr, exit_code, duration_ms}` | python/JS multi-field assertions |
| `stdout` | stdout only | `contains`, `regex`, `llm-rubric` over `--help` text |
| `stderr` | stderr only | error-message assertions |
| `json` | stdout parsed & re-emitted (fails if not JSON) | `is-json`, JSON-path on `--json` tools |
| `exit_code` | the exit code as a string | `equals: "0"` / `"2"` |

Run console scripts (or `python -m ...`) from the target project via `config.cwd`; pass
fixtures through `vars` and template them into `config.argv`. Example:

```yaml
providers:
  - id: file://../../locveil-commons/eval_commons/providers/cli_provider.py
    config:
      cwd: ../locveil-voice
      argv: ["irene-config-validate", "--config-file", "{{config}}", "--json"]
      return_mode: exit_code
tests:
  - vars: { config: configs/minimal.toml }
    assert: [{ type: equals, value: "0" }]
```

**Scope (deliberate).** Deterministic, single-shot invocations only. Two things are out:
*interactive REPLs* (`irene-cli`, `device-test` with no command) need scripted stdin with
prompt-matching — a later extension behind this same interface; *long-running services*
(servers, `mqtt-sniffer`, `broadlink-cli --learn`) are already covered by the WS/MQTT/HTTP
transport providers and smoke tests, or need live hardware. The provider accepts a fixed
`config.stdin` string for trivial pipe/confirm cases, but does not drive an interactive
session.

---

## 6. DeepSeek as the judge

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

## 7. Phased roadmap

- **Phase 1 (now).** promptfoo runner · WS-audio provider · WER scorer · DeepSeek
  `llm-rubric` UX judging · promptfoo built-in multi-turn for conversational UX ·
  MQTT provider available for `locveil-bridge` · **CLI provider** for the `argparse`
  console scripts in both projects (single-shot, deterministic).
- **Phase 1.5 (if persona depth is insufficient).** Drop DeepEval `ConversationSimulator`
  into `sim_user_provider.py`, behind the same YAML interface — no project changes.
- **Phase 2 (UI simulation).** `ui_provider.py` (Playwright goal-driven agent) slots into
  the *existing* shared-provider boundary. The UX judge machinery (rubric + DeepSeek) is
  reused verbatim — "talks" becomes "clicks," scoring is unchanged. Touches no existing
  project.

The shared-provider boundary is drawn precisely so each phase is a change *here*, never a
rewrite *there*.

---

## 8. Risks & gotchas

1. **DeepSeek-as-judge on Russian: CALIBRATED 2026-07-02.** A 20-case human-labeled set
   (native Russian speaker; 16 confident + 4 borderline) measured against the shipped
   rubrics through the same llm-rubric→DeepSeek path: after two disciplined rubric
   iterations, **16/16 agreement, Cohen's κ = 1.0 in-sample** (from 81%/κ 0.625 pre-tuning),
   0 false-accepts / 0 false-rejects, verdicts stable across repeat runs at temp 0. The set,
   gold labels, scorer and method live in `examples/ru-ux-calibration/`. Caveat: κ is
   in-sample (the rubric was tuned on this set) — re-measure on FRESH negatives as suites
   grow, and re-run the set after ANY rubric edit (an earlier fix regressed a neighboring
   criterion). English rubrics carry the same structural improvements but are uncalibrated.
2. **No packaged-config reuse in promptfoo.** Reuse is `file://` refs into a *pinned*
   checkout, not `npm install`. Pin per project; treat provider edits as a versioned bump.
3. **MQTT + WER + CLI + UI are the only bespoke code — by design.** Isolated here, never
   per-project. The streaming WS protocol is bespoke too (stateful binary handshake). The
   CLI provider is generic subprocess plumbing; per-project specifics stay in YAML (argv,
   cwd, fixtures).
4. **Per-mode re-runs.** The `return_mode` PoC runs audio more than once per utterance;
   acceptable for now, flagged for a single-run fan-out optimization (§4).
5. **Localization discipline.** Judge user-facing CHOICE/response values in Russian; never
   ask the judge to grade translated technical identifiers (model/driver/service names are
   canonical and self-matchable).

---

## 9. How a project consumes this (in one screen)

```yaml
# locveil-voice/eval/promptfooconfig.yaml  — PURE YAML, no project code
providers:
  - id: file://../../locveil-commons/eval_commons/providers/ws_audio_provider.py
    config: { ws_url: ws://localhost:6000/ws/audio, return_mode: full }

defaultTest:
  options:
    provider:                       # the DeepSeek judge, for llm-rubric/g-eval
      file://../../locveil-commons/eval/shared/deepseek-judge.yaml

tests: file://tests/*.yaml          # the per-project cases live here, as YAML
```

That's the whole contract: install promptfoo, point at the shared providers + judge,
write YAML cases. Everything else is in this package.
