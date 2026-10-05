"""Workbench contract machine schemas — owner guard (IMPL-15; HK-12 owed, HK-13 executed).

The plugin contract's machine half lives in packages/workbench/schemas/ and is
enumerated in contracts/workbench/STAMP.json next to the contract types. This guard
keeps the three artifacts ONE statement: the manifest-fragment schema is field-identical
to `ManifestFragment` in src/contract.ts, the runtime-config schema accepts exactly what
the dev server generates from the owner-edited shell config and what the loader reads,
and both reject the shapes the loader refuses.
"""
import json
import re
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

REPO = Path(__file__).resolve().parents[2]
WB = REPO / "packages/workbench"
FRAGMENT = json.loads((WB / "schemas/manifest-fragment.schema.json").read_text())
RUNTIME = json.loads((WB / "schemas/runtime-config.schema.json").read_text())
CONTRACT_TS = (WB / "src/contract.ts").read_text()
STAMP = json.loads((REPO / "contracts/workbench/STAMP.json").read_text())


def _ts_fields(interface: str, source: str) -> dict[str, bool]:
    """{field: required} for a flat TS interface (comments tolerated)."""
    body = re.search(rf"interface {interface} \{{(.*?)\n\}}", source, re.S).group(1)
    body = re.sub(r"/\*.*?\*/", "", body, flags=re.S)
    return {m.group(1): m.group(2) != "?"
            for m in re.finditer(r"^\s+(\w+)(\??):", body, re.M)}


def test_schemas_are_valid_json_schema():
    for schema in (FRAGMENT, RUNTIME):
        jsonschema.Draft202012Validator.check_schema(schema)


def test_stamp_enumerates_the_contract_as_code_and_both_schemas():
    assert STAMP["artifacts"] == [
        "packages/workbench/src/contract.ts",
        "packages/workbench/schemas/manifest-fragment.schema.json",
        "packages/workbench/schemas/runtime-config.schema.json",
    ]


def test_fragment_schema_is_field_identical_to_the_contract_type():
    fields = _ts_fields("ManifestFragment", CONTRACT_TS)
    assert set(FRAGMENT["properties"]) == set(fields)
    assert set(FRAGMENT["required"]) == {f for f, required in fields.items() if required}


def test_demo_plugin_manifest_shape_validates():
    """The shape scripts/build-demo.mjs emits — the reference a product repo copies."""
    demo = {"id": "demo", "version": "0.1.0", "entry": "./index.js",
            "styles": ["./style.css"],
            "peers": {"react": "^18", "react-dom": "^18", "react-router-dom": "^6",
                      "locveil-ui-kit": "^0.1"}}
    jsonschema.validate(demo, FRAGMENT)
    build = (WB / "scripts/build-demo.mjs").read_text()
    for key in demo:  # the script still emits every key this test pins
        assert re.search(rf"^\s+{key}:", build, re.M), f"build-demo.mjs no longer emits {key}"
    built = WB / "demo-plugin/dist/manifest.json"
    if built.is_file():  # after a local build: the REAL output must validate too
        jsonschema.validate(json.loads(built.read_text()), FRAGMENT)


@pytest.mark.parametrize("bad", [
    {"version": "1", "entry": "./i.js", "peers": {}},                 # no id
    {"id": "x", "version": "1", "entry": "./i.js"},                   # no peers
    {"id": "x", "version": "1", "entry": "./i.js", "peers": {"react": 18}},
    {"id": "x", "version": "1", "entry": "./i.js", "peers": {}, "styles": "a.css"},
])
def test_fragment_schema_rejects_what_the_loader_cannot_use(bad):
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, FRAGMENT)


def _runtime_from_shell_config(config: dict) -> dict:
    """scripts/serve.mjs, in Python: a location becomes a mounted url, a dormant slot
    passes through untouched."""
    plugins = []
    for entry in config.get("plugins", []):
        if "location" in entry:
            plugins.append({"url": f"/plugins/{len([p for p in plugins if 'url' in p])}/",
                            "backends": entry.get("backends", {})})
        else:
            plugins.append(entry)
    return {"plugins": plugins}


def test_runtime_config_generated_from_the_shell_config_validates():
    config = json.loads((WB / "workbench.config.json").read_text())
    runtime = _runtime_from_shell_config(config)
    assert any("url" in p for p in runtime["plugins"]) and any("gate" in p for p in runtime["plugins"])
    jsonschema.validate(runtime, RUNTIME)


@pytest.mark.parametrize("bad", [
    {},                                                               # no plugins
    {"plugins": [{}]},                                                # neither url nor gate
    {"plugins": [{"url": "/p/0/", "gate": {"all": ["x"]}}]},          # both
    {"plugins": [{"id": "s", "title": "S", "gate": {"all": []}}]},    # empty gate
    {"plugins": [{"id": "s", "title": {"ru": "С"}, "gate": {"all": ["x"]}}]},
    {"plugins": [{"url": "/p/0/", "backends": {"api": 8080}}]},
])
def test_runtime_schema_rejects_what_the_loader_refuses(bad):
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, RUNTIME)
