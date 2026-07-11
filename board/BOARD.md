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

- [ ] **PROD-4 — Normative ops spec** (D-12) in `process/`: the converged pattern (sdcard
      clone update-time-only, `/mnt/data/<name>-config`, repo-owns-config rsync, `.env`
      secrets, systemd oneshot `RequiresMountsFor=/mnt/data` ONLY, GHCR pull-not-build, log
      rotation, 127.0.0.1 healthchecks, start-period > fleet boot) + a conformance checklist.
      Shared *scripts* only at the third consumer (rule of three). Delegates on completion:
      voice BUILD-18 (narrowed) + bridge OPS-15.
- [>] **PROD-6 — Problem-report spec + report-protocol machine core** (D-12; RESCOPED by
      council HK-3, 2026-07-11 — was "spec-level unification only"). Commons owns the shared
      inbox truth (voice ceded the ARCH-30-era de-facto ownership; the reports repo is the
      first CONSUMER, never the owner). Two-part form per the owner's contract instinct:
      the wire-visible surface as a small versioned machine core —
      `process/report-protocol/report-protocol.json`, tags **`report-protocol-vN`**, ticket
      TYPE as a first-class dimension (extension-proofed for feature-requests-as-v2) —
      pinned + test-validated by voice, bridge, AND the reports repo (its bootstrap
      generates labels from the pin); judgment/policy stays prose in
      `process/problem-reports.md` (retention, leak fence, redaction boundary, choreography
      semantics, lens co-ownership governance). No SKILL.md pinned block in v1 (HK-3 q4:
      the core catches the observed drift class). Commons-side executed 2026-07-11
      (spec + core authored, `report-protocol-v1` tagged). Consumption delegations ride the
      PROD-14 delegation record (one intake per repo); PROD-6 closes with them.
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
- [>] **PROD-14 — locveil-reports: org move + credential cutover + re-points** (council
      HK-3, decided 2026-07-11 over two rounds — positions in `JOURNAL.md`; spec home:
      PROD-6). Decision: transfer `droman42/wb-user-reports` → **`locveil/locveil-reports`**
      (private, non-negotiably) as a sequenced slug-and-credential sweep — no redirect
      reliance anywhere (both collectors POST; a 301 is not reliably replayed; both spool
      durably so the window loses nothing but must stay short). Council finding: the
      cross-repo triage PAT is fine-grained under `droman42` and **presumed dead since the
      2026-07-11 code-repo org move** (last triage 2026-07-06) — re-mint regardless.
      **Phase 0 — DONE 2026-07-11** (`wb-user-reports@15d788b`): all 16 stale
      `droman42/wb-mqtt-*` refs in triage.yml/lens files/README/bootstrap.sh →
      `locveil/locveil-*`; live lens-label descriptions updated. (Ticket #2 verified
      closed-complete; `fix-pr-open` is its terminal outcome label by design.)
      **Phase 1 — OWNER checklist (gate: do the org checks FIRST — the GHCR lesson).**
      Progress 2026-07-11: (2) cross-repo PAT re-minted under the org + secret updated
      (owner); (3) transfer+rename EXECUTED — the repo is `locveil/locveil-reports`
      (private; secrets/issues/labels survived; local remote re-pointed). Reports-repo
      protocol consumption also DONE (`locveil-reports@676091f`+`ef0b3d4`): core pinned as
      `report-protocol.pin.json`, `bootstrap.sh` generates labels from the pin,
      `protocol-check` CI green (compares live labels weekly + on push), README pointer
      flipped to `process/problem-reports.md`, post-transfer self-references swept.
      **Phase 1 COMPLETE 2026-07-11** (journal): App installed + verified live (plumbing
      run on #2), device PATs everywhere, end-to-end smoke GREEN (ticket #3: sent →
      protocol-correct filing → triage → needs-owner). Residual: org base-permissions
      check (owner); voice delegation gains two finds — `[reports]` enabled in the
      canonical WB7 profile config + stale `wb7.env` port (6000→8080); owner closes #3
      via `/inbox`. Remaining board action: the two delegations below.
      (1) org settings: allow fine-grained PAT access; members' base repo permission =
      none (bundle privacy boundary becomes the org's policy); Actions allowlist covers
      `anthropics/claude-code-action`; (2) re-mint `REPORTS_CROSS_REPO_TOKEN` NOW:
      fine-grained, resource owner `locveil`, repos `locveil-voice`+`locveil-bridge`,
      Contents+PR write → update the repo secret; (3) transfer + rename the repo to
      `locveil/locveil-reports`; (4) Claude GitHub App: configure on the org to cover the
      transferred private repo + both code repos; (5) mint the device PAT: fine-grained,
      owner `locveil`, repo `locveil-reports` only, Issues+Contents write → WB7
      `/mnt/data/locveil-voice-config/.env` (`IRENE_REPORTS_TOKEN`) + voice runtime
      `[reports].repo = "locveil/locveil-reports"`, and
      `/mnt/data/locveil-bridge-config/.env` (`WB_REPORTS_TOKEN`) + bridge `system.json`
      explicit `reports.repo`; restart both; (6) smoke test end-to-end: file a report from
      a device → spool/deliver → triage runs → fix-PR lands on a `locveil/*` repo; verify
      both spools drained. **Phase 2 — delegations** (pull, verify per
      `task-start-reconciliation`, file local IDs, write back):
      - **Delegation → locveil-voice**: (1) slug sweep — inbox `SKILL.md` (4 sites),
        `problem-report-inbox` invariant (2 sites), `config-master.toml` example,
        design-doc operative refs (BUILD-14 ledger text reconciles at its own intake);
        (2) drift fixes: adopt the ping-pong guard + bridge's affirmative post-merge ledger
        wording; (3) `lens-voice.md` co-ownership re-review in the reports repo (VWB-26
        pattern); (4) protocol consumption (after `report-protocol-v1`): pin the core,
        one conformance test on the collector's emitted labels/prefix/path, restructure
        `locveil-voice/docs/design/problem_reports.md` shared sections into pointers to
        `process/problem-reports.md` (no ARCH-30 status flip). Voice ID: **ARCH-46**
        (intake 2026-07-11; narrowed — the slug sweep + the `[reports]`-in-profile find
        were already done by voice BUILD-31 before this write-back).
        **Verification (commons, 2026-07-11) — one item BOUNCED (owner decision):**
        items 1–3 + the smoke finds verified done (lens re-review `1ca251e` is a genuine
        VWB-26-pattern pass — found and fixed a real stale claim; conformance test 11/11;
        sweep clean; all seven profiles carry `[reports]`). Item 4's doc restructure was
        delivered as annotate-and-defer: a commons-ownership header was added but §5 (the
        envelope) and §7 (triage choreography) remain IN FULL — two complete copies of the
        shared vocabulary, the two-sources-of-truth pattern `process/problem-reports.md`
        §1 forbids. NOT accepted: replace §5 + §7 bodies with pointers to the commons spec
        (+ the core pin) as agreed in HK-3 round 2; voice-side content stays. ARCH-46
        remains open voice-side until the lift-out lands.
      - **Delegation → locveil-bridge**: (1) VWB-29-shaped re-point — slug sweep
        (SKILL.md ×5, invariant command, INSTALL.md, design-doc operative refs), make
        `reports.repo` explicit in `system.json` and DROP the slug schema default (HK-3
        q4 round 1) → openapi regen + `contracts/` pin bump + UI regen + voice re-pin
        chain; spool-drain verification post-cutover; (2) `lens-bridge.md` co-ownership
        re-review (VWB-30 as pre-named); (3) protocol consumption: pin the core, one
        conformance test over `service.py:210/216`, retire the hardcodes into
        pin-validated form. Bridge IDs: **VWB-35** (re-point) / **VWB-36** (lens re-review —
        the pre-named VWB-30 was stale at intake: that serial was consumed 2026-07-09 by the
        bridge's REL-5 remediation; re-serialed per assigned-once) / **VWB-37** (protocol
        consumption). Written back at intake 2026-07-11.
      - **Reports-repo consumption** (no ledger there; executed commons-side post-transfer):
        `bootstrap.sh` generates labels from the pinned core + trivial CI compare; README
        pointer flips from voice's design doc to `process/problem-reports.md`.
