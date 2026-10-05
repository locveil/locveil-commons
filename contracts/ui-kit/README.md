# ui-kit — owned contract surface (cross-reference, package-style)

The shared React component kit + design tokens (PROD-10; normative style rules:
`../../docs/design/ui/stylebook.md`). The artifact is the whole package at
**`../../packages/ui-kit/`** at a `ui-kit-vX` tag.

- **Surface = the package at the tag** (exports of `src/index.ts`, tokens, stylebook
  conformance). The STAMP declares `artifacts: []` on purpose — HEAD legitimately
  advances between tags and nothing is byte-locked; consumers take tags.
- **Owner guard** (the STAMP's `guard`): `../../eval/tests/test_ui_kit_tokens.py` — the
  token values in `tokens/locveil.css` and their machine mirror `tokens/locveil.json`
  agree, theme by theme.
- **Consumption**: product plugins receive it as a workbench import-map singleton at
  runtime (strict-major peers — `workbench` contract); build-time co-development uses
  `file:` links by design (voice config-ui), which are NOT pins.
- **Version authority**: `STAMP.json` + tag (first stamped at v1.2; v1/v1.1 predate the
  stamp and are frozen history; the tag carries its STAMP from v1.3.0). An added export
  or token = minor; a removed/renamed one = major.
