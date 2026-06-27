"""W1 — audio conditioning (eval_commons.audio.conform) → must produce files the provider's
own validator (wav_to_pcm16_frames) accepts."""
import numpy as np

from eval_commons.audio import wav_to_pcm16_frames
from eval_commons.audio.conform import conform_to_pcm16, write_pcm16_wav


def _validates(path, rate=16000):
    # exhaust the generator; it raises ValueError on a non-conformant file
    list(wav_to_pcm16_frames(path, sample_rate=rate))
    return True


def test_native_16k_mono_roundtrips(tmp_path):
    t = np.linspace(0, 1, 16000, endpoint=False, dtype=np.float32)
    sig = 0.5 * np.sin(2 * np.pi * 440 * t)
    pcm = conform_to_pcm16(sig, 16000)
    assert len(pcm) == 16000 * 2  # one int16 per sample, no resample
    out = tmp_path / "a.wav"
    write_pcm16_wav(str(out), pcm)
    assert _validates(str(out))


def test_downmix_stereo_to_mono(tmp_path):
    n = 16000
    stereo = np.zeros((n, 2), dtype=np.float32)
    stereo[:, 0] = 0.4
    stereo[:, 1] = -0.4  # mean → ~0
    pcm = conform_to_pcm16(stereo, 16000)
    assert len(pcm) == n * 2  # mono output, same sample count
    arr = np.frombuffer(pcm, dtype="<i2")
    assert abs(int(arr.mean())) < 50  # cancelled to near-silence
    out = tmp_path / "b.wav"
    write_pcm16_wav(str(out), pcm)
    assert _validates(str(out))


def test_resample_48k_to_16k(tmp_path):
    secs = 0.5
    t = np.linspace(0, secs, int(48000 * secs), endpoint=False, dtype=np.float32)
    sig = 0.3 * np.sin(2 * np.pi * 220 * t)
    pcm = conform_to_pcm16(sig, 48000)
    got = len(pcm) // 2
    assert abs(got - int(16000 * secs)) <= 2  # resampled to 16 kHz length
    out = tmp_path / "c.wav"
    write_pcm16_wav(str(out), pcm)
    assert _validates(str(out))


def test_int16_input_scaled(tmp_path):
    sig = (np.ones(16000) * 16000).astype(np.int16)
    pcm = conform_to_pcm16(sig, 16000)
    arr = np.frombuffer(pcm, dtype="<i2")
    assert 15000 < int(arr.mean()) < 17000  # preserved magnitude through int→float→int


def test_empty_is_empty():
    assert conform_to_pcm16(np.zeros((0,), dtype=np.float32), 16000) == b""
