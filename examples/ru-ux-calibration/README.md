# RU UX judge calibration set

Measures whether the DeepSeek judge's UX pass/fail can be trusted in CI (ARCHITECTURE §7.1;
filed as wb-mqtt-voice TEST-16). 20 canned assistant replies across the two live rubrics
(`confirms_action_ru`, `graceful_failure_ru`), graded through the **same** `llm-rubric` →
DeepSeek path the live suites use, against the **shipped** shared rubric files.

- `promptfooconfig.yaml` — the set (echo provider; asserts reference
  `shared/rubrics/ru/*.txt`).
- `gold_labels.yaml` — human labels (native Russian speaker, 2026-07-02): 16 confident +
  4 `borderline` (excluded from κ; either verdict acceptable).
- `score.py` — joins the eval output with the gold labels → raw agreement, Cohen's κ,
  contingency, per-case disagreements.

Run:

```sh
DEEPSEEK_API_KEY=... promptfoo eval -c promptfooconfig.yaml -o out.json --no-cache
python3 score.py out.json
```

## Results (2026-07-02)

| Rubric iteration | Agreement | κ | Notes |
|---|---|---|---|
| shipped co-equal form | 13/16 = 81% | 0.625 | judge too strict on terse replies («Окей.», short polite failure), too lenient on bureaucratese («код 502, обратитесь к администратору») |
| + terse-passes / bureaucratese-fails / no-next-step-ok | 15/16 = 94% | 0.875 | residual: mixed-language confirmation («Готово! Timer set») passed |
| + in-condition mixed-language example | **16/16 = 100%** | **1.000** | verdicts stable across repeat runs (temp 0); all 4 borderlines got defensible verdicts |

**Verdict: UX pass/fail is CI-trustworthy for the Russian rubrics** — with two standing caveats:

1. **κ = 1.0 is in-sample** — the rubric was tuned on this very set (two iterations). Add fresh
   negatives as the suites grow and re-measure before leaning harder on the number.
2. **Re-run this set after ANY rubric edit.** A previous fix (an emphatic language *override*)
   silently regressed the tone criterion; the co-equal-conditions form plus targeted in-condition
   clarifications is what survived measurement.

The English rubrics (`shared/rubrics/en/*.txt`) carry the same structural improvements but are
**uncalibrated** — build an EN twin of this set if EN UX verdicts ever gate anything.
