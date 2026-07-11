"""Audio helpers for streaming providers: WAV → PCM16 frames."""

from __future__ import annotations

import wave
from typing import Iterator


def wav_to_pcm16_frames(path: str, sample_rate: int = 16000, frame_ms: int = 32) -> Iterator[bytes]:
    """Yield raw PCM16 (16-bit signed, mono) frames of ~`frame_ms` from a WAV file.

    Validates the fixture matches the negotiated `sample_rate` and is 16-bit mono — the
    /ws/audio contract expects raw PCM16 with no resampling on the wire. Resampling /
    format conversion is intentionally out of scope: keep fixtures in the target format so
    tests measure the ASR, not our converter.
    """
    with wave.open(path, "rb") as wf:
        if wf.getsampwidth() != 2:
            raise ValueError(f"{path}: expected 16-bit PCM (sampwidth=2), got {wf.getsampwidth()}")
        if wf.getnchannels() != 1:
            raise ValueError(f"{path}: expected mono, got {wf.getnchannels()} channels")
        if wf.getframerate() != sample_rate:
            raise ValueError(
                f"{path}: sample_rate {wf.getframerate()} != negotiated {sample_rate}; "
                "re-record/resample the fixture to match."
            )
        frames_per_chunk = max(1, int(sample_rate * frame_ms / 1000))
        while True:
            chunk = wf.readframes(frames_per_chunk)
            if not chunk:
                return
            yield chunk
