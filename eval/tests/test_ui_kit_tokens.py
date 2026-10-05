"""ui-kit design tokens — owner guard (IMPL-16; the "natural first guard" PROD-10 named).

packages/ui-kit/tokens/locveil.css is what products load; tokens/locveil.json is the
machine mirror the stylebook and tooling read. They are synced by hand, so this test is
the sync: every colour the JSON states for a theme must be the value the CSS declares
for that theme. The package's contract is the ui-kit STAMP, whose `guard` points here.
"""
import json
import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
TOKENS = REPO / "packages/ui-kit/tokens"
CSS = (TOKENS / "locveil.css").read_text(encoding="utf-8")
MIRROR = json.loads((TOKENS / "locveil.json").read_text(encoding="utf-8"))
STAMP = json.loads((REPO / "contracts/ui-kit/STAMP.json").read_text(encoding="utf-8"))


def _block(selector: str) -> dict[str, str]:
    """Custom properties of the FIRST `selector { … }` block."""
    body = re.search(rf"^{re.escape(selector)} \{{(.*?)^\}}", CSS, re.S | re.M).group(1)
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r"--([\w-]+):\s*([^;]+);", body)}


def _kebab(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()


@pytest.mark.parametrize("theme,selector", [("light", ":root"), ("dark", ".dark")])
def test_json_mirror_matches_the_css(theme, selector):
    declared = _block(selector)
    for name, value in MIRROR["themes"][theme].items():
        var = _kebab(name)
        assert var in declared, f"{theme}: --{var} is in locveil.json but not in the CSS"
        assert declared[var] == value, (
            f"{theme}: --{var} is {declared[var]!r} in locveil.css but {value!r} in "
            "locveil.json — sync the mirror (the CSS is what products load)")


def test_both_themes_declare_the_same_variables():
    light, dark = _block(":root"), _block(".dark")
    themed = {v for v in light if v in dark}
    assert set(dark) <= set(light), f"dark-only tokens: {sorted(set(dark) - set(light))}"
    assert {"background", "foreground", "primary", "border"} <= themed


def test_stamp_is_the_package_style_declaration():
    assert STAMP["artifacts"] == [] and STAMP["guard"] == "eval/tests/test_ui_kit_tokens.py"
    assert STAMP["tag"] == f"ui-kit-v{STAMP['version']}"
