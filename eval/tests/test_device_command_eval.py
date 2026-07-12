"""TEST-18 Slice B plumbing: the mock bridge, the fixtures→tests generator, the assertion."""

import json
import threading
import urllib.request
from pathlib import Path

import pytest
import yaml

from eval_commons.assertions.device_command_assert import get_assert
from eval_commons.fixtures_to_tests import generate
from eval_commons.mock_bridge import serve

PINS = Path(__file__).resolve().parents[2] / "contracts" / "pins"
CATALOG_PIN = PINS / "catalog"
FIXTURES_PIN = PINS / "crossover-fixtures"


@pytest.fixture(scope="module")
def bridge():
    server = serve(CATALOG_PIN / "catalog.golden.json", port=0)  # ephemeral port
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    yield base
    server.shutdown()


def _get(base, path):
    with urllib.request.urlopen(f"{base}{path}", timeout=5) as r:
        return json.loads(r.read())


def _post(base, path, payload):
    req = urllib.request.Request(f"{base}{path}", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read())


def test_mock_bridge_serves_the_pinned_catalog(bridge):
    catalog = _get(bridge, "/system/catalog")
    pin = json.loads((CATALOG_PIN / "PIN.json").read_text())
    assert catalog["version"] == pin["catalog_version"]


def test_mock_bridge_captures_both_address_forms_fixture_shaped(bridge):
    _post(bridge, "/_reset", {})
    device_reply = _post(bridge, "/devices/children_room_tv/canonical",
                         {"capability": "power", "action": "on", "params": None})
    assert device_reply["success"] is True
    room_reply = _post(bridge, "/rooms/bedroom/canonical",
                       {"group": "light", "action": "off", "scope": "all"})
    assert room_reply["success"] is True
    # scope=all fans out to every light member (bedroom has 7 in the real golden)
    assert len(room_reply["results"]) > 1
    _get(bridge, "/devices/shower_sauna_sensors/state")

    captured = _get(bridge, "/_captured?since=0")["captured"]
    assert captured == [
        {"kind": "actuate", "device_id": "children_room_tv", "capability": "power",
         "action": "on", "params": None},
        {"kind": "room-group", "room_id": "bedroom", "group": "light",
         "action": "off", "scope": "all"},
        {"kind": "read", "device_id": "shower_sauna_sensors"},
    ]


def test_mock_bridge_auto_scope_uses_group_default(bridge):
    _post(bridge, "/_reset", {})
    reply = _post(bridge, "/rooms/bedroom/canonical",
                  {"group": "light", "action": "on", "scope": "auto"})
    assert reply["scope_applied"] == "default"
    assert [r["device_id"] for r in reply["results"]] == ["bedroom_spots"]


def test_generator_covers_every_fixture():
    doc = json.loads((FIXTURES_PIN / "crossover_fixtures.json").read_text())
    tests = yaml.safe_load(generate(FIXTURES_PIN / "crossover_fixtures.json"))
    assert len(tests) == len(doc["fixtures"])
    by_id = {t["metadata"]["fixture"]: t for t in tests}
    f10 = by_id["F10"]
    assert f10["vars"]["utterance"] == "включи свет в детской"
    assert f10["vars"]["expect"]["kind"] == "room-group"
    assert f10["metadata"]["tier"] == "1"


def _envelope(captured, metadata=None, text="ok"):
    return json.dumps({"captured": captured,
                       "reply": {"text": text, "success": True,
                                 "intent_name": "smart_home.power_on",
                                 "metadata": metadata or {}}}, ensure_ascii=False)


def test_assert_actuate_pass_and_fail():
    expect = {"kind": "actuate", "device_id": "children_room_tv",
              "capability": "power", "action": "on", "params": None}
    ctx = {"vars": {"expect": expect}}
    good = _envelope([{"kind": "actuate", "device_id": "children_room_tv",
                       "capability": "power", "action": "on", "params": None}])
    assert get_assert(good, ctx)["pass"] is True
    wrong_device = _envelope([{"kind": "actuate", "device_id": "appletv_children",
                               "capability": "power", "action": "on", "params": None}])
    assert get_assert(wrong_device, ctx)["pass"] is False
    nothing = _envelope([])
    assert get_assert(nothing, ctx)["pass"] is False


def test_assert_clarify_requires_no_command_and_candidates():
    expect = {"kind": "clarify", "capability": "playback",
              "candidates": ["children_room_tv", "appletv_children"]}
    ctx = {"vars": {"expect": expect}}
    good = _envelope([], metadata={"clarification": True,
                                   "candidates": ["appletv_children", "children_room_tv"]})
    assert get_assert(good, ctx)["pass"] is True
    leaked = _envelope([{"kind": "actuate", "device_id": "children_room_tv",
                         "capability": "playback", "action": "pause", "params": None}],
                       metadata={"clarification": True})
    assert get_assert(leaked, ctx)["pass"] is False


def test_assert_read_accepts_any_of():
    expect = {"kind": "read", "any_of": [
        {"device_id": "bedroom_hvac", "capability": "climate", "field": "room_temperature"},
        {"device_id": "bedroom_heating", "capability": "climate", "field": "room_temperature"}]}
    ctx = {"vars": {"expect": expect}}
    assert get_assert(_envelope([{"kind": "read", "device_id": "bedroom_heating"}]),
                      ctx)["pass"] is True
    assert get_assert(_envelope([]), ctx)["pass"] is False


def test_mock_bridge_serves_options(bridge):
    # by_value select → the catalog's own table keys (VWB-19 §11.2 fallback)
    data = _get(bridge, "/devices/mf_amplifier/options/inputs")
    assert data["success"] is True and "cd" in data["data"]
    # parametric select → the deterministic stand-in list
    data = _get(bridge, "/devices/children_room_tv/options/inputs")
    assert data["data"] == ["hdmi1", "hdmi2", "av", "component"]
    data = _get(bridge, "/devices/appletv_children/options/apps")
    assert "YouTube" in data["data"]
