"""Docs-manifest coherence (HK-6/PROD-17; convention: process/user-docs.md §4).

The manifest is the scope of record for user-facing docs. This test keeps it and the
tree bijective: the manifest validates against the org schema, every non-pending node's
file exists, every root file is registered, pending-gate nodes name their gate, and the
surface globs reference real ground. Additions ride their causing task — a doc committed
without a node fails here, in the same change (the node policy IS this test).
"""
import json
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

REPO = Path(__file__).resolve().parents[2]
MANIFEST = json.loads((REPO / "docs/manifest.json").read_text())
SCHEMA = json.loads((REPO / "process/user-docs/manifest.schema.json").read_text())


def test_manifest_validates_against_org_schema():
    jsonschema.validate(MANIFEST, SCHEMA)


def test_every_present_node_file_exists():
    for n in MANIFEST["nodes"]:
        if n["status"] != "pending-gate":
            assert (REPO / n["path"]).is_file(), f"node '{n['id']}' → missing {n['path']}"


def test_pending_gate_nodes_name_their_gate():
    for n in MANIFEST["nodes"]:
        if n["status"] == "pending-gate":
            assert n.get("gate"), f"node '{n['id']}' is pending-gate without a gate"


def test_every_root_file_is_registered():
    registered = {n["path"] for n in MANIFEST["nodes"]}
    for root in MANIFEST["roots"]:
        p = REPO / root
        files = [p] if p.is_file() else sorted(p.rglob("*.md")) if p.is_dir() else []
        assert files, f"root '{root}' matches nothing"
        for f in files:
            rel = str(f.relative_to(REPO))
            assert rel in registered, f"unregistered user-facing file: {rel}"


def test_covers_reference_declared_surfaces():
    surfaces = set(MANIFEST["surfaces"])
    for n in MANIFEST["nodes"]:
        for s in n.get("covers", []):
            assert s in surfaces, f"node '{n['id']}' covers undeclared surface '{s}'"


def test_schema_stamp_coheres():
    """The SCHEMA is the contract (HK-13 q5); the manifest is instance data."""
    stamp = json.loads((REPO / "contracts/docs-manifest-schema/STAMP.json").read_text())
    assert stamp["contract"] == "docs-manifest-schema"
    assert stamp["tag"] == f"docs-manifest-schema-v{stamp['version']}"
    assert stamp["artifacts"] == ["process/user-docs/manifest.schema.json"]
    jsonschema.Draft202012Validator.check_schema(SCHEMA)
