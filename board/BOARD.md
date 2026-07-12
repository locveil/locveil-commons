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
- [ ] **PROD-7 — Contract tagging + scripted re-pin** (D-11): bridge tags `contract-vN`
      releases with artifacts (bridge VWB-29, filed at intake); voice gets `make repin
      CONTRACT=vN` + staleness gate (voice BUILD-24). Commons side: none beyond this entry —
      write local IDs back when the sessions pick them up. Bridge ID: VWB-29 (intake filed
      2026-07-08, uncommitted-mechanism last use). Voice ID: BUILD-24.
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
- [ ] **PROD-16 — The contract convention + the coordinated cut** (decided by council
      **HK-5**, 2026-07-12, one round with all THREE product keepers — arc in
      `BOARD_DONE.md` HK-5; **normative: `process/contracts.md`**). Decision: one org-wide
      convention — contract classes; uniform layout **enforced immediately** (owner q3:
      `contracts/<name>/` owned + `contracts/pins/<name>/` consumed + registry README
      indexing both, direction-labeled; no grandfathering); STAMP core
      `{contract, version, tag, date, owner_repo}`; family-named tags, **no prose
      history** (STAMP + tag are the only version authority from first tag on); two-layer
      enforcement — new vendored **`contract_guard.py`** (coherence-only; commons regime
      2, `packages/contract-guard/`, tags `contract-guard-vN`; scope-guard stays
      ledger-only) + mandatory per-repo conformance tests and day-one owner-side guards;
      staleness via runtime version-reporting + release-time re-pin flows, NEVER
      cross-repo push gates; prose contracts = block-pin style canonized; per-instance
      config inputs (bridge descriptors) are NOT pins; sidecar stamps for third-party
      formats; repo-internal generated contracts (voice BUILD-26) reuse the same
      mechanics. First catalog tag: **`catalog-v1.5`** (lineage continues; README
      changelog STAYS as narrative — STAMP + tag are the machine-readable authority).
      Commons-side deliverables — ALL EXECUTED 2026-07-12: the spec; **contract-guard
      v1** (`packages/contract-guard/contract_guard.py`, tag `contract-guard-v1`, wired
      into `hooks/pre-commit` + path-gated `contract-guard` CI job); commons restructure
      (`contracts/pins/{catalog,crossover-fixtures}/`, `report-protocol` →
      `contracts/report-protocol/` + STAMP sidecar + per-contract READMEs, tag v1
      untouched); registry README; eval re-point (4 test/module path sets — a 4th
      consumer, `test_device_command_eval.py`, found and fixed; suite 40/40 green);
      guard green with 3 by-design legacy warnings (strict PINs arrive at next re-pins).
      Execution order: `process/contracts.md` §6. Delegation record:
      - **Delegation → locveil-bridge**: (1) VWB-29 RESCOPED — the owner-side cut:
        catalog → `contracts/catalog/`, code-level `CONTRACT_VERSION` constant, STAMP
        core fields, tag `catalog-v1.5`, registry README (changelog kept, continued);
        (2) relocate consumed pins NOW per q3 (report-protocol pin →
        `contracts/pins/report-protocol/` + test paths + the reports-repo lens teaching
        note); (3) NEW small task: device-integration owner-side guard (committed
        schema-validating example fixture + CI check) closing the model's own gap,
        pre-VWB-39; (4) vendor contract-guard when tagged. Bridge IDs: (write back).
      - **Delegation → locveil-voice**: (1) ARCH-47 UNGATED and rescoped as the
        convention's first voice instance — `contracts/ws-protocol/` STAMP + doc-header
        "Protocol version" line + served code constant + version-triple conformance test
        + `register` version fields, tag `ws-protocol-v1`; wake-pack sidecar stamp
        (`wake-pack-v1`, content hashes — third-party manifest never forked);
        (2) BUILD-24 born against the final bridge layout (generalized `make repin`,
        staleness at release time; NOTE: the commons restructure moved the pin to
        `contracts/pins/catalog/` — voice's `eval/Makefile` +
        `device.promptfooconfig.yaml` reference the OLD
        `../../locveil-commons/contracts/` paths, re-point them with this task or the
        restructure); (3) NEW small task: restructure voice `contracts/`
        to the pins shape (immediate per q3); (4) BUILD-26 cites the convention (internal
        openapi drift guard + STAMP, same mechanics in-repo); (5) vendor contract-guard
        when tagged. Voice IDs: (write back).
      - **Delegation → locveil-satellite**: (1) OPS-3-shaped task — restructure to the
        pins shape, upgrade the WS commit-pin to an artifact-copy pin with PIN.json NOW
        (stamped pin when `ws-protocol-v1` lands), vendor contract-guard, wire the CI
        job, fix the stale `contracts/README.md` status line; (2) DES-4 mirrors
        device-integration per this shape; (3) OPS-1 gains the wake-pack
        hash-at-publish requirement. Satellite IDs: (write back).
