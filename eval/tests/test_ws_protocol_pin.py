"""The eval WS provider vs the pinned ws-protocol (IMPL-19; HK-13 rider).

`eval_commons/providers/ws_audio_provider.py` IMPLEMENTS voice's WebSocket protocol.
The protocol is pinned here — the document plus its machine core — at
contracts/pins/ws-protocol/, and this test is that pin's conformance test: hermetic, no
server, no sibling checkout. It holds the provider to the pinned definitions from both
directions: what it SENDS must be a valid `audio` client frame, and it must do the right
thing with every server frame the core calls valid, unknown or terminal.
"""
import json
from pathlib import Path

import pytest

from eval_commons.providers import ws_audio_provider as provider

REPO = Path(__file__).resolve().parents[2]
PIN_DIR = REPO / "contracts/pins/ws-protocol"
PIN = json.loads((PIN_DIR / "PIN.json").read_text(encoding="utf-8"))
CORE = json.loads((PIN_DIR / "frames.golden.json").read_text(encoding="utf-8"))
FRAMES = CORE["frames"]

JSON_TYPES = {"string": str, "integer": int, "boolean": bool, "array": list, "object": dict,
              "number": (int, float)}


def _cases(frame: str, verdict: str) -> list[dict]:
    """Live cases only: a RETIRED case states nothing (the guide's harness rule) — the
    server no longer sends such a frame and a receiver owes it nothing."""
    return [c for c in FRAMES[frame]["cases"]
            if c["verdict"] == verdict and "json" in c and not c.get("retired")]


def _transcript(name: str) -> list[dict]:
    path = PIN_DIR / f"transcript.{name}.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def _assert_conforms(sent: dict, frame: str) -> None:
    spec = FRAMES[frame]
    allowed = set(spec["required"]) | set(spec["optional"])
    assert set(spec["required"]) <= set(sent), f"{frame}: missing {set(spec['required']) - set(sent)}"
    assert set(sent) <= allowed, f"{frame}: sends keys the protocol does not define: {set(sent) - allowed}"
    for key, value in sent.items():
        want = JSON_TYPES[spec["types"][key]]
        assert isinstance(value, want) and not (want is int and isinstance(value, bool)), (
            f"{frame}.{key}: {value!r} is not a {spec['types'][key]}")
    assert sent.get("type") == spec["type"]


# ---------------------------------------------------------------- the pin itself


def test_provider_and_pin_agree_on_the_major():
    assert CORE["contract"] == "ws-protocol"
    assert CORE["protocol_major"] == provider.PROTOCOL_MAJOR
    assert PIN["version"].split(".")[0] == str(provider.PROTOCOL_MAJOR)
    assert CORE["channels"]["audio"]["opening"] == "audio.register"


# ---------------------------------------------------------------- what the provider sends


@pytest.mark.parametrize("config", [
    {},
    {"mode": "single"},
    {"mode": "streaming", "client_id": "bench_node", "room_name": "Кухня", "sample_rate": 8000},
    {"sample_rate": "16000"},   # profile files hand strings in; the frame must still carry an integer
])
def test_register_frame_is_a_valid_opening_frame(config):
    _assert_conforms(provider.build_register(config), "audio.register")


def test_end_frame_is_the_pinned_end_frame():
    _assert_conforms(provider.END_FRAME, "audio.end")
    assert provider.END_FRAME in [c["json"] for c in _cases("audio.end", "valid")]


def test_register_frame_is_none_of_the_rejected_shapes():
    sent = provider.build_register({})
    for case in _cases("audio.register", "invalid"):
        assert sent != case["json"], f"provider sends the rejected shape {case['id']}"


def test_the_core_carries_wrong_type_cases_the_register_frame_avoids():
    """From v1.2.0 the server type-checks opening frames. The pinned core must carry the
    wrong-JSON-type cases for the keys this provider sends, and `_assert_conforms` above
    is what keeps the provider on the right side of each."""
    wrong_type = {c["id"] for c in _cases("audio.register", "invalid")
                  if c.get("violation") == "wrong-json-type"}
    assert {"audio.register/client-id-not-string", "audio.register/sample-rate-not-integer",
            "audio.register/wants-audio-not-boolean", "audio.register/mode-not-string"} <= wrong_type


# ---------------------------------------------------------------- what the provider receives


@pytest.mark.parametrize("case", _cases("audio.registered", "valid"), ids=lambda c: c["id"])
def test_every_valid_ack_is_accepted(case):
    provider.expect_registered(case["json"])


@pytest.mark.parametrize("case", _cases("audio.error", "valid"), ids=lambda c: c["id"])
def test_error_is_terminal_also_in_place_of_the_ack(case):
    with pytest.raises(RuntimeError):
        provider.expect_registered(case["json"])
    with pytest.raises(RuntimeError, match="server error"):
        provider.handle_server_frame(case["json"], [])


@pytest.mark.parametrize("case", _cases("audio.partial", "valid"), ids=lambda c: c["id"])
def test_partials_accumulate(case):
    partials: list[str] = []
    assert provider.handle_server_frame(case["json"], partials) is None
    assert partials == [case["json"]["text"]]


@pytest.mark.parametrize("case", _cases("audio.response", "valid"), ids=lambda c: c["id"])
def test_every_valid_response_ends_the_utterance(case):
    assert provider.handle_server_frame(case["json"], []) == case["json"]


def test_frames_the_provider_does_not_use_are_ignored_not_fatal():
    """Receivers ignore unknown frame types and unknown keys — the rule every minor of
    the protocol rests on. `trace` is a known type this provider never asks for."""
    ignorable = [c["json"] for c in _cases("audio.trace", "valid")]
    ignorable += [u["json"] for u in CORE["unknown"]
                  if u["channel"] == "audio" and u["direction"] == "s2c"]
    assert ignorable, "the pinned core lost its unknown-type cases for audio s2c"
    for frame in ignorable:
        partials: list[str] = []
        assert provider.handle_server_frame(frame, partials) is None and partials == []


# ---------------------------------------------------------------- whole exchanges


@pytest.mark.parametrize("name,server_may_end_utterances", [
    ("audio-batch", False), ("audio-trace", False), ("audio-streaming", True)])
def test_recorded_exchanges_drive_the_provider_to_a_response(name, server_may_end_utterances):
    """Replay the server side of a real recorded exchange through the provider's
    handlers. In batch mode every `end` the client sent is answered by exactly one final
    response; in streaming mode the server may also end an utterance from the audio
    itself, so there are at least as many responses as `end` frames — and the provider,
    which sends one utterance, stops at the first."""
    lines = [l for l in _transcript(name) if l.get("channel") == "audio"]
    server_text = [l for l in lines if l["kind"] == "text" and l["direction"] == "s2c"]
    ends = [l for l in lines if l["kind"] == "text" and l["direction"] == "c2s"
            and l.get("frame") == "audio.end"]
    assert server_text and ends
    provider.expect_registered(server_text[0]["json"])
    finals, partials = [], []
    for line in server_text[1:]:
        done = provider.handle_server_frame(line["json"], partials)
        if done is not None:
            finals.append(done)
    assert all(f["type"] == "response" for f in finals)
    if server_may_end_utterances:
        assert len(finals) >= len(ends) and partials, "streaming exchange carries partials"
    else:
        assert len(finals) == len(ends)


def test_a_rejected_registration_surfaces_as_an_error():
    server_text = [l for l in _transcript("audio-rejected")
                   if l["kind"] == "text" and l["direction"] == "s2c"]
    with pytest.raises(RuntimeError):
        provider.expect_registered(server_text[0]["json"])
