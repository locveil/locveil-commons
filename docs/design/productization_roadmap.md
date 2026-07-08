# Productization roadmap — from eval-commons to domovoy-commons

**Status: RECORD + ROADMAP, written 2026-07-08 at the joint productization session (voice-side
BUILD-20, committed `wb-mqtt-voice@7214eb7`). The normative decision record is
`../wb-mqtt-voice/docs/design/productization.md` (D-1..D-12, user-approved) — this document
summarizes it, adds the name-sweep results, the full cross-repo task manifest, and the phased
path to the desired end state: cross-repo design sessions running FROM this repo. When the
restructuring lands (voice BUILD-21), this file seeds `board/` and the decision record migrates
here; until then this repo remains plain eval-commons and nothing else changes.**

---

## 1. What was decided (session summary, 2026-07-08)

Two products — **Irene / wb-mqtt-voice** (the voice assistant) and **wb-mqtt-bridge** (the
smart-home hub) — are valuable standalone and contract-coupled (the canonical `DeviceCommand`
boundary, ARCH-26), which makes a joint product possible without merging code. The joint
product: **a fully local, privacy-first, Russian-first voice-controlled smart home.**

### D-1 — Product name: Domovoy (Домовой)
The house spirit who lives in the house, guards it, and never leaves — the privacy story in
one word. Wake-word personas (Ирина, Валера, Наташа) are *voices of* the product, not the
product. Runners-up recorded: Penates, Terem, Ochag. **Sweep results and the open lock
decision: §2 below.**

### D-2/D-3 — ONE umbrella repo = THIS repo, renamed `domovoy-commons`
No repo sprawl (no separate ui-kit / contracts / ops repos). Target layout:

```
domovoy-commons/
├── board/            # cross-repo initiative ledger (PROD-N)      — regime 3
├── process/          # ops spec, shared CLAUDE.md invariant blocks, report policy spec
├── docs/design/      # cross-repo design docs
├── eval/             # the test framework, as today (own package + tag)
├── packages/core-py/ # shared runtime code: logging, dynamic loader — regime 2
├── packages/ui-kit/  # stylebook + shared React components (next release)
├── contracts/        # pins of product-owned artifacts + crossover fixtures — regime 1
└── site/             # landing page (GitHub Pages)
```

Three ownership regimes keep one repo safe:
1. **Generated contracts** — owned by a product repo; commons holds only pins. Catalog/openapi
   stay bridge-owned; the WS wire protocol stays voice-owned (`websocket-api.md`);
   `crossover_fixtures.json` is genuinely bidirectional and stays co-owned here.
2. **Co-owned shared code** — commons owns; products pin versions. The eval framework + the
   D-8 extractions. Ownership FLIPS on extraction (voice stops owning the loader, becomes
   consumer #1).
3. **Process & product artifacts** — commons owns: board, ops spec, invariant blocks, suite
   manifests, landing page.
Packages are versioned separately via prefixed tags (`eval-vX`, `core-py-vX`, `ui-kit-vX`),
each with its own `pyproject.toml`/`package.json` — a test-framework tweak never forces a
version event on a production dependency.

### D-4/D-5 — Cross-repo idea discipline: PROD tasks + board-as-outbox
`design-then-implement` lifted one level. The commons gets a light ledger (`PROD-N` in
`board/`), journal, memory dir; **cross-repo design sessions run from this repo** (its future
CLAUDE.md instructs loading sibling context). Placement rule: a design defining a
concept/contract both products consume lives HERE; a design whose primary artifact is one
repo's code lives in that repo, even when the session ran here. On completion a PROD task
**delegates**: the delegation text is committed in the board entry (co-owned ground — being
writable by both sides is this repo's purpose), the receiving repo pulls it, verifies per its
own `task-start-reconciliation`, files a local ID, writes the ID back. **This retires the
uncommitted-sibling-filing mechanism** (fragile: invisible until noticed, lost to `git clean`).
The board entry lists delegated IDs but never asserts their status — per-repo ledgers own
status. Recorded stress test for a future PROD design: **Home Assistant support in parallel to
Wirenboard** — if the canonical DeviceCommand contract survives HA unchanged, voice gets zero
tasks (HA = a new driven adapter behind the bridge's ports + at most a contract minor bump);
if voice needs changes, the contract leaked WB-specifics. The delegation pattern is itself an
architectural finding.

### D-6/D-7 — `domovoy-satellite`: a THIRD product repo, starting now
The ESP32 satellite is a product, not a library: PCB (SKIDL/KiCad) + firmware
(ESP-IDF/PlatformIO) + enclosure, hardware-revision cadence unrelated to software tags,
gerber/binary artifacts. Own CLAUDE.md (same invariant family, heavy `HW-GATED` use), ledger,
journal. The satellite-side design corpus moves out of voice; **the voice repo's top-level
`ESP32/` tree is outdated and gets DELETED, not migrated** (user verdict). The WS protocol doc
STAYS voice-owned; the satellite pins it by version — same pattern as voice pinning the bridge
catalog. Common firmware/PCB pieces across future satellite variants live within the satellite
repo (they graduate to commons only if a second firmware consumer ever exists).

### D-8/D-9 — Shared code: rule of two; UI = two apps + shared kit
Code moves into `packages/core-py` only when the second consumer is real and committed.
First two extractions (both filed): the **dynamic code loader** (voice owns today, bridge
wants it) and the **logging scheme** (startup-rollover + timed-rotation family that exists
twice by hand-copy: bridge OPS-12 → voice BUG-30 "ported verbatim" — the drift pattern this
design retires). The rest surface naturally. **`ui-kit`** (stylebook + shared React
components) enters as a commons npm package next release, consumed by both config UIs as a
versioned dependency; it gets its own repo only if it ever needs its own cadence. **Config UI
product decision: two apps + shared kit now**; the kit's component boundaries keep a future
one-shell-with-plugins configurator reachable — but no plugin framework before two real
plugins exist.

### D-10 — Work coordination: the per-repo ledgers STAY
GitHub Projects and Jira explicitly rejected: the ledger system's properties — in-context
every session, greppable, machine-guarded (`check_scope.py`), offline, versioned with the code
— are exactly right for a one-person + Claude shop; external trackers coordinate *people*.
The only missing piece was the cross-repo layer — solved by the D-4/D-5 board.

### D-11 — Releases: per-component semver + calver suite manifests
Each component keeps its own semver + changelog (voice 15.x, bridge toward 1.0, contract
explicitly semver-ish: additive = minor / breaking = major; ui-kit + firmware when they
exist). A **suite release is a tested-together statement, not a lockstep version**: a manifest
here — "Domovoy 2026.07 = voice vX + bridge vY + contract vZ + images …" — gated on this
repo's cross-suites passing against exactly those pins. **Contract distribution formalized:**
the bridge tags `contract-vN` releases with artifacts attached (bridge VWB-29); the voice
re-pin becomes `make repin CONTRACT=vN` + a staleness gate that goes red when the pin trails
the newest tag (voice BUILD-24) — staleness becomes a machine failure, not a memory note.

### D-12 — Ops spec, invariant blocks, landing page, report policy
- **Normative ops spec** in `process/`: the pattern both repos converged on by hand-copy
  (sdcard clone update-time-only, `/mnt/data/<name>-config` runtime tree, repo-owns-config
  rsync, `.env` secrets, systemd oneshot with `RequiresMountsFor=/mnt/data` ONLY, GHCR
  pull-not-build, log rotation, 127.0.0.1 healthchecks, start-period > fleet boot) written
  once + a conformance checklist per repo. Shared *scripts* only at the third consumer
  (satellite / Pi image — rule of three).
- **Shared CLAUDE.md invariants**: normative blocks in `process/`; each repo keeps its copy
  between markers (CLAUDE.md must live in-repo to be in-context) with a drift-guard script
  failing when a marked block diverges. Per-repo invariants stay outside markers;
  same-slug-different-meaning cases get renamed apart (`config-master-canonical` means a
  single canonical TOML in voice and the-JSON-tree-is-canonical in the bridge — it splits).
  Verified drift inventory: voice `productization.md` §2 (also records a correction — journal
  direction is NOT drift; both repos are newest-on-top).
- **Landing page** = `site/` (GitHub Pages): the joint story, per-product blurbs +
  screenshots, honest quickstart ("you need a Wiren Board 7, a mic, …"), routing into
  per-repo docs. **Narrative + routing ONLY** — never duplicates reference material the
  per-repo docs own. The suite manifest is its "current release" section. Blocked only on the
  name lock (§2).
- **Problem-report policy spec** in `process/`: envelope, redaction regex, rate limits,
  retention, labels — today mirrored in prose across `problem_reports.md` (voice) and
  `problem_reports_bridge.md` (bridge). One normative spec; `wb-user-reports` stays a separate
  PRIVATE repo (a privacy boundary, not an organizational one) and consumes it, as do both
  collectors. Spec-level unification only — no shared Python/TS library at household scale.

---

## 2. Name availability sweep (run 2026-07-08)

| Check | Domovoy | Penates (runner-up) |
|---|---|---|
| PyPI base name | **TAKEN** — `domovoy` v0.11.0 = carlos-sarmiento/domovoy, an ACTIVE Home-Assistant automation framework (AppDaemon-like, running homes since 2023, HA community thread) — **same niche** | TAKEN but dead — `penates` v0.0.0, "Add your description here" placeholder, last upload 2024-12-12 (PEP-541 reclaim plausible) |
| PyPI prefixed (`*-core`) | `domovoy-core` FREE | (unchecked; base squat is inert) |
| npm | `domovoy` FREE | `penates` FREE |
| crates.io | FREE (404) | (unchecked) |
| GitHub user/org | `domovoy` TAKEN (repos live under `droman42/*` anyway) | `penates` TAKEN (same mitigation) |
| GitHub repo-name collisions | carlos-sarmiento/domovoy ★41 (the HA framework) + small unrelated | tiny + unrelated (inventory system ★0, CLI web UI ★2) |
| Domains (RDAP: 200=registered, 404=likely free) | `domovoy.com` REG · `domovoy.dev` REG · **`domovoy.io` likely FREE** · `getdomovoy.com` FREE | **`penates.io` likely FREE** · `penates.dev` REG |

**Assessment.** Everything Domovoy mechanically needs is available: `droman42/domovoy-*`
repos, `domovoy-core`/`domovoy-eval`/`domovoy-ui-kit` on PyPI, `domovoy` on npm and crates,
`domovoy.io`. The one real issue is **mindshare, in exactly the wrong niche**: an active
"Domovoy" HA automation framework holds the PyPI base name and HA-community presence — and
this product plans HA support (D-4). Searches like "domovoy home assistant" will collide.
Penates' collisions are negligible (a dead placeholder + unrelated micro-repos).

**Recommendation (Claude): keep Domovoy**, with two disciplines: (1) never publish a bare
`domovoy` package — always `domovoy-*`; (2) the landing page's search anchor is "Domovoy
smart home", and the HA-support docs must name-distinguish early ("not related to the Domovoy
HA automation framework"). The colliding project is a developer *library*; this is a consumer
*product* with hardware + voice identity. Pivoting to Penates is free until anything ships —
**the lock is the owner's call (BUILD-21 step 1).**

---

## 3. Task manifest — everything filed 2026-07-08, by repo and purpose

### wb-mqtt-voice (committed, `7214eb7`) — all `[deferred]`, nothing blocks the v15.0.0 tag

| Task | Purpose | Gates |
|---|---|---|
| **BUILD-20** ✓ DONE | The productization design itself (`docs/design/productization.md`, D-1..D-12) | — |
| **BUILD-21** | Commons bootstrap: name lock (sweep §2 done — decision pending), `gh` rename eval-commons → domovoy-commons (OWNER ACTION), restructure to the D-2 layout, bootstrap `board/` + commons CLAUDE.md, transplant seed backlog, re-point voice `eval/` refs | name lock |
| **BUILD-22** | domovoy-satellite bootstrap (repo creation = OWNER ACTION) + ESP32 estate relocation out of voice; DELETE the outdated `ESP32/` tree; re-home ARCH-22 design intent | can run parallel to BUILD-21 |
| **BUILD-23** | Shared CLAUDE.md invariant blocks + drift guard — voice-side adoption (markers, guard beside check_scope, same-slug renames) | BUILD-21 + the commons PROD task authoring the blocks |
| **BUILD-24** | Scripted contract re-pin (`make repin CONTRACT=vN`) + staleness gate | bridge VWB-29 |
| **ARCH-42** | DESIGN: extract the dynamic code loader → `packages/core-py` (voice = consumer #1) | BUILD-21 |
| **ARCH-43** | DESIGN: extract the logging scheme → `packages/core-py` (retires the BUG-30/OPS-12 hand-copy pair) | BUILD-21 |
| **BUILD-18** (narrowed) | Voice-side ops-spec conformance pass, once the D-12 spec exists | the commons ops-spec PROD task |

### wb-mqtt-bridge (filed UNCOMMITTED — maintainer verifies + accepts; `check_scope.py` green with them)

| Task | Purpose | Gates |
|---|---|---|
| **VWB-29** | Tag `contract-vN` releases + attach `contracts/` artifacts — the machine-readable upstream for voice BUILD-24 | — |
| **CORE-7** | Adopt the shared dynamic loader from core-py (driver/module loading; hexagon placement verified at start) | voice ARCH-42 + BUILD-21 |
| **OPS-14** | Adopt the shared logging package, replacing the OPS-12 local implementation (VWB-28 evidence-glob compat is design input) | voice ARCH-43 + BUILD-21 |
| **OPS-15** | Bridge-side ops-spec conformance (the REL-2 layout is the spec's reference pattern — expected mostly no-op, naming dialects real) | the commons ops-spec PROD task |
| **OPS-16** | CLAUDE.md invariant blocks + drift guard in the `ledger-guard` CI job; `config-master-canonical` split | same as BUILD-23 |

Plus `docs/design/productization_bridge.md` (uncommitted) — the bridge's side of the shared
spec, deliberately the LAST filing to use the uncommitted mechanism (D-5 retires it).

### This repo (eval-commons → domovoy-commons) — seed backlog for `board/` (become PROD-N at BUILD-21)

1. Name lock (sweep done, §2 — owner decision) → unblocks landing page.
2. Rename + restructure + consumer re-points (executed by voice BUILD-21).
3. Board bootstrap: PROD ledger conventions, commons CLAUDE.md with the D-4/D-5 session
   discipline; migrate `productization.md` here with a pointer left in voice.
4. Normative ops spec (D-12) → delegates voice BUILD-18-narrowed + bridge OPS-15.
5. Shared CLAUDE.md invariant blocks + drift guard → delegates voice BUILD-23 + bridge OPS-16.
6. Problem-report policy spec (D-12).
7. Contract tagging + scripted re-pin pair (D-11) → bridge VWB-29 + voice BUILD-24.
8. core-py package bootstrap; loader + logging extraction designs (voice ARCH-42/43) →
   bridge CORE-7 + OPS-14 adoptions.
9. Landing page in `site/` + the first suite manifest (D-11/D-12).
10. ui-kit package + stylebook (D-8/D-9, next release).
11. FUTURE PROD design: Home Assistant in parallel to Wirenboard (D-4's stress test).

---

## 4. The roadmap — how to arrive at "designing from the commons"

**Phase 0 — Ship release 1 first (now → both tags).** Nothing productization-related blocks
or precedes it. Voice: ARCH-25 WB7 bring-up (starts 2026-07-09) → REL-3 → tag v15.0.0.
Bridge: VWB-13 → REL-3 → REL-4 → tag. One independent step can happen any time: a normal
bridge session verifies + accepts the five intake tasks.

**Phase 1 — Name lock + commons bootstrap (voice BUILD-21; the phase that creates the
desired state).**
1. OWNER: lock the name (§2 — keep Domovoy per recommendation, or pivot to Penates).
2. OWNER: `gh repo rename` eval-commons → domovoy-commons; optionally register `domovoy.io` /
   `getdomovoy.com` (both looked free 2026-07-08 — domains move fast, re-check at purchase).
3. OWNER (cheap, do with #2): rename the local sibling dir to match
   (`mv ~/development/eval-commons ~/development/domovoy-commons` + `git remote set-url`).
4. Claude session IN THIS REPO: restructure to the D-2 layout; write the commons CLAUDE.md —
   the PROD ledger conventions, the board-as-outbox mechanics, the placement rule, the
   instruction that cross-repo sessions load sibling CLAUDE.md/memory as needed; bootstrap
   `board/` from §3's seed backlog; document the per-package tag scheme; migrate
   `productization.md` here (pointer left in voice).
5. Voice session: re-point `eval/` refs (BUILD-21's tail) — `file://` paths, `pip install -e`,
   eval/README, CLAUDE.md Testing section.
6. Bridge session: same re-point, arriving as the first board-as-outbox delegation.

**→ Desired state reached at the end of Phase 1:** you `cd ~/development/domovoy-commons`,
start a session, and any cross-repo idea becomes a PROD design task with committed
delegations — exactly how today's session ran, but with a permanent home, a board, and no
uncommitted filings.

**Phase 2 — Satellite bootstrap (voice BUILD-22; parallel to Phase 1).** OWNER:
`gh repo create droman42/domovoy-satellite` (sibling working copy, never a subdir). Claude:
CLAUDE.md + ledger + journal skeleton; relocate the design corpus from voice; delete the
`ESP32/` tree; re-home ARCH-22's remaining intent; first satellite ledger tasks (PCB
direction/SKIDL evaluation, firmware architecture vs the pinned WS protocol).

**Phase 3 — First PROD wave (from the board, in rough dependency order).**
Contract tagging pair (VWB-29 → BUILD-24) → ops spec (→ BUILD-18-narrowed + OPS-15) →
invariant blocks + drift guard (→ BUILD-23 + OPS-16) → core-py bootstrap + the two
extractions (ARCH-42/43 → CORE-7 + OPS-14) → report policy spec → landing page + first suite
manifest ("Domovoy 2026.xx" naming starts here). Next release adds ui-kit; the HA design
waits until it's wanted.

**Standing owner-action checklist distilled:** (a) name lock; (b) repo rename + local dir
rename; (c) `gh repo create domovoy-satellite`; (d) optional domain registration; (e) one
normal bridge session to accept the intake five.
