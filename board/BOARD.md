# Locveil board — the cross-repo initiative ledger (PROD-N)

The D-4/D-5 board (`docs/design/productization.md`). One entry per cross-repo initiative,
stable ID `PROD-N`, referenced in commit messages (`PROD-3: …`).

## Conventions

- **A cross-repo idea = a PROD task; the deliverable is a design doc.** Placement rule: a
  design defining a concept/contract both products consume lives in this repo's
  `docs/design/`; a design whose primary artifact is one repo's code lives in that repo's
  `docs/design/`, even when the session ran here.
- **Board-as-outbox (D-5):** on completion a PROD task *delegates* — the delegation text is
  committed in the entry below (this repo is co-owned ground; both product repos may write
  here). The receiving repo's session pulls the delegation, verifies it per its own
  `task-start-reconciliation`, files it under a local ID, and **writes that ID back into the
  entry**. Nothing lives uncommitted in a sibling working tree.
- **The board never asserts a delegated task's status** — per-repo ledgers own status. An
  entry lists delegated IDs; it closes when its own commons-side deliverable is done and all
  delegations have local IDs written back.
- Statuses: `[ ]` open · `[>]` in progress · `[x]` done. Session notes go to
  `JOURNAL.md` (newest on top), not here.
- **IMPL-N (HK-10, 2026-07-14):** implementation work genuinely on commons (regime-2/3
  code under `packages/`, `site/`, `eval/`) that is not itself a cross-repo initiative
  lives under `## IMPL`. PROD stays cross-repo initiatives; HK stays council topics.
- **Ledger discipline (HK-1 / PROD-13, normative: `process/ledger-discipline.md`):** this
  board is the active ledger; completed entries MOVE to `BOARD_DONE.md` in the same change
  as their journal entry. Council topics carry the `HK-N` prefix; being born-decided they
  file directly into `BOARD_DONE.md` (a deferred council parks its HK entry here). Guarded
  by scope-guard (`packages/scope-guard/`, config `.scope-guard.toml`).

## Ledger

Completed entries live in `BOARD_DONE.md` (moved on close; `process/ledger-discipline.md`).

## PROD — cross-repo initiatives

- [ ] **PROD-4 — Deployment coordination + ops conformance** (REFRAMED by council HK-7,
      2026-07-12 — was "Normative ops spec", D-12; the spec stays the deliverable, the
      scope now owns the deployment-coordination pain the owner called "a mess"). Scope:
      (1) ONE compose story with real startup order across the three WB7 containers —
      voice **BUILD-28**, whose own "seeded when BUILD-21 lands" trigger is finally
      discharged here; (2) the normative spec in `process/` codifying the converged
      pattern (sdcard clone update-time-only, `/mnt/data/<name>-config`, repo-owns-config
      sync, `.env` secrets, systemd oneshot, GHCR pull-not-build, log rotation, local
      healthchecks) + a conformance checklist — RECONCILING the stale claims the
      cancelled 2026-07-11 council round inventoried (units require more than the old
      text listed; start-period is dialect not constant; `.env` lives in the runtime
      tree); (3) the **readiness contract** as a named dependency: health-gated ordering
      requires voice ARCH-45 (`/health` reports healthy during ~90s model warmup today) —
      the contract (what compose waits on, per container) is decided HERE, the
      `/health`/`/ready` implementations stay repo-owned; (4) the
      **config-master→deployment-profiles reconciliation convention** (BUILD-31's
      still-unfiled lesson), dialect-aware — voice's TOML master/profiles need the gate,
      bridge's `config-master-tree` is canonical as-is and needs none
      *(AMENDED by the PROD-24 council, 2026-07-14: the "bridge needs none" claim is
      falsified — Workbench controller write APIs put bridge IN scope; the org-wide
      master↔staged reconciliation convention (staged proposals + explicit human
      promotion, dev-phase shape decided at PROD-24, final form deferred to a further
      productization step) is owned HERE; the auth posture for those write APIs is also
      decided here — PROD-24's binding condition: no write API ships before it)*; (5) **secrets
      posture joins** (HK-7 q3): bridge **CORE-8** (committed broker password is in git
      history — rotation is a near-term op) and voice confirms its own exposure class at
      intake. Shared *scripts* only at the third consumer (rule of three). Delegations:
      voice — BUILD-18 (narrowed conformance pass, stands), BUILD-28 (re-point at intake
      to this entry), ARCH-45 dependency noted in its design, NEW local task for the
      master→profiles gate mechanism (voice files it regardless of this entry's pace;
      write the ID back). Voice write-back — lead ID: **BUILD-18** + BUILD-28 (+ gate
      task ID pending). Bridge — OPS-15 (stands), CORE-8 (joins: secrets posture +
      the rotation op). Bridge write-back — lead ID: **OPS-15** + CORE-8.
- [ ] **PROD-8 — core-py bootstrap + first two extractions** (D-8): `packages/core-py`
      skeleton (own pyproject, `core-py-vX` tags), then the two designs — dynamic code
      loader (voice ARCH-42; voice consumer #1, bridge #2 via CORE-7) and logging scheme
      (voice ARCH-43; retires the BUG-30/OPS-12 hand-copy → bridge OPS-14).
      **COUNCIL-DECIDED 2026-07-16 (PROD-8 council, 2 rounds; keepers voice+bridge —
      satellite is not a core-py Python consumer).** Both support-with-conditions; both
      confirm entry-points is the discovery spine (voice: 13 provider groups + one
      `DynamicLoader`; bridge: `locveil_bridge.devices`, 9 drivers) and that bridge authored
      the logging scheme (OPS-12 DONE → voice BUG-30 is the copy). **Decisions:**
      **(1) Shared loader = the entry-point-group registry only** (voice's `DynamicLoader`
      engine) — the genuine rule-of-two leaf. Voice's `EntryPointMetadata` build-time metadata
      quartet (`get_python_dependencies`/`get_platform_support`/`get_supported_architectures`/
      `get_platform_dependencies` — dependency-closure + the load-bearing arch gate) and all its
      values stay voice-side; bridge's by-name config resolver (`class_loader.py`) stays
      bridge-side. Each auxiliary graduates to core-py only on its own second consumer.
      **(2) "Config-based driver loading" = unify resolution, keep entry points.** Replacing
      entry points with runtime config-path discovery is REJECTED — it breaks the offline
      catalog generator (`dump_catalog`) that builds the voice-pinned golden without loading a
      single driver. CORE-7 stays a self-contained infra swap; no catalog-contract bump.
      **(3) The UI/panel driver-availability gating is a SEPARATE bridge task**, never a rider
      on CORE-7. Today the surface is split-brained (operational pages gate on loaded drivers →
      404 + absent from catalog; config pages / nav / workbench still show configured-but-
      unloaded devices). The invariant "no driver → no device pages AND config pages" is a
      presentation + possible catalog-contract change; that task decides suppress-vs-surface.
      **(4) Sequencing locks:** ARCH-50 is a HARD PREDECESSOR of ARCH-42 (its hardcodings
      inventory feeds the loader design); the `packages/core-py` skeleton is cut AFTER ARCH-50 +
      ARCH-42 land (surface known first); the logging extraction (ARCH-43 → OPS-14) is PARKED —
      loader first, logging a later round (bridge's OPS-12 is the reference when it resumes).
      **Delegations (board-as-outbox):** voice — reconcile **ARCH-42** scope to "extract the
      entry-point-group discovery engine only; metadata contract + values stay voice-side;
      preserve the `build_analyzer`→`get_provider_class`→classmethod seam"; confirm ARCH-50-first
      and fold the dead `get_provider_capabilities` (`components/base.py:216`, zero call sites)
      into ARCH-50's dead-code sweep; ARCH-43 parked. Voice write-back — lead ID: **ARCH-42**
      (+ ARCH-50, ARCH-43) — **RECONCILED AT INTAKE 2026-07-16 (voice session), all three entries
      amended in the voice ledger:** ARCH-42 narrowed to the entry-point-group registry only
      (`utils/loader.py:133` `DynamicLoader`), with the `EntryPointMetadata` quartet
      (`core/metadata.py:25`) + values explicitly voice-side, the `build_analyzer`→
      `get_provider_class`→classmethod seam named as preserved, and ARCH-50 recorded as a hard
      predecessor on both entries; ARCH-50 carries the dead `get_provider_capabilities`
      (`components/base.py:216` — zero call sites VERIFIED at intake, resolves as delete per
      `dead-code-remove-not-fix`); ARCH-43 marked PARKED. No scope drift found — the council's
      voice-side claims all held against repo reality. **SEQUENCING LOCK DISCHARGED 2026-07-16
      (voice session, same day):** ARCH-50 DONE (review + all 8 remediation tasks landed) →
      ARCH-42 DONE — the design is AGREED and committed at
      `../locveil-voice/docs/design/core_py_loader_extraction.md`. **The `packages/core-py` skeleton is UNBLOCKED**
      ("surface known first" is satisfied). Surface summary for the skeleton cut: module
      `entry_point_loader.py`, class `DynamicLoader` ONLY (no module-level singleton — consumers
      own theirs); methods `discover_providers(namespace, enabled=None, base_class=None)` /
      `get_provider_class(namespace, name, base_class=None)` (single-EP load) /
      `list_available_providers` / `list_registered` (names without import) /
      `get_discovery_failures` / `clear_cache`; Python 3.11, importlib.metadata only; own
      pyproject + tests; tag **`core-py-v1`**. Consumption = vendored copy at tag with STRICT pin
      (consumer pins/core-py + byte-identity test — first vendored RUNTIME code). Voice follow-up:
      **ARCH-58** `[release]` (migration, gated on `core-py-v1`).
      **Voice write-back (2026-07-18) — ARCH-58 DONE; voice's half of PROD-8 is CLOSED.** The
      migration executed against **`core-py-v1.1`**: the FIRST strict pin refused v1 — the tag
      was cut before the "PROD-8 amended" commit added the STAMP, so the v1 tree cannot satisfy
      pins-complete-and-verbatim — and commons cut the v1.1 packaging correction (artifact
      bytes diff-verified unchanged; STAMP note + board journal record it). Voice landed: the
      `core-py` family in `.repin.toml` (the BUILD-43 sequencing held — declared once, new
      format), strict pin + byte-identity test, `utils/entry_points.py` singleton, the full
      20-file sweep, `startup_validation` on `list_registered`, DynamicLoader deleted from
      `utils/loader.py`. Acceptance: suite 1433 green, analyzer JSON byte-identical ×6 profiles,
      import contracts 11/11, guards + `repin --check --fail-on any` green. **CONSUMERS NOTE:
      bridge CORE-7 vendors at `core-py-v1.1`** (not v1 — same bytes, but only v1.1's tree
      carries the STAMP a conforming pin needs). Remaining in this entry: bridge CORE-7 + the
      parked logging extraction. Bridge CORE-7 codes against the
      design's §5 (base_class native, loader never in domain/, no golden drift, `list_registered`
      for dump_catalog). Bridge — reconcile **CORE-7** (adopt the core-py registry for the
      driver axis, keep the config resolver local, no config→entry-point unification, loader in
      `utils/`/behind a port never `domain/`, zero new import-linter exceptions, no catalog
      drift; FIX the stale gate "voice BUILD-21" → "PROD-8 / core-py exists"; fold the dead
      `config/validation.py:89,94` pre-HK-8-prefix cleanup) AND file at intake the **new
      UI/panel driver-availability gating task**. Bridge write-back — lead ID: **CORE-7** + the
      new UI-gating ID — **RECONCILED AT INTAKE 2026-07-16 (bridge session), both delegations
      executed:** CORE-7 reconciled as **(d) scope drifted → redefined** (owner consulted before
      the edit per the bridge dialect's STOP rule) — narrowed to the entry-point-group registry
      only, `utils/class_loader.py` kept bridge-side, the config→entry-point unification recorded
      as REJECTED with the `dump_catalog` reason, and the stale **"voice BUILD-21"** gate corrected
      to **"PROD-8 / core-py exists"**. Driver axis verified live: the `locveil_bridge.devices`
      group, 9 drivers (`backend/pyproject.toml:98-107`) → `domain/devices/service.py:51-52`. The
      dead-code fold VERIFIED at intake and folded into CORE-7: `validate_class_references`
      (`infrastructure/config/validation.py:67-97`, the board's cited `:89,94` prefixes) has zero
      call sites — `validate_device_configs` never calls it, so `device_class` is **never validated
      at startup at all**. New UI-gating task filed: **UI-20** `[P1]` `[release]`.
      **Intake correction — decision 3's "split-brained" wording understates it: the surface is
      THREE-brained.** Beyond the raw-config-vs-loaded-driver split, (a) **room membership is a
      loaded-driver surface too** since the 2026-06-08 refactor (`domain/rooms/service.py:203-240`
      derives `room.devices` by walking `DeviceManager.devices`), so the device vanishes the moment
      a room is selected — the nav only shows it unfiltered; and (b) a **third brain**,
      `GET /devices/{id}/persisted_state` (`presentation/api/routers/state.py:75-92`), reads the
      state store directly and answers **200 with a stale snapshot** for a device the rest of the
      runtime denies exists. Root cause: `domain/devices/service.py:116-120` logs and skips with no
      retained status — the deliberate opposite of the setup()-failure policy (`:154-183`, device
      stays registered). UI-20 owns the suppress-vs-surface verdict and must make all three obey.
      **SKELETON CUT 2026-07-18 (commons session): `packages/core-py/` EXISTS — tag
      `core-py-v1`** (distribution `locveil-core-py` 1.0.0). `entry_point_loader.py` implements
      the design's §2 surface exactly — class only, no module-level singleton, `importlib.metadata`
      on py3.11 only, faithful cache + failure-ledger semantics plus the three agreed deltas
      (`base_class=` rejection into the ledger, single-EP `get_provider_class`, import-free
      `list_registered`); behavior suite 23 tests green; own pyproject + README per the guards'
      precedent. Amended same day (owner: "no new contract?" — right): the owned surface
      **`contracts/core-py/`** (STAMP `core-py` v1 + cross-ref README, registry row) landed per
      `process/contracts.md` §2 — the pin convention requires the owner's STAMP verbatim inside
      every consumer pin, and the first stamp already carries the `artifacts` completeness list
      (exactly `entry_point_loader.py`; tests/pyproject never travel). **ARCH-58 (voice) and
      CORE-7 (bridge) are UNBLOCKED** — they vendor at the tag with the strict pin +
      byte-identity test (design §3/§5). **Entry stays OPEN until both
      adoption write-backs arrive (owner ruling 2026-07-18)**; at close, also decide whether the
      parked logging extraction (ARCH-43 → OPS-14) spins off as its own entry or PROD-8 closes
      title-narrowed to the loader.
      The board lists delegated IDs but never asserts their status — per-repo ledgers own it.
- [ ] **PROD-9 — Landing page + first suite manifest** (D-11/D-12): `site/` on GitHub Pages
      at `locveil.com` — joint story, per-product blurbs, honest quickstart, routing only
      (never duplicates per-repo reference docs); the calver suite manifest ("Locveil
      2026.xx = voice vX + bridge vY + contract vZ + images …", gated on the cross-suites
      passing against exactly those pins) is its "current release" section. Unblocked by
      PROD-1.
- [ ] **PROD-11 — FUTURE design: Home Assistant in parallel to Wirenboard** (D-4's stress
      test): if the canonical DeviceCommand contract survives HA unchanged, voice gets zero
      tasks; if voice needs changes, the contract leaked WB-specifics. Waits until wanted.
- [ ] **PROD-18 — Catalog contract evolution, round 1** (HK-7 cluster B — the two
      designs that self-declared board-bound before the board existed). Members: bridge
      **VWB-33** (language-data contribution convention — catalog nouns/aliases vs voice
      donation verbs; convention prose may land in commons `process/`; binds voice's
      donation schema, a config-ui surface) + **VWB-34** (confirmation-timing published
      in the contract; the tier-3 async-job pattern is a real API redesign touching
      voice + UI). Voice seat/first consumer: **QUAL-82** (AC louver control, gated on
      VWB-33). **Binding condition (bridge):** one design arc, ONE batched golden/openapi
      cut, ONE voice re-pin — never two. Delegations: bridge — VWB-33 + VWB-34 intake
      reconciliation (their pre-board "once the board lands" wording converts to this
      entry's reference). Bridge write-back — lead ID: **VWB-33** + VWB-34. Voice —
      QUAL-82 gains the PROD-18 gate reference. Voice ID: **QUAL-82**.
- [ ] **PROD-19 — Intake consolidation: one door, locveil-reports** (HK-7 cluster C):
      retire the last pre-board public-issue intake channel; all problem/feature intake
      flows through the locveil-reports pipeline (`report-protocol-v1`). Delegations:
      voice — **BUILD-14**, RECONCILE at intake (the uncommitted-filing mechanism is
      retired; `wb-user-reports` is now `locveil/locveil-reports`). Voice ID:
      **BUILD-14**. Bridge — file the twin AT intake (HK-7 finding: BUILD-14's "the
      bridge repo has the same question" claim had no bridge task behind it). Bridge
      ID: **OPS-28** (written back 2026-07-14; reconciled — no pre-board machinery on
      the bridge side, but the public Issues tab is enabled bare; posture decided
      jointly with BUILD-14).
- [ ] **PROD-20 — Satellite first-light chain (visibility entry, HW-GATED)** (HK-7 q6,
      owner ruling: light PROD). The coupled multi-repo burst that fires when the
      satellite's first conforming descriptor reaches the bridge: satellite descriptor
      (DES-4 lineage) → bridge **DRV-37** (EspManagedDevice implementation, BLOCKED on
      it) → **VWB-39** (descriptor-pin conformance test) → the first deck vocabulary
      contract cut (golden bump) → ONE voice re-pin → config-ui panel. No new local IDs
      now — the members exist and per-deck tasks stay unfiled until first light BY
      DESIGN; the chain executes repo-to-repo per convention; this entry exists so the
      burst lands SEEN, not as a surprise. Closes when the first chain completes
      end-to-end and the re-pin is verified. IDs on record: bridge DRV-37 + VWB-39;
      satellite DES-4/FW-1 lineage. HW-GATED — no timing asserted.
## IMPL — commons implementation

- [ ] **IMPL-8 — contract-guard v3.1: ARTIFACTS-PATH rule (Option B — owner pick
      2026-07-18 at PROD-26 close)** (`packages/contract-guard`): every entry in a STAMP's
      `artifacts` list MUST be repo-root-relative and resolve at HEAD; a bare/ambiguous
      name FAILS (`ARTIFACTS-PATH`). Kills the false-drift class bridge VWB-43 found at
      OPS-32's first v3 run: v3 resolves artifacts from the repo root, so the catalog
      STAMP's bare `README.md` compares the ROOT readme on both sides (green by luck
      until the next root-README edit → baffling CONTENT-DRIFT on the catalog family) and
      its `catalog.golden.json`/`openapi.json` degrade to CONTENT-UNVERIFIABLE. Option A
      (folder-first resolution) REJECTED — one canonical path form beats two coexisting
      conventions. **Rollout coupling is real and sequenced by design:** bridge's catalog
      STAMP violates the rule and a STAMP is tag bytes, so bridge re-vendors v3.1 only
      AFTER its VWB-43 catalog cut rewrites the three entries as `contracts/catalog/…`
      (from the v3.1 tag its `[[tool]]` manifest nags — correct and advisory); voice and
      satellite stamps are repo-root already and may re-vendor freely; commons' own
      stamps all conform. The legacy singular `artifact` field stays informational —
      never validated (report-protocol's folder-relative singular is frozen history).
      Deliverable: rule + synthetic smoke tests per the v3 pattern, tag
      `contract-guard-v3.1` + STAMP bump in the same change.
