"""W2 — worklist derivation from a promptfoo YAML (eval_commons.record.worklist)."""
import textwrap

import pytest

from eval_commons.record.worklist import key_for, missing_jobs, resolve_worklist


def _write(tmp_path, body):
    p = tmp_path / "ws.promptfooconfig.yaml"
    p.write_text(textwrap.dedent(body), encoding="utf-8")
    return str(p)


def test_key_for():
    assert key_for("fixtures/timer_10min.wav") == "timer_10min"
    assert key_for("a/b/c.WAV") == "c"


def test_dedupes_shared_fixture_and_keeps_reference(tmp_path):
    yaml_path = _write(tmp_path, """
        tests:
          - description: ASR
            vars: { audio: fixtures/timer_10min.wav, reference: поставь таймер на десять минут }
          - description: Intent
            vars: { audio: fixtures/timer_10min.wav }
          - description: UX
            vars: { audio: fixtures/timer_10min.wav }
          - description: Failure
            vars: { audio: fixtures/light_unreachable.wav }
    """)
    jobs = {j.key: j for j in resolve_worklist(yaml_path)}
    assert set(jobs) == {"timer_10min", "light_unreachable"}
    assert jobs["timer_10min"].prompt == "поставь таймер на десять минут"
    assert len(jobs["timer_10min"].used_by) == 3          # three cases share it
    assert jobs["light_unreachable"].prompt is None       # judge-only case, no reference


def test_conflicting_reference_raises(tmp_path):
    yaml_path = _write(tmp_path, """
        tests:
          - description: A
            vars: { audio: fixtures/x.wav, reference: один }
          - description: B
            vars: { audio: fixtures/x.wav, reference: два }
    """)
    with pytest.raises(ValueError, match="conflicting reference"):
        resolve_worklist(yaml_path)


def test_missing_jobs(tmp_path):
    (tmp_path / "fixtures").mkdir()
    (tmp_path / "fixtures" / "present.wav").write_bytes(b"x")
    yaml_path = _write(tmp_path, """
        tests:
          - description: A
            vars: { audio: fixtures/present.wav, reference: x }
          - description: B
            vars: { audio: fixtures/absent.wav, reference: y }
    """)
    jobs = resolve_worklist(yaml_path)
    missing = {j.key for j in missing_jobs(jobs, str(tmp_path))}
    assert missing == {"absent"}


def test_cases_without_audio_ignored(tmp_path):
    yaml_path = _write(tmp_path, """
        tests:
          - description: cli-ish
            vars: { cmd: "do-thing --flag" }
          - description: audio
            vars: { audio: fixtures/only.wav, reference: текст }
    """)
    jobs = resolve_worklist(yaml_path)
    assert [j.key for j in jobs] == ["only"]
