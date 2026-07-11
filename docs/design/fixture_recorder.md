# Design — voice-fixture recorder (`eval-fixture-record`)

**Status:** DESIGN AGREED · 2026-06-27 (the §14 decisions are signed off; implementation pending — see §13) ·
**Lands in:** locveil-commons (shared) · **Drives:** the WS-audio system suites of every consuming project
(first: locveil-voice, then locveil-bridge).

> locveil-commons has no ledger/journal process yet, so this document is **self-contained**: it carries the motivation,
> the decisions *and their rationale*, the interface, the scope boundary, the risks, and an explicit implementation
> worklist (§13) that stands in for ledger tasks until one exists.

---

## 0. Why this exists

The WS-audio system tests (`ws_audio_provider.py`) consume audio **fixtures** that must be **16 kHz / mono / 16-bit
PCM WAV** — the `/ws/audio` wire format. `eval_commons/audio/wav_to_pcm16_frames()` *validates* this and **refuses to
resample** on purpose (so tests measure the ASR, not a converter). Today fixtures are produced ad hoc with an `ffmpeg`
one-liner (see a consumer's `eval/fixtures/README.md`): manual, no prompt to read, no review/redo, no format
guarantee, and no link to the `reference:` text the test will score against. The WS suites are **blocked on missing
fixtures**, so a first-class recorder is on the critical path.

This is a **dev tool**, run locally by a human with a microphone; it never runs in CI.

## 1. Where it lives — and why not in a consumer (decision record)

**Decision: the recorder lives in locveil-commons; it implements its own microphone handling and does *not* reuse any
consumer project's audio code.**

The dependency direction settles it. locveil-commons is the **lower, shared layer** — both locveil-voice and
locveil-bridge depend *on* it (`uv pip install -e ../../locveil-commons`). If the recorder imported a consumer's mic stack
(e.g. `irene`'s audio input), that edge would point **back up at a consumer**, and since locveil-voice already depends
on locveil-commons it would be a literal **dependency cycle**. Three consequences, any one disqualifying:

- **Reusability dies.** locveil-commons must stay project-agnostic; coupling it to `irene` means locveil-bridge (no
  `irene`) can't record fixtures — the shared tool would serve only one of its two consumers.
- **Wrong concern.** A consumer's mic input is *runtime* (VAD, wake-word, streaming into the live ASR pipeline). The
  recorder is *capture-to-disk*. They overlap only at "read PCM from a device"; sharing drags a heavyweight,
  pipeline-coupled subsystem into a small tool.
- **The home already exists.** `eval_commons/audio/` is the project-agnostic audio module (it owns
  `wav_to_pcm16_frames`). The recorder's capture + format-conditioning belong here as siblings.

This is the textbook case where **a little duplication beats the wrong dependency**: a small, self-contained
`sounddevice` recorder is strictly better than importing across the project boundary.

The clean split that keeps it honest — **logic here, data in the consumer**:

| Concern | Home |
|---|---|
| Capture, format-conditioning, worklist resolution, interactive loop (the *logic*) | locveil-commons |
| Which mic / gain / capture rate on *this* machine (the *data*) | consumer's git-ignored `eval/profiles/recording.env`, passed *in* |

locveil-commons never hard-codes a consumer path; the consumer hands it the config + a fixtures dir + the YAML to read.

## 2. Requirements

**Functional**
- **R1 — Conformant output.** Every saved fixture is 16 kHz / mono / 16-bit PCM WAV, validated by the *same*
  `wav_to_pcm16_frames` invariants the provider enforces (reused as the acceptance gate — nice symmetry).
- **R2 — Two modes.** *Targeted*: record the fixture(s) a project needs, showing the line to read. *Freeform*: record
  an arbitrary named WAV with no test awareness.
- **R3 — Single source of truth.** The targeted worklist (which fixtures, and the prompt text for each) is **derived
  from the project's promptfoo YAML**, not a separate manifest that can drift.
- **R4 — Interactive capture.** Per fixture: show prompt → countdown → record → **play back → keep / redo / skip**.
  The redo loop is the point; a flubbed take must be cheap to discard.
- **R5 — Machine-local mic config** in the consumer (git-ignored), passed into the tool.
- **R6 — Safe by default.** Record only the *missing* fixtures; never clobber an existing one without `--force`.

**Non-functional**
- Project-agnostic (works for voice and bridge unchanged).
- The microphone dependency is **opt-in** (an extra), so core locveil-commons installs stay lean.
- Zero dependency on any consumer's code (§1).

## 3. Component model

A new package `eval_commons/record/`, plus conditioning helpers added to the existing `eval_commons/audio/`:

```
eval_commons/
  audio/
    __init__.py        wav_to_pcm16_frames  (exists)
                       + conform_to_pcm16(frames, src_rate, src_ch) -> bytes   (NEW: downmix+resample+PCM16)
                       + write_pcm16_wav(path, pcm, rate=16000)               (NEW: stdlib `wave` writer)
  record/
    __init__.py
    worklist.py        parse a promptfoo YAML -> [FixtureJob{key, path, prompt, used_by}]   (pure, unit-tested)
    capture.py         sounddevice capture + device discovery                (mic; thin)
    session.py         the interactive controller (prompt→record→playback→keep/redo/skip)
    cli.py             argparse entrypoint, config loading, mode dispatch
```

**Entry point.** A console script `eval-fixture-record` (new `[project.scripts]`), so it resolves in the consumer's
venv once locveil-commons is installed there. Mic deps are an optional extra (§8); the script prints an actionable error
if they're absent rather than failing on import.

## 4. CLI contract

```
eval-fixture-record [--from-yaml YAML] [--fixtures-dir DIR] [--config FILE]
                    [--list] [--devices] [--force] [--seconds N] [--free NAME] [KEY ...]
```

| Invocation | Behavior |
|---|---|
| (no positional) | Read the YAML, compute the worklist, record every fixture **referenced but missing** on disk, interactively. |
| `KEY ...` (e.g. `timer_10min`) | Record just those fixtures; prompt text looked up from the YAML by key. |
| `--free NAME` | Freeform: record to `<fixtures-dir>/NAME.wav`, no YAML lookup, ask the user for an optional prompt to read. |
| `--list` | Print the worklist (each fixture: key, path, prompt, which cases use it, present/missing) and exit. |
| `--devices` | List input devices (`sounddevice.query_devices`) so the user can pick the index/name for the config; exit. |
| `--force` | Re-record fixtures that already exist (default skips present ones). |
| `--seconds N` | Fixed-duration capture instead of press-Enter-to-stop. |

**The fixture key** is the **basename of `vars.audio`** (`fixtures/timer_10min.wav` → `timer_10min`). That path is
already the join key in the YAML, so "identify by id" = "identify by fixture key." No new id field on test cases.

## 5. Source of truth: deriving the worklist from the YAML

`worklist.py` parses the consumer's `ws.promptfooconfig.yaml` and walks `tests[]`:

- `vars.audio` → the fixture path (→ key).
- `vars.reference` → the **prompt to read aloud**. For WER cases this already exists and *is* the spoken text — so the
  fixture and its WER target stay in sync **by construction** (you record exactly what the test scores).

**Decision (needs a tiny consumer-side change): `reference` is the canonical "what was said" for *every* audio case.**
Judge-only cases (e.g. `light_unreachable`) currently have **no** `reference` — the spoken line lives only as prose in
`fixtures/README.md`. Rather than invent a second field, **add `reference` to judge cases too**: it doubles as the
recording script and is harmless to the test (judge cases don't assert WER against it). One field, always the script,
and the README table becomes derivable.

- **Many cases → one fixture** (e.g. `timer_10min` backs 3 cases): dedupe by fixture key. If two cases give *different*
  `reference` for the *same* fixture, that's a YAML inconsistency → **error and name both cases** (the tool surfaces
  drift instead of silently picking one).

## 6. Mic master config (the data/logic split, R5)

Lives in the **consumer**, git-ignored, mirroring `eval/profiles/configs/custom.env`:

```
# eval/profiles/recording.env   (git-ignored; commit a recording.env.example next to it)
REC_INPUT_DEVICE=USB Audio        # name substring OR numeric index (name preferred — indices shift)
REC_CAPTURE_RATE=48000            # device-native capture rate; conditioned down to 16k on save
REC_CAPTURE_CHANNELS=1            # 1 if the mic is mono; >1 is downmixed
REC_COUNTDOWN_S=1                 # beep/countdown before recording starts
REC_GAIN_DB=0                     # optional post-gain
```

The Makefile sources this and passes values via env/flags; locveil-commons reads them, never a consumer path.
`--devices` exists precisely to populate `REC_INPUT_DEVICE`.

## 7. Capture mechanics & format conditioning

- **Capture** at the device-native rate/channels from the config, 16-bit, via `sounddevice`.
- **Stop:** press-Enter-to-stop (default) or `--seconds N`. VAD auto-stop is out of v1 (§10).
- **Condition** to the wire format — *the one place resampling is legitimate* (capture-time conditioning), explicitly
  distinct from the provider's no-resample-on-the-wire stance:
  1. downmix to mono (channel mean), 2. resample to 16 kHz, 3. quantize to PCM16, 4. write with stdlib `wave`.
  - **Prefer native 16 kHz mono capture when the device supports it** → no resampling at all (best fidelity).
    Resample only when the device can't deliver 16 k.
- **Validate** the written file by running it back through `wav_to_pcm16_frames`; if it doesn't satisfy
  sampwidth=2 / mono / rate=16000, fail loudly. The provider's own validator is the recorder's acceptance gate.

## 8. Dependencies & packaging

- New optional extra in `pyproject.toml`:
  ```
  [project.optional-dependencies]
  record = ["sounddevice>=0.4", "numpy>=1.24"]   # + a resampler (see below)
  [project.scripts]
  eval-fixture-record = "eval_commons.record.cli:main"
  ```
- **Resampling (decided, §14):** **native-16 kHz capture first**; resample only when the device can't deliver 16 k,
  via **`soxr`** (small, high-quality). No always-on resample path.
- Core locveil-commons deps are **unchanged**; recording is `pip install -e '../../locveil-commons[record]'` in the
  consumer venv. The script degrades with a clear message if the extra isn't installed.

## 9. Consumer integration

A thin `make record` target in each consumer's `eval/Makefile`, mirroring `make cli` / `make ws`:

```make
record:          ## record missing voice fixtures interactively (needs a mic + [record] extra)
	set -a; -include profiles/recording.env; set +a; \
	eval-fixture-record --from-yaml ws.promptfooconfig.yaml --fixtures-dir fixtures $(FIXTURE)
record-devices:  ## list input devices to fill REC_INPUT_DEVICE
	eval-fixture-record --devices
```

`make record` (all missing), `make record FIXTURE=timer_10min` (one), `make record-list`. The consumer also ships a
committed `profiles/recording.env.example` and updates `fixtures/README.md` to point at `make record` (keeping the
`ffmpeg`/TTS recipe as the non-interactive alternative).

## 10. Scope (deliberate)

**In v1:** targeted + freeform recording · YAML-derived worklist · interactive keep/redo/skip · format conditioning +
validation · device discovery · machine-local mic config · safe-by-default (missing-only).

**Out (flagged, not forgotten):**
- **`--verify`** — after a take, stream it through a *running* SUT's ASR (`/asr/*` or the ws provider) and show the
  transcript so the user confirms recognizability *before* saving. Valuable, but needs a live SUT → deferred (§14).
- **VAD auto-stop** — needs threshold tuning; press-Enter is robust and simple for v1.
- **Batch/non-interactive** capture, **TTS-synthesized** fixtures (the `ffmpeg`/TTS recipe stays as the scripted path),
  non-Russian niceties.

## 11. Risks & gotchas

1. **Resampling degrades the measurement.** A poor resampler corrupts exactly what the ASR test measures. Mitigation:
   prefer native-16k capture; use a quality resampler; validate every write; document the capture-vs-wire distinction
   so nobody later "unifies" the recorder's resample with the provider's no-resample rule.
2. **Device portability.** Indices shift between boots/machines → match by **name** primarily; `--devices` to discover.
3. **Reference drift.** The `reference` is both the recording script and the WER target, so recording keeps them in
   sync *at record time*; but editing `reference` later silently staleness the WAV. v1 documents "re-record on
   reference change"; a content marker/hash to detect it is a v2 idea.
4. **Headless/CI.** Recording is local-human only; the tool must detect "no input device" and exit with guidance, never
   hang. CI never invokes it.
5. **Git-ignored fixtures.** The tool writes into a git-ignored dir; versioning (lfs / ignore-exception) stays the
   consumer's call, already noted in `fixtures/README.md`.

## 12. Testing the tool

The mic + interactive loop can't be unit-tested, so the design factors the **pure** parts to be testable (under
locveil-commons' `dev` extra / pytest):
- `worklist.py` — key extraction, dedup, the same-fixture-conflicting-reference error, missing-on-disk detection.
- `audio.conform_to_pcm16` / `write_pcm16_wav` — feed synthetic frames at various rates/channels, assert the output
  passes `wav_to_pcm16_frames` (downmix correctness, resample to exactly 16 k, sampwidth=2).
- config loading — name-vs-index device resolution, defaults.
`capture.py` / `session.py` stay thin and are exercised manually (smoke) with a real mic.

## 13. Implementation worklist (stands in for ledger tasks)

locveil-commons has no ledger yet, so the follow-up tasks are listed here explicitly; lift them into a ledger if/when one
exists (see §15):

- **W1 — audio:** ✅ `conform_to_pcm16` + `write_pcm16_wav` in `eval_commons/audio/conform.py` (5 unit tests; output
  validated against `wav_to_pcm16_frames`). *(Placed in `audio/conform.py`, not `__init__`, so the core audio module
  stays stdlib/numpy-free for the streaming providers.)*
- **W2 — worklist:** ✅ `record/worklist.py` YAML resolver (5 unit tests; dedup + conflict guard verified against the
  real locveil-voice config via `--list`).
- **W3 — capture:** ✅ `record/capture.py` (sounddevice capture + `query_devices`; `--devices` smoke-verified). Mic
  loop is manual-only by nature.
- **W4 — session:** ✅ `record/session.py` interactive controller (prompt/countdown/record/playback/keep-redo-skip).
  Smoke-only (needs a human at a mic).
- **W5 — CLI + packaging:** ✅ `record/cli.py`, `[project.scripts] eval-fixture-record`, `[record]` extra. `--list` /
  `--devices` / conflict-exit-2 / happy-exit-0 verified. *(README section still TODO.)* *(`--base-dir` replaces the
  design's `--fixtures-dir`: audio paths already carry the `fixtures/` prefix, so the base is the YAML's dir.)*
- **W6 — consumer wiring (locveil-voice first):** ⬜ `make record` + `recording.env.example`; add `reference` to the
  judge case(s) (§5 — `--list` confirms `light_unreachable` has none); repoint `fixtures/README.md` at `make record`.
  Lands in the **locveil-voice repo → needs a ledger task there.** Then mirror for locveil-bridge.
- **W7 — (deferred):** ⬜ `--verify` against a live SUT.

## 14. Decisions (agreed 2026-06-27)

1. **Console-script name** — **`eval-fixture-record`**.
2. **Resampling** — **native-16 kHz capture first, `soxr` as the fallback** when the device can't deliver 16 k (no
   always-resample path). See §7–8.
3. **Mic config format** — **`.env`**, consistent with `profiles/*.env`. See §6.
4. **`--verify` (ASR self-check)** — **deferred** (needs a running SUT); v1 ships without it. See §10/W7.

## 15. Note: locveil-commons has no process scaffolding (left open, by decision)

This repo currently has an **empty `CLAUDE.md`** and no ledger/journal — which is why this doc is exhaustive and
carries its own worklist. locveil-commons will **likely adopt a slightly different process** than the sibling projects,
so that question is **deliberately left open for now** (maintainer's call, 2026-06-27); the invariants are **not** being
ported yet. Until a process exists, treat §13 as the task list and record completion in commit messages. (When the time
comes, the locveil-voice → bridge handoff brief at `../locveil-bridge/INVARIANTS_HANDOFF.md` is a starting point, to be
adapted to whatever shape locveil-commons settles on.)
```
