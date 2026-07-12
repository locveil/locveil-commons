"""promptfoo Python assertion for the device-command producer tests (TEST-18 Slice B).

Compares the provider's envelope (`{"captured": [...], "reply": {...}}`) against the
crossover fixture's `expect` (passed as the test var `expect`, verbatim from
`contracts/pins/crossover-fixtures/crossover_fixtures.json`):

- actuate / room-group : exactly ONE command captured, dict-equal to `expect` minus `kind`-
                         irrelevant keys (the capture is already fixture-shaped);
- clarify              : NO command captured; the reply is a clarification whose candidate
                         set equals `expect.candidates`;
- read                 : at least one read captured whose device is one of the accepted
                         targets (`device_id` or `any_of[*].device_id`).

promptfoo entrypoint: get_assert(output, context) -> GradingResult dict
"""

from __future__ import annotations

import json
from typing import Any, Dict


def _fail(reason: str) -> Dict[str, Any]:
    return {"pass": False, "score": 0.0, "reason": reason}


def _ok(reason: str = "matched") -> Dict[str, Any]:
    return {"pass": True, "score": 1.0, "reason": reason}


def get_assert(output: str, context: Dict[str, Any]) -> Dict[str, Any]:
    expect = (context.get("vars") or {}).get("expect")
    if isinstance(expect, str):  # promptfoo may pass structured vars as JSON strings
        expect = json.loads(expect)
    if not isinstance(expect, dict):
        return _fail("test var 'expect' missing or malformed")

    try:
        envelope = json.loads(output)
    except (TypeError, json.JSONDecodeError):
        return _fail(f"provider output is not the JSON envelope: {output!r:.200}")
    if "error" in envelope:
        return _fail(envelope["error"])

    captured = envelope.get("captured", [])
    reply = envelope.get("reply", {})
    kind = expect.get("kind")

    if kind in ("actuate", "room-group"):
        commands = [c for c in captured if c.get("kind") in ("actuate", "room-group")]
        if len(commands) != 1:
            return _fail(f"expected exactly 1 canonical command, captured {len(commands)}: "
                         f"{commands} (reply: {reply.get('text')!r})")
        got = commands[0]
        # the capture is fixture-shaped; compare only the keys the fixture pins
        mismatches = {k: (v, got.get(k)) for k, v in expect.items() if got.get(k) != v}
        if mismatches:
            return _fail(f"command mismatch {mismatches} (captured {got})")
        return _ok()

    if kind == "clarify":
        commands = [c for c in captured if c.get("kind") != "read"]
        if commands:
            return _fail(f"expected a clarification but a command was emitted: {commands}")
        metadata = reply.get("metadata") or {}
        if not metadata.get("clarification"):
            return _fail(f"reply is not a clarification: {reply.get('text')!r}")
        want = set(expect.get("candidates") or [])
        got_candidates = set(metadata.get("candidates") or [])
        if want and got_candidates and want != got_candidates:
            return _fail(f"clarification candidates {got_candidates} != expected {want}")
        return _ok()

    if kind == "read":
        accepted = {t["device_id"] for t in expect.get("any_of", [])} \
            if "any_of" in expect else {expect.get("device_id")}
        reads = [c for c in captured if c.get("kind") == "read"]
        if not reads:
            return _fail(f"no state read captured (reply: {reply.get('text')!r})")
        if not any(r.get("device_id") in accepted for r in reads):
            return _fail(f"read hit {[r.get('device_id') for r in reads]}, "
                         f"expected one of {sorted(accepted)}")
        return _ok()

    return _fail(f"unknown expect kind: {kind!r}")
