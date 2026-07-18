# packages/ — co-owned shared code (ownership regime 2: commons owns, products pin versions)

Code moves in only under the **rule of two** — the second consumer must be real and
committed, nothing speculative (D-8). Each package versions independently via prefixed tags
(`core-py-vX`, `ui-kit-vX`) with its own `pyproject.toml`/`package.json`; the eval framework
lives at `../eval/` (tag `eval-vX`) for historical continuity.

Packages:

- **core-py** — PROD-8: the shared `DynamicLoader` entry-point-group discovery engine
  (voice ARCH-42 design; consumers vendor `entry_point_loader.py` at a `core-py-vX` tag
  with a strict pin + byte-identity test). The logging-scheme extraction is PARKED by
  the PROD-8 council — loader first.
- **ui-kit** — PROD-10: stylebook-governed tokens + React components for the product UIs
  (`ui-kit-vX`).
- **workbench** — PROD-24: the plugin-host shell (`workbench-vX`).
- **brand** — IMPL-7: canonical logo/wordmark assets, consumed by the kit `<Logo>`,
  favicons, and later `site/`.
- **scope-guard** / **contract-guard** — the process guards (`scope-vX`,
  `contract-guard-vX`), vendored by all repos.
