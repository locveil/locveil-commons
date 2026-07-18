# workbench — owned contract surface (cross-reference, package-style)

THE plugin contract (HK-11/PROD-24; normative: `../../docs/design/workbench.md` §4 +
`../../packages/workbench/README.md`) — the surface voice's and bridge's workbench
plugins code against: the frozen import-map singleton set (react / react-dom(/client) /
react/jsx-runtime / react-router-dom@6 / locveil-ui-kit), strict-major `peers`
refuse-and-surface, the build-emitted manifest fragment
(`{id, version, entry, styles[], peers{}, backendCompat?}`), and `runtime-config.json`.

- **Surface = the package + contract types at a `workbench-vX` tag.** No `artifacts`
  byte-enumeration yet — the machine-readable schemas (manifest fragment +
  runtime-config) are OWED at the next bump (recorded in the STAMP note, PROD-26);
  from then on they drift-check.
- **Consumption**: plugins build against `locveil-workbench/contract` and the demo-plugin
  shape; product repos pin via repin once the schema artifacts exist. Live `file:` links
  during the Workbench arc are co-development, not pins.
- **Version authority**: `STAMP.json` + tag (first stamped at `workbench-v1.2`;
  v1/v1.1 predate the stamp and are frozen history).
