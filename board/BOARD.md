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
- **Ledger discipline (HK-1 / PROD-13, normative: `process/ledger-discipline.md`):** this
  board is the active ledger; completed entries MOVE to `BOARD_DONE.md` in the same change
  as their journal entry. Council topics carry the `HK-N` prefix; being born-decided they
  file directly into `BOARD_DONE.md` (a deferred council parks its HK entry here). Guarded
  by scope-guard (`packages/scope-guard/`, config `.scope-guard.toml`).

## Ledger

Completed entries live in `BOARD_DONE.md` (moved on close; `process/ledger-discipline.md`).

## PROD — cross-repo initiatives

- [ ] **PROD-4 — Normative ops spec** (D-12) in `process/`: the converged pattern (sdcard
      clone update-time-only, `/mnt/data/<name>-config`, repo-owns-config rsync, `.env`
      secrets, systemd oneshot `RequiresMountsFor=/mnt/data` ONLY, GHCR pull-not-build, log
      rotation, 127.0.0.1 healthchecks, start-period > fleet boot) + a conformance checklist.
      Shared *scripts* only at the third consumer (rule of three). Delegates on completion:
      voice BUILD-18 (narrowed) + bridge OPS-15.
- [ ] **PROD-8 — core-py bootstrap + first two extractions** (D-8): `packages/core-py`
      skeleton (own pyproject, `core-py-vX` tags), then the two designs — dynamic code
      loader (voice ARCH-42; voice consumer #1, bridge #2 via CORE-7) and logging scheme
      (voice ARCH-43; retires the BUG-30/OPS-12 hand-copy → bridge OPS-14).
- [ ] **PROD-9 — Landing page + first suite manifest** (D-11/D-12): `site/` on GitHub Pages
      at `locveil.com` — joint story, per-product blurbs, honest quickstart, routing only
      (never duplicates per-repo reference docs); the calver suite manifest ("Locveil
      2026.xx = voice vX + bridge vY + contract vZ + images …", gated on the cross-suites
      passing against exactly those pins) is its "current release" section. Unblocked by
      PROD-1.
- [ ] **PROD-10 — ui-kit package + stylebook** (D-8/D-9, next release): `packages/ui-kit`
      npm package consumed by both config UIs (`../locveil-voice/config-ui`,
      `../locveil-bridge/ui`); component boundaries keep one-shell-with-plugins reachable —
      no plugin framework before two real plugins exist.
- [ ] **PROD-11 — FUTURE design: Home Assistant in parallel to Wirenboard** (D-4's stress
      test): if the canonical DeviceCommand contract survives HA unchanged, voice gets zero
      tasks; if voice needs changes, the contract leaked WB-specifics. Waits until wanted.
- [ ] **PROD-17 — User-facing docs: the org convention + the docs manifest** (decided by
      council **HK-6**, 2026-07-12, two rounds, all three keepers — arc in
      `BOARD_DONE.md` HK-6; **normative: `process/user-docs.md`** + machine schema
      `process/user-docs/manifest.schema.json`). Decision digest: scope taxonomy with
      audience column (operator docs IN scope; ADR class ABOLISHED — dissolve/archive);
      style conventions from the exemplar corpora (no tracking language incl.
      schema/OpenAPI descriptions; Graphviz .dot+render pairs; status banners audited;
      EN docs, RU product surface quoted — no Russian docs today); the hardened rule:
      **docs-verdict line in every completion entry** (`docs: <node-ids>` /
      `docs: none — <why>`), caused-vs-discovered split, release-cut + phase-gate manifest
      reviews, docs-review tasks fileable any time and a COMMONS-filed one fans out to
      all repos via board-as-outbox; the **docs manifest** as repo-internal contract
      (`docs/manifest.json` + `contracts/docs-manifest/` STAMP @ docs-manifest-v1; small
      repo-owned surface→glob vocabulary; pending-gate slots; derives_from;
      canonical{invariant,stamp,guard} carve-out; per-repo coherence test on the
      drift-guard pattern — promotion to shared tooling at rule-of-two); node policy:
      additions ride the causing task (the failing test IS the policy), floor gates
      coverage loss only — **floor applies where the capability exists** (owner round-2),
      removals by tombstone/filed supersession; **CONTRIBUTING.md required per repo,
      inside the manifest** (audience: contributor). Commons-side deliverables — spec +
      schema + **scope-guard 1.2.0 `scope-v5`** (docs-verdict presence rule +
      re-pinned shared-invariants block with the new invariant) + template seeds
      (skeleton manifest, CONTRIBUTING stub, verdict config key) EXECUTED 2026-07-12;
      commons' own manifest + CONTRIBUTING.md pending as commons follow-up work under
      this entry. Org README: folded into PROD-9 (no artifact now). Delegation record:
      - **Delegation → locveil-voice**: (1) DOC-shaped task — live stale fixes: the
        `build-docker.md` port-6000 quartet + `websocket-api.md` :6000 example line, one
        pointer sentence in `guides/satellite.md` to the satellite provisioning runbook,
        verify the voice-trigger HF link, fix the `QUICKSTART.md` "ESP32 satellite
        controllers (WB7/WB8)" mislabel; (2) author `docs/manifest.json` +
        `contracts/docs-manifest/` + the coherence test; CONTRIBUTING.md gains the
        contracts-registry + eval links and its manifest node; (3) rule-dialect update
        (CLAUDE.md invariant points at the manifest; `ops/INSTALL.md` enters scope);
        (4) re-pin scope-guard @ `scope-v5` (block + `docs_verdict_since` config).
        Voice IDs: **DOC-11 (live stale fixes), DOC-12 (manifest + coherence test +
        CONTRIBUTING), BUILD-35 (dialect + scope-v5 re-pin)** — all `[release]` (filed
        2026-07-12, voice `51ce922`; status lives in the voice ledger).
      - **Delegation → locveil-bridge**: (1) DOC staleness pass — CONTRIBUTING.md
        pre-VWB-29 contract paths, the OpenAPI field-description design-doc refs
        (config-ui-stays-functional: regen openapi + UI types same change), the 5
        REL-4-unverified diagrams; (2) manifest + coherence test + dialect update;
        (3) **ADR dissolution, one task**: 0006 → CONTRIBUTING dependency-policy section
        + OPS-19 re-point; 0001–0005 verify-and-archive with supersession banners;
        (4) re-pin scope-guard @ `scope-v5`. Bridge ID: (write back).
      - **Delegation → locveil-satellite**: (1) OPS-shaped task — author the manifest
        (pending-gate nodes for FW-gated docs naming their gates; derives_from onto
        `docs/devices/`; phase-crossing reviews) + create CONTRIBUTING.md (phase
        process, pin discipline, leaf-truth corpus rule, per-phase toolchain map);
        (2) the provisioning-README user-grade pass (strip tracking refs; replace the
        `.pio` publish line with an execution-layer-neutral note deferring to DES-3);
        (3) re-pin scope-guard @ `scope-v5`. Satellite ID: (write back).
