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
      bridge's `config-master-tree` is canonical as-is and needs none; (5) **secrets
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
- [ ] **PROD-10 — ui-kit package + stylebook** (D-8/D-9, next release): `packages/ui-kit`
      npm package consumed by both config UIs (`../locveil-voice/config-ui`,
      `../locveil-bridge/ui`); component boundaries keep one-shell-with-plugins reachable —
      no plugin framework before two real plugins exist. **Sequencing note (HK-7):**
      bridge OPS-13 (eslint-9/vite-6 toolchain pass, absorbing UI-8) must not run twice —
      if ui-kit lands first it imposes its own toolchain; coordinate the order at
      whichever activates first.
      **Design-phase shape (owner discussion 2026-07-12; premise: the owner is not a UI
      professional and expresses intent by sketch and plain words — the proven precedent
      is `locveil-bridge/docs/design/ui/remote.png`, the paper scan that became
      `RemoteControlLayout.tsx`; sketches carry zoning/hierarchy fully, the stylebook
      supplies what they can't: color, type, spacing, radii, states):**
      three stages when this activates —
      (1) **Extraction**: reverse-engineer the IMPLICIT design system from what the owner
      already approved — the two shipped UIs + the remote scan — into a draft token
      inventory + a divergence list (where the two UIs quietly disagree);
      (2) **Style council — preference elicitation by RENDERED A/B, never by terms**: the
      dossier mechanism repurposed — pages show rendered variants (density, radius, type
      pairs, contrast, light/dark) side by side; the owner clicks preferences +
      free-words comments (RU/EN both fine); each click becomes a token. 2–3 rounds;
      no design vocabulary required from the owner, ever;
      (3) **Codification**: tokens file → the stylebook (prose + rendered examples; a
      docs-manifest node per HK-6) → ui-kit components built ON the tokens → a
      **`ui-style` skill** in commons as the executable half (the council/scope-guard
      pattern: every future UI session loads the stylebook instead of reading about it),
      versioned with the package (`ui-kit-vX`). Tooling prep at activation: install the
      `frontend-design` skill (anthropics/skills) for the professional-realization side;
      `skill-creator` to author `ui-style`; Storybook as the kit's living workbench.
      Standing rule: owner sketches remain first-class input — a zoning sketch + the
      token system IS a professional spec.
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
      ID: (write back).
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
- [ ] **PROD-21 — Python backend layout & naming: the org convention + both migrations**
      (decided by council **HK-8**, 2026-07-13, three measured rounds — arc in
      `BOARD_DONE.md` HK-8; **normative: `process/python-layout.md`**, which satisfies
      design-then-implement for the tasks below). Decision digest: layout org-wide =
      `<component>/src/<pkg>/` + `<component>/tests/` (outside the package); product
      data at repo root — config tree named `config/` SINGULAR org-wide (matches the WB7
      runtime trees); Dockerfiles in root `docker/` with root build context (file axis =
      dialect: voice per-arch justified by ML profiles, bridge per-component justified by
      OPS-11's arch-identical finding); UNIFORM import rename for product backends —
      `irene`→`locveil_voice`, `wb_mqtt_bridge`→`locveil_bridge`; shared-library
      namespaces keep truthful neutral names (`eval_commons` STAYS — owner ruling on the
      principled rule, no exception); single-file vendored guards exempt; persona
      "Irene" stays in all user-visible strings; wire/deployed identifiers never ride
      layout tasks. Commons-side: the spec (landed 2026-07-13) + template line +
      CONTRIBUTING/process-README pointers. Delegation record:
      - **Delegation → locveil-voice**: **BUILD-36**, ONE tree churn (~4.5–5 days,
        keeper checklist of 2026-07-13 is the reconciliation baseline): (1) layout —
        `irene/` → `backend/src/`, pyproject/lock/type-configs into `backend/`;
        configs/assets/ops/docker/docs/contracts/eval stay at root; 3 known
        `__file__`-relative fixes; (2) tests — 142 files → `backend/tests/`;
        (3) uniform rename `irene`→`locveil_voice` + dist → `locveil-voice` (+11
        self-ref extras), 13 entry-point groups, 8 config-master/profile lines,
        config-ui type regen; (4) `configs/` → `config/` (q2 ruling) incl. the
        `config-master-file` invariant text; (5) eval venv wiring → `backend/.venv`;
        (6) env family `IRENE_*`→`LOCVEIL_VOICE_*` + scripts `locveil-voice-*` with
        `irene-*` aliases for one release; scripted WB7 cutover (compose keys + the ONE
        hand-edited secrets `.env` key + update.sh) + smoke; (7) all 6 images rebuilt +
        boot-verified (BUILD-11 bar); docs sweep via the manifest suspect-set. Execute
        in the current quiet-ledger window (closes at ARCH-49/next release push).
        Voice ID: **BUILD-36** (filed 2026-07-13; keeper checklist reconciled to repo
        at intake — counts verified ✓).
      - **Delegation → locveil-bridge**: (1) **CORE-10** (~1 day) — rename
        `wb_mqtt_bridge`→`locveil_bridge` (imports+strings+entry points+import-linter
        contract refs+device-state-mapping+CI ref+docs), scripts `wb-catalog`→
        `locveil-catalog`, `wb-openapi`→`locveil-openapi`, retire `wb-api`; the
        deliberate **catalog-v1.7** minor cut (STAMP bump + UI type regen per
        config-ui-stays-functional); delete the 4 inert test `sys.path` shims;
        (2) **CORE-11** (~½ day, separate commits) — `backend/config/` → root
        `config/` (loader/CLI defaults, ~15 test paths, update.sh rsync line, CI
        filter, `config-master-tree` invariant text, one DRV-36 design-doc path line;
        NO contract cut) + Dockerfiles → `docker/Dockerfile.{backend,ui}` root
        context (4 CI lines, dockerignore merge; runtime assets stay with ui/);
        (3) **OPS-26** (owner-gated) — `meta/driver` cutover `wb_mqtt_bridge`→
        `locveil-bridge`, riding the same deploy cycle, separately revertible
        (retained qos=1 republish-in-place: no broker migration; visible effect = one
        string in the WB UI). One voice re-pin after CORE-10 covers catalog v1.6+v1.7.
        Bridge ID: **CORE-10 DONE 2026-07-13** (rename `wb_mqtt_bridge`→`locveil_bridge`
        + scripts `locveil-openapi`/`locveil-catalog`, `wb-api` retired + `catalog-v1.7`
        minor cut, golden byte-identical — voice re-pin covers v1.6+v1.7; wire `meta/driver`
        deliberately preserved for OPS-26) + **CORE-11 DONE 2026-07-13** (config
        `backend/config/`→root `config/`, singular per §1 + Dockerfiles→`docker/` with
        root context, both images build-verified locally; two commits, NO contract cut,
        golden byte-identical; reconciliation surfaced the LG cert-path/CWD coupling → the
        offline catalog build + regen now run from the repo root = the deployment root, as
        the container does from `/app`) + **OPS-26 DONE 2026-07-13** (owner-gate lifted;
        `meta/driver` value `wb_mqtt_bridge`→`locveil-bridge`, the two default literals flipped,
        republish-in-place — no broker migration, no persisted-state coupling; live topic flips
        on the next WB7 image deploy, separately revertible). **The entire PROD-21 bridge share
        is consumed** (CORE-10 + CORE-11 + OPS-26 all DONE). All in `locveil-bridge`
        `docs/action_plan{,_DONE}.md`; reconciled at intake (bridge already src-layout, so no
        layout move owed). Bridge owes voice ONE re-pin covering catalog v1.6+v1.7.
- [ ] **PROD-22 — contract-guard: verify the STAMP-named git tag exists** (shared-tooling gap
      surfaced by PROD-21/CORE-10, filed by the bridge 2026-07-13). The catalog-v1.7 cut set
      `STAMP.json`'s `"tag": "catalog-v1.7"` and passed scope-guard + contract-guard + the golden
      drift test **green**, but the `catalog-v1.7` git tag itself was never created — a false green:
      `contract_guard.py` checks STAMP coherence + pinned-copy hashes, **not** that the tag it names
      actually exists. A consumer cannot re-pin against a tag that doesn't exist (voice pins AGAINST
      the family tag). The bridge owner caught it manually and created `catalog-v1.7` @ `73f8179`.
      **Scope (commons, `packages/contract-guard/contract_guard.py`):** for each contract carrying a
      STAMP, assert the tag named in `STAMP.tag` resolves as a git tag object — catches the "forgot
      to create it entirely" failure mode; remote-push verification is explicitly OUT of scope (a
      local tag object is the bar, since a guard can't see the remote). Ship as **`contract-guard-v2`**.
      No council needed — mechanical enforcement, no new convention. **Delegations:** bridge — an OPS
      task to re-vendor `contract-guard-v2` (sha-verify against the tag) + re-run the hook/CI (bridge
      write-back: pending); voice — same on its next re-pin cycle (voice ID: pending). Commons-side
      deliverable: EXECUTED 2026-07-13 — `contract_guard.py` 1.1.0 (`TAG-MISSING` fail
      on owned STAMPs, `TAG-UNCHECKED` warning outside git; functional-tested both ways;
      commons run green — its own tags resolve), tagged **`contract-guard-v2`**.
