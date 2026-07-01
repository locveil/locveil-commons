"""Derive the fixture recording worklist from a promptfoo YAML (the single source of truth).

Each test case's `vars.audio` names a fixture; `vars.reference` is the line to read aloud.
The fixture KEY is the basename of the audio path without extension — the same join key the
YAML already uses. Many cases may share one fixture; we dedupe by key and error if two cases
give conflicting reference text for the same fixture (a YAML inconsistency worth surfacing).

Pure (only `pyyaml`) — no audio deps — so `--list` works without the `record` extra.
See `docs/design/fixture_recorder.md` §5.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import List, Optional

import yaml

# `{{env.VAR}}` in an audio path (e.g. fixtures/{{env.EVAL_LANG}}/timer_10min.wav) — the recorder reads
# RAW YAML (promptfoo isn't in the loop), so resolve these against os.environ ourselves. Mirrors the
# subset of promptfoo's {{env.*}} that appears in `vars.audio`.
_ENV_RE = re.compile(r"\{\{\s*env\.(\w+)\s*\}\}")


def _render_env(text: str) -> str:
    return _ENV_RE.sub(lambda m: os.environ.get(m.group(1), ""), text)


@dataclass
class FixtureJob:
    key: str
    path: str                       # audio path exactly as written in the YAML
    prompt: Optional[str] = None    # `reference` text to read aloud; None if the case has none
    used_by: List[str] = field(default_factory=list)  # case descriptions referencing this fixture


def key_for(audio_path: str) -> str:
    """`fixtures/timer_10min.wav` → `timer_10min`."""
    return os.path.splitext(os.path.basename(audio_path))[0]


def resolve_worklist(yaml_path: str, language: Optional[str] = None) -> List[FixtureJob]:
    """Parse a promptfoo config and return one `FixtureJob` per distinct fixture.

    `language` (from EVAL_LANG) selects one language when cases are duplicated per language and tagged
    `metadata.language` — so the two languages' same-named fixtures (fixtures/<lang>/timer_10min.wav)
    don't collide on key or conflict on reference text. Cases with no `language` tag always match
    (single-language YAMLs stay unchanged). `{{env.VAR}}` in the audio path is resolved against the
    environment (EVAL_LANG → the language subdir)."""
    with open(yaml_path, encoding="utf-8") as f:
        doc = yaml.safe_load(f) or {}

    jobs: "dict[str, FixtureJob]" = {}
    for case in doc.get("tests") or []:
        if not isinstance(case, dict):
            continue
        case_lang = (case.get("metadata") or {}).get("language")
        if language and case_lang and case_lang != language:
            continue  # a different language's case — skip
        vars_ = case.get("vars") or {}
        audio = vars_.get("audio")
        if not audio:
            continue
        audio = _render_env(audio)  # fixtures/{{env.EVAL_LANG}}/… → fixtures/<lang>/…
        key = key_for(audio)
        prompt = vars_.get("reference")
        desc = case.get("description", "<case>")

        job = jobs.get(key)
        if job is None:
            jobs[key] = FixtureJob(key=key, path=audio, prompt=prompt, used_by=[desc])
            continue
        if prompt and job.prompt and prompt.strip() != job.prompt.strip():
            raise ValueError(
                f"fixture '{key}': conflicting reference text between cases "
                f"'{job.used_by[0]}' and '{desc}':\n  {job.prompt!r}\n  {prompt!r}"
            )
        job.prompt = job.prompt or prompt
        job.used_by.append(desc)

    return list(jobs.values())


def missing_jobs(jobs: List[FixtureJob], base_dir: str) -> List[FixtureJob]:
    """Subset of `jobs` whose fixture file does not yet exist under `base_dir`."""
    return [j for j in jobs if not os.path.exists(os.path.join(base_dir, j.path))]
