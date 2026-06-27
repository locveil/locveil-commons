"""Interactive record loop: prompt → record → playback → keep / redo / skip.

Thin glue over `capture` (mic) and `audio.conform` (conditioning + write). Kept thin on
purpose — the testable logic lives in `worklist` and `audio.conform`; this orchestrates a
human at a microphone and can only be smoke-tested. See `docs/design/fixture_recorder.md` §4/§7.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from ..audio import wav_to_pcm16_frames
from ..audio.conform import conform_to_pcm16, write_pcm16_wav
from .capture import play, record_seconds, record_until_enter
from .worklist import FixtureJob


@dataclass
class Mic:
    device: object
    rate: int
    channels: int
    countdown_s: float


def _validate(path: str) -> None:
    """Acceptance gate: run the saved file through the provider's own format validator."""
    for _ in wav_to_pcm16_frames(path):  # first pull triggers sampwidth/mono/rate checks
        break


def record_one(job: FixtureJob, out_path: str, mic: Mic, seconds: Optional[float] = None) -> bool:
    """Run the interactive loop for one fixture. Returns True if saved, False if skipped."""
    print(f"\n=== {job.key}  →  {out_path}")
    print(f"    say: «{job.prompt}»" if job.prompt else "    (no reference text — freeform)")
    if job.used_by:
        print(f"    used by: {', '.join(job.used_by)}")

    while True:
        audio = (record_seconds(mic.rate, mic.channels, mic.device, seconds, mic.countdown_s)
                 if seconds else
                 record_until_enter(mic.rate, mic.channels, mic.device, mic.countdown_s))

        if len(audio) == 0:
            print("    (nothing captured)")
        else:
            print("    ▶ playback")
            play(audio, mic.rate)

        choice = input("    [k]eep / [r]e-record / [s]kip ? ").strip().lower()
        if choice.startswith("k"):
            if len(audio) == 0:
                print("    nothing to keep — recording again")
                continue
            pcm = conform_to_pcm16(audio, mic.rate)
            os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
            write_pcm16_wav(out_path, pcm)
            _validate(out_path)
            print(f"    ✓ saved {out_path}")
            return True
        if choice.startswith("s"):
            print("    skipped")
            return False
        # anything else → re-record
