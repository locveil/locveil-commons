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
- [ ] **PROD-25 — CI checkouts must fetch tags for contract-guard: the convention +
      consumer sweep** (filed 2026-07-15 by the bridge session, off bridge **OPS-30**).
      Finding: contract-guard-v2's `TAG-MISSING` rule (PROD-22) resolves owned STAMP tags
      via `git tag -l`, but the default `actions/checkout` clone is shallow AND tag-less —
      the rule can never pass in a CI job whose checkout doesn't opt into tags. The bridge
      hit it live: the OPS-27 re-pin push failed its own path-gated CI job unnoticed
      (run 29317709478, 2026-07-14), every later push skipped the job, and the first
      `workflow_dispatch` (2026-07-15) re-exposed it as a 3× TAG-MISSING false alarm —
      nothing wrong with the contracts. Fix class is one line: `fetch-tags: true` on the
      guard job's checkout (shallow stays fine — the rule only needs the tag ref). Sweep
      verified 2026-07-15: **commons' own `.github/workflows/contract-guard.yml` is latently
      broken NOW** (runs the v2 source package, two owned STAMPs name tags
      `docs-manifest-v1`/`report-protocol-v1`, bare checkout — fires on the next
      `contracts/**` push); **voice** (`ci.yml` contract-guard step) and **satellite**
      (`contract-guard.yml`) are vendored at v1 (no tag rule yet) with bare checkouts —
      the gap bites at their contract-guard-v2 re-pin, so the checkout fix should ride
      that re-pin. Deliverables: (1) amend `process/contracts.md` §4 (the consumption
      model) — a CI job running contract-guard must give its checkout tags, with the
      failure signature named; (2) fix the commons workflow (same change); (3) delegate
      the checkout fix + v2 re-pin to voice and satellite (local IDs to be written back).
      IDs on record: bridge **OPS-30** (done 2026-07-15 — the reference fix).
      **Commons deliverables (1)+(2) EXECUTED 2026-07-15** (sprint-02 discovery
      reserve): `process/contracts.md` §4 gained the CI-checkout requirement with the
      failure signature named; `.github/workflows/contract-guard.yml` checkout gained
      `fetch-tags: true`. Remaining: the voice + satellite delegations (checkout fix
      rides their contract-guard-v2 re-pins). Voice ID: **BUILD-38** (written back
      2026-07-15; intake correction — the sweep's "voice at v1" was stale: voice's
      BUILD-37 had already re-vendored v2 on 2026-07-14, leaving only two v1 labels,
      so voice was latently broken NOW like commons; BUILD-38 = checkout fix + label
      bumps, TAG-MISSING signature reproduced and cleared by simulation). Satellite
      ID: **OPS-8** (written back 2026-07-15; same intake correction — the sweep's
      "satellite at v1" was stale: satellite's OPS-5 had already re-vendored v2 on
      2026-07-14, so its guard job was latently broken NOW, both owned STAMPs firing;
      fix landed standalone, failure + fix both reproduced in a tag-less local clone).
      **REOPENING FINDING (satellite session, 2026-07-15 — the fix class is a dud):**
      `fetch-tags: true` does NOT deliver tags on the default shallow single-commit
      fetch — actions/checkout#1467: the flag only drops `--no-tags`, and git tag
      auto-following can't see tags on unfetched commits, so STAMP tags pointing at
      older commits never arrive. Proof, live: satellite's flag-fix run 29414821199
      FAILED (2× TAG-MISSING, checkout log shows no tag refspec in the fetch);
      **commons' own post-fix run dd7c270 (29414186194) FAILED identically — the
      EXECUTED deliverable (2) is defective and the §4 amendment (1) prescribes the
      dead one-liner.** Voice's BUILD-38 was cleared "by simulation" — same latent
      state expected on its next live run. Working fix (satellite **OPS-9**, done
      2026-07-15): an explicit `git fetch --tags --depth=1 origin` step after
      checkout — verified from checkout's exact clone-procedure replica AND live
      green (satellite run 29415097500 @ 5761e7d). Back on commons + voice: re-fix
      the workflows and re-word §4 (fix class: explicit tag-fetch step, or
      `fetch-depth: 0` where full history is acceptable — the flag alone never works).
      **REOPENING DISCHARGED 2026-07-15 (voice session):** voice's next live run
      confirmed the prediction (run 29417879036, 4× TAG-MISSING with the flag set) →
      voice **BUILD-39** (explicit-step fix per the OPS-9 reference, re-simulated +
      pushed); commons re-fixed in the same breath — `contract-guard.yml` now runs the
      explicit `git fetch --tags --depth=1 origin` step and §4 is re-worded to name
      the dud (flag-only prescriptions removed, OPS-9 recorded as the reference, all
      three failing runs cited). Remaining before close: bridge confirms OPS-30 on
      checkout@v6 with a live tag-resolving run (repo-to-repo heads-up; v6 may or may
      not share #1467's behavior), and a green `contracts/**`-path run lands on
      commons + voice.

## IMPL — commons implementation
