"""Microphone capture via `sounddevice`. Reached only on the recorder path (the `record`
extra); `sounddevice`/`numpy` are imported lazily so `--list` works without them.
See `docs/design/fixture_recorder.md` §7.
"""
from __future__ import annotations

import sys
import time
from typing import Optional, Union


def list_devices() -> str:
    """Human-readable table of audio devices (for filling `REC_INPUT_DEVICE`)."""
    import sounddevice as sd

    return str(sd.query_devices())


def resolve_device(spec: Union[str, int, None]) -> Optional[int]:
    """Resolve a config value → a sounddevice input-device index.

    `spec` may be None/'' (system default), a numeric index, or a case-insensitive name
    substring (preferred — indices shift between boots/machines).
    """
    if spec is None or spec == "":
        return None
    try:
        return int(spec)
    except (TypeError, ValueError):
        pass
    import sounddevice as sd

    spec_l = str(spec).lower()
    for i, dev in enumerate(sd.query_devices()):
        if dev["max_input_channels"] > 0 and spec_l in dev["name"].lower():
            return i
    raise ValueError(f"no input device matching {spec!r}; run with --devices to list them")


def _countdown(seconds: float) -> None:
    for n in range(int(seconds), 0, -1):
        print(f"    recording in {n}…", end="\r", flush=True)
        time.sleep(1)
    print(" " * 30, end="\r")


def record_until_enter(rate: int, channels: int, device, countdown_s: float = 1.0):
    """Record until the user presses Enter; returns a float32 array shaped (n, channels)."""
    import numpy as np
    import sounddevice as sd

    _countdown(countdown_s)
    chunks = []
    stream = sd.InputStream(
        samplerate=rate, channels=channels, device=device, dtype="float32",
        callback=lambda indata, frames, t, status: chunks.append(indata.copy()),
    )
    print("    ● recording — press Enter to stop", flush=True)
    with stream:
        input()
    return np.concatenate(chunks) if chunks else np.zeros((0, channels), dtype="float32")


def record_seconds(rate: int, channels: int, device, seconds: float, countdown_s: float = 1.0):
    """Fixed-duration capture; returns a float32 array shaped (n, channels)."""
    import sounddevice as sd

    _countdown(countdown_s)
    print(f"    ● recording {seconds:g}s…", flush=True)
    audio = sd.rec(int(seconds * rate), samplerate=rate, channels=channels,
                   device=device, dtype="float32")
    sd.wait()
    return audio


def play(audio, rate: int) -> None:
    """Play back a captured array (for the keep/redo decision)."""
    import sounddevice as sd

    sd.play(audio, rate)
    sd.wait()
