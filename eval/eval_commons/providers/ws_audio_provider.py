"""promptfoo Python provider: drive a stateful streaming-ASR WebSocket endpoint.

Speaks the locveil-voice `/ws/audio` protocol (see irene/runners/webapi_router.py):

    client → TEXT  {"type":"register","client_id":..,"room_name":..,"sample_rate":16000,
                    "wants_audio":false,"mode":"streaming"}
    server → TEXT  {"type":"registered","client_id":..,"session_id":..}
    client → BINARY  raw PCM16 frames (16-bit signed, mono)
    client → TEXT  {"type":"end"}
    server → TEXT  {"type":"partial","text":..}            # 0+ times, streaming mode only
    server → TEXT  {"type":"response","text":..,"success":bool,"error":..,"confidence":..,
                    "intent_name":..,"timestamp":..,"metadata":{..}}
                   # QUAL-55 canonical result shape: `intent_name` is a TOP-LEVEL key (older
                   # SUT builds carried it under metadata.intent_name — read with fallback).
                   # metadata.audio_processing.transcribed_text holds the RECOGNIZED speech on
                   # the batch/offline-ASR path (where no `partial`s are emitted); the WER tier
                   # reads it so it scores ASR accuracy, not the assistant's reply.

This protocol is stateful + binary, so promptfoo's built-in declarative WebSocket
provider cannot drive it — hence this shared custom provider.

promptfoo entrypoint:  call_api(prompt, options, context) -> {"output": str}

`prompt`  : path to a WAV fixture (16 kHz mono PCM16 recommended) OR, if config.text is
            set, ignored (text-injection mode for backends that accept it).
`config`  : {
              ws_url:        "ws://localhost:6000/ws/audio",
              client_id:     "eval_node",
              room_name:     "Тест",
              sample_rate:   16000,
              mode:          "streaming" | "single",
              frame_ms:      32,
              connect_timeout_s: 5,
              response_timeout_s: 30,
              return_mode:   "full" | "transcript" | "response_text",
            }

`return_mode` (see ARCHITECTURE.md §4) controls the output shape so one provider serves
both deterministic (WER/intent) and UX-judge assertions.
"""

from __future__ import annotations

import asyncio
import json
from typing import Any, Dict, List

from eval_commons.audio import wav_to_pcm16_frames


def call_api(prompt: str, options: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    config = (options or {}).get("config", {}) or {}
    try:
        result = asyncio.run(_run(prompt, config))
    except Exception as exc:  # surface transport failures as a provider error, not a crash
        return {"error": f"ws_audio_provider failed: {type(exc).__name__}: {exc}"}

    return_mode = config.get("return_mode", "full")
    if return_mode == "transcript":
        return {"output": result["transcript"]}
    if return_mode == "response_text":
        return {"output": result["response_text"]}
    return {"output": json.dumps(result, ensure_ascii=False)}


async def _run(prompt: str, config: Dict[str, Any]) -> Dict[str, Any]:
    # Imported lazily so the package is importable without `websockets` until first use.
    import time

    import websockets

    ws_url = config.get("ws_url", "ws://localhost:6000/ws/audio")
    sample_rate = int(config.get("sample_rate", 16000))
    mode = config.get("mode", "streaming")
    frame_ms = int(config.get("frame_ms", 32))
    response_timeout = float(config.get("response_timeout_s", 30))

    register = {
        "type": "register",
        "client_id": config.get("client_id", "eval_node"),
        "room_name": config.get("room_name", "Тест"),
        "sample_rate": sample_rate,
        "wants_audio": False,
        "mode": mode,
    }

    partials: List[str] = []
    final: Dict[str, Any] = {}
    started = time.monotonic()

    async with websockets.connect(ws_url, open_timeout=float(config.get("connect_timeout_s", 5))) as ws:
        await ws.send(json.dumps(register))
        registered = json.loads(await asyncio.wait_for(ws.recv(), timeout=response_timeout))
        if registered.get("type") != "registered":
            raise RuntimeError(f"expected 'registered', got {registered!r}")

        # Stream the fixture as PCM16 frames. config.text would be an alternative injection
        # path for backends that accept text instead of audio (left for the consuming project).
        for frame in wav_to_pcm16_frames(prompt, sample_rate=sample_rate, frame_ms=frame_ms):
            await ws.send(frame)
        await ws.send(json.dumps({"type": "end"}))

        while True:
            msg = json.loads(await asyncio.wait_for(ws.recv(), timeout=response_timeout))
            mtype = msg.get("type")
            if mtype == "partial":
                partials.append(msg.get("text", ""))
            elif mtype == "response":
                final = msg
                break
            elif mtype == "error":
                raise RuntimeError(f"server error: {msg.get('error')}")
            # ignore any other control frames

    metadata = final.get("metadata", {}) or {}
    # Recognized transcript, in priority order:
    #   1. metadata.audio_processing.transcribed_text — the authoritative ASR output the SUT
    #      surfaces on the batch path (offline ASR like sherpa_onnx/vosk emits no `partial`s,
    #      so this is the only place the *recognized speech* — not the reply — is exposed).
    #   2. the last streaming `partial` — the recognized text when the SUT streams ASR.
    #   3. the reply text — last-resort proxy so WER stays defined if neither is present.
    asr_text = ((metadata.get("audio_processing") or {}).get("transcribed_text") or "").strip()
    transcript = asr_text or (partials[-1] if partials else final.get("text", ""))
    return {
        "transcript": transcript,
        "response_text": final.get("text", ""),
        # QUAL-55 canonical shape puts intent_name top-level; older SUT builds (QUAL-54)
        # carried it under metadata — read both so the provider spans SUT versions.
        "intent_name": final.get("intent_name") or metadata.get("intent_name"),
        "success": bool(final.get("success", False)),
        "partials": partials,
        "latency_ms": round((time.monotonic() - started) * 1000, 1),
        "metadata": metadata,
    }
