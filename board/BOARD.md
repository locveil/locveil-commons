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
- [ ] **PROD-27 — Logging-scheme extraction (OPTIONAL — spun off from PROD-8 at its
      close, owner ruling 2026-07-18)** (D-8's second leaf, parked by the PROD-8 council:
      "loader first, logging a later round"). Scope when activated: extract the shared
      logging scheme — bridge **OPS-12** (DONE) is the authored reference implementation,
      voice **BUG-30** is the hand-copy it retires (voice-side task: parked **ARCH-43**;
      bridge-side cleanup: OPS-14). Home: `packages/core-py` (second module beside
      `entry_point_loader.py`), tag = a `core-py-vX` minor/major per surface impact, strict
      pin + byte-identity consumption exactly like the loader (the ARCH-58/CORE-7 shape is
      the template). Rule-of-two is already satisfied in principle (the hand-copy pair IS
      two consumers) — this entry is OPTIONAL and trigger-driven, not queued: activate on
      owner interest, the next logging-shape pain in either repo, or a third consumer
      (satellite firmware logging is NOT one — different runtime). No delegations until
      activated; design-then-implement applies (ARCH-43 un-parks as the design task).
- [ ] **PROD-28 — HK-13 execution: single-sourced contract graph + enforcement gaps
      closed** (decision of record: HK-13 in `BOARD_DONE.md`, decided 2026-10-05, two
      rounds, all three keepers + commons; the normative rules already landed in
      `process/contracts.md` §1–§5 in the HK-13 landing commit — that text plus the HK-13
      entry is the design of record for the rule set). **Tagging (owner ruling q8,
      re-confirmed round 2): every task filed from this entry is tagged `[release]` in its
      receiving ledger**; the keepers' dissents are recorded in HK-13, not reopened. **Tag
      form:** every cut below is three-part (`-vX.Y.Z`); pre-HK-13 tags stay frozen.
      **Wave 0 — each repo, now, independent of everything else:** un-gate the guards in
      CI (run on every push), make layer-2 suites run when contracts move, fix known
      rotted pointers. **Commons build (this repo) — wave 0:** `contract-guard` CI job
      loses its path gate; a pytest job runs `eval/tests` (the layer-2 pin + manifest
      tests, never in CI before); a `repin --check` step. **Commons build — wave 1, ONE
      tag set (the keepers' sweep-once condition):** (1) **contract-guard v4** →
      `contract-guard-v4.0.0`: `artifacts` key mandatory (legacy STAMP = WARN until its
      next cut; an empty list needs a guard pointer that resolves — settle the pointer
      vocabulary here, package-style contracts included); pin completeness (pin files
      cover the carried owner STAMP's `artifacts`); reserved names (`README.md` /
      `PIN.json` never enumerated, no duplicate file names in one family — fails at the
      owner); STAMP at HEAD equals STAMP at its tag; every pointer field resolves to a
      file; registry `<family>-vX` strings equal the STAMP/PIN tag; an unlisted file in a
      strict pin folder FAILS; three-part version form for STAMPs dated from 2026-10-05.
      (2) **repin v2** → `repin-v2.0.0`: pin file set derived from the owner's STAMP
      `artifacts` at the tag (STAMP always included; consumer `files` kept only as the
      fallback for pre-enumeration tags); absent cross-repo destination skipped, not
      never-pinned (voice's CI blocker); touch-the-family from a diff base using `dest`
      paths + a structured `conformance` path; a `minor` severity level with patch gaps as
      their own class (release gates: families fail on minor+, patch and `[[tool]]` gaps
      warn); `[[tool]]` entries carry path + sha256, verified locally. (3) The pinned
      contract-triad block re-worded to the HK-13 rules — ships with the next scope tag
      (blocks version with scope tags, HK-2). (4) **Commons surfaces:** `report-protocol`
      STAMP gains `artifacts` → `report-protocol-v1.0.1` (bytes only; re-pin owed: voice,
      bridge); new owned family **`docs-manifest-schema`**
      (`contracts/docs-manifest-schema/`, artifact
      `process/user-docs/manifest.schema.json`, first tag `docs-manifest-schema-v1.0.0`)
      and the internal `contracts/docs-manifest/` STAMP retired as instance data; the
      **workbench machine schemas** owed since HK-12 (manifest-fragment + runtime-config)
      land as enumerated artifacts at the next workbench cut — bridge's plugin and voice's
      config-ui are waiting on them; remaining commons STAMPs declare `artifacts`. (5)
      **Generated org-wide graph page** (owner-ticked rider): built from the four repos'
      STAMPs + `.repin.toml` files — a view, never a source. (6) When voice's WS machine
      core lands: commons pins `ws-protocol` for the eval WS provider with a hermetic
      conformance test against the fixtures, and `CLAUDE.md`'s WS source-of-truth rule
      gains the matching machine-core sentence (ends the HK-12 eval deferral for this one
      edge). **Delegations (board-as-outbox; owners cut FIRST, then ONE sweep per repo
      after the commons tag set):** **bridge** — (a) the README split, startable
      immediately (guard v3.1 already accepts the shape; it MUST land before guard v4 is
      vendored): `catalog-v1.10.0` with new enumerated
      `contracts/catalog/catalog-contract.md` (param semantics + the versioning rule;
      README keeps intro, changelog, file list, regeneration, drift-guard and realism
      notes) and `device-integration-v1.2.0` with new enumerated
      `contracts/device-integration/convention.md` (who must conform, the `wb-mqtt-v1`
      profile, REST URL conventions, the descriptor + test-locked example, pin/conformance
      rules; README becomes index + history); update the generator and test file lists,
      the hand-written device-integration STAMP, the cross-link and the docs-manifest
      nodes; three-level versions in `dump_catalog.py`; CORE-12 takes the next catalog
      version (batching withdrawn); re-pin owed: voice + commons (catalog), satellite
      (first pin, via DES-4); (b) CI: un-gate guard + repin steps, touch-the-family once
      repin v2 exists, image-dispatch gate at minor-or-major with tools warning; (c) the
      sweep: re-vendor the tag set, migrate `.repin.toml` (drop `files`), re-pin
      `report-protocol-v1.0.1`; (d) docs-manifest remediation: the drifted schema copy
      becomes a pin of `docs-manifest-schema`, the internal STAMP retires, the "no tag
      cut" prose is re-truthed; (e) reconcile VWB-39's stale text at intake. Bridge ID:
      _pending write-back_. **voice** — (a) wave 0: un-gate contract-guard, close the
      layer-2 path-gate hole (pytest must trigger on `contracts/**` and every enumerated
      artifact path), fix the `docs/manifest.json` guard pointer still naming
      `irene/tests/…`; (b) owner cuts: `ws-protocol-v1.0.1` (bytes only, served value
      stays "1"; absorbs the two post-tag drifts `939a205` + `346a5f3`; STAMP enumerates
      `docs/guides/websocket-api.md`; the version test compares the MAJOR only),
      `trace-format-v1.0.1` (`docs/guides/tracing.md` enumerated whole — the DOC-14
      refusal is remediated by owner ruling q3), `ui-openapi` and `wake-pack` STAMPs
      declare (empty list + resolving guard pointer; wake-pack may ride ASSET-6), internal
      docs-manifest STAMP retired for a `docs-manifest-schema` pin (the manifest test
      becomes hermetic), ARCH-48 narrowed to a major-only comparison; (c) the sweep:
      re-vendor the tag set, drop `files` from `.repin.toml`, re-stamp every pin (both
      catalog destinations at `catalog-v1.10.0`; the re-stamp fixes the two rotted
      `conformance` pointers), delete the manual re-pin recipe in
      `contracts/pins/report-protocol/README.md`, add the CI `repin --check` step and the
      dispatch gate; (d) **the WS machine core — design AND implementation now (owner
      amendment q7; round 2 q4: all slices in order, nothing waits for FW-1a and FW-1a
      waits for nothing):** design doc first (satellite reviews it — one frames file vs
      one per frame type, unique flat file names), then slice 1
      `contracts/ws-protocol/frames.golden.json` + an owner test validating real frames
      from the existing WS suites, slice 2 JSONL transcripts, slice 3
      `ws-protocol.schema.json`; lands as `ws-protocol-v1.1.0`. **Approved amendment to
      `ws-protocol-doc-canonical` (owner, round 2 q3), verbatim:**
      "`contracts/ws-protocol/` additionally holds the protocol's hand-written machine
      core (golden frames, transcripts, schema). It is subordinate to the document: on
      disagreement the document wins and the core is fixed. Never generated from code; a
      wire change updates document and core in the same change." Voice ID: _pending
      write-back_. **satellite** — (a) `esp32-site-v1.1.0` as a standalone cut (STAMP
      enumerates the template only; not riding DES-5); re-pin owed: voice; (b) ONE sweep
      after the commons tag set: re-vendor scope-guard + contract-guard + repin (it trails
      on two today, unfiled), un-gate the CI workflow, drop `files`, trim both pin READMEs
      (manual recipes + stale lines out), pin `docs-manifest-schema` and retire the
      internal STAMP, fix the registry's "no git tag" line, touch-the-family hard from
      FW-1a start (its own offer); (c) re-pin `ws-protocol` at `v1.0.1`, then at `v1.1.0`
      — FW-1a's conformance test consumes the pinned fixtures from the day they exist and
      is never gated on them; (d) DES-4 amended: its pin set comes from the
      `device-integration-v1.2.0` STAMP and it waits for that cut (confirmed: nothing
      consumes the pin yet). Satellite ID: _pending write-back_. **Sequencing:** wave 0
      and the owner cuts need no new tooling and start on intake; the commons tag set is
      on every repo's `[release]` path, so commons builds first; each consumer then sweeps
      once. Keeper and coordinator estimates, not measured: about 12 owner sessions across
      the four repos (voice ~5, bridge ~3.25, satellite ~0.5, commons ~3). The board lists
      delegated IDs but never asserts their status — per-repo ledgers own it. Closes when
      the commons build is done and all three lead IDs are written back. **Commons intake
      (2026-10-05):** the build is filed as **IMPL-10 … IMPL-19** under `## IMPL` (one task =
      one commit).

## IMPL — commons implementation

- [ ] **IMPL-12 — commons adopts HK-13: CI wave 0 + config migration** (PROD-28, filed at
      intake 2026-10-05; after IMPL-10/11). `contract-guard` CI job loses its path gate; a
      pytest job runs `eval/tests` (layer 2 — never in CI before); `repin --check` step
      with touch-the-family; `.repin.toml` migrated to the v2 shape; hook updated.
- [ ] **IMPL-17 — contract-triad block re-worded to HK-13, scope cut** (PROD-28 commons
      build item 3, filed at intake 2026-10-05). `process/claude-blocks/contract-triad.md`
      digests the new rules (declared artifacts, three-part tags + three levels, reserved
      names, release severity); ships as a block-only scope release (script bytes
      unchanged); commons' `CLAUDE.md` re-pinned in the same change. Re-pin owed: voice,
      bridge, satellite.
- [ ] **IMPL-18 — generated org-wide contract graph page** (PROD-28 commons build item 5;
      owner-ticked HK-13 rider, filed at intake 2026-10-05). A generator reads the four
      repos' STAMPs and `.repin.toml` files and writes the owner → consumer graph as a
      view — never a source; regenerated on demand, checked for freshness where the
      siblings are on disk.
- [ ] **IMPL-19 — commons pins `ws-protocol` for the eval WS provider** (PROD-28 commons
      build item 6, filed at intake 2026-10-05; GATED on voice's `ws-protocol-v1.1.0`
      machine-core cut). Pin + a hermetic conformance test against the golden frames;
      `CLAUDE.md`'s WS source-of-truth rule gains the machine-core sentence; ends the
      HK-12 eval deferral for this one edge.
