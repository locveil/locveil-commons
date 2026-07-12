# Locveil board — DONE ledger

Completed `PROD-N` / `HK-N` entries, MOVED here from `BOARD.md` on close (same change as
the journal entry — `process/ledger-discipline.md`). Frozen history: entries are never
re-edited; delegated IDs listed inside them are pointers, never status assertions.

## PROD — cross-repo initiatives

- [x] **PROD-1 — Name lock + registrations** (D-1). Sweep run 2026-07-08 under "Domovoy"
      (`docs/design/productization_roadmap.md` §2); owner superseded with the invented word
      **Locveil**, locked 2026-07-11: `locveil.com` (Porkbun) + `locveil.ru` (REG.RU)
      registered, GitHub org `locveil` claimed, `.io` dropped (`.com` is canonical).
      Discipline: never publish a bare `locveil` package — always `locveil-*`.
      **Residual (owner):** `locveil.eu` pending REG.RU ID verification →
      `docs/design/locveil_domain_registration.md` tracks it.
- [x] **PROD-2 — Rename + restructure + consumer re-points** (D-2/D-3; executes voice
      BUILD-21). CLOSED 2026-07-11: GitHub repos renamed under org `locveil` + local dirs +
      remotes (owner); D-2 restructure landed (eval framework → `eval/` with history,
      distribution renamed `locveil-eval`, import package stays `eval_commons`; `board/`
      `process/` `packages/` `site/` created; name sweep of repo-owned files — pinned
      contract artifacts untouched, they pick up new names at the next re-pin). Both
      delegations carry local IDs: voice **BUILD-21** (executed `locveil-voice@d0c0755`),
      bridge **OPS-20** (executed `locveil-bridge@bd256d8` — the first completed
      board-as-outbox round-trip). Residue lives in the product ledgers: voice BUILD-29 +
      bridge OPS-21 (the coordinated deployment-identity rename — image basenames,
      container/unit names, controller paths; both owner-gated), and one operational note:
      **each repo needs one CI publish before its next controller `update.sh`** (pull refs
      now say `ghcr.io/locveil/*`). Delegation record:
      - **Delegation → locveil-voice** (BUILD-21 tail, existing voice ID): (1) re-point
        `eval/` refs — `file://` paths now `../../locveil-commons/eval/...`, `pip install -e
        ../locveil-commons/eval`, eval/README + CLAUDE.md Testing section (these BROKE when
        the sibling dirs were renamed — do first); (2) sibling-path/name refs in
        CLAUDE.md/README/docs (`wb-mqtt-*`/`eval-commons` → `locveil-*`; ledger/journal/
        release-doc history is HISTORY — never rewrite); (3) rename the `domovoy` uid-1000
        container user → `locveil` in `docker/Dockerfile.{x86_64,aarch64,armv7}` +
        `ops/update.sh` comments (baked into images → rebuild+redeploy; uid 1000 unchanged,
        no chown fallout expected); (4) GHCR cutover `ghcr.io/droman42/*` →
        `ghcr.io/locveil/*` (CI publish + `ops/update.sh`; old images stay pullable);
        (5) replace `docs/design/productization.md` with a pointer to the migrated copy here
        (migrated @ voice 92d1abd). Voice ID: **BUILD-21**.
      - **Delegation → locveil-bridge** (first board-as-outbox delegation): same set for the
        bridge — (1) re-point its `eval/` references to `../locveil-commons/eval` (broken by
        the dir rename); (2) sibling-name sweep in docs (history untouched); (3) `domovoy`
        container user → `locveil` in `backend/Dockerfile` + `ui/Dockerfile` (Alpine
        `adduser`) + comment refs in `ops/update.sh` and `ui/nginx.conf.template` (rebuild +
        redeploy); (4) GHCR cutover to `ghcr.io/locveil/*`; (5) WARNING from the voice
        execution: the dir rename bricks `backend/.venv` (absolute console-script shebangs) —
        rebuild it (`uv sync`) before trusting any gate; (6) keep live deployment identifiers
        (container names, systemd units, controller paths, image basenames) — the voice side
        filed that as its own task (BUILD-29); mirror it. Verify per
        `task-start-reconciliation`, file a local ID, write it back here. Bridge ID:
        **OPS-20** (written back 2026-07-11).
- [x] **PROD-3 — Board bootstrap** (D-4/D-5). This file + `JOURNAL.md`, commons CLAUDE.md
      with the session discipline (cross-repo sessions run from here, sibling context
      loading, placement rule, outbox mechanics, per-package tag scheme), decision record
      migrated from voice (`docs/design/productization.md`), seed backlog transplanted from
      `productization_roadmap.md` §3 → this ledger. Done 2026-07-11.
- [x] **PROD-5 — Shared CLAUDE.md invariant blocks + drift guard** (D-12; decided by
      council HK-2, 2026-07-11 — positions/synthesis in `JOURNAL.md`; normative:
      `process/claude-md.md`). Decision: commons `process/` is the single normative source
      for shared process rules; each repo carries **pinned digest blocks** between
      `locveil:begin/end` markers (digests + pointers, dialect-free, byte-identical;
      repo-local LAW stays outside and repo-owned), versioned with the existing `scope-vX`
      tags (single pin) and enforced by a `claudemd` hash rule in scope-guard from
      `scope-v3` — fully local, no sibling checkout in hooks/CI. Hard criterion: adoption
      must NOT grow a product CLAUDE.md (the duplicated ledger mechanics come out).
      `config-master-canonical` renames apart BOTH sides (voice `config-master-file`,
      bridge `config-master-tree`). Satellite seeding: commons authors
      `process/new-repo-template/`; voice BUILD-22 instantiates it (guard + hooks live from
      day one). v1 blocks: `shared-invariants` + `cross-repo-board` (the board digest fixes
      the "sessions search for board process" gap; includes the repos-are-siblings line and
      the council pointer). CI job-naming convention added to `ledger-discipline.md` §4.
      Commons-side executed 2026-07-11 (blocks, template, spec, scope-v3, own adoption).
      Closed 2026-07-11: both consumptions confirmed same day (journal entries).
      Delegation record:
      - **Delegation → locveil-voice** (pre-assigned voice ID BUILD-23 — narrow at intake
        per `task-start-reconciliation`; the "separate drift-guard script" wording is dead,
        scope-guard won): (1) insert both blocks from `process/claude-blocks/` between
        markers; delete the long-form ledger/rotation prose they replace (net line count
        must not grow); (2) re-pin scope-guard at `scope-v3` + add the `[claude]` section
        to `.scope-guard.toml` (`--hash-blocks` prints the hashes); (3) rewrite the stale
        pre-board bullet in `cross-repo-source-of-truth` (board-as-outbox vs direct
        operational filings); (4) rename `config-master-canonical` → `config-master-file`
        + legend row (frozen archives untouched); (5) BUILD-22 gains the dependency:
        instantiate `process/new-repo-template/`, never freehand. Voice ID: BUILD-23
        (consumed 2026-07-11).
      - **Delegation → locveil-bridge** (pre-assigned bridge ID OPS-16 — REDEFINE at
        intake: its ledger text references `check_scope.py`, deleted in OPS-22): (1) same
        block insertion + long-form dedup (~55 duplicated triad lines come out; net line
        count must not grow); (2) re-pin at `scope-v3` + `[claude]` config; (3) rewrite the
        false sovereignty preamble (CLAUDE.md:6-9) and the retired uncommitted-intake
        clause; (4) rename `config-master-canonical` → `config-master-tree` (4 references;
        frozen archive untouched). Bridge ID: OPS-16 (consumed 2026-07-11, redefined at
        intake with owner approval).
- [x] **PROD-6 — Problem-report spec + report-protocol machine core** (D-12; RESCOPED by
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
- [x] **PROD-12 — The council: structured cross-repo discussions (skill + keepers + dossier)**
      (filed + built 2026-07-11, owner-designed over three analysis rounds). A `/council`
      skill in this repo runs a housekeeping/design topic as a moderated discussion: commons
      Claude coordinates, per-repo **keeper subagents** (`.claude/agents/{voice,bridge}-keeper.md`,
      read-only lenses loaded with their repo's CLAUDE.md/ledger/journal) argue their repo's
      interests, the owner decides. The discussion renders on a **dossier artifact** (private
      web page, one per topic, updated in place each round) carrying an on-page form whose
      **Copy button serializes only the fields the owner changed** into a `council-reply`
      paste-block — the terminal paste is the sole return channel (artifact CSP blocks
      network by design). Ground rules, committed as `process/council.md`: decisions are
      treated EXACTLY as if reached in the terminal — accepted outcomes land as PROD
      entries/`process/` specs with board-as-outbox delegations, `board/JOURNAL.md`
      summarizes, the dossier is an ephemeral view and never a record; one channel per round;
      seeding = `PROD-N` (this board only, initially) | free text | bare (topic typed into
      the dossier form); keepers reconcile a seeded entry against reality before arguing;
      keepers never write files. Deliverables: `.claude/skills/council/SKILL.md`,
      `.claude/skills/council/dossier-template.html`, the two keeper agents,
      `process/council.md` (+ satellite-keeper when that repo exists). First live topic
      shook it down: HK-1.
- [x] **PROD-13 — Ledger & journal discipline harmonization + scope-guard** (HK-1, the
      first council topic, decided 2026-07-11 — positions/synthesis in `JOURNAL.md`).
      Decision: every repo adopts the ledger triad (active+DONE split, rotating journal,
      record-at-completion), the DONE ledger also rotates with a hard ID-resolution
      guarantee (archived declarations stay in the checker's known-ID set), and the two
      `check_scope.py` scripts are superseded by ONE commons-owned tool — **the UNION of
      both rule sets** (neither repo's was a superset), config-driven per repo, at
      `packages/scope-guard/` (distribution `locveil-scope-guard`, tag `scope-vX`,
      stdlib-only single file each consumer VENDORS at a pinned tag). Enforcement:
      pre-commit hook (`core.hooksPath`) + path-gated `ledger-guard` CI job; rotation only
      via explicit `--rotate` (its own commit; hooks/CI never mutate; CI warns at
      high-water, fails at hard ceiling). v1 extra rules: journal+DONE watermarks,
      archive-pointer integrity, completion-journal cross-check, required-task-tags
      (config), board rule pack. File renames: dropped — naming is per-repo config
      (owner q6). Normative spec: `process/ledger-discipline.md`. Commons-side execution
      immediate (owner q1 amendment). Delegation record:
      - **Delegation → locveil-voice**: consume scope-guard at the pinned tag `scope-v2`
        (was `scope-v1`; re-tagged after the bridge consumption caught a `--rotate journal`
        bug — v1 wrote archives character-per-line. Everything below holds at v2.) —
        (1) vendor `packages/scope-guard/scope_guard.py` + author `.scope-guard.toml`
        (start from `packages/scope-guard/examples/voice.scope-guard.toml`, verified
        against the voice tree 2026-07-11 — parity with the local checker PLUS two TRUE
        pre-existing findings the cutover must fix: the DONE I18N section is unsorted
        (1,2,8,3,7,4,5,6 — invisible to the old checker, whose `[A-Z]+` ordering regex
        never matches `I18N`), and RELEASE_PLAN_DONE.md is over the 4000-line hard
        ceiling); (2) retire `scripts/check_scope.py` and
        re-point the `ledger-guard` job + `ledger` paths-filter in
        `.github/workflows/ci.yml`; (3) install the committed-hooks mechanism (`hooks/`
        + `core.hooksPath`) running `--check` pre-commit; (4) update invariant text
        (`single-task-ledger`, `one-active-journal` in CLAUDE.md; RELEASE_PLAN.md gate
        wording) in the SAME change as the cutover; (5) adopt DONE-ledger rotation
        (RELEASE_PLAN_DONE.md is at ~4.3k lines) and run the overdue journal rotation
        (1510 > ~1500 high-water) via `--rotate`; (6) keep the required-task-tags rule ON
        (`[release]`/`[deferred]`). Cutover proof: vendored tool green before deleting the
        local script. Verify per `task-start-reconciliation`, file a local ID, write it
        back here. Voice ID: BUILD-30 (consumed 2026-07-11 at scope-v2; both advertised
        pre-existing findings confirmed real and fixed; voice's rotation attempt hit the
        same v1 `--rotate` bug concurrently with the bridge — corrupted first-pass
        commits rebuilt, nothing had been pushed).
      - **Delegation → locveil-bridge**: same shape at tag `scope-v2` — (1) vendor the
        script + author `.scope-guard.toml` (start from
        `packages/scope-guard/examples/bridge.scope-guard.toml`, verified green against
        the bridge tree 2026-07-11; aliases + tombstones stay ON); (2) retire
        `scripts/check_scope.py`, re-point `ledger-guard` + paths-filter in
        `.github/workflows/build-arm.yml`; (3) committed-hooks mechanism, `--check`
        pre-commit (work-on-main: the hook is the only pre-CI gate); (4) update
        `single-task-ledger`/`one-active-journal` invariant text in the same change;
        (5) define the DONE-rotation rule (new for bridge) per
        `process/ledger-discipline.md` §2 and run the overdue journal rotation
        (1625 > ~1500) via `--rotate`. Cutover proof as above. Verify per
        `task-start-reconciliation`, file a local ID, write it back here. Bridge ID:
        OPS-22 (consumed 2026-07-11; the rotation step caught the v1 `--rotate` bug →
        fixed here as scope-v2).
- [x] **PROD-14 — locveil-reports: org move + credential cutover + re-points** (council
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
        **Bounce RESOLVED 2026-07-11** (`locveil-voice@49c868a`, verified by commons):
        §5/§7 bodies are pointers to the spec + pin, voice-side content intact, zero
        spec-grade vocabulary residue. Voice delegation fully accepted. **Lift-out landed same-day**
        (voice `49c868a`): §5/§7 bodies → pointers + voice-side remainder (D-11 rationale,
        outcome-3a note); stale §7.3/§7.4 cross-refs re-pointed incl. `report_bundle.py`.
      - **Delegation → locveil-bridge**: (1) VWB-29-shaped re-point — slug sweep
        (SKILL.md ×5, invariant command, INSTALL.md, design-doc operative refs), make
        `reports.repo` explicit in `system.json` and DROP the slug schema default (HK-3
        q4 round 1) → openapi regen + `contracts/` pin bump + UI regen + voice re-pin
        chain; spool-drain verification post-cutover; (2) `lens-bridge.md` co-ownership
        re-review (VWB-30 as pre-named); (3) protocol consumption: pin the core, one
        conformance test over `service.py:210/216`, retire the hardcodes into
        pin-validated form. Bridge ID: **VWB-35** (re-point) / **VWB-36** (lens re-review —
        the pre-named VWB-30 was stale at intake: that serial was consumed 2026-07-09 by the
        bridge's REL-5 remediation; re-serialed per assigned-once) / **VWB-37** (protocol
        consumption). Written back at intake 2026-07-11.
        **Verification (commons, 2026-07-11) — ACCEPTED in full:** sweep clean (two
        design-doc mentions are deliberate history annotations), schema default dropped +
        fail-fast validator, `system.json` explicit AND enabled, regen chain landed
        (suite 704; catalog golden correctly unchanged), pin + conformance 5/5, lens
        re-review genuine (`locveil-reports@6a5dc62`), spool trivially drained (verified:
        no spool dir was ever created). Flag, not a bounce: bridge `openapi.json` changed
        → the voice-side contracts pin is one rev stale; rides the normal re-pin cadence
        (PROD-7 / voice BUILD-24).
      - **Reports-repo consumption** (no ledger there; executed commons-side post-transfer):
        `bootstrap.sh` generates labels from the pinned core + trivial CI compare; README
        pointer flips from voice's design doc to `process/problem-reports.md`.

- [x] **PROD-15 — locveil-satellite bootstrap** (executes D-6/D-7 with dated amendments;
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
        (registry/config-ui staleness flag rides it or files separately). Voice ID:
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
        stay UNFILED until first-light (HW-GATED, satellite-triggered). Bridge ID:
        **DRV-34** (items 1a+5, folded — the supersession annotations) + **DRV-35**
        (item 1b — ESP32/ delete + DRV-7 retirement, blocked on satellite import
        confirmation) + **VWB-38** (item 2) + **DRV-36** (item 3) + **VWB-39** (item 4)
        (pulled + verified at intake 2026-07-12; per-deck cutover tasks left unfiled
        per this entry).
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
      **CLOSED 2026-07-12** — close condition met same-day: the commons-side deliverables
      shipped with the decision; both product delegations carry written-back local IDs
      (voice **BUILD-22**/**ARCH-47**; bridge **DRV-34/35/36** + **VWB-38/39**) and the
      satellite born backlog is filed under local IDs in the new repo's ledger. Status of
      every delegated task lives in the per-repo ledgers, per convention. Follow-through in
      the same close: the `cross-repo-board` shared block now names the fourth sibling
      (`../locveil-satellite`) — source edited in `process/claude-blocks/`, tagged
      **scope-v4**, hash re-pinned in all four CLAUDE.mds the same day.

## HK — council topics

- [x] **HK-1 — Ledger & journal discipline harmonization** (the first live council topic;
      bare seed, decided 2026-07-11 in one keeper round + one owner round). Decision and
      execution filed as **PROD-13** (delegations there); normative convention:
      `process/ledger-discipline.md`. The keeper round corrected the brief — union of rule
      sets, not "bridge's because strictest"; both product journals were over their own
      high-water at decision time. Also established THIS convention: `HK-N` is a tracked
      board prefix; council topics are born-decided and file directly into this DONE ledger.
- [x] **HK-2 — Cross-repo CLAUDE.md harmonization** (second council topic; bare seed,
      decided 2026-07-11 in one keeper round + one owner round). Decision and execution
      filed under the pre-existing **PROD-5** (the keepers' unanimous finding: the topic IS
      PROD-5 — execute it, don't re-design it); normative convention:
      `process/claude-md.md`. Keeper round found the root cause of the owner's "sessions
      search for board process" complaint: neither product CLAUDE.md mentioned the board at
      all, and both still taught the retired pre-board uncommitted-intake mechanism.
      Owner amendments: none to the proposal; the session-start **inbox story** was
      explicitly deferred as "much bigger — the next HK exercise".
- [x] **HK-3 — The inbox story: locveil-reports move + report-protocol contract** (third
      council topic; bare seed, decided 2026-07-11 over TWO owner rounds — the first
      multi-round council). Outcomes filed as **PROD-14** (the move + credential cutover +
      re-points; phase 0 executed in-session) and **PROD-6 rescoped** (commons-owned
      two-part truth: `report-protocol-vN` machine core + prose spec — the owner's
      "smells like a contract" instinct, confirmed by both keepers, who converged
      unanimously on commons ownership; voice ceded the ARCH-30-era de-facto ownership).
      Round-2 extension check ("feature requests through the same channel") passed: ticket
      TYPE is a first-class core dimension; a future type is a vN bump, not a redesign.
      Council craft note: the round-1 "conflict" between keepers dissolved on inspection
      (voice opposed prose parameterization, not the block; bridge demoted its own block
      to optional once the machine core existed).
- [x] **HK-4 — locveil-satellite bootstrap** (fourth council topic; bare seed, decided
      2026-07-12 over FOUR owner rounds — the longest council yet). Decision and execution
      filed as **PROD-15** (delegations there). Round arc: round 1 reconciled the brief
      against both repos — stale claim caught (the voice `ESP32/` review was already DONE
      and verdicted DELETE 2026-07-08), half-story caught (bridge's HVAC modules are
      shipped ESP8266 drivers, not movable ESP32 estate — the movable set is exactly
      voice ARCH-23 + bridge DRV-7), and the owner's duplication claim verified with a
      twist (the fresh general bridge doc is newer but WEAKER than the bench-confirmed
      build docs — merge claim-by-claim, never newest-wins). Round 2: wake pack =
      flash-time pin of voice's unmodified artifact; rooms = provisioning-time NVS (voice
      pushback accepted with the NVS-default-seed compromise); the two-layer "convention
      down, descriptors up" contract. Round 3 absorbed three owner pushbacks: NEW
      **EspManagedDevice** driver class (WB-passthrough ruled out by the owner), fully
      design-time contract (latency conceded static, no runtime negotiation, one retained
      firmware-version topic kept as tripwire), per-device firmware apps (FR-1
      single-image retired — the GPIO14 double-booking proved the owner's bench point).
      Round 4 (coordinator-only, no keeper cost): toolchain — pcbparts / Serena-SKiDL /
      Espressif MCPs day one; skidl-skills and the PlatformIO commitment deliberately NOT
      installed at bootstrap — both mandatory satellite design tasks (DES-2/DES-3).
