"""promptfoo Python assertion: WER/CER scoring via jiwer.

No eval tool in scope ships WER/CER, so this is the bespoke ASR-accuracy scorer.

promptfoo entrypoint:  get_assert(output, context) -> {pass, score, reason}

The provider `output` may be:
  - a JSON string (return_mode=full)        → we read the `transcript` field, OR
  - the plain recognized transcript string  (return_mode=transcript).

Test vars consumed (from `context["vars"]`):
    reference       : the ground-truth transcript (required)
    wer_threshold   : max acceptable WER (default 0.20)
    metric          : "wer" (default) | "cer"

Russian normalization: NFC, lowercase, strip punctuation, collapse whitespace, and map ё→е
(common ASR/reference mismatch). Override by passing normalize=false in vars to compare raw.
"""

from __future__ import annotations

import json
import re
import unicodedata
from typing import Any, Dict


# English cardinal number-words → digits, so an ASR that writes "10" and a reference that says "ten"
# (or vice versa) don't count as a WER substitution — the recognition is correct either way. Covers the
# common small cardinals that show up in voice commands; unknown words pass through unchanged.
_EN_NUM = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12",
    "thirteen": "13", "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
    "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30", "forty": "40",
    "fifty": "50", "sixty": "60", "seventy": "70", "eighty": "80", "ninety": "90",
    "hundred": "100", "thousand": "1000",
}


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text or "").lower().replace("ё", "е")
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip()
    return " ".join(_EN_NUM.get(w, w) for w in text.split())


def _extract_transcript(output: str) -> str:
    output = output or ""
    stripped = output.strip()
    if stripped.startswith("{"):
        try:
            return json.loads(stripped).get("transcript", "") or ""
        except json.JSONDecodeError:
            pass
    return output


def get_assert(output: str, context: Dict[str, Any]) -> Dict[str, Any]:
    import jiwer  # lazy import

    vars_ = (context or {}).get("vars", {}) or {}
    reference = vars_.get("reference")
    if reference is None:
        return {"pass": False, "score": 0.0, "reason": "wer_scorer: missing `reference` var"}

    threshold = float(vars_.get("wer_threshold", 0.20))
    metric = vars_.get("metric", "wer")
    do_norm = vars_.get("normalize", True)

    hypothesis = _extract_transcript(output)
    ref, hyp = (
        (_normalize(reference), _normalize(hypothesis)) if do_norm else (reference, hypothesis)
    )

    score_fn = jiwer.cer if metric == "cer" else jiwer.wer
    error_rate = float(score_fn(ref, hyp))
    passed = error_rate <= threshold

    return {
        "pass": passed,
        "score": max(0.0, 1.0 - error_rate),  # higher is better, for promptfoo aggregation
        "reason": (
            f"{metric.upper()}={error_rate:.3f} (threshold {threshold:.2f}) "
            f"| ref='{ref}' hyp='{hyp}'"
        ),
    }
