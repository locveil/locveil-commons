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
- [x] **PROD-7 — Contract tagging + scripted re-pin** (D-11). CLOSED 2026-07-12 as
      **absorbed and executed by PROD-16** (the HK-5 contract convention generalized this
      entry's whole scope): bridge tagging landed as family-named tags per
      `process/contracts.md` §3 — first cut `catalog-v1.5` (VWB-29, rescoped at PROD-16
      intake; the original `contract-vN` naming was superseded by family tags); voice's
      scripted re-pin + staleness gate landed as BUILD-24 (`scripts/repin.py`,
      `make repin CONTRACT=… [TAG=…]`, `make repin-check` release-time gate — first
      scripted re-pin executed same day, upgrading the commons catalog pin to the strict
      PIN.json shape and clearing the recorded openapi staleness). Both pre-named IDs
      (VWB-29, BUILD-24) delivered under their PROD-16 rescopes; nothing of this entry's
      scope remains undelivered.
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

- [x] **PROD-16 — The contract convention + the coordinated cut** (decided by council
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
        pre-VWB-39; (4) vendor contract-guard when tagged. Bridge write-back — lead ID: **VWB-29** (rescoped in place) + VWB-40,
        VWB-41, OPS-23 (filed 2026-07-12, bridge
        `17734d8`; status lives in the bridge ledger).
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
        when tagged. Voice write-back — lead ID: **ARCH-47** (ungated + rescoped in place) + BUILD-24
        (rescoped), BUILD-32 (pins-shape restructure + eval re-point, [release]),
        BUILD-33 (vendor contract-guard v1, [release]), BUILD-26 (annotated) (filed
        2026-07-12, voice `23ee00a`; status lives in the voice ledger).
      - **Delegation → locveil-voice (follow-up, owner decision 2026-07-12 — the
        completeness ruling's first instance):** add the **local COMPLETE catalog pin**,
        closing voice's push-time schema-conformance gap (the corner its own keeper
        flagged in HK-5). (1) `contracts/pins/catalog/` in voice holding the owner's
        FULL tagged artifact set at `catalog-v1.5` — `catalog.golden.json`,
        `openapi.json`, `STAMP.json`, byte-identical (`process/contracts.md` §2: a pin
        is always complete; usage never shapes it) + strict `PIN.json` (`files` hashes,
        conformance pointer). (2) Extend `scripts/repin.py` so
        `make repin CONTRACT=catalog` updates BOTH copies — the commons crossover pin
        and this local pin — in ONE run at the same tag (they must never diverge);
        `make repin-check` covers both. (3) NEW named conformance test in voice's
        NORMAL CI suite (hermetic, push-time): binds voice's emitted-command/client
        shapes to the pinned `CatalogResponse`/action schemas — the crossover suite in
        commons stays the release-cadence deep gate, this is the fast local stub check.
        (4) Registry README: the commons cross-reference note adjusts (local pin now
        exists; the commons copy remains the shared crossover pin). contract-guard
        picks the new pin up with zero changes. Voice ID: **BUILD-34** (filed +
        completed 2026-07-12, voice `a51f709`; status lives in the voice ledger).
      - **Delegation → locveil-satellite**: (1) OPS-3-shaped task — restructure to the
        pins shape, upgrade the WS commit-pin to an artifact-copy pin with PIN.json NOW
        (stamped pin when `ws-protocol-v1` lands), vendor contract-guard, wire the CI
        job, fix the stale `contracts/README.md` status line; (2) DES-4 mirrors
        device-integration per this shape; (3) OPS-1 gains the wake-pack
        hash-at-publish requirement. Satellite write-back — lead ID: **OPS-3 (new, filed + executed same
        session — the pins were born STAMPED: `ws-protocol-v1`/`wake-pack-v1` had already
        tagged by pull time, so the interim unstamped step collapsed; reconciliation also
        stood up the satellite's own `esp32-site` owned surface, tag `esp32-site-v1` —
        voice's pre-tag pin can fill version/tag at its next re-pin), DES-4 (amended in
        place: pins-shape mirror; intake note — the `device-integration-v1` tag carries
        the pre-convention STAMP, core fix post-tag with no bump, `v1.1` request goes
        repo-to-repo at authoring), OPS-1 (amended in place: wake-pack hash-at-publish)**
        (filed 2026-07-12, satellite `fcc6989`; status lives in the satellite ledger).
      **CLOSED 2026-07-12, same day as decided.** All four delegations executed and
      commons-verified (bridge 4/4, voice 5/5 + follow-up BUILD-34 4/4, satellite 3/3 —
      journal entries per verification); every write-back in. The org now runs ONE
      contract convention end to end: uniform layout in all four repos, family tags
      (catalog-v1.5 · device-integration-v1 · report-protocol-v1 · ws-protocol-v1 ·
      wake-pack-v1 · esp32-site-v1 · ui-openapi-v1 · contract-guard-v1 · scope-v4),
      contract-guard vendored everywhere (0 warnings in all three products; commons: 1
      by-design pending-pin warning), conformance tests in every normal CI suite.
      Residuals, recorded: crossover-fixtures strict PIN at the next fixtures task;
      device-integration STAMP core is post-tag (satellite requests v1.1 repo-to-repo at
      descriptor authoring); STAMP `artifacts` list + guard completeness rule =
      contract-guard v1.1 at the next natural bump.

- [x] **PROD-17 — User-facing docs: the org convention + the docs manifest** (decided by
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
      commons' own manifest + CONTRIBUTING.md EXECUTED 2026-07-12 (docs/manifest.json +
      contracts/docs-manifest/ @ docs-manifest-v1 + eval/tests/test_docs_manifest.py,
      registry row; eval suite 46/46). Org README: folded into PROD-9 (no artifact now). Delegation record:
      - **Delegation → locveil-voice**: (1) DOC-shaped task — live stale fixes: the
        `build-docker.md` port-6000 quartet + `websocket-api.md` :6000 example line, one
        pointer sentence in `guides/satellite.md` to the satellite provisioning runbook,
        verify the voice-trigger HF link, fix the `QUICKSTART.md` "ESP32 satellite
        controllers (WB7/WB8)" mislabel; (2) author `docs/manifest.json` +
        `contracts/docs-manifest/` + the coherence test; CONTRIBUTING.md gains the
        contracts-registry + eval links and its manifest node; (3) rule-dialect update
        (CLAUDE.md invariant points at the manifest; `ops/INSTALL.md` enters scope);
        (4) re-pin scope-guard @ `scope-v5` (block + `docs_verdict_since` config).
        Voice write-back — lead ID: **DOC-11 (live stale fixes), DOC-12 (manifest + coherence test +
        CONTRIBUTING), BUILD-35 (dialect + scope-v5 re-pin)** — all `[release]` (filed
        2026-07-12, voice `51ce922`; status lives in the voice ledger).
      - **Delegation → locveil-bridge**: (1) DOC staleness pass — CONTRIBUTING.md
        pre-VWB-29 contract paths, the OpenAPI field-description design-doc refs
        (config-ui-stays-functional: regen openapi + UI types same change), the 5
        REL-4-unverified diagrams; (2) manifest + coherence test + dialect update;
        (3) **ADR dissolution, one task**: 0006 → CONTRIBUTING dependency-policy section
        + OPS-19 re-point; 0001–0005 verify-and-archive with supersession banners;
        (4) re-pin scope-guard @ `scope-v5`. Bridge write-back — lead ID: **DOC-14 (staleness pass),
        DOC-13 (manifest + coherence test + dialect), DOC-15 (ADR dissolution),
        OPS-24 (scope-v5 re-pin)** (filed 2026-07-12, bridge `ee1dca3`; status lives
        in the bridge ledger).
      - **Delegation → locveil-satellite**: (1) OPS-shaped task — author the manifest
        (pending-gate nodes for FW-gated docs naming their gates; derives_from onto
        `docs/devices/`; phase-crossing reviews) + create CONTRIBUTING.md (phase
        process, pin discipline, leaf-truth corpus rule, per-phase toolchain map);
        (2) the provisioning-README user-grade pass (strip tracking refs; replace the
        `.pio` publish line with an execution-layer-neutral note deferring to DES-3);
        (3) re-pin scope-guard @ `scope-v5`. Satellite ID: **OPS-4 (all three items,
        filed + executed same session — manifest born `docs-manifest-v1` with the
        FW/PCB-gated classes as pending-gate nodes naming their gates and the
        canonical-reference floor slot staffed by PROD-16's `esp32-site` surface;
        `docs_verdict_since` set 2026-07-13, the day after the re-pin: same-day
        completions predate the rule and DONE is frozen history). Upstream nit for the
        commons manifest follow-up: the template skeleton's `$comment` key fails the
        schema's own `additionalProperties: false` — drop the key or admit it in the
        schema** (filed 2026-07-12, satellite `547878f`; status lives in the satellite
        ledger).
      **CLOSED 2026-07-12, same day as decided.** All three delegations executed and
      commons-verified (voice DOC-11/DOC-12/BUILD-35 — :6000 fixes confirmed gone,
      manifest test 8/8, guard v5 byte-identical; bridge DOC-13/14/15 + OPS-24 — ADRs
      dissolved and archived, 0006 policy in CONTRIBUTING with OPS-19 re-pointed,
      9 diagrams verified, manifest test 8/8, and the description scrub cut
      **catalog-v1.6** correctly as a contract bump; satellite OPS-4 — 7-node manifest
      with 3 honest pending-gate slots, first CONTRIBUTING.md, provisioning README
      user-grade, guard v5). First live catch by the HK-5 staleness gate: voice's
      `repin-check` correctly reports both catalog pins trailing v1.6 — rides the
      normal re-pin cadence, description-only delta. All four repos now run manifest +
      verdict discipline. docs: contributing, contracts-registry — created/extended by
      the commons execution; readme untouched (no behavior it describes changed).

- [x] **PROD-21 — Python backend layout & naming: the org convention + both migrations**
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
        at intake — counts verified ✓)
        **BOUNCE (commons verification 2026-07-13, before the WB7 cutover):** two
        precise asks. (1) HARD, boot-breaking: all EIGHT config files (master, example,
        6 profiles) still say `discovery_paths = ["irene.intents.handlers"]` while the
        entry-point groups are renamed `locveil_voice.*` — intent discovery finds
        nothing; flip the 8 lines (checklist item 3's "8 config lines" — this was it;
        no other dotted `irene.*` values exist in the tree, swept). (2) SOFT but
        cutover-critical: config-file comments + `config-example.md` still teach
        `IRENE_REPORTS_TOKEN`/`IRENE_ASSETS_ROOT` while the code family is
        `LOCVEIL_VOICE_*` — the operator reads exactly these during the hand-edited
        secrets step; sweep them. Then run the boot verification and CONFIRM the
        fail-fast tripwire actually fires on (1) before the fix (one profile, one boot —
        the tripwire claim deserves its proof). Noted, not bounced: the runtime config
        FILENAME stays `irene.toml` in compose — legal as deployment identity per
        `python-layout.md` §3; keep deliberately or file the follow-up, voice's call.
        Everything else verified CLEAN: layout, zero irene imports, 175 pyproject refs,
        script aliases, config/ singular, catalog re-pin v1.5→v1.7 already executed..
        **BOUNCE RESOLVED — voice BUILD-36 @ b95f3b9 (2026-07-13):** both asks done.
        (1) 8 `discovery_paths` lines flipped to `locveil_voice.intents.handlers`. BUT the
        requested tripwire proof CONTRADICTS the "boot-breaking" severity: `discovery_paths`
        is a VESTIGIAL config field — `IntentHandlerManager.initialize`
        (`backend/src/locveil_voice/intents/manager.py:97`) discovers from the HARDCODED
        namespace `"locveil_voice.intents.handlers"` and never reads `config["discovery_paths"]`
        (nor `auto_discover`). Proof (one profile, embedded-armv7, the stale value in place):
        all 8 enabled handlers resolve, missing=none, the `ValueError` tripwire does NOT fire;
        the x86_64 image `/health` was already healthy before any fix. Flipped anyway to keep
        the config honest — but the field is dead-for-discovery; **voice flags it for removal
        as a separate cleanup** (models.py Field + intent_component plumbing + build_analyzer
        skip-list + 8 configs). No test can catch a stale value BECAUSE the value is unused.
        (2) Stale env/run refs swept across all 8 configs + `config-example.md`: `IRENE_*`→
        `LOCVEIL_VOICE_*` incl. the config-master `LOCVEIL_VOICE_<SECTION>__<KEY>` override
        examples (the live override syntax), header-comment run commands → the split-layout
        model. Owner confirms the WB7 container sets only the ONE token env key, so the cutover's
        hand-edited `.env` step is exactly `ops/cutover-env-locveil-voice.sh`'s scope. Runtime
        `irene.toml` filename kept per §3 (voice's deliberate call). Verified: config-validate +
        build-analyzer all profiles green; config-integrity tests pass.
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
      **CLOSED 2026-07-13.** Both delegations executed and commons-verified: bridge
      CORE-10/CORE-11/OPS-26 accepted with one cosmetic fleck (3 inert sys.path lines,
      opportunistic cleanup); voice BUILD-36 accepted after ONE bounce round — the 8
      discovery_paths lines + the stale IRENE_* env comments — whose demanded tripwire
      proof also corrected the bounce's own severity call (the field is plumbed but DEAD
      for discovery; flipped for honesty, removal flagged voice-side). Both repos now
      run `backend/src/locveil_*` + root `config/` + root `docker/`; catalog re-pinned
      @ v1.7 both copies; remaining BUILD-36 tail (arm images + the scripted WB7
      cutover) is voice-ledger status per the board's own rule. First Opus-executed
      delegations: clean on everything mechanical, missed exactly one string-as-data
      item — the bounce loop caught it pre-cutover, as designed.
      **Voice write-back 2026-07-13:** BUILD-36 formally closed in the voice ledger @ `c0067e7`
      (owner-closed; the WB7 tail — 6-image rebuild/deploy + boot-verify + `ops/cutover-env-locveil-voice.sh`
      + smoke — deferred to the owner's install, any controller breakage a fresh BUG). The "plumbed but
      DEAD" finding is filed as voice **ARCH-50** (release review: every hardcoding / declared-but-unhonored
      config that violates the entry-points dynamic build-and-loading contract; seed = the handler manager's
      hardcoded namespace vs `discovery_paths`).
      docs: none — board/ledger artifacts only.


- [x] **PROD-22 — contract-guard: verify the STAMP-named git tag exists** (shared-tooling gap
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
      No council needed — mechanical enforcement, no new convention. **Delegations executed 2026-07-14** (by the
      commons session on owner instruction, filed per each repo's discipline): bridge
      ID: **OPS-27** · voice ID: **BUILD-37** · satellite ID: **OPS-5** (satellite ADDED
      at execution — the original list named bridge+voice only; it vendors the same
      guard). Commons-side
      deliverable: EXECUTED 2026-07-13 — `contract_guard.py` 1.1.0 (`TAG-MISSING` fail
      on owned STAMPs, `TAG-UNCHECKED` warning outside git; functional-tested both ways;
      commons run green — its own tags resolve), tagged **`contract-guard-v2`**.
      **CLOSED 2026-07-14.** contract-guard 1.1.0 @ `contract-guard-v2` vendored
      byte-identical in all three product repos; the new rule paid for itself on
      arrival — TAG-MISSING fired in BOTH bridge and satellite (`docs-manifest-v1`
      stamped but never tagged: the 2nd and 3rd instances of the exact false-green
      class this entry was filed about); tags created at each STAMP's landing commit
      and pushed. Voice was clean (all four tags existed). All guards green in all
      four repos. docs: none — vendored tooling; each repo's ledger carries its own
      verdict.
- [x] **PROD-23 — Build the `/sprint` skill** (HK-9 execution task; normative:
      `process/sprints.md` — the convention landed with the council, this entry built
      its executable half). **CLOSED 2026-07-14, same day as filed.** Deliverable:
      `.claude/skills/sprint/` — `SKILL.md` (the executable procedure: plan/close
      modes, one-sprint-at-a-time, contributor-round mechanics with the cost mapping
      S≈0.1/M≈0.3/L≈1/XL≈2+/council≈0.5 session-equivalents, no repo-side writes at
      plan time) + `scoping-template.html` (round 0: theme, sessions, bench slots,
      excluded repos, reserve; `sprint-reply` delta grammar) +
      `selection-template.html` (round 1+: selectable rows with
      `data-cost`/`data-bench`/`data-deps`, live JS dependency closure — checking a
      row auto-pulls its deps, unchecking drops dependents — fill gauge against
      usable capacity = sessions − reserve − the pre-reserved close-deploy slot,
      "the can is full" goes red, bench ledger, ghost visibility rows excluded from
      serialization, cross-sprint override toggles, conflict cards). Copy-delta
      machinery inherited from the council dossier (localStorage drafts keyed
      topic+round, delta-only serialization). Both side-find delegations executed
      same day by the commons session on owner instruction, filed repo-side per the
      quick-task precedent: voice — stale gate-prose sweep (ARCH-42/43 + BUILD-18
      re-anchored off closed BUILD-21 to commons PROD-8/PROD-4; UI-4's Gate-2 block
      discharged; `locveil-voice@bcb669b`). Voice ID: **DOC-13**. Bridge — VWB-39
      dep line re-anchored (artifact exists; DRV-37 not "DRV-36's implementation";
      `locveil-bridge@19b7014`). Bridge ID: **DOC-16**. docs: contributing — the
      new Sprints row in the process list; the convention itself landed at HK-9.

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
- [x] **HK-5 — contracts in general** (fifth council topic; the first parked seed
      convened, and the first with all THREE product keepers — satellite-keeper's debut,
      which stale-flagged its own repo's README). Decided 2026-07-12 in ONE keeper round +
      one owner round; decision and execution filed as **PROD-16** (delegations there);
      normative convention: `process/contracts.md`. Round arc: reconnaissance corrected
      the brief — catalog is **v1.4 not "1.5"** (no version field, no tags anywhere; the
      prose `contract_patch` accumulator in the voice pin is the symptom), "PROD-7 in
      flight" overstated (VWB-29 + BUILD-24 both unbuilt — making the coordinated cut
      near-free), and commons self-flagged the same disease (`report-protocol.json`
      carries no in-artifact version). Keepers converged unanimously on two-layer
      enforcement (thin coherence checker + per-repo conformance tests; semantics never
      in the shared tool) and on prose-contracts-as-block-pins; satellite's
      new-tool-not-scope-guard argument beat voice's mild extension preference. Owner
      rulings: uniform layout ENFORCED IMMEDIATELY (bridge's grandfathering objection
      overruled); `catalog-v1.5` — README changelog stays as narrative, STAMP + tag
      become the machine-readable version authority (owner mid-landing correction);
      staleness never a push gate (voice's hard condition confirmed).
- [x] **HK-6 — User-facing documentation harmonization** (sixth council topic; bare
      seed, decided 2026-07-12 over TWO owner rounds, all three product keepers).
      Decision and execution filed as **PROD-17** (delegations there); normative:
      `process/user-docs.md` + `process/user-docs/manifest.schema.json`. Round arc:
      round 1 audited both exemplar corpora and root-caused the rule failure —
      the only LAW with zero mechanical enforcement and no artifact slot for the
      verdict (live exhibits: voice's port-6000 quartet missed twice; bridge's REL-4
      fixing 11 of ~22 docs at the gate; the satellite's provisioning README
      contradicting its own DES-3) — plus the template bug (the rule never reached
      the satellite). Owner rulings round 1: ADRs INTERNAL (dissolve/archive), org
      README folds into PROD-9, no Russian docs today, operator docs in scope,
      verdict in the DONE entry. Round 2 engineered the owner's docs-manifest idea
      into a repo-internal contract (pending-gate slots, surface→glob suspect sets,
      derives_from, CONTRIBUTING-in-the-manifest — proven by bridge's CONTRIBUTING
      drifting stale in under 24 hours outside the old rule's scope); the node
      policy became a failing test instead of an approval. Owner rulings round 2:
      floor only where the capability exists; docs-review tasks fileable any time,
      a commons-filed one fans out to all repos. Landed same day: spec + schema +
      scope-guard 1.2.0 @ scope-v5 (docs-verdict presence rule; shared-invariants
      block gains the invariant) + template seeds. docs: none — process/board
      artifacts only (the convention itself; first verdict line under its own rule).
- [x] **HK-7 — Open-task triage: what deserves a PROD umbrella** (seventh council
      topic; bare seed, decided 2026-07-12 in one keeper round + one owner round; voice +
      bridge keepers — satellite excused, 7 fresh tasks). The sweep: **63 open tasks
      inventoried complete** (voice 26, bridge 37; all post-release `[deferred]`, zero
      open `[release]` anywhere). Result: 5 already ride PRODs correctly (ARCH-42/43 +
      CORE-7/OPS-14 on PROD-8; BUILD-18 + OPS-15 on PROD-4), **~51 stay repo-local**
      (both keepers argued against board inflation — every umbrella costs intake,
      write-backs, and contract-cut ceremony), 7 formed four clusters. Owner rulings:
      **PROD-4 REFRAMED in place** to deployment coordination + ops conformance
      (absorbs BUILD-28 whose board-seed trigger misfired 2026-07-11; ARCH-45 readiness
      contract as named dependency; master→profiles convention dialect-aware; CORE-8
      secrets posture joins); **PROD-18** filed (catalog contract evolution: VWB-33 +
      VWB-34 + voice QUAL-82 seat; one arc, one cut, one re-pin); **PROD-19** filed
      (intake consolidation on locveil-reports; BUILD-14 + bridge twin at intake);
      **PROD-20** filed as a LIGHT visibility entry (satellite first-light chain,
      HW-GATED — owner chose visibility over repo-to-repo silence, the round's one
      flip); PROD-10 gained the OPS-13/UI-8 toolchain-sequencing note; BUILD-13 (Pi
      python-satellite image) STAYS voice-published (the python satellite is a voice
      deployment mode, HK-4 lineage). Side findings handed to repo sessions: voice
      TEST-20/BUG-42 are two open tasks about the same flaky test with contradictory
      evidence (merge); bridge UI-8 subsumed by OPS-13 (tombstone) + two stale-wording
      re-anchors; OPS-19's mirror-policy generalization waits for rule-of-two. Voice
      files the master→profiles gate mechanism regardless — BUILD-31's lesson finally
      has a home. docs: none — board/ledger artifacts only; no manifest node describes
      individual board entries.
- [x] **HK-8 — Python backend source-root convention** (eighth council topic; bare
      seed, decided 2026-07-13 over THREE rounds, voice + bridge keepers; satellite
      pre-scoped by the owner as consumer-at-most). Decision and execution filed as
      **PROD-21**; normative: `process/python-layout.md`. Round arc: round 1 found the
      owner right TWICE about different layers — voice's layout wrong/name right,
      bridge's layout right/name wrong — and proposed an asymmetric cure; the owner
      overruled with "voice is multi-component too" (correct — config-ui is a peer of
      bridge's ui/) and "if we rename at all, we rename everything", plus the
      human-interpretable-blast-radius format mandate. Round 2's honest re-pricing
      COLLAPSED voice's round-1 minefield (no external plugins exist; the deployed
      config is derived and regenerates via update.sh; the durable-actions alarm was
      wrong — prod state is a bind mount): voice withdrew opposition and signed uniform
      (~4.5–5-day one-churn BUILD-36 vs bridge's ~1-day CORE-10 with the deliberate
      catalog-v1.7 cut). Round 3 folded in two owner additions — the bridge config tree
      ruled PRODUCT DATA and leveled to root, Dockerfiles consolidated to root docker/
      (both CORE-11; the OPS-11 arch-identical finding settled per-component file
      naming) — and ruled eval_commons STAYS under the principled rule (product
      backends = locveil_*; shared libraries = truthful neutral names; the org's own
      PROD-2 dist/import precedent). Also settled: config/ SINGULAR org-wide; scripts
      locveil-catalog/locveil-openapi with wb-api retired; irene-* aliases one release;
      vendored guards exempt; persona in user-visible strings; OPS-26 wire cutover
      owner-gated on the same deploy cycle. Council craft note: a mid-round addition
      queued to a running keeper stranded silently — re-engage after the notification,
      never mid-flight. docs: contributing — the process-kit pointer row; plus the new
      spec itself and the template/process-README rows.
- [x] **HK-9 — Sprint planning: convention + `/sprint` skill** (ninth council topic;
      bare seed → owner brief of 7 rules, decided 2026-07-14 over two rounds, all three
      keepers; **normative: `process/sprints.md`**; execution filed as **PROD-23**).
      Decision digest: capacity currency = owner-attended sessions + a separate
      bench-slot budget, never calendar effort (anchor: BUILD-36 predicted 4.5–5 days
      by its own keeper, realized 2h45m — ~10×); effort classes S/M/L/XL +
      attempt-slot + no-data-is-legal; 30% discovery reserve (50% with XL/HW),
      incidents displace reserve visibly; sprint file `board/sprints/sprint-NN.md`
      lists IDs and NEVER asserts status (zero repo churn; HK-1 required-task-tags
      earmark resolved: no new tags); deps v1 = fresh per-sprint closures in proposal
      artifacts (standing `deps:` field parked as v2; partial deps = split the task);
      travels-with groups = single selectable rows; blocked/unstartable pull members =
      visibility rows; planned councils first-class ≈0.5 day + enabling-council rule;
      rule3×rule7 (PROD pull into an excluded repo) always surfaced to the owner.
      Round-2 delta (owner): the **shippable invariant** — every sprint closes with
      each involved repo deployABLE per its OWN existing gates (per-repo definition
      declared in the sprint file; deployable ≠ deployed — the WB7 deploy is one
      pre-reserved owner slot; binds the deployability gate, never a `[release]` scope
      gate); cut atomicity not group confinement (cut-coupled members land in the
      cut's sprint; design/implement may straddle; trailing sibling pin
      version-tolerable); cross-sprint features declared in the sprint file only, with
      mandatory zero-effort carry-over rows, HW-GATED auto-declared cross-sprint by
      default, mid-sprint declaration owner-only; naming = plain `sprint-NN` (all
      three keepers independently flagged date/release-shaped names as pre-empting the
      parked release-numbering council); close labeling = SHA-in-sprint-file
      (`repo@sha` + one-line verdict; unanimous keeper opposition to repo-side sprint
      tags — tag namespaces are guard-checked contract machinery, planning facts live
      commons-side); close runs each repo's repin-check; sprint review appends
      realized stats (the calibration loop). Side-finds delegated via PROD-23: voice
      stale gate-prose sweep, bridge VWB-39 dep line. docs: none — process convention
      + board artifacts; no commons manifest node covers process/ internals.
