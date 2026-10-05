# locveil-workbench

The **Locveil Workbench** shell (IMPL-1): chrome + the plug-in contract as code +
HK-11 runtime assembly. Normative design: `../../docs/design/workbench.md` (§3 shell,
§4 contract as amended by HK-11). Tags: `workbench-vX.Y.Z` — the consumed surface is three
byte-locked files (`contracts/workbench/STAMP.json`): the contract types `src/contract.ts`
and the machine schemas `schemas/manifest-fragment.schema.json` +
`schemas/runtime-config.schema.json` (owner guard: `eval/tests/test_workbench_schemas.py`).
Editing any of the three is a contract cut; the rest of the shell moves freely.

## What the shell provides

- **Chrome** (wireframe as ratified): logo · one tab per plugin (+ status dot) · RU/EN
  locale switch · light/dark theme toggle · the BugReport button (Material glyph as raw
  SVG, quiet-grey/amber hover) delegating to the active plugin's `reportHook` ·
  reserved auth-guard slot (`#wb-auth-slot`, PROD-4 drops in later) · the single bottom
  action-bar slot (`#wb-bottom-slot`).
- **The import map** — the HK-11 singleton contract: `react`, `react/jsx-runtime`,
  `react-dom(/client)`, `react-router-dom` (major 6), `locveil-ui-kit`. Vendor bundles
  are built from the shell's own installed versions (`npm run build:vendor`); the shell
  externalizes the same names, so one instance of everything exists by construction.
- **The loader**: reads `/runtime-config.json`, fetches each plugin's build-emitted
  `dist/manifest.json` fragment, validates `peers` **strict-major refuse-and-surface**
  (a mismatched plugin renders as a failed tab naming the disagreement), injects the
  fragment's `styles`, dynamic-imports the entry, registers the default-exported
  `WorkbenchPlugin`. Dormant slots (gate, no location) trigger **zero** activity and
  render disabled with their gate named.

## For plugin authors (voice UI-17, bridge UI-18)

- Types only: `import type { WorkbenchPlugin, PageProps } from "locveil-workbench/contract"`
  — never import shell runtime modules. **A product repo resolves that specifier to its
  PINNED copy, not to this package:** pin the `workbench` family
  (`contracts/pins/workbench/contract.ts`) and map it in the plugin's `tsconfig.json` —
  `"paths": { "locveil-workbench/contract": ["../contracts/pins/workbench/contract.ts"],
  "react": ["./node_modules/@types/react"] }` (the second entry lets the pinned file's own
  React type import resolve). No `file:` dependency on `locveil-workbench`: with a live
  link, a change to the contract types here would reach a plugin's type-check without a
  re-pin. The imports are type-only and erased at build, so the bundle is unaffected.
  Reference: bridge UI-23 (`workbench-plugin/`), with a test and a CI step that fail if
  the types stop resolving to the pin.
- Build an ESM bundle with the six singleton names EXTERNAL (see
  `scripts/build-demo.mjs` for the exact shape), emit `manifest.json`
  `{id, version, entry, styles[], peers{}}` into your dist, disable Tailwind preflight
  in your build (the shell owns the one preflight + tokens.css).
- i18n is plugin-local; the shell passes `locale` in `PageProps`.

## Run it

```bash
npm install && npm run build     # vendor + shell + demo plugin
npm run serve                    # http://localhost:6107 — mounts workbench.config.json locations
npm run dev                      # vite build --watch (pair with npm run serve; reload per change)
```

`workbench.config.json` is the owner-edited config: per plugin `{"location": "<path to
a plugin dist>", "backends": {"api": "http://<controller-ip>:<port>"}}` (dev-phase:
sibling repo paths; **backends are deployment facts — absolute origins, IP AND port —
delivered to pages as `PageProps.backends`**, IMPL-6; on the WB7 host-network the voice
backend is `:8080`, the bridge backend `:8000`), or `{"id", "title", "gate"}` for a
dormant slot. The serve script mounts locations under `/plugins/<n>/` and generates
`/runtime-config.json`; published-artifact URLs are the productization step. Plugins
must use `backends` for every fetch — relative URLs resolve against the SHELL origin,
never the controller.
