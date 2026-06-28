"""Keep-on-failure trace capture (eval_commons.failures, D-13)."""
import json

from eval_commons.failures import keep_failure_traces, _find_request_id, _is_failure


def _traces(tmp_path, *ids):
    d = tmp_path / "run"
    d.mkdir()
    for rid in ids:
        (d / f"{rid}.json").write_text(json.dumps({"request_id": rid}), encoding="utf-8")
    return d


def _results(tmp_path, records):
    # promptfoo's nested shape: {"results": {"results": [...]}}
    p = tmp_path / "results.json"
    p.write_text(json.dumps({"results": {"results": records}}), encoding="utf-8")
    return p


def test_copies_only_failing_traces(tmp_path):
    traces = _traces(tmp_path, "ok1", "bad1", "bad2")
    results = _results(tmp_path, [
        {"success": True,  "response": {"output": {"metadata": {"request_id": "ok1"}}}},
        {"success": False, "response": {"output": {"metadata": {"request_id": "bad1"}}}},
        {"success": False, "response": {"output": {"metadata": {"request_id": "bad2"}}}},
    ])
    out = tmp_path / "failures"
    copied = keep_failure_traces(results, traces, out)
    assert {p.stem for p in copied} == {"bad1", "bad2"}
    assert {p.stem for p in out.glob("*.json")} == {"bad1", "bad2"}
    # without --prune the source is untouched
    assert {p.stem for p in traces.glob("*.json")} == {"ok1", "bad1", "bad2"}


def test_prune_drops_non_failing_from_source(tmp_path):
    traces = _traces(tmp_path, "ok1", "bad1")
    results = _results(tmp_path, [
        {"success": True,  "response": {"output": {"metadata": {"request_id": "ok1"}}}},
        {"success": False, "response": {"output": {"metadata": {"request_id": "bad1"}}}},
    ])
    keep_failure_traces(results, traces, tmp_path / "failures", prune=True)
    assert {p.stem for p in traces.glob("*.json")} == {"bad1"}  # only the failure survives


def test_output_as_json_string_and_gradingresult_shape(tmp_path):
    # provider output stored as a JSON string + pass flag under gradingResult (version drift)
    traces = _traces(tmp_path, "bad1")
    results = _results(tmp_path, [
        {"gradingResult": {"pass": False},
         "response": {"output": json.dumps({"metadata": {"request_id": "bad1"}})}},
    ])
    copied = keep_failure_traces(results, traces, tmp_path / "failures")
    assert [p.stem for p in copied] == ["bad1"]


def test_missing_trace_skipped_quietly(tmp_path):
    traces = _traces(tmp_path)  # empty — case failed before a trace was written
    results = _results(tmp_path, [
        {"success": False, "response": {"output": {"metadata": {"request_id": "gone"}}}},
    ])
    assert keep_failure_traces(results, traces, tmp_path / "failures") == []


def test_find_request_id_recursive():
    assert _find_request_id({"a": {"metadata": {"request_id": "x"}}}) == "x"
    assert _find_request_id('{"metadata": {"request_id": "y"}}') == "y"
    assert _find_request_id({"no": "id"}) is None


def test_is_failure_variants():
    assert _is_failure({"success": False})
    assert not _is_failure({"success": True})
    assert _is_failure({"gradingResult": {"pass": False}})
    assert not _is_failure({"unknown": "shape"})  # unclassifiable → not a failure
