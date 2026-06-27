"""Capture-time audio conditioning: arbitrary mic input → 16 kHz mono PCM16 WAV.

This is the ONE place resampling is legitimate (conditioning a recording on the way to
disk), deliberately distinct from `wav_to_pcm16_frames` in this package, which refuses to
resample on the wire so tests measure the ASR, not a converter. See
`docs/design/fixture_recorder.md` §7.

`numpy` is imported at module top because this module is reached only on the recorder path
(the `record` optional extra). The core `eval_commons.audio` (`wav_to_pcm16_frames`) stays
stdlib-only so the streaming providers never pull numpy.
"""
from __future__ import annotations

import wave

import numpy as np

TARGET_RATE = 16000


def conform_to_pcm16(audio: "np.ndarray", src_rate: int) -> bytes:
    """Downmix to mono, resample to 16 kHz, quantize to little-endian PCM16; return raw bytes.

    `audio` is shaped `(n,)` (mono) or `(n, channels)`; dtype float (assumed in [-1, 1]) or
    a signed-integer PCM type. Native-16 kHz input skips the resampler entirely (best fidelity);
    `soxr` is imported lazily only when a resample is actually needed.
    """
    a = np.asarray(audio)
    if a.size == 0:
        return b""

    # → float32 in [-1, 1]
    if np.issubdtype(a.dtype, np.integer):
        peak = float(max(abs(int(np.iinfo(a.dtype).min)), int(np.iinfo(a.dtype).max)))
        a = a.astype(np.float32) / peak
    else:
        a = a.astype(np.float32)

    # downmix to mono
    if a.ndim == 2:
        a = a.mean(axis=1)
    elif a.ndim != 1:
        raise ValueError(f"expected 1-D or 2-D audio, got shape {a.shape}")

    # resample only when the device couldn't give us 16 kHz (native-16k-first)
    if src_rate != TARGET_RATE:
        import soxr

        a = soxr.resample(a, src_rate, TARGET_RATE)

    # quantize to PCM16 (clip guards the +1.0 edge from overflowing)
    pcm = (np.clip(a, -1.0, 1.0) * 32767.0).round().astype("<i2")
    return pcm.tobytes()


def write_pcm16_wav(path: str, pcm: bytes, rate: int = TARGET_RATE) -> None:
    """Write raw mono PCM16 `pcm` bytes to a WAV file at `rate` (default 16 kHz)."""
    with wave.open(path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(pcm)
