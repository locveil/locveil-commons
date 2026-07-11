"""Guards for contracts/crossover_fixtures.json (TEST-18 Slice A).

Every fixture's `expect` must bind to entities that actually exist in the pinned
golden catalog — device ids, capabilities, actions, params (with ranges/enums),
room ids, semantic groups, sensor fields. When a re-pin changes the catalog,
these tests point at exactly which fixtures need re-authoring.
"""

import json
from pathlib import Path

import pytest

CONTRACTS = Path(__file__).resolve().parents[2] / "contracts"

FANOUT_ALLOW_LIST = {"light", "cover"}  # canonical_first.md §10 (VWB-23)
SCOPES = {"auto", "all", "one"}


@pytest.fixture(scope="module")
def catalog():
    return json.loads((CONTRACTS / "catalog.golden.json").read_text())


@pytest.fixture(scope="module")
def fixtures_doc():
    return json.loads((CONTRACTS / "crossover_fixtures.json").read_text())


@pytest.fixture(scope="module")
def devices(catalog):
    return {d["id"]: d for d in catalog["devices"]}


@pytest.fixture(scope="module")
def rooms(catalog):
    return {r["id"]: r for r in catalog["rooms"]}


def _capability(device: dict, name: str) -> dict | None:
    for cap in device.get("capabilities") or []:
        if cap["name"] == name:
            return cap
    return None


def _action(cap: dict, name: str) -> dict | None:
    for act in cap.get("actions") or []:
        if act["name"] == name:
            return act
    return None


def test_pin_agreement(fixtures_doc):
    pin = json.loads((CONTRACTS / "PIN.json").read_text())
    assert fixtures_doc["catalog_version"] == pin["catalog_version"], (
        "fixtures were authored against a different catalog than the pin — "
        "re-author bindings after the re-pin"
    )


def test_ids_unique_and_shapes(fixtures_doc):
    fixtures = fixtures_doc["fixtures"]
    ids = [f["id"] for f in fixtures]
    assert len(ids) == len(set(ids))
    for f in fixtures:
        assert f["tier"] in (1, 2), f["id"]
        assert f["utterance"]["ru"].strip(), f["id"]
        assert f["expect"]["kind"] in ("actuate", "room-group", "read", "clarify"), f["id"]


def test_all_expect_kinds_covered(fixtures_doc):
    kinds = {f["expect"]["kind"] for f in fixtures_doc["fixtures"]}
    assert kinds == {"actuate", "room-group", "read", "clarify"}


def test_context_rooms_exist(fixtures_doc, rooms):
    for f in fixtures_doc["fixtures"]:
        room = (f.get("context") or {}).get("room")
        if room is not None:
            assert room in rooms, f"{f['id']}: unknown context room {room}"


def _validate_params(fid: str, action: dict, params: dict | None):
    specs = {p["name"]: p for p in action.get("params") or []}
    for name, spec in specs.items():
        if spec.get("required"):
            assert params and name in params, f"{fid}: required param {name} missing"
    if not params:
        return
    for name, value in params.items():
        assert name in specs, f"{fid}: param {name} not in the contract"
        spec = specs[name]
        if spec.get("values"):
            # Irene sends the CANONICAL token (§5a); the bridge maps canonical → wire
            allowed = {v["canonical"] for v in spec["values"]}
            assert value in allowed, f"{fid}: enum value {value!r} not in {sorted(allowed)}"
        else:
            if spec.get("min") is not None:
                assert value >= spec["min"], f"{fid}: {name}={value} below min {spec['min']}"
            if spec.get("max") is not None:
                assert value <= spec["max"], f"{fid}: {name}={value} above max {spec['max']}"


def test_actuate_fixtures_bind(fixtures_doc, devices):
    for f in fixtures_doc["fixtures"]:
        e = f["expect"]
        if e["kind"] != "actuate":
            continue
        assert e["device_id"] in devices, f"{f['id']}: unknown device {e['device_id']}"
        cap = _capability(devices[e["device_id"]], e["capability"])
        assert cap, f"{f['id']}: {e['device_id']} has no capability {e['capability']}"
        action = _action(cap, e["action"])
        assert action, f"{f['id']}: no action {e['capability']}.{e['action']} on {e['device_id']}"
        _validate_params(f["id"], action, e.get("params"))


def test_room_group_fixtures_bind(fixtures_doc, rooms, devices):
    for f in fixtures_doc["fixtures"]:
        e = f["expect"]
        if e["kind"] != "room-group":
            continue
        fid = f["id"]
        assert e["room_id"] in rooms, f"{fid}: unknown room {e['room_id']}"
        assert e["group"] in FANOUT_ALLOW_LIST, f"{fid}: group {e['group']} outside allow-list"
        assert e["scope"] in SCOPES, fid
        # the action must exist on at least one of the room's group members
        member_actions = set()
        for d in devices.values():
            if d["room"] != e["room_id"]:
                continue
            for cap in d.get("capabilities") or []:
                if cap.get("group") == e["group"]:
                    member_actions.update(a["name"] for a in cap.get("actions") or [])
        assert member_actions, f"{fid}: room {e['room_id']} has no {e['group']}-group members"
        assert e["action"] in member_actions, (
            f"{fid}: action {e['action']} not offered by any {e['group']} member "
            f"of {e['room_id']} (has: {sorted(member_actions)})"
        )


def _validate_read_target(fid: str, devices: dict, target: dict):
    assert target["device_id"] in devices, f"{fid}: unknown device {target['device_id']}"
    cap = _capability(devices[target["device_id"]], target["capability"])
    assert cap, f"{fid}: {target['device_id']} has no capability {target['capability']}"
    fields = {fld["name"] for fld in cap.get("fields") or []}
    assert target["field"] in fields, (
        f"{fid}: field {target['field']} not on {target['device_id']}.{target['capability']} "
        f"(has: {sorted(fields)})"
    )


def test_read_fixtures_bind(fixtures_doc, devices):
    for f in fixtures_doc["fixtures"]:
        e = f["expect"]
        if e["kind"] != "read":
            continue
        targets = e["any_of"] if "any_of" in e else [e]
        assert targets, f["id"]
        for target in targets:
            _validate_read_target(f["id"], devices, target)


def test_clarify_fixtures_bind(fixtures_doc, devices):
    for f in fixtures_doc["fixtures"]:
        e = f["expect"]
        if e["kind"] != "clarify":
            continue
        fid = f["id"]
        assert len(e["candidates"]) >= 2, f"{fid}: a clarification needs >=2 candidates"
        wanted = e["capability"] if isinstance(e["capability"], list) else [e["capability"]]
        for dev_id in e["candidates"]:
            assert dev_id in devices, f"{fid}: unknown candidate {dev_id}"
            # string or list: every candidate must carry at least one of the named capabilities —
            # since DRV-28 one user goal can bind different capabilities per device (set-temperature
            # is climate.set_setpoint on a floor, temperature.set on an AC)
            assert any(_capability(devices[dev_id], c) for c in wanted), (
                f"{fid}: candidate {dev_id} lacks all of {wanted} — "
                "the ambiguity would not arise"
            )
        # the clarification must be genuine: all candidates in one room
        candidate_rooms = {devices[d]["room"] for d in e["candidates"]}
        assert len(candidate_rooms) == 1, f"{fid}: candidates span rooms {candidate_rooms}"
