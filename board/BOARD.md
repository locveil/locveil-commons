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
- [ ] **PROD-4 — Normative ops spec** (D-12) in `process/`: the converged pattern (sdcard
      clone update-time-only, `/mnt/data/<name>-config`, repo-owns-config rsync, `.env`
      secrets, systemd oneshot `RequiresMountsFor=/mnt/data` ONLY, GHCR pull-not-build, log
      rotation, 127.0.0.1 healthchecks, start-period > fleet boot) + a conformance checklist.
      Shared *scripts* only at the third consumer (rule of three). Delegates on completion:
      voice BUILD-18 (narrowed) + bridge OPS-15.
- [ ] **PROD-5 — Shared CLAUDE.md invariant blocks + drift guard** (D-12) in `process/`:
      normative blocks, per-repo copies between markers, guard script failing on divergence;
      same-slug renames (`config-master-canonical` splits). Drift inventory:
      `docs/design/productization.md` §2. Delegates: voice BUILD-23 + bridge OPS-16.
- [ ] **PROD-6 — Problem-report policy spec** (D-12) in `process/`: envelope, redaction
      regex, rate limits, retention, labels — one normative spec consumed by both collectors
      and the private `wb-user-reports`. Spec-level unification only.
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
      `process/council.md` (+ satellite-keeper when that repo exists). First live topic will
      shake it down.
- [>] **PROD-13 — Ledger & journal discipline harmonization + scope-guard** (HK-1, the
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
      - **Delegation → locveil-voice**: consume scope-guard at the pinned tag `scope-v1` —
        (1) vendor `packages/scope-guard/scope_guard.py` + author `.scope-guard.toml`
        (start from `packages/scope-guard/examples/voice.scope-guard.toml`, verified green
        against the voice tree 2026-07-11); (2) retire `scripts/check_scope.py` and
        re-point the `ledger-guard` job + `ledger` paths-filter in
        `.github/workflows/ci.yml`; (3) install the committed-hooks mechanism (`hooks/`
        + `core.hooksPath`) running `--check` pre-commit; (4) update invariant text
        (`single-task-ledger`, `one-active-journal` in CLAUDE.md; RELEASE_PLAN.md gate
        wording) in the SAME change as the cutover; (5) adopt DONE-ledger rotation
        (RELEASE_PLAN_DONE.md is at ~4.3k lines) and run the overdue journal rotation
        (1510 > ~1500 high-water) via `--rotate`; (6) keep the required-task-tags rule ON
        (`[release]`/`[deferred]`). Cutover proof: vendored tool green before deleting the
        local script. Verify per `task-start-reconciliation`, file a local ID, write it
        back here. Voice ID: _pending_.
      - **Delegation → locveil-bridge**: same shape at tag `scope-v1` — (1) vendor the
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
        _pending_.
