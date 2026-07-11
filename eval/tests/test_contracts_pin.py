"""The Irene↔bridge contract pin is internally consistent and post-v1.1 (locveil-voice TEST-17).

The pin is a one-way-inward copy of the bridge's committed artifacts (contracts/README.md).
These tests make it *load-bearing*: the golden must validate against the pinned openapi's
own CatalogResponse schema, the stamps must agree, and the v1.1 shape guarantees the voice
resolver codes against (aliases, localized enum labels, units, values-XOR-options_from)
must actually hold — so re-pinning a stale/pre-patch artifact fails loudly here instead of
silently downstream.
"""
import json
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

CONTRACTS = Path(__file__).resolve().parents[2] / "contracts"


@pytest.fixture(scope="module")
def golden():
    return json.loads((CONTRACTS / "catalog.golden.json").read_text())


@pytest.fixture(scope="module")
def openapi():
    return json.loads((CONTRACTS / "openapi.json").read_text())


@pytest.fixture(scope="module")
def stamp():
    return json.loads((CONTRACTS / "STAMP.json").read_text())


@pytest.fixture(scope="module")
def pin():
    return json.loads((CONTRACTS / "PIN.json").read_text())


def all_params(golden):
    for d in golden["devices"]:
        for cap in d.get("capabilities") or []:
            for a in cap.get("actions") or []:
                for p in a.get("params") or []:
                    yield d["id"], cap["name"], a["name"], p


# ------------------------------------------------------------------ schema consistency

def test_golden_validates_against_pinned_catalog_schema(golden, openapi):
    """The two halves of the pin can never disagree: the golden IS a CatalogResponse."""
    schema = {"$ref": "#/components/schemas/CatalogResponse",
              "components": openapi["components"]}
    jsonschema.validate(golden, schema)


def test_stamp_matches_golden_version(golden, stamp):
    assert stamp["catalog_version"] == golden["version"]


def test_pin_matches_stamp(pin, stamp):
    assert pin["bridge_commit"] == stamp["bridge_commit"]
    assert pin["catalog_version"] == stamp["catalog_version"]


# ------------------------------------------------------------------ v1.1 shape guards

def test_params_carry_values_xor_options_from(golden):
    """The documented rule: a param is a stable enum OR a dynamic set, never both."""
    for did, cap, act, p in all_params(golden):
        assert not (p.get("values") and p.get("options_from")), (did, cap, act, p["name"])


def test_aliases_are_authored(golden):
    """VWB-21 landed real vocabulary — a pre-patch artifact would have none."""
    assert any(d.get("aliases") for d in golden["devices"])
    assert any(r.get("aliases") for r in golden["rooms"])


def test_enum_labels_are_localized_ru(golden):
    """VWB-20 G3: every LABELED enum value includes Russian.

    VWB-19 (§11.2) added by_value input triplets with `labels: null` — deliberate:
    wire = canonical = table key (CD/aux/usb), technical identifiers that are
    self-matchable and never translated. Null labels are legal; a non-null label
    set without Russian is still a contract violation."""
    seen = 0
    for _, _, _, p in all_params(golden):
        for v in p.get("values") or []:
            seen += 1
            if v.get("labels") is None:
                continue
            assert "ru" in v["labels"], v
    assert seen > 0  # the scenario enum must exist at all


def test_units_present_on_params(golden):
    """VWB-20 G4: ranged setters carry units (°C / %)."""
    units = {p.get("unit") for _, _, _, p in all_params(golden) if p.get("unit")}
    assert {"°C", "%"} <= units


def test_no_empty_capability_husks(golden):
    """VWB-20 G-minor: capabilities with neither actions nor fields are suppressed."""
    for d in golden["devices"]:
        for cap in d.get("capabilities") or []:
            assert cap.get("actions") or cap.get("fields"), (d["id"], cap["name"])
