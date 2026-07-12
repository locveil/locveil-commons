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
- [ ] **PROD-15 — locveil-satellite bootstrap** (executes D-6/D-7 with dated amendments;
      decided by council **HK-4**, 2026-07-12, four rounds — arc in `BOARD_DONE.md` HK-4,
      positions/synthesis in `JOURNAL.md`). Decision: repo NOW from
      `process/new-repo-template/`; one ledger triad, prefixes `DES/PCB/FW/OPS` +
      required per-device tags, HW-GATED marker; normative phase-gate process DES→PCB→FW
      with per-phase nested CLAUDE.md + MCP sets. Charter: **ESP32-only**; escalates to
      embedded-generally only if the HVAC ESP8266 firmware rewrite ever happens (recorded
      trigger; HVAC drivers/configs stay bridge-side ALWAYS). Firmware: shared ESP-IDF
      components (`locveil_wifi/_wb_mqtt/_ota/_identity/_ir_baseband`) + **per-device
      apps** (compile-time identity + NVS identity assertion; FR-1 single-image retired —
      the GPIO14 double-booking); `boards/<device>/` PCB projects; `provisioning/` (nginx
      Plane B moves — D-6 amended); `contracts/` pins (voice WS protocol @vN, voice
      wake-pack @vN, bridge device-integration-convention @vN). Wake pack: flash-time pin
      of voice's UNMODIFIED artifact (hash-verifiable; version reported in `register`;
      OTA model updates optional/later). Rooms: provisioning-time NVS, registry
      authoritative (optional build-time NVS default seed). Integration contract:
      "convention down, descriptors up" — bridge owns the versioned
      device-integration-convention (wb-mqtt-v1 + REST URL conventions day one +
      capability vocabulary; ha-mqtt-v1 later as a second profile), satellite owns
      conforming per-device descriptors (required timing/availability fields,
      `confirm_latency_ms` STATIC), mirrored pins + CI conformance, fully DESIGN-TIME
      (vocabulary reconciliation at the DES gate; no runtime negotiation; one retained
      firmware-version topic as the stale-pin tripwire). New bridge driver class:
      **EspManagedDevice** (descriptor-native; one-time openapi bump; golden catalog
      waits for the first deck config). Python desktop satellite STAYS in voice; frozen
      history never migrates; plain moves + journal pointers. Toolchain day one: pcbparts
      MCP + Serena-over-cloned-SKiDL (PCB), Espressif docs + component-registry MCPs
      (FW); **no PlatformIO installs and no skidl-skills install at bootstrap** — both
      are mandatory satellite design tasks (owner round-4 amendments). Commons-side
      deliverables (done 2026-07-12): D-6 dated amendment in
      `docs/design/productization.md`, satellite-keeper agent authored
      (`.claude/agents/satellite-keeper.md`, activates with the repo), this entry.
      Delegation record:
      - **Delegation → locveil-voice** (BUILD-22 — REDEFINE at intake per this decision):
        (1) create `locveil-satellite` from `process/new-repo-template/` (never
        freehand); seed the HK-4 skeleton + the born backlog below into its ledger;
        (2) migrate the design corpus with the recorded reconciliation AND demote
        `esp32_satellite.md` §4 wire tables to a pointer at
        `locveil-voice/docs/guides/websocket-api.md` + the version pin; (3) DELETE the
        top-level `ESP32/` tree in the same change (2026-07-08 verdict reconfirmed);
        (4) the nginx package: move the Plane-B tree, pin the TLS-e2e template copy
        (`test_arch36_tls_e2e.py` tether), update the `locveil-voice/ops/INSTALL.md`
        pointer, export-close ARCH-44 with pointer, record the WB7 ops handover;
        (5) export-close ARCH-23 with pointer; (6) NEW ARCH task: WS-protocol version
        stamp + wake-pack pin surface + `register` version-reporting fields
        (registry/config-ui staleness flag rides it or files separately). Voice IDs:
        **BUILD-22** (redefined at intake 2026-07-12, items 1–5) + **ARCH-47** (item 6;
        staleness-flag decision deferred to its task start).
      - **Delegation → locveil-bridge**: (1) export task — annotate the superseded
        ESP32ManagedDevice text (`locveil-bridge/docs/action_plan.md` §5.1 area), fix the
        back-pointers, hand the `ESP32/` tree to the satellite import, DELETE it + retire
        DRV-7 with a journal pointer once satellite confirms the import; (2) design task:
        the device-integration-convention (guide + `device-descriptor.schema.json` +
        version stamp; wb-mqtt-v1 as promotion of the REQUIREMENTS FR-text, REST
        conventions from day one, external-vs-Locveil ownership marked); (3) design task:
        **EspManagedDevice** driver (descriptor-native, driven adapter, one-time openapi
        bump; design-then-implement); (4) descriptor-pin conformance test (the VWB-37
        pattern); (5) amend `locveil-bridge/docs/design/productization_bridge.md` §85-87
        generator note with the two-layer shape (dated, HK-4). Per-deck cutover tasks
        stay UNFILED until first-light (HW-GATED, satellite-triggered). Bridge IDs:
        (write back).
      - **Satellite born backlog** (its first session files these as local IDs; listed as
        seed only, status never asserted here): DES-1 harmonize the bridge ESP32 doc
        corpus claim-by-claim (build docs = leaf truth; REQUIREMENTS truth pass; pin-map
        re-audit — the GPIO14 lesson); DES-2 skidl-skills review/rethink/adoption
        (focused session); DES-3 firmware execution-layer decision — PlatformIO vs
        pioarduino-lineage vs native idf.py, incl. docs-MCP IDF-version alignment,
        background-monitor pattern, and a mandatory pin/strapping audit step (MANDATORY
        before any FW phase starts); DES-4 adopt the descriptor format for the deck
        devices; OPS-1 own the firmware/model publish pipeline into the WB7
        `/srv/esp32/`; OPS-2 wire the day-one toolchain (pcbparts + Espressif docs +
        component-registry MCPs, Serena + gitignored `references/` clones + bootstrap
        script, single root `.mcp.json`).
