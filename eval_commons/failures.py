"""Keep-on-failure trace capture (D-13 / wb-mqtt-voice TEST-13) — project-agnostic.

After a promptfoo run whose SUT was launched with tracing, read the results JSON and, for every
FAILING test, copy its trace ``<traces_dir>/<request_id>.json`` into ``<out>/`` (default
``traces/failures``), optionally pruning the rest. The SUT surfaces ``request_id`` in each
response's ``metadata`` (the correlation enabler) and writes one ``<request_id>.json`` per request,
so a failing case becomes replayable (``--listen``/``--step``) from the *actual* failing run.

No project specifics — wb-mqtt-bridge (and any future consumer) reuses this unchanged. It honours the
harness rule: execution/glue logic lives in eval-commons; projects carry YAML + a thin Makefile that
invokes ``python -m eval_commons.failures`` from the ``ws`` target.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, List, Optional, Set


def _load_results(path: Path) -> List[dict]:
    """Return the per-test result records, tolerant of promptfoo's nesting/version drift.

    promptfoo `-o results.json` nests as ``{"results": {"results": [...]}}``; also accept a bare
    list or ``{"results": [...]}``.
    """
    doc = json.loads(path.read_text(encoding="utf-8"))
    node: Any = doc.get("results", doc) if isinstance(doc, dict) else doc
    if isinstance(node, dict):
        node = node.get("results", [])
    return node if isinstance(node, list) else []


def _is_failure(result: dict) -> bool:
    """A result failed if its success/pass flag is falsey (the flag's name varies across versions)."""
    if "success" in result:
        return not result["success"]
    grading = result.get("gradingResult") or {}
    if "pass" in grading:
        return not grading["pass"]
    return False  # unknown shape → treat as pass (never hoard traces we can't classify)


def _find_request_id(obj: Any) -> Optional[str]:
    """Recursively locate a ``request_id`` (parsing embedded JSON strings) — robust to however
    promptfoo wraps a Python provider's dict output in the results JSON."""
    if isinstance(obj, str):
        s = obj.strip()
        if s[:1] in ("{", "["):
            try:
                return _find_request_id(json.loads(s))
            except Exception:
                return None
        return None
    if isinstance(obj, dict):
        rid = obj.get("request_id")
        if isinstance(rid, str) and rid:
            return rid
        for value in obj.values():
            found = _find_request_id(value)
            if found:
                return found
        return None
    if isinstance(obj, list):
        for value in obj:
            found = _find_request_id(value)
            if found:
                return found
    return None


def keep_failure_traces(results_path, traces_dir, out_dir, prune: bool = False) -> List[Path]:
    """Copy every failing case's ``<request_id>.json`` from `traces_dir` into `out_dir`.

    Returns the list of copied paths. With ``prune=True`` the non-failing traces in `traces_dir`
    are deleted (keep only the failures — the rest are noise). Missing traces are skipped quietly
    (a case can fail before the SUT writes a trace, e.g. a transport error).
    """
    results_path, traces_dir, out_dir = Path(results_path), Path(traces_dir), Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    kept: Set[str] = set()
    copied: List[Path] = []
    for result in _load_results(results_path):
        if not _is_failure(result):
            continue
        rid = _find_request_id(result)
        if not rid:
            continue
        src = traces_dir / f"{rid}.json"
        if not src.exists():
            continue
        dst = out_dir / f"{rid}.json"
        shutil.copy2(src, dst)
        copied.append(dst)
        kept.add(rid)
    if prune:
        for trace in traces_dir.glob("*.json"):
            if trace.stem not in kept:
                trace.unlink()
    return copied


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(prog="eval-keep-failures", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--results", required=True, help="promptfoo results JSON (from `promptfoo eval -o`)")
    p.add_argument("--traces-dir", required=True, help="dir where the SUT wrote <request_id>.json traces")
    p.add_argument("--out", default="traces/failures", help="dir to copy failing traces into")
    p.add_argument("--prune", action="store_true", help="delete the non-failing traces from --traces-dir")
    a = p.parse_args(argv)
    copied = keep_failure_traces(a.results, a.traces_dir, a.out, prune=a.prune)
    print(f"kept {len(copied)} failing trace(s) in {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
