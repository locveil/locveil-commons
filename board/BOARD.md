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
      **Sprint-01 (2026-07-14) activated the design phase** — stages ①–④ selected
      (`board/sprints/sprint-01.md`); the deploy-split design + Workbench shell council
      split out as **PROD-24** (its wireframe/plug-in contract shapes ④'s component
      boundaries); the HK-7 sequencing note is resolved by sprint-01 decision 1: bridge
      OPS-13 runs first, ui-kit targets eslint-9/vite-6 — the migration runs once.
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
- [>] **PROD-24 — the Locveil Workbench: workstation UI shell + deploy-split** (filed at
      sprint-01 planning, 2026-07-14; **shell council DECIDED 2026-07-14** — two rounds,
      all three keepers, owner wireframe sketch as seed; the dossier was a view, this
      entry is the record). Naming **operations / workbench** ratified.
      **Council decisions:**
      (1) **Wireframe ratified as sketched**: shell chrome = logo + one tab per plugin +
      problem-report button (Material `BugReport` glyph in bridge-ui's quiet-grey/amber
      treatment; the SVG ships in ui-kit, no MUI dependency); left sidebar = the active
      plugin's pages; main area = the selected page. **Repo = plugin** (one tab per
      product). Shell = React 18 SPA living in commons **`packages/workbench`**
      (tags `workbench-vX`).
      (2) **Classification**: voice config-ui → workbench (voice's operations column is
      empty by design; **6 pages** — the Overview page + own top bar retire into shell
      chrome/Monitoring; a per-plugin **status slot** in the contract preserves
      connection/health visibility) · bridge `ui` + appliance/room pages → operations
      (the unbuilt "admin route / auth shell" scope is deleted from operations — the
      Workbench answers it once) · bridge device-setup/topology-setup/voice-setup →
      workbench under one Bridge tab (IR learning = sidebar entry; voice-setup stays
      under Bridge — it is a bridge-backend surface) · satellite on-device softAP/admin
      UI → neither class (D-16) · satellite provisioning/config page → workbench, all
      privileged writes via a **controller-side privileged broker** (owner overruled the
      CLI-only reading of D-17: the CLI's functionality MUST be replicated in the UI;
      CLI and page become peer clients of ONE privileged code path — the CA-key
      privilege boundary survives, the SSH-only gate does not; D-17 second amendment
      lands via the expanded DES-5) · PROD-9 landing page → a third class (public
      site), out of shell v1.
      (3) **Write model — DEV-PHASE convention** (owner ruling: fine while the owner is
      the only user/customer; the FINAL design/convention is **deferred to a further
      productization step**): config targets classify by ownership — *repo-owned*
      (bridge config tree, voice WB7 TOML): workbench pages write **staged proposals**
      via controller APIs (bridge: `data/staged-config/` in the writable data mount),
      promotion to the canonical repo is an explicit human commit, live mounts stay
      read-only, `update.sh` one-way sync unchanged · *device-owned* (desktop/ESP32
      satellite config): direct write via a device-local endpoint — the desktop-satellite
      config page is **voice-owned** under the Voice tab (it edits the same CoreConfig
      `[satellite]`/`[vad]`/`[voice_trigger]` sections; same dev-phase deferral) ·
      *privileged* (cert operations): the satellite broker with narrow verbs
      (`list/status/approve/reject-pending` now; `revoke-issued/renew` when DES-5
      defines them).
      (4) **Plug-in contract v1 headlines**: `{id, title, pages (runtime-registrable —
      UI-16-proof), i18n bundles RU/EN + shell-provided locale, per-page backend targets
      (heterogeneous device-class backends allowed), per-plugin status slot, optional
      report hook, dormant verbs with named gates, optional plugin gate}`; plugin source
      lives in its owning repo (openapi generators stay repo-side; the shell consumes
      built artifacts — exact mechanism in the design doc); dormant plugins are
      registry-declared, not rendered.
      (5) **Reporter pipeline deferred** out of v1 (the chrome button stays; a
      shell-level fallback is designed later under PROD-19). **Auth: PROD-4 owns it** —
      v1 documents the trusted-LAN assumption and reserves an auth-guard slot; bridge's
      binding condition on record: **no write API ships before PROD-4's auth decision
      lands**. Toolchain clarification of sprint-01 decision 1: eslint-9 flat config is
      the shared target; vite majors are per-consumer; ui-kit publishes version-agnostic
      ESM.
      (6) **Desktop satellite = the provisioning page's test target** (voice's
      `locveil-voice-satellite` runs the same CSR flow against the same Plane-B
      endpoints; re-provisionable by clearing its credentials dir; the read-only panel
      needs the broker/list surface first; re-provisioning leaves the old cert trusted
      for its full term — the DES-5 gap, rendered honestly, never papered over).
      **Commons deliverable LANDED:** the deploy-split design doc —
      `docs/design/workbench.md` (2026-07-14) — codifies (2)+(3)+(4) + the reserved-verbs
      table + change control; it also fixes the dev-phase plugin consumption mechanism
      (`file:` deps on sibling repos' BUILT plugin packages — never TS sources; final
      distribution deferred to productization). ui-kit component boundaries (PROD-10 ④)
      consume it. Entry stays open on the three write-backs.
      **Delegations (board-as-outbox):**
      satellite — **DES-5 expansion**: the cert-lifecycle design absorbs the broker (one
      privileged path, two clients), the full verb vocabulary, the workstation
      operator-credential design (client cert from the home CA vs a separate secret),
      and an **OPS earmark** for the ansible-deploy rework (owner: not this sprint).
      Satellite ID: (write back).
      voice — (a) satellite-local config endpoint design (`design-then-implement`,
      dev-phase shape; new attack surface → PROD-4 auth posture applies); (b) the
      declared sprint-02 config-ui adoption task grows the 6-page cut (Overview + Header
      retire) + status-slot wiring. Voice IDs: (write back).
      bridge — UI-17 intake (sprint-01 row) grows: the staged-write API shape + the
      planned-docs DOC follow-up (device-setup/topology-setup: "Apply stages via the
      controller API; promotion is a commit"; topology-setup's live-vs-file open
      question is answered = staging; the admin-shell rows across all four planned
      pages). Bridge ID: (write back).
