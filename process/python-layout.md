# Python backend layout & naming — the org convention (HK-8, normative)

Decided by council HK-8 (2026-07-13, three rounds, voice + bridge keepers — the blast
radii were measured, not estimated; arcs in `board/JOURNAL.md`). Applies to every Locveil
repo with Python product code; the satellite and all newborns inherit it via
`new-repo-template/`. On disagreement with per-repo text, this file wins. This document
satisfies `design-then-implement` for the migration tasks it delegates.

## 1. Layout

- A Python backend is a **component**: `<component>/` (canonically `backend/`) holding
  `pyproject.toml`, the lockfile, type-checker configs, and:
  - `<component>/src/<import_package>/` — src-layout, always;
  - `<component>/tests/` — beside `src/`, OUTSIDE the import package (wheels stay slim;
    no `sys.path` shims).
- UI components are peers (`config-ui/`, `ui/`) — never inside the backend component.
- **Product data lives at repo root, never inside a component**: the config tree, assets,
  `ops/`, `docker/`, `docs/`, `contracts/`, `eval/`, vendored `scripts/`. Test: if
  config-ui, images, ops sync, or a sibling repo consumes it, it is not backend property.
- **The config tree is named `config/` (singular), org-wide** — matching the WB7 runtime
  trees (`/mnt/data/locveil-*-config/config/`).
- **Dockerfiles live in repo-root `docker/`, built with repo-root context.** The file
  axis is repo dialect with both shapes justified on record: per-arch files where
  platform contents genuinely differ (voice: per-platform ML profiles), per-component
  files where images are arch-identical and multi-platform manifests do the work
  (bridge: the OPS-11 finding — per-arch variants there would be a regression).
  Image *runtime assets* (entrypoints, nginx templates) stay with their component —
  `docker/` holds build recipes only.

## 2. Naming

- **Published names** (distributions, images, tags, console scripts) are `locveil-*` —
  the standing org rule.
- **Product backend import packages are `locveil_<repo>`**: `locveil_voice`,
  `locveil_bridge`, future `locveil_core` etc. — the import name, the distribution, the
  image, and the repo tell one story.
- **Shared-library namespaces keep truthful, neutral names** (`eval_commons` — its
  distribution is already `locveil-eval` per the PROD-2 precedent). The test is truth,
  not prefix: a retired or external vendor brand in an import name is a defect
  (`wb_mqtt_bridge` was one); a neutral descriptive name is not.
- **Single-file vendored tools are exempt** (`scope_guard.py`, `contract_guard.py`):
  they are not import packages consumers code against, and renaming them churns every
  vendoring repo for nothing.
- **The product persona stays in user-visible strings**: UI copy, wake word, docs prose
  say "Irene". Only importable/published identifiers carry `locveil`.

## 3. What a layout/rename task may NEVER touch

Wire-visible and deployed identifiers are deployment identity, not code identity — each
needs its own owner-gated task if ever changed: MQTT `meta/driver` strings, retained
topic contents, env-file keys on the controller (changed only by a scripted, smoked
cutover step inside the migration task), persisted state paths (prod state lives on
bind mounts — verify before assuming), entry-point group names *as consumed by deployed
configs* (change code + config-master + profiles in the same change; the deployed copy
is derived and regenerates on update).

## 4. Migration principles (proven in the HK-8 measurement rounds)

- **One tree churn per repo** — layout + tests + rename + docs together; the expensive
  parts (docs sweep, lockfile, image rebuilds, controller cutover) must not run twice.
- Every migration task carries its keeper-measured checklist as the
  `task-start-reconciliation` baseline.
- Ops cutovers are scripted (the `migrate-to-locveil.sh` / BUILD-29 playbook), then
  smoked; hand-edited files (the controller secrets `.env`) are named in the task, not
  discovered.
- Console-script renames keep old names as zero-cost aliases for one release where
  consumers span repos; hard-cut where all callers are in-repo.
- Deliberate contract cuts ride the migration (a rename that moves generated schema
  names is a minor contract bump — tag, STAMP, UI regen, one consumer re-pin), never
  silent.

## 5. Instances (PROD-21)

voice **BUILD-36** (backend/src move + tests out + `locveil_voice` rename + dist
`locveil-voice` + `configs/`→`config/` + eval venv → `backend/.venv` + scripted WB7
cutover; ~4.5–5 days, one churn); bridge **CORE-10** (`locveil_bridge` rename + script
renames + `catalog-v1.7` cut; ~1 day), **CORE-11** (config tree + Dockerfiles to root;
~½ day), **OPS-26** (meta/driver wire cutover, owner-gated, same deploy cycle);
commons — this spec + the template line; eval framework and vendored guards unchanged
by ruling.
