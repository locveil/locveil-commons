# Locveil board — DONE ledger

Completed `PROD-N` / `HK-N` entries, MOVED here from `BOARD.md` on close (same change as
the journal entry — `process/ledger-discipline.md`). Frozen history: entries are never
re-edited; delegated IDs listed inside them are pointers, never status assertions.

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
