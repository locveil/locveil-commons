# eval-commons

Shared, **declarative (YAML-first)** test & evaluation providers, reused across multiple
projects. Code lives here once; **consuming projects carry only YAML.**

- **System tests** — deterministic assertions over WebSocket / MQTT / HTTP transports.
- **UX tests** — judged by an LLM acting as a human (**DeepSeek** judge).
- **UI simulation** — goal-driven browser agent *(Phase 2)*.

Full rationale, component model, reuse strategy, and risks: **[ARCHITECTURE.md](ARCHITECTURE.md)**.

## What's here

```
eval_commons/providers/   ws_audio · mqtt · sim_user (1.5 stub) · ui (2 stub)
eval_commons/assertions/  wer_scorer (jiwer WER/CER)
eval_commons/audio/       WAV → PCM16 frame helpers
shared/                   deepseek-judge.yaml · promptfooconfig.base.yaml · rubrics/ru-ux.yaml
examples/                 .env.example
```

## Quick start (from a consuming project)

```bash
# 1. Runner (the only npm dep projects need)
npm install -g promptfoo            # or: npx promptfoo@latest

# 2. This package (for the Python providers/assertions)
pip install -e /path/to/eval-commons    # or just reference the files by path

# 3. Wire your project's eval/promptfooconfig.yaml at the shared providers + judge,
#    then write YAML test cases. See wb-mqtt-voice/eval/ for a worked example.
export DEEPSEEK_API_KEY=sk-...
promptfoo eval -c eval/promptfooconfig.yaml
```

## Versioning across projects

promptfoo has no packaged-config install, so each project references this repo by
`file://` path into a **pinned checkout** (git submodule or tagged sibling clone). Pin per
project so provider changes are explicit, reviewed bumps — never silent breaks across N
projects. See ARCHITECTURE.md §3.
