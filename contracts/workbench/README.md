# workbench — owned contract surface (cross-reference, package-style)

THE plugin contract (HK-11/PROD-24; normative: `../../docs/design/workbench.md` §4 +
`../../packages/workbench/README.md`) — the surface voice's and bridge's workbench
plugins code against: the frozen import-map singleton set (react / react-dom(/client) /
react/jsx-runtime / react-router-dom@6 / locveil-ui-kit), strict-major `peers`
refuse-and-surface, the build-emitted manifest fragment
(`{id, version, entry, styles[], peers{}, backendCompat?}`), and `runtime-config.json`.

- **Surface = three enumerated files at a `workbench-vX.Y.Z` tag** (STAMP `artifacts`,
  byte-locked): the contract types `packages/workbench/src/contract.ts` and the two
  machine schemas `packages/workbench/schemas/manifest-fragment.schema.json` +
  `runtime-config.schema.json`. The shell around them advances between tags.
- **Owner guard**: `../../eval/tests/test_workbench_schemas.py` — the fragment schema is
  field-identical to `ManifestFragment`, the runtime schema accepts what the dev server
  generates from the shell config, both reject what the loader refuses.
- **Consumption**: plugins build against `locveil-workbench/contract` and the demo-plugin
  shape; product repos PIN this family (`contracts/pins/workbench/`) and validate their
  build-emitted `manifest.json` against the pinned fragment schema. Live `file:` links
  during the Workbench arc are co-development, not pins.
- **Version authority**: `STAMP.json` + tag (first stamped at v1.2; v1/v1.1 predate the
  stamp and are frozen history; the tag carries its STAMP from v1.3.0).
