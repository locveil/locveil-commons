# Locveil board — DONE ledger

Completed `PROD-N` / `HK-N` / `IMPL-N` entries, MOVED here from `BOARD.md` on close
(same change as the journal entry — `process/ledger-discipline.md`). Frozen history:
entries are never re-edited; delegated IDs listed inside them are pointers, never status
assertions.

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
- [x] **PROD-8 — core-py bootstrap + first two extractions** (D-8): `packages/core-py`
      skeleton (own pyproject, `core-py-vX` tags), then the two designs — dynamic code
      loader (voice ARCH-42; voice consumer #1, bridge #2 via CORE-7) and logging scheme
      (voice ARCH-43; retires the BUG-30/OPS-12 hand-copy → bridge OPS-14).
      **COUNCIL-DECIDED 2026-07-16 (PROD-8 council, 2 rounds; keepers voice+bridge —
      satellite is not a core-py Python consumer).** Both support-with-conditions; both
      confirm entry-points is the discovery spine (voice: 13 provider groups + one
      `DynamicLoader`; bridge: `locveil_bridge.devices`, 9 drivers) and that bridge authored
      the logging scheme (OPS-12 DONE → voice BUG-30 is the copy). **Decisions:**
      **(1) Shared loader = the entry-point-group registry only** (voice's `DynamicLoader`
      engine) — the genuine rule-of-two leaf. Voice's `EntryPointMetadata` build-time metadata
      quartet (`get_python_dependencies`/`get_platform_support`/`get_supported_architectures`/
      `get_platform_dependencies` — dependency-closure + the load-bearing arch gate) and all its
      values stay voice-side; bridge's by-name config resolver (`class_loader.py`) stays
      bridge-side. Each auxiliary graduates to core-py only on its own second consumer.
      **(2) "Config-based driver loading" = unify resolution, keep entry points.** Replacing
      entry points with runtime config-path discovery is REJECTED — it breaks the offline
      catalog generator (`dump_catalog`) that builds the voice-pinned golden without loading a
      single driver. CORE-7 stays a self-contained infra swap; no catalog-contract bump.
      **(3) The UI/panel driver-availability gating is a SEPARATE bridge task**, never a rider
      on CORE-7. Today the surface is split-brained (operational pages gate on loaded drivers →
      404 + absent from catalog; config pages / nav / workbench still show configured-but-
      unloaded devices). The invariant "no driver → no device pages AND config pages" is a
      presentation + possible catalog-contract change; that task decides suppress-vs-surface.
      **(4) Sequencing locks:** ARCH-50 is a HARD PREDECESSOR of ARCH-42 (its hardcodings
      inventory feeds the loader design); the `packages/core-py` skeleton is cut AFTER ARCH-50 +
      ARCH-42 land (surface known first); the logging extraction (ARCH-43 → OPS-14) is PARKED —
      loader first, logging a later round (bridge's OPS-12 is the reference when it resumes).
      **Delegations (board-as-outbox):** voice — reconcile **ARCH-42** scope to "extract the
      entry-point-group discovery engine only; metadata contract + values stay voice-side;
      preserve the `build_analyzer`→`get_provider_class`→classmethod seam"; confirm ARCH-50-first
      and fold the dead `get_provider_capabilities` (`components/base.py:216`, zero call sites)
      into ARCH-50's dead-code sweep; ARCH-43 parked. Voice write-back — lead ID: **ARCH-42**
      (+ ARCH-50, ARCH-43) — **RECONCILED AT INTAKE 2026-07-16 (voice session), all three entries
      amended in the voice ledger:** ARCH-42 narrowed to the entry-point-group registry only
      (`utils/loader.py:133` `DynamicLoader`), with the `EntryPointMetadata` quartet
      (`core/metadata.py:25`) + values explicitly voice-side, the `build_analyzer`→
      `get_provider_class`→classmethod seam named as preserved, and ARCH-50 recorded as a hard
      predecessor on both entries; ARCH-50 carries the dead `get_provider_capabilities`
      (`components/base.py:216` — zero call sites VERIFIED at intake, resolves as delete per
      `dead-code-remove-not-fix`); ARCH-43 marked PARKED. No scope drift found — the council's
      voice-side claims all held against repo reality. **SEQUENCING LOCK DISCHARGED 2026-07-16
      (voice session, same day):** ARCH-50 DONE (review + all 8 remediation tasks landed) →
      ARCH-42 DONE — the design is AGREED and committed at
      `../locveil-voice/docs/design/core_py_loader_extraction.md`. **The `packages/core-py` skeleton is UNBLOCKED**
      ("surface known first" is satisfied). Surface summary for the skeleton cut: module
      `entry_point_loader.py`, class `DynamicLoader` ONLY (no module-level singleton — consumers
      own theirs); methods `discover_providers(namespace, enabled=None, base_class=None)` /
      `get_provider_class(namespace, name, base_class=None)` (single-EP load) /
      `list_available_providers` / `list_registered` (names without import) /
      `get_discovery_failures` / `clear_cache`; Python 3.11, importlib.metadata only; own
      pyproject + tests; tag **`core-py-v1`**. Consumption = vendored copy at tag with STRICT pin
      (consumer pins/core-py + byte-identity test — first vendored RUNTIME code). Voice follow-up:
      **ARCH-58** `[release]` (migration, gated on `core-py-v1`).
      **Voice write-back (2026-07-18) — ARCH-58 DONE; voice's half of PROD-8 is CLOSED.** The
      migration executed against **`core-py-v1.1`**: the FIRST strict pin refused v1 — the tag
      was cut before the "PROD-8 amended" commit added the STAMP, so the v1 tree cannot satisfy
      pins-complete-and-verbatim — and commons cut the v1.1 packaging correction (artifact
      bytes diff-verified unchanged; STAMP note + board journal record it). Voice landed: the
      `core-py` family in `.repin.toml` (the BUILD-43 sequencing held — declared once, new
      format), strict pin + byte-identity test, `utils/entry_points.py` singleton, the full
      20-file sweep, `startup_validation` on `list_registered`, DynamicLoader deleted from
      `utils/loader.py`. Acceptance: suite 1433 green, analyzer JSON byte-identical ×6 profiles,
      import contracts 11/11, guards + `repin --check --fail-on any` green. **CONSUMERS NOTE:
      bridge CORE-7 vendors at `core-py-v1.1`** (not v1 — same bytes, but only v1.1's tree
      carries the STAMP a conforming pin needs). Remaining in this entry: bridge CORE-7 + the
      parked logging extraction. Bridge CORE-7 codes against the
      design's §5 (base_class native, loader never in domain/, no golden drift, `list_registered`
      for dump_catalog). Bridge — reconcile **CORE-7** (adopt the core-py registry for the
      driver axis, keep the config resolver local, no config→entry-point unification, loader in
      `utils/`/behind a port never `domain/`, zero new import-linter exceptions, no catalog
      drift; FIX the stale gate "voice BUILD-21" → "PROD-8 / core-py exists"; fold the dead
      `config/validation.py:89,94` pre-HK-8-prefix cleanup) AND file at intake the **new
      UI/panel driver-availability gating task**. Bridge write-back — lead ID: **CORE-7** + the
      new UI-gating ID — **RECONCILED AT INTAKE 2026-07-16 (bridge session), both delegations
      executed:** CORE-7 reconciled as **(d) scope drifted → redefined** (owner consulted before
      the edit per the bridge dialect's STOP rule) — narrowed to the entry-point-group registry
      only, `utils/class_loader.py` kept bridge-side, the config→entry-point unification recorded
      as REJECTED with the `dump_catalog` reason, and the stale **"voice BUILD-21"** gate corrected
      to **"PROD-8 / core-py exists"**. Driver axis verified live: the `locveil_bridge.devices`
      group, 9 drivers (`backend/pyproject.toml:98-107`) → `domain/devices/service.py:51-52`. The
      dead-code fold VERIFIED at intake and folded into CORE-7: `validate_class_references`
      (`infrastructure/config/validation.py:67-97`, the board's cited `:89,94` prefixes) has zero
      call sites — `validate_device_configs` never calls it, so `device_class` is **never validated
      at startup at all**. New UI-gating task filed: **UI-20** `[P1]` `[release]`.
      **Intake correction — decision 3's "split-brained" wording understates it: the surface is
      THREE-brained.** Beyond the raw-config-vs-loaded-driver split, (a) **room membership is a
      loaded-driver surface too** since the 2026-06-08 refactor (`domain/rooms/service.py:203-240`
      derives `room.devices` by walking `DeviceManager.devices`), so the device vanishes the moment
      a room is selected — the nav only shows it unfiltered; and (b) a **third brain**,
      `GET /devices/{id}/persisted_state` (`presentation/api/routers/state.py:75-92`), reads the
      state store directly and answers **200 with a stale snapshot** for a device the rest of the
      runtime denies exists. Root cause: `domain/devices/service.py:116-120` logs and skips with no
      retained status — the deliberate opposite of the setup()-failure policy (`:154-183`, device
      stays registered). UI-20 owns the suppress-vs-surface verdict and must make all three obey.
      **SKELETON CUT 2026-07-18 (commons session): `packages/core-py/` EXISTS — tag
      `core-py-v1`** (distribution `locveil-core-py` 1.0.0). `entry_point_loader.py` implements
      the design's §2 surface exactly — class only, no module-level singleton, `importlib.metadata`
      on py3.11 only, faithful cache + failure-ledger semantics plus the three agreed deltas
      (`base_class=` rejection into the ledger, single-EP `get_provider_class`, import-free
      `list_registered`); behavior suite 23 tests green; own pyproject + README per the guards'
      precedent. Amended same day (owner: "no new contract?" — right): the owned surface
      **`contracts/core-py/`** (STAMP `core-py` v1 + cross-ref README, registry row) landed per
      `process/contracts.md` §2 — the pin convention requires the owner's STAMP verbatim inside
      every consumer pin, and the first stamp already carries the `artifacts` completeness list
      (exactly `entry_point_loader.py`; tests/pyproject never travel). **ARCH-58 (voice) and
      CORE-7 (bridge) are UNBLOCKED** — they vendor at the tag with the strict pin +
      byte-identity test (design §3/§5). **Entry stays OPEN until both
      adoption write-backs arrive (owner ruling 2026-07-18)**; at close, also decide whether the
      parked logging extraction (ARCH-43 → OPS-14) spins off as its own entry or PROD-8 closes
      title-narrowed to the loader.
      **Bridge adoption write-back (2026-07-18, evening) — CORE-7 executed; the bridge half of
      the loader arc is done (status lives in the bridge ledger).** Vendored at **`core-py-v1.1`**
      per the consumer note (v1 refused by construction — its tree predates the STAMP); the pin
      was taken by the bridge's own vendored repin tool (`.repin.toml` core-py family + strict
      PIN.json + byte-identity conformance test, the ARCH-58 shape; hashes bit-identical to
      voice's pin). §5 conditions all held: singleton in `utils/` (never `domain/`), zero new
      import-linter exceptions, registry re-keyed by class name (the configs' vocabulary),
      fresh-discovery semantics kept for `/reload`; the dead `validate_class_references` folded
      out with the swap. Verified by driving it: 9/9 drivers via `discover_providers
      (base_class=DevicePort)` with an empty failure ledger; `dump_catalog` golden byte-identical
      (79 devices) — no contract movement, as the council scoped. Bridge follow-ups filed off a
      config-driven-loading analysis (voice's slim-image pattern, bridge dialect): **CORE-13**
      (config-driven driver activation — the config tree already declares demand via
      `device_class`, no new config format; failure policy decided WITH UI-20) and **OPS-35**
      (per-driver pip EXTRAS + profile-driven slim images — deliberately NOT the
      `EntryPointMetadata` quartet, which stays voice-side per the council; graduation only on a
      genuine second metadata consumer). **Both adoption write-backs are now in** — the close +
      the logging-extraction spin-off question are the board keeper's per the owner ruling.
      The board lists delegated IDs but never asserts their status — per-repo ledgers own it.
      **CLOSED 2026-07-18 — both adoption write-backs in and COMMONS-VERIFIED.** Voice
      ARCH-58 (verified earlier same day: three-way byte identity pin==importable==tag,
      strict PIN, 20-file sweep, suite 1433 green, analyzer byte-identical ×6) and bridge
      CORE-7 (verified at close: pin + owner STAMP byte-identical to `core-py-v1.1`,
      importable copy in `utils/` == pin, identity test wired, `discover_providers
      ("locveil_bridge.devices", base_class=DevicePort)` live in `domain/devices/service.py`
      via the `utils/entry_points.py` singleton, `class_loader.py` untouched since CORE-10,
      `validate_class_references` gone (0 refs), dump_catalog golden byte-identical — no
      contract movement as the council scoped, CI green job-level). Both consumers pinned at
      **`core-py-v1.1`** — the v1 packaging correction (tag must carry its STAMP) is the
      arc's recorded lesson, caught by the first strict pin. Bridge follow-ups CORE-13 +
      OPS-35 filed bridge-side off the adoption analysis. **The parked logging extraction is
      SPUN OFF as PROD-27 (optional, owner ruling at close)** — this entry closes on the
      loader alone. docs: none — package README + design doc are the integrator surface,
      both current. contracts: none at close — the arc's surfaces carried their own verdicts
      (core-py-v1 cut, owned-surface amendment, v1.1 packaging correction).

- [x] **PROD-10 — ui-kit package + stylebook** (D-8/D-9, next release): `packages/ui-kit`
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
      **① Extraction LANDED 2026-07-14:** `docs/design/ui/token-inventory-draft.md`
      (tiered token evidence) + `docs/design/ui/divergence-list.md` (the stage-②
      council agenda, D1–D10). Owner evidence-tier ruling applied: T1 = remote pages +
      remote scan only; appliance pages + config-ui = inventory, not taste. Headline
      finds: bridge `ui/` is a STOCK shadcn install with never-chosen default theme
      values (the token carrier exists, empty); @mui/material + emotion have ZERO
      imports — Material icons are the only real MUI usage (and icon names are a
      backend-manifest contract); the remote is a deliberately dark, theme-independent
      island (its stiffness mechanism documented as a fluid-rebuild requirement, D10);
      shadcn/ui feasibility verdict: strong yes (owner's "standard components" hunch
      confirmed — inventory §9). Tooling prep: frontend-design + skill-creator
      installed (owner cp).
      **② Style council DECIDED 2026-07-14** (two rounds of rendered choices, owner
      seed "blued steel, island stays black-ish"): neutrals = steel-A «Воронение»
      (hue 211-213, light `210 25% 97.5%` / dark near-black `213 26% 8.5%`) · accent =
      **steel-blue, polished dark calibration** (`207 70% 42%` light / `207 80% 62%`
      dark) — monochrome-metallic, color reserved for meaning · icons = **SPLIT**
      (lucide stroke in workbench/chrome; Material filled stays inside the island —
      manifest names remain a contract) · chrome radius **0.75rem** (island ladder
      untouched) · compact density · system type stack ratified (offline-first, no
      webfonts) · status tokens ratified with **tested-stays-blue** owner ruling ·
      dual theme day one · shadcn/radix base ratified · island as-shipped + D10 fluid
      implementation deferred to a dedicated **bridge wireframe/layout session**
      (owner-announced; bridge files it at that session's intake).
      **③ Codification LANDED 2026-07-14:** tokens
      `packages/ui-kit/tokens/locveil.css` + `.json` (seed of the ui-kit package) ·
      stylebook `docs/design/ui/stylebook.md` (docs-manifest node `stylebook`, new
      `ui-kit` surface) · **`ui-style` skill** (`.claude/skills/ui-style/`) as the
      executable half. Remaining: **④ ui-kit-v1** (components on the tokens, Storybook,
      radix/`components.json`, first tag) — unblocked: OPS-13 done bridge-side,
      shell contract (PROD-24) decided, tokens decided.
      **Sprint-01 (2026-07-14) activated the design phase** — stages ①–④ selected
      (`board/sprints/sprint-01.md`); the deploy-split design + Workbench shell council
      split out as **PROD-24** (its wireframe/plug-in contract shapes ④'s component
      boundaries); the HK-7 sequencing note is resolved by sprint-01 decision 1: bridge
      OPS-13 runs first, ui-kit targets eslint-9/vite-6 — the migration runs once.
      **④ ui-kit-v1 LANDED — PROD-10 CLOSED 2026-07-14** (all four stages ran in one
      day): `packages/ui-kit` = `locveil-ui-kit` 0.1.0, tag **`ui-kit-v1`** — 17
      primitives on radix + the tokens (Button, Badge, StatusChip/StatusDot with the D8
      recipes, Card, Label, Input, Textarea, Alert, Skeleton, Separator, Tabs, Dialog,
      Tooltip, Select, Checkbox, Switch, Slider, Icon with owned 16/20px sizing),
      tailwind preset, version-agnostic ESM + types (deps externalized — vite majors
      stay per-consumer), eslint-9 flat config, Storybook workbench with a dual-theme
      toolbar (the assembly story is the council's round-2 mock rebuilt on the real
      components). Verified: install 0 vulnerabilities · typecheck + lint clean · lib
      build · storybook build. Deployment-class-agnostic by design (owner Q&A on
      record): one kit for workbench AND operations; future controller-UI council adds
      token sections/profiles, never a second kit. Write-backs: voice **UI-17**
      (config-ui adoption, declared cross-sprint → sprint-02) + bridge **UI-17**
      (adoption plan inside its Workbench-split design) — both filed at PROD-24 intake;
      the HK-7 sequencing note resolved by sprint-01 decision 1 (OPS-13 ran first).
      docs: stylebook — the node covers the ui-kit surface; the package README is the
      consumer doc.
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

- [x] **PROD-24 — the Locveil Workbench: workstation UI shell + deploy-split** (filed at
      sprint-01 planning, 2026-07-14; **shell council DECIDED 2026-07-14** — two rounds,
      all three keepers, owner wireframe sketch as seed; the dossier was a view, this
      entry is the record). **CLOSED 2026-07-14, same day as filed** — council decided, design doc landed, all three write-backs verified present in the sibling ledgers (voice ARCH-51 + UI-17, bridge UI-17, satellite DES-5 expansion + OPS-6). Naming **operations / workbench** ratified.
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
      consume it. All three write-backs arrived the same day (below).
      **Delegations (board-as-outbox):**
      satellite — **DES-5 expansion**: the cert-lifecycle design absorbs the broker (one
      privileged path, two clients), the full verb vocabulary, the workstation
      operator-credential design (client cert from the home CA vs a separate secret),
      and an **OPS earmark** for the ansible-deploy rework (owner: not this sprint).
      Satellite ID: **DES-5** (expanded in place) + **OPS-6** (ansible earmark)
      (written back 2026-07-14 at intake; reconciled clean — CLI verbs, D-17's
      "config-ui may call the same scripts later" hook, and the ansible target all
      verified; today's CLI `revoke` = the board's `reject-pending`).
      voice — (a) satellite-local config endpoint design (`design-then-implement`,
      dev-phase shape; new attack surface → PROD-4 auth posture applies); (b) the
      declared sprint-02 config-ui adoption task grows the 6-page cut (Overview + Header
      retire) + status-slot wiring. Voice IDs: **ARCH-51** (a) + **UI-17** (b)
      (written back 2026-07-14 at intake; reconciled clean — page count, Header status,
      CoreConfig sections all verified).
      bridge — UI-17 intake (sprint-01 row) grows: the staged-write API shape + the
      planned-docs DOC follow-up (device-setup/topology-setup: "Apply stages via the
      controller API; promotion is a commit"; topology-setup's live-vs-file open
      question is answered = staging; the admin-shell rows across all four planned
      pages). Bridge ID: **UI-17** (bridge-repo serial — distinct from voice's UI-17
      above). docs: none — the deliverable IS a design record (`docs/design/workbench.md`);
      the commons manifest carries no design-doc node class and no existing node's
      coverage is invalidated.

- [x] **PROD-25 — CI checkouts must fetch tags for contract-guard: the convention +
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
      **CLOSED 2026-07-17 — all three remaining conditions verified in live CI
      (write-backs):** (1) commons green: run 29435212549 @ 8cb7880 executed the guard
      job with the explicit-fetch workflow (18967ae an ancestor) — passing `--check`
      with two tag-naming owned STAMPs proves the tags resolved; (2) voice green: run
      29435718102 @ 4175aeb (contains the BUILD-39 fix) executed the `contract-guard`
      job with success — every later voice run merely path-skipped it; (3) bridge
      OPS-30 on checkout@v6 confirmed live TWICE: dispatch run 29412862181 failed 3×
      TAG-MISSING on the bare checkout, the fix push ran the guard green at 11:58
      (29413490074) and again at 17:20 (29436060503) — answering the entry's open
      question: **v6 does NOT share #1467's behavior; the flag works there.** §4
      gains the v6 footnote (the flag-form ban is scoped to v4's shallow-SHA path;
      bridge's working flag-on-v6 is the recorded exception, protected from
      "fixing"). docs: none — process file amended in place, per this entry's
      own filing precedent.

- [x] **PROD-26 — HK-12 execution: convention-enforcement hardening** (decision of record:
      HK-12 in `BOARD_DONE.md`, decided 2026-07-18; normative severity policy already landed
      as `process/contracts.md` §5 in the HK-12 landing commit). **Commons build (this
      repo):** (1) `packages/repin/` — promote the voice BUILD-24 engine (generic ~120 lines:
      registry-keyed newest-tag parser, fetch-at-tag + sha256 + PIN.json writer, `--check`,
      CLI) with per-repo TOML family config (multi-dest + per-dest conformance + `pinned_by`
      as config; multi-dest writes legal only into commons), remote-first tokenless
      `ls-remote` + offline fallback (WARN + fetch age), untagged-family skip-warn in CI
      mode, vendored-tools-manifest family kind; tag **`repin-v1`** + `contracts/repin/`
      STAMP + registry row from day one. (2) contract-guard v3: registry-keyed orphan-tag
      rule, content-drift rule (`git show tag:path` vs HEAD), `vendorable_roots` explicit
      config (commons: `packages/*`; products default empty), mid-bump local tolerance
      (hook warns / CI strict); tag `contract-guard-v3`. (3) scope-guard v7: `contracts:`
      verdict line ("created, bumped, or first consumed"; owner bumps record `re-pin owed:
      <consumers>` — normative; per-repo `contracts_verdict_since`, DONE frozen) +
      unknown-prefix rule; tag scope-v7; `process/ledger-discipline.md` gains the verdict
      spec. (4) Pinned contract-triad block: source in `process/claude-blocks/`, digest only
      (STAMP+tag+registry same change; bump = tag+STAMP together; pins complete & verbatim;
      consumers move only by re-pin tasks). (5) Commons stamps: `contracts/workbench/`
      (contract types + runtime-config schema + manifest-fragment schema + peers semantics),
      `contracts/ui-kit/`, STAMP folders for scope-guard + contract-guard (closing the
      registry cross-reference gap); eval deferral + the non-candidate list recorded in
      `contracts/README.md`. Commons adopts its own medicine in the same arc (verdict line
      on, vendorable_roots set, repin config for its consumed pins). **Delegations
      (board-as-outbox, ONE sweep per repo — the keepers' sequencing condition):**
      voice — BUILD-41 (contract-guard v3 re-vendor) + BUILD-42 (scope-v7 + verdict date) +
      BUILD-43 (adopt vendored repin at `repin-v1`, convert `FAMILIES` to config, keep
      `make repin`/`repin-check`, pre-commit warn stage; SEQUENCED BEFORE ARCH-58 so the
      core-py family is declared once in the new format) + the trace-format contract task
      (voice-owned, doc-canonical — the shape today lives only in voice's trace-persistence
      design doc)
      + block re-pin (mechanical carve-out) + answer satellite's wake-pack-v1.x bump
      confirmation. Voice write-back (2026-07-18) — lead ID **BUILD-41** (sub-IDs: BUILD-42,
      the guard+block halves executed as ONE commit per the keepers' condition; BUILD-43 repin
      adoption — `.repin.toml` with the catalog multi-dest + the `[[tool]]` manifest, dry-run
      verified both dests at catalog-v1.7; **DOC-14** the trace-format contract —
      `trace-format-v1` cut doc-canonical on `docs/guides/tracing.md` with a version-triple
      test; found live: the commons docs-manifest schema caps `surfaces` at 10, so voice's
      trace-format glob-trigger mapping waits for the next schema bump). The satellite filing
      **BUILD-44 ANSWERED same day** (tagged-bumps-only + flat-sha256-enumeration
      parse-stability across v1.x + drift re-stamp & immutable `/resolve/<revision>/` URLs at
      the cut; execution filed as voice ASSET-6, gated on the next trained words); ARCH-58
      annotated to declare the core-py family in the new `.repin.toml` format. Status lives in
      the voice ledger. Bridge — guard sweep (contract-guard
      v3 + scope-v7 + verdict date + third block, one OPS task per its round-1 condition) +
      repin adoption (family config: report-protocol now, workbench pin when stamped) + the
      workbench-plugin CI job (owed regardless — zero coverage today) + satellite's
      device-integration-v1.1 minor-tag request (repo-to-repo). Bridge write-back (2026-07-18) —
      lead ID **OPS-32** (guard + block halves as ONE commit per the keepers' round-1 condition;
      `.contract-guard.toml` born with explicitly empty `vendorable_roots`, the keeper's recorded
      posture; `contracts_verdict_since = 2026-07-18`). Sub-IDs: **OPS-33** repin adoption
      (`.repin.toml` = report-protocol family + the `[[tool]]` manifest at
      scope-v7.1/contract-guard-v3/repin-v1; ordinary CI at `--fail-on major`; the workbench
      family joins when commons ships the machine schemas at the next workbench bump) and
      **OPS-34** the workbench-plugin CI job (sibling commons checkout + ui-kit build — the
      `file:` deps). The satellite filing executed as **VWB-42**: `device-integration-v1.1` cut
      with an artifacts-enumerated STAMP (repo-root-relative paths), arming CONTENT-DRIFT for the
      family; re-pin owed: satellite (their DES-4 takes the first pin). Found live by the first
      v3 run: the catalog STAMP's pre-v3 `artifacts` entries are bare names where v3 reads
      repo-root-relative — a latent root-README false-drift trap, filed bridge-side as VWB-43
      (fix rides the next catalog cut). Status lives in the bridge ledger. Satellite — guard sweep + repin adoption (hook stage with offline fallback +
      the same freshness check inside `publish_model_pack.py verify/publish`) + the
      `contracts/README.md:35` drift one-liner (contract-guard-v1 → v2, found live in HK-12
      round 2) + born-stamped clauses in DES-5 and the D-16 Stage-2 design + execute the two
      greenlit repo-to-repo filings. Satellite write-back (2026-07-18) — lead ID **OPS-11**
      (sub-IDs OPS-12 guard+block sweep, OPS-13 repin adoption; the two filings executed
      repo-to-repo: voice **BUILD-44** (wake-pack bump confirmation — plus a same-day
      addendum: the satellite's OPS-13 smoke test found the published pack ALREADY drifted,
      HF mutable-ref URLs) and bridge **VWB-42** (device-integration-v1.1 minor tag); status
      lives in the satellite ledger). The board lists
      delegated IDs but never asserts their status — per-repo ledgers own it. Sequencing:
      commons build first (repin-v1 + guard tags are what the sweeps vendor); satellite's
      major-gap severity stays advisory until FW first light (§5); nothing here gates FW-2.
      **PROGRESS 2026-07-18 — item (1) DONE: `packages/repin/` EXISTS, tag `repin-v1`**
      (distribution `locveil-repin` 1.0.0, stdlib single file). Engine promoted faithfully +
      the HK-12 deltas: per-repo `.repin.toml` (families/dests/tools; `pinned_by` +
      `default_fail_on` config), `--fail-on none|major|any` severity ladder, remote-first
      tokenless `ls-remote` with stale-clone fallback (WARN + fetch age) and offline
      no-source degradation (warn at none/major, fail at any), untagged-family drift check,
      `check_only` families (repin refused, check allowed), commons-only cross-repo dest
      validation, `[[tool]]` vendored-tools manifest. Behavior suite: 15 tests on real
      throwaway git repos, green. Owned surface `contracts/repin/` (STAMP v1 + `artifacts`
      list + registry row) cut IN THE SAME CHANGE as the tag — §2–3 walked at creation, per
      this very council. Commons adopted: `.repin.toml` (catalog family `check_only` —
      voice's multi-dest stamps it; crossover-fixtures joins at its strict-PIN task) +
      pre-commit warn stage in `hooks/pre-commit`; live check green (catalog current at
      v1.7 via real ls-remote). Product sweeps may now vendor at `repin-v1`; guard v3/v7
      (items 2–3) are the remaining commons build.
      **PROGRESS 2026-07-18 (same day) — items (2), (3), (5) DONE.** contract-guard
      **v3** (script 3.0.0 — major now tracks the tag family; tag `contract-guard-v3`):
      ORPHAN-TAG (registry-keyed, reverse of TAG-MISSING), CONTENT-DRIFT (STAMPs carrying
      `artifacts` are byte-frozen at their tag; package-style contracts opt out by not
      enumerating), VENDORABLE-UNREGISTERED (`.contract-guard.toml`: `vendorable_roots` —
      commons sets `packages/*` — + `non_contract` + `contract_names`), and `--relax-tags`
      (hook warns mid-bump, CI strict; the hook line updated). scope-guard **v7** (1.4.0,
      tag `scope-v7`): CONTRACTS-VERDICT (per-repo `contracts_verdict_since`; commons cut
      over 2026-07-18, HK-12's own entry retro-carries the line per the HK-6 rollout
      precedent) + UNKNOWN-PREFIX; spec landed as `process/ledger-discipline.md` §7. All
      new rules smoke-tested on synthetic repos (orphan/drift/vendorable/relax;
      verdict-present vs -missing vs pre-cutover; rogue prefix) and both guards run green
      live. Item (5) stamps cut: `contracts/scope/` + `contracts/contract-guard/`
      (drift-checked `artifacts`, first stamp of each family — v1..v6 / v1..v2 recorded
      as frozen pre-stamp history) and package-style `contracts/ui-kit/` +
      `contracts/workbench/` at their existing v1.2 tags (deliberately no byte
      enumeration — HEAD advances between tags; the workbench manifest-fragment +
      runtime-config JSON Schemas are RECORDED OWED at the next workbench bump); registry
      updated incl. the non-candidate record.
      **PROGRESS 2026-07-18 (same day) — item (4) DONE; THE COMMONS BUILD IS COMPLETE.**
      The `contract-triad` pinned block authored (`process/claude-blocks/contract-triad.md`
      — 4 digest invariants: surface-with-the-artifact, pins-complete-and-verbatim,
      contracts-verdict, staleness ladder), pinned into commons' own CLAUDE.md + hashed in
      `.scope-guard.toml`, shipped at **`scope-v7.1`** (blocks version with scope tags per
      HK-2 single-pin; additive — script bytes unchanged from v7, STAMP bumped 7→7.1 in
      the same change). **The product sweeps vendor `scope-v7.1` + `contract-guard-v3` +
      `repin-v1` in one pass each** (v7.1 supersedes the v7 reference above). **ENTRY
      STAYS OPEN until all three product write-backs arrive (owner ruling 2026-07-18)** —
      commons has nothing left to build; what remains is delegation execution + IDs
      written back, per board-as-outbox.
      **CLOSED 2026-07-18 — all three product sweeps executed same-day and independently
      VERIFIED by commons** (vendored bytes cmp'd against tags, block hashes exact,
      configs read, live guard/repin runs, CI checked job-level): satellite **OPS-11**
      (OPS-12 sweep / OPS-13 repin; publish-tool freshness gate; born-stamped clauses;
      filings executed), voice **BUILD-41** (BUILD-42 one-commit sweep / BUILD-43 repin
      with the catalog multi-dest preserved / **DOC-14** `trace-format-v1` doc-canonical
      with a version-triple test; BUILD-44 answered → ASSET-6), bridge **OPS-32** (OPS-33
      repin / OPS-34 workbench-plugin CI job — its first live run failed on exactly the
      new job, then fixed: the gate gates; **VWB-42** cut `device-integration-v1.1`
      STAMP-in-tree, satellite's DES-4 unblocked). **The machinery caught three real
      defects on day one:** the published wake pack already drifted on HF mutable refs
      (voice BUILD-44 addendum), core-py's v1 tag couldn't satisfy a conforming pin
      (→ `core-py-v1.1` packaging correction), and bridge's catalog STAMP bare-name
      `artifacts` create a false-CONTENT-DRIFT trap (bridge **VWB-43** + commons
      **IMPL-8**, Option B, filed at close). Residuals riding other vehicles: workbench
      machine schemas at the next workbench bump (recorded in its STAMP), the
      docs-manifest 10-surface cap at the next docs-manifest bump (voice's live find,
      recorded in the write-back above), Wave-B revival stays available if release
      instrumentation ever wants an org dashboard. docs: none — closure entry; process
      docs landed with the execution items. contracts: none — the close moves no
      surface; every surface cut during execution carried its own verdict
      (repin-v1, contract-guard-v3, scope-v7/v7.1, the four sweep stamps,
      trace-format-v1, device-integration-v1.1, core-py-v1.1).

## IMPL — commons implementation

- [x] **IMPL-1 — Workbench shell v1** (`packages/workbench`): implement
      `docs/design/workbench.md` §3 (the shell: chrome — logo, plugin tabs +
      status badges, locale switch, Material `BugReport` button, reserved auth-guard
      slot; sidebar; content outlet; React 18 SPA on ui-kit tokens) and §4 (the plug-in
      contract as code: `WorkbenchPlugin`/`PageDescriptor`, dormant-gate semantics, the
      dev-phase `file:` consumption wiring — built sibling packages, never TS sources);
      first `workbench-v1` tag. The registry may be a hand-maintained list until two
      real plugins exist (PROD-10 rule). Gates: **ui-kit-v1** (PROD-10 ④ — the shell
      builds ON the tokens); plugin content arrives via voice UI-17 + bridge UI-17
      (their designs feed the registry — no blocking dep for the chrome itself). Write
      APIs stay separately gated on PROD-4's auth decision (the shell ships without
      them). Sprint-02 candidate. Filed at HK-10 — this entry is `workbench.md`'s
      anchoring live task (evidence-anchoring rule, first application).
      **DONE 2026-07-15** — `packages/workbench` = `locveil-workbench` 0.1.0, tag
      **`workbench-v1`**. Landed: the chrome per the ratified wireframe (plugin tabs +
      status dots, RU/EN switch, theme toggle, the Material-glyph BugReport button
      delegating to the active plugin's reportHook, reserved `#wb-auth-slot` +
      `#wb-bottom-slot`); the contract AS CODE (`locveil-workbench/contract`, types
      only — WorkbenchPlugin/PageDescriptor/PluginStatus/ManifestFragment/
      GateDescriptor); **HK-11 implemented natively**: the shell itself externalizes
      the singleton set and ships vendor ESM bundles behind the import map (one react
      by construction — react-dom-client vendor is 4 kB, proving the re-export chain),
      loader with strict-major refuse-and-surface, style inject, dormant slots with
      zero activity + conjunctive gates; `scripts/serve.mjs` (mounts config locations,
      generates runtime-config) + `workbench.config.json` (owner-edited); an in-tree
      demo plugin built exactly as a product repo would (externals + build-emitted
      fragment) proving the loading path. Verified: install 0 vulns · typecheck + lint
      clean · vendor/shell/demo builds · full HTTP path live (runtime-config, fragment,
      entry, styles, vendor, SPA fallback). Honest caveat: browser-render E2E is one
      `npm run serve` away — machine checks stop at the HTTP layer. Consumers next:
      voice UI-17 + bridge UI-18 compile against `locveil-workbench/contract` and the
      demo-plugin build shape. docs: none — the package README is the consumer doc
      (ui-kit precedent).

- [x] **IMPL-2 — scope-guard: UNREFERENCED-evidence check** (`packages/scope-guard`):
      the missing fourth direction of evidence checking (HK-10 ruling 1,
      `process/ledger-discipline.md` §6) — an evidence doc on disk (`[evidence] dirs`)
      that no entry in active+DONE references is an error (config-toggled:
      `unreferenced = "error"|"warn"|"off"`, default warn for consumers, error in
      commons). Ships at the next `scope-vX` tag; consumers adopt on re-pin per §3.
      S/M class. Acceptance: commons run flags a synthetic orphan; the anchored
      `fixture_recorder.md` (HK-10 sweep) passes.
      **DONE 2026-07-15** — scope_guard.py 1.3.0, tag **`scope-v6`** (pyproject aligned
      from a stale 1.0.0 in the same change). The check: an evidence doc on disk whose
      repo-relative path AND basename both appear nowhere in active+DONE →
      `UNREFERENCED evidence` (config `unreferenced = "error"|"warn"|"off"`, default
      warn; commons runs error via `.scope-guard.toml`). Acceptance ran exactly as
      specified: commons clean (the HK-10-anchored `fixture_recorder.md` passes), a
      synthetic orphan flagged as error, clean again after removal.
      `ledger-discipline.md` §3 rule-union + §6 updated to shipped-state. Consumers
      adopt at their next `scope-vX` re-pin (default warn keeps their first run
      honest, not red). docs: none — normative process file updated in place.
- [x] **IMPL-3 — ui-kit: StatusChip recipes must be statically extractable** (filed +
      fixed 2026-07-15 by the voice session at UI-18 intake — first real consumer
      adoption; found-and-fixed, S class, discovery reserve). `status-chip.tsx` built
      its per-variant classes through a **template literal**
      (`bg-[hsl(var(${h})_70%_96%)]` joined at runtime): Tailwind's extractor only
      generates arbitrary-value utilities it can read whole, so (a) the REAL five
      variant recipes were never generated in any consumer — StatusChip rendered
      unstyled — and (b) the `${h}` pseudo-candidate WAS extracted into consumer CSS,
      where the `$` breaks lightningcss minification (voice's vite-8 build failed on
      exactly this; the kit's own vite-6/esbuild pipeline never minified with
      lightningcss, which is why it stayed latent). Fix: one fully-literal class
      string per variant (`recipe: Record<StatusVariant, string>`), values identical
      to the council-ratified recipe. Kit check + build green; dist carries zero `${`
      and all five literal recipes; voice's consumer build is the live verification.
      Sweep: no other template-literal classNames in kit src. Rides the pre-`ui-kit-v2`
      working tree (dev-phase `file:` consumers pick it up on rebuild); next kit tag
      carries it. docs: none — kit
      source fix only (stylebook values unchanged; README consumption prose unaffected).
- [x] **IMPL-4 — ui-kit: Toast + AlertDialog (+ Tooltip adoption unblocked)** (filed
      2026-07-15 by the voice session at UI-19 execution intake — direct operational
      filing). The stylebook §7 names Toast ("no more `window.confirm`"), AlertDialog
      and Tooltip as adopted standards, but `ui-kit-v1` ships only Tooltip — Toast and
      AlertDialog are missing, so consumers cannot comply (voice UI-19 ported with
      `window.confirm` kept, 3 sites; bare `title=` attrs kept). Deliverable: the two
      shadcn-base components themed on the tokens (Toast needs the viewport/provider
      story decided for the PLUGIN context — the shell likely owns the viewport, one
      per page won't do), stories in the workbench, next `ui-kit-vX` tag. First
      consumers: voice **UI-21** (gated on this), bridge at its restyle. S/M class.
      **DONE 2026-07-15** — ui-kit 0.1.1, tag **`ui-kit-v1.1`** (minor tag = additive
      per the contracts convention; plugin `peers: ^0.1` keeps matching — zero
      refuse-churn, the shell loader's 0.x strict-minor rule unchanged). Landed:
      Toast (radix) + Toaster + a module-scope toast bus in `use-toast` — **the
      plugin-context answer falls out of HK-11: the kit is an import-map singleton, so
      the bus is one shared instance across shell and plugins by construction; the
      SHELL renders the single viewport** (workbench App gained `<Toaster/>`, plugins
      only call `toast()`; standalone apps render their own) — plus AlertDialog (full
      shadcn set on the tokens, destructive recipe from the status hues) and the
      feedback stories (RU content). Verified: 0 vulns, check clean, kit build (26 kB),
      storybook build, workbench check + rebuild green (vendor kit bundle 376→412 kB).
      Voice **UI-21** ungated; bridge picks the pair up at its restyle. docs: none —
      stylebook §7 already named both as standards; the package README precedent
      stands.

- [x] **IMPL-5 — the bottom action-bar surface: ActionBar + ActionBarHost** (filed AND
      done 2026-07-15 — consumer-demanded: voice's UI-19 port parked its two colliding
      `fixed bottom-0` bars "waiting on a plugin-contract bottom-slot surface that
      doesn't exist yet"; IMPL-1 had shipped the slot as a placeholder with the API
      deferred to the first consumer — voice became that consumer). Design = the IMPL-4
      pattern reused: `<ActionBar>` in **locveil-ui-kit** registers its children into a
      module-scope bus (ONE instance across shell and plugins through the HK-11
      import-map singleton — no prop drilling, works from any depth of a plugin tree);
      the shell renders the single `<ActionBarHost/>` in its bottom slot (in normal
      flex flow, not fixed); single-occupancy latest-wins with a dev warning; unmount
      clears; standalone apps render their own host (the Toaster symmetry).
      Plugin-owned `fixed bottom-0` is now implementable-around and stays banned
      (stylebook §8). Landed: kit 0.1.2 / tag **`ui-kit-v1.2`** (additive — plugin
      peers `^0.1` keep matching) + workbench App hosts the slot / tag
      **`workbench-v1.1`** (contract addition recorded in workbench.md §4) + a
      BottomActionBar story + the demo plugin now renders an ActionBar + toast ACROSS
      the bundle boundary (the cross-bundle proof, verified in the built artifacts).
      Verified: both packages check + build green, storybook green, serve path intact
      (with the voice plugin mounting from its real dist alongside). First consumer:
      voice collapses ApplyChangesBar + the LocalizationsPage bar into `<ActionBar>` at
      its port — voice ID: **UI-22** (written back 2026-07-15). docs: none — workbench.md §4 amended in place; package READMEs are the
      consumer docs.

- [x] **IMPL-6 — backend targets reach plugins: `PageProps.backends`** (filed AND done
      2026-07-15 — owner-demanded at the first controller run: "how do we tell voice
      and bridge how to reach their backends? IP needs to be passed thru — what about
      ports?"). The contract prose promised per-page backend targets since PROD-24;
      contract-as-code v1 shipped only `locale` — plugins would have fallen back to
      same-hostname defaults and hit the SHELL origin instead of the WB7. Decision
      implemented: **deployment facts live in the owner-edited shell config, never in
      build artifacts** — per-plugin `backends: {"api": "http://<wb7-ip>:<port>"}`
      (absolute origins, IP AND port explicit; WB7 host-network reference: voice
      backend `:8080`, bridge backend `:8000` — verified from both repos' compose
      files), passed config → serve runtime-config → loader → `PageProps.backends`.
      CORS is already `*` on both backends, so the browser talks to the controller
      directly — no shell proxying. Additive contract change (old-built plugins ignore
      the extra prop): tag **`workbench-v1.2`**, 0.1.1; workbench.md §4 amended; the
      demo plugin's About page renders its backends map as the visible proof; config
      merged with the externally-mounted voice AND bridge plugin entries. Consumer
      note (repo-to-repo): each plugin must route its fetches through
      `PageProps.backends` ("api" is the conventional primary key) — relative URLs
      resolve against the shell origin, the HK-11 gotcha class. Voice consumed
      2026-07-15: **UI-23** (written back; synchronous re-point in the page wrapper —
      child-before-parent effect ordering makes a useEffect too late). docs: none —
      workbench.md + package README amended in place.
- [x] **IMPL-7 — the Locveil logo: brand package + ui-kit `<Logo>` + Workbench top
      bar** (filed AND done 2026-07-17 — owner delivered the browser-designed assets:
      mark 2b, nested chevrons/roof + wordmark B, parted-veil `o`; 5 SVGs + usage
      README, drawn in the chrome's icon language, 24px grid/stroke-2). Intake
      analysis found the delivery's two self-flagged guesses were real defects: the
      prescribed structure wiring (`hsl(var(--status-pristine))`) names a nonexistent
      token AND targets a bare-hue token class — invalid CSS, invisible house; the
      correct pair is `--primary` (form was right) + `--muted-foreground`. Fallback
      hexes were ~20 chroma points off-token. **Owner decisions:** (1) canonical home
      is an independently reusable `packages/brand/` (landing page, presentation
      templates consume the raw SVGs) with the ui-kit component as its token-wired
      rendition; (2) fallbacks snapped to exact token renditions — #2073B6/#51A6EC
      accent, #607080/#8794A1 structure (locveil.css rendered to hex; re-snap when
      tokens move); (3) **the Latin wordmark is universal** — no Cyrillic lockup ever,
      closing the delivery's «локвейл» open item; (4) **Workbench top bar carries the
      horizontal lockup** at the width of the right-hand function cluster
      (`height={32}` → 124px ≈ the RU/EN+theme+report cluster), replacing the
      IMPL-1 placeholder gradient square. Landed: `packages/brand/` (5 snapped SVGs +
      corrected README), kit `<Logo>` (`logo.tsx`, variants mark/mark-16/wordmark/
      horizontal/stacked, colors wired internally so consumers cannot mis-wire;
      path data must stay byte-equal to brand SVGs), Identity/Logo stories,
      TopBar swap, stylebook **§10**. Verified live: kit check+build green (30.8 kB),
      workbench check+build green, storybook built and both stories screenshot-proven
      on dark (token-wired accent renders polished-steel bright, correct). Follow-ups
      open elsewhere: favicon adoption (mark-16) and consumer re-vendors ride the next
      ui-kit tag; `site/` consumes brand/ at PROD-9. docs: stylebook.
      **AMENDED 2026-07-17 (owner, off the first live screenshot):** decision (4)'s
      "function cluster" reading was wrong — the owner meant the **plugin-pages
      sidebar**. Landed same day: the top bar gains a dedicated **logo region exactly
      as wide as the sidebar** via one shared `--wb-rail-w` (13rem, shell.css) consumed
      by both the TopBar region and the PluginView aside — same-width BY CONSTRUCTION,
      tabs start flush with the content area. workbench.md §3 wireframe prose amended;
      InChrome story re-mirrored. Verified on the live shell (:6107): region edge ==
      sidebar edge, tab flush with content.
      **AMENDED 2026-07-17 (owner follow-up, same day):** the parked favicon adoption
      executed — brand/ gains a generated `favicon.ico` (16 from mark-16, 32/48 from
      mark, transparent, light fallbacks; regen recipe in the brand README), workbench
      `public/` holds byte-identical copies (favicon.svg = mark-16 verbatim + the ico),
      `index.html` carries both icon links (SVG preferred, ICO fallback), serve.mjs
      MIME map gains `.ico`. Verified live on :6107 — svg 200 image/svg+xml, ico 200
      (correct MIME after the next serve restart). Favicon follow-up hereby closed;
      only consumer re-vendors + site/ adoption remain elsewhere.

- [x] **IMPL-8 — contract-guard v3.1: ARTIFACTS-PATH rule (Option B — owner pick
      2026-07-18 at PROD-26 close)** (`packages/contract-guard`): every entry in a STAMP's
      `artifacts` list MUST be repo-root-relative and resolve at HEAD; a bare/ambiguous
      name FAILS (`ARTIFACTS-PATH`). Kills the false-drift class bridge VWB-43 found at
      OPS-32's first v3 run: v3 resolves artifacts from the repo root, so the catalog
      STAMP's bare `README.md` compares the ROOT readme on both sides (green by luck
      until the next root-README edit → baffling CONTENT-DRIFT on the catalog family) and
      its `catalog.golden.json`/`openapi.json` degrade to CONTENT-UNVERIFIABLE. Option A
      (folder-first resolution) REJECTED — one canonical path form beats two coexisting
      conventions. **Rollout coupling is real and sequenced by design:** bridge's catalog
      STAMP violates the rule and a STAMP is tag bytes, so bridge re-vendors v3.1 only
      AFTER its VWB-43 catalog cut rewrites the three entries as `contracts/catalog/…`
      (from the v3.1 tag its `[[tool]]` manifest nags — correct and advisory); voice and
      satellite stamps are repo-root already and may re-vendor freely; commons' own
      stamps all conform. The legacy singular `artifact` field stays informational —
      never validated (report-protocol's folder-relative singular is frozen history).
      Deliverable: rule + synthetic smoke tests per the v3 pattern, tag
      `contract-guard-v3.1` + STAMP bump in the same change.
      **DONE 2026-07-18 (same day).** Rule shipped exactly as specified: entries must be
      repo-root-relative AND resolve to a file at HEAD; bare names and ghost paths FAIL
      `ARTIFACTS-PATH` (no --relax escape — a shape error is never a mid-bump state); bad
      entries are excluded from the drift comparison so one mistake doesn't cascade.
      Smoke-tested synthetic (bare name / ghost path / drift-still-works / relax-immune);
      the sequencing note aged out before execution — bridge's VWB-43 landed FIRST
      (`catalog-v1.8`, repo-root artifacts, bridge guard at zero warnings), so the
      rollout coupling this entry recorded is already moot and all four repos can take
      v3.1 freely. Poetic acceptance: the first live v3.1 run CONTENT-DRIFT-failed the
      guard's OWN family (edited script, un-bumped stamp) — the bump to `3.1` was forced
      by the very rule it ships. Tag `contract-guard-v3.1`, STAMP + registry in the same
      change, script 3.1.0. docs: none — guard README row + STAMP note updated in place;
      no manifest node covers the guard (integrator surface). contracts:
      contract-guard-v3.1 cut; re-pin owed: voice, bridge, satellite (their `[[tool]]`
      manifests nag from this tag; re-vendor is a one-commit quick task each).

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
- [x] **HK-10 — Evidence anchoring + the commons IMPL prefix** (tenth council topic;
      owner terminal decisions in-session, 2026-07-14 — born-decided, no keeper round:
      both rulings are process-mechanical). **Ruling 1 — evidence anchoring:** every
      design doc AND every review doc must be referenced by at least one ledger entry
      (active or DONE); a doc whose scope is not fully executed needs an OPEN task
      reference; fully-executed docs are anchored by the completion entries that cite
      them. Org-wide; normative: `process/ledger-discipline.md` §6. The product repos
      already run the ledger→doc directions (voice's evidence index, bridge's path-scan
      dead links); the missing doc→ledger direction (a doc on disk that nothing
      references) becomes the scope-guard `UNREFERENCED evidence` check — filed as
      commons **IMPL-2**, ships at the next `scope-vX` tag, consumers adopt on re-pin.
      Commons config extended: `docs/review` joins `[evidence] dirs`. Orphan sweep at
      decision time: ONE true orphan — `docs/design/fixture_recorder.md` (pre-board
      eval-framework design, implemented in `eval/`; anchored henceforth by THIS entry
      as its historical record); all other commons design docs verified anchored.
      **Ruling 2 — the IMPL prefix:** implementation work genuinely on commons
      (regime-2/3 code: `packages/`, `site/`, `eval/`) that is not itself a cross-repo
      initiative gets **IMPL-N** under `## IMPL` on the board ledger (prefix registered
      in `.scope-guard.toml`; IMPL chosen over BUILD/CORE because it collides with no
      product-repo workstream — "commons IMPL-3" is unambiguous cross-repo). PROD stays
      cross-repo initiatives; HK stays councils. First filings: **IMPL-1** (Workbench
      shell v1 — implements `docs/design/workbench.md` §3–4, gated on ui-kit-v1; the
      shell design doc thereby gains its anchoring live task, ruling 1's first
      application) + **IMPL-2** (the guard check above). No repo delegations: the rule
      reaches products mechanically at their next scope-guard re-pin; their existing
      partial forms stand until then. docs: none — normative process file updated in
      place (`ledger-discipline.md` §5–6); CONTRIBUTING's existing ledger-discipline
      row still covers it; no manifest node invalidated.
- [x] **HK-11 — Workbench runtime assembly from multiple repos** (eleventh council
      topic; the sprint-02 planned council — owner directive at sprint planning: "this
      should be a council"; decided 2026-07-15, one round, all three keepers + commons).
      **Decision: native ESM dynamic import + import map** — unanimous; Module
      Federation rejected (couples build tooling across repos, violating the
      vite-majors-per-consumer ruling), iframes/web-components rejected (amputate the
      plugin contract). Mechanics (normative elaboration: `docs/design/workbench.md` §4
      as amended): import-map singleton set frozen at react / react-dom(/client) /
      react/jsx-runtime / react-router-dom (**pinned major 6** — voice and bridge both
      ship 6.30.4 today, zero migration; v7 later = coordinated contract bump) /
      locveil-ui-kit; everything else bundles per-plugin (i18n = plugin-local instances
      + shell locale signal); **build-emitted manifest fragments** in each plugin's dist
      (`{id, version, entry, styles[], peers{}, backendCompat?}`) with the shell config
      carrying locations + dormant slots only (dormant = id+title+gate, NO location,
      zero shell activity; gates support conjunctions); **peer mismatch = strict
      refuse-and-surface** (owner ruling); shell owns style inject/remove + tokens +
      the single preflight; dev loop = build --watch + reload, no cross-bundle HMR, no
      serving pipelines in v1; fragment schema versions with **workbench-vX**; published
      URLs + pinning = productization-step contracts act. **Owner Q&A on record:** "must
      all parties harmonize on one vite version (and other tools)?" — NO: the boundary
      is runtime ESM, bundler-blind; what must match is the runtime peer majors,
      enforced mechanically by peers+refuse; tool convergence stays welcome but never
      contractual (MF was rejected precisely because it would force harmonization).
      **Owner ruling q5: the standalone config-ui app RETIRES at voice UI-17**, with the
      `config-ui-stays-functional` DoD re-anchored to the plugin build in the same
      change. Satellite exception now citable: its panel code lives commons-side, tags
      only (recorded in workbench.md §4). Delegations: voice — UI-17 intake corrections
      (stale `file:` sentence → runtime loading; standalone retirement + DoD re-anchor;
      lib-mode externals; router stays 6) + the **Monaco-CDN side-find** (jsdelivr fetch
      at runtime in a privacy-first product — voice files a local bundle-Monaco task;
      write the ID back). Voice IDs: **UI-17** (all four corrections applied to the
      entry at sprint-02 intake, 2026-07-15) + **UI-20** (bundle-Monaco; CDN loader
      verified live in TomlPreview/DiffViewer at filing). Written back 2026-07-15. Bridge — UI-18 intake refinement
      (externals + fragment emission + single-file bundle) + same-change amendment to
      `../locveil-bridge/docs/design/ui/workbench_split.md` §2.1 — absorbed into the
      already-filed UI-18,
      no new ID expected. Bridge ID: **UI-18** (confirmed at intake 2026-07-15 —
      refinement + the §2.1 amendment landed in one bridge change; intake finding:
      IMPL-1 done discharges UI-18's shell gate, task startable). Satellite — none
      (zero obligations; conditions recorded). IMPL-1 is hereby unblocked. docs: none —
      design record amended in place (workbench.md is not a manifest node; the stylebook
      node's ui-kit surface is unaffected).

- [x] **HK-12 — Convention-enforcement hardening** (twelfth council topic; seeded free-text
      by the owner 2026-07-18 after the PROD-8 core-py cut missed its owned contract surface
      until the owner asked "no new contract?" — a repeated org-wide class, especially around
      pinning new contract versions. Decided 2026-07-18, two rounds, all three keepers +
      commons; execution: **PROD-26**). Diagnosis confirmed by the keepers with paper trails
      in all three product repos (voice: WS protocol shipped long before stamping, catalog
      consumed unpinned until HK-5 forced BUILD-34; bridge: catalog-v1.7 false green,
      docs-manifest tagless 2 days, v1.5/v1.6 re-pin-owed prose rot; satellite: 4 instances
      in 6 days incl. an owned surface consumed by voice before registration, plus LIVE drift
      found during round 2 — its registry still cited contract-guard-v1 while running v2):
      the guards verify coherence of what EXISTS; omissions were invisible; the prose
      conventions weren't in context at the miss. **Decisions:** **(1) Wave A hardening:**
      contract-guard v3 = orphan-tag rule (tag→STAMP, keyed to the `contracts/README.md`
      registry, never tag-pattern sniffing) + content-drift rule (owned bytes at HEAD ≠ bytes
      at the STAMP's tag with no version move ⇒ FAIL) + `vendorable_roots` explicit config
      (empty default; commons sets `packages/*`) + mid-bump tolerance (local hook warns, CI
      strict); scope-guard v7 = required `contracts:` verdict in completion entries (wording
      "created, bumped, or FIRST CONSUMED a cross-repo surface"; owner-side bumps record
      `re-pin owed: <consumers>` — normative; per-repo `contracts_verdict_since`, DONE
      frozen) + unknown-prefix rule (a task id whose prefix isn't in guard config FAILS);
      plus a pinned contract-triad CLAUDE.md block on the block-pin lane. **(2) repin
      promotion (owner amendment, round 2):** voice's `scripts/repin.py` engine is promoted
      to commons `packages/repin/` (tags `repin-vN`, own `contracts/repin/` STAMP from day
      one), `FAMILIES` becomes per-repo TOML config (multi-dest + per-dest conformance
      pointers preserved; cross-repo pin WRITES legal only into commons, co-owned ground);
      tag lookup remote-first via tokenless `ls-remote` with offline fallback (WARN + fetch
      age, never network-required-to-commit); untagged families skip-warn in CI; satellite's
      vendored-tools manifest (`scope-vX`/`contract-guard-vN`/`repin-vN`) rides as a family
      kind. **(3) Severity = bridge's three-case model** (owner pick over voice's
      never-fails ladder and the strict push-gate): staleness fails CI only on
      touch-the-family / release workflows / major-gap (per-repo configurable; satellite
      advisory until FW first light); warn everywhere else; pre-commit warn-only.
      `process/contracts.md` §5 amended in this landing (supersedes "never a push gate";
      public-repo assumption recorded). **(4) Wave B central freshness job DROPPED** —
      repin + the re-pin-owed verdict cover both directions; revivable as one commons
      workflow if release instrumentation wants it. **(5) Procedure skills DEFERRED**
      (bridge showed the miss mode is en-passant riders that skills don't intercept; the
      verdict line fires at every completion regardless). **(6) Contract-candidate sweep:**
      stamp commons-side NOW — `contracts/workbench/` (types + runtime-config schema +
      manifest schema; unanimous top ask — voice's config-ui DoD hard-wires it, bridge's
      plugin consumes it live with zero CI coverage), `contracts/ui-kit/`, STAMP folders for
      the shared tools (scope-guard, contract-guard, repin); voice files the utterance-trace
      format contract task (voice-owned, doc-canonical); satellite's DES-5 + D-16 API
      surfaces get born-stamped clauses; eval DEFERRED to its first hermetic gate (live
      co-dev is the designed asymmetry); NON-candidates on record: the raw MQTT topic tree
      (golden holds zero topic strings by design; canonical REST already pinned via
      openapi), pymotivaxmc2 (PyPI pinning suffices), brand (no second external consumer),
      `meta/locveil` (stays inside device-integration), `components/locveil_*` (internal).
      Side-finds greenlit round 1: satellite executes two repo-to-repo filings (voice
      wake-pack-v1.x bump confirmation; bridge device-integration-v1.1 request) + its
      registry-README drift one-liner. Delegations + write-backs: **PROD-26**. docs: none —
      normative change landed in `process/contracts.md` §5 (process file, not a manifest
      node); the dossier is ephemeral by convention. contracts: none — decision entry;
      §5 is process text, no versioned surface moved (execution surfaces ride PROD-26).
