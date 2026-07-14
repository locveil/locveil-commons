# sprint-01 — plan

Planned 2026-07-14 via `/sprint` (PROD-23 machinery, first run; convention
`process/sprints.md`). Three rounds: scoping + two selection rounds, all three keepers in
contributor mode. This file lists task IDs, classes and budgets — **it never asserts a
task's status**; per-repo ledgers own status.

## Header

- **Theme:** ui-kit package + stylebook (PROD-10) + first-sprint calibration
- **Dates:** owner stated none — capacity is session-denominated (opened 2026-07-14)
- **Budgets:** 12 owner-attended sessions · discovery reserve 30% (3.6) · 1 close-deploy
  slot pre-reserved · **usable 7.4** · bench/rack slots **0**
- **Excluded repos:** none
- **Selected:** 7.3 session-equivalents · bench 0/0

## Decisions at planning

1. **OPS-13 × ui-kit ordering** (the HK-7 must-not-run-twice note): OPS-13 runs early
   this sprint; ui-kit ④ targets eslint-9 flat config + vite 6 from day one. The
   migration runs once. (Round-1 conflict card.)
2. **CORE-8** rides with PROD-4 — the PROD-4 council is the natural sprint-02 opener;
   no standalone execution this sprint. (Round-1 conflict card.)
3. **UI class naming** (owner, round 2): **operations** (controller-deployed — bridge
   `ui`) / **workbench** (workstation-deployed — the **Locveil Workbench**: one shell,
   repos plug in panels). The shell council ratifies and uses these terms.
4. Style council budgeted at 2 rounds; a 3rd round, if needed, draws on the discovery
   reserve (two councils in one sprint make owner review latency the binding resource).

## Per-repo shippable definitions (§6, keeper-verified at planning)

- **voice** — `ci.yml` green (ledger-guard scope-v5 · contract-guard-v2 · py-dev-gates:
  pyright 0 / 10 import contracts / lock, config, donation + armv7 torch-free gates ·
  unit suite + offline smoke e2e · config-ui check+lint+build+tests) + multi-arch GHCR
  dispatch path + WB7 `git pull && ops/update.sh` + manual `/health` smoke. Caveat on
  record: `update.sh` has no built-in health smoke; `/health` is liveness-only until
  ARCH-45.
- **bridge** — import-linter 6/6 · pyright 0 · pytest 725 · `ui` check+build
  (config-ui-stays-functional) · scope-guard `--check` · contract-guard v2 (incl.
  TAG-MISSING) · docs-manifest test · both armv7 GHCR images build · WB7 `update.sh`
  path.
- **satellite (pre-first-light)** — all four guards green (scope-guard · contract-guard
  v2 · esp32-site 9/9 markers · docs-manifest) + provisioning surface intact. Verified
  green at planning.

## Selected rows

### commons

| ID | gist | class | cost | group |
|---|---|---|---|---|
| PROD-10 ① | extraction: implicit design system from the two shipped UIs + remote scan → token inventory + divergence list (incl. tooling prep) | L | 1.0 | PROD-10 backbone |
| PROD-10 ② | style council — rendered A/B preference elicitation, 2 budgeted rounds | council | 1.0 | PROD-10 backbone |
| PROD-10 ③ | stylebook: tokens file + stylebook (docs-manifest node) + `ui-style` skill | L | 1.0 | PROD-10 backbone |
| PROD-10 ④ | `packages/ui-kit` bootstrap on the tokens, Storybook workbench, `ui-kit-v1` tag; eslint-9/vite-6 toolchain (decision 1) | L | 1.0 | PROD-10 backbone |
| PROD-24 (split) | deploy-split design doc: classify every UI surface into operations vs workbench; reconcile satellite D-17 | M | 0.5 | PROD-24 |
| PROD-24 (council) | shell council: Workbench wireframe + plug-in contract + naming ratification; design only (no plugin framework before two real plugins) | council | 0.5 | PROD-24 |

### locveil-voice

| ID | gist | class | cost | group |
|---|---|---|---|---|
| TEST-20 + BUG-42 | recorder-declined test flake, both modes | M batch | 0.3 | travels-with (same test file) |
| QUAL-78 | filter 2xx /health probes from access log; ships in the close-deploy image | S | 0.1 | — |

### locveil-bridge

| ID | gist | class | cost | group |
|---|---|---|---|---|
| OPS-13 | UI toolchain migration eslint 8→9 flat + vite 6; runs early (decision 1); absorbs UI-8 at intake | L | 1.0 | — |
| (files at intake) | UI surfaces intake/classification design: the four ID-less `docs/planned/` pages + `ui/` into operations/workbench + ui-kit adoption plan — bridge files a local ID, write-back to PROD-24 | M–L | 0.5 | travels-with PROD-24 (split) |
| (files at intake) | PROD-19 twin: locveil-reports intake-consolidation task — the board write-back slot has been empty since HK-7 | S | 0.1 | — |

### locveil-satellite

| ID | gist | class | cost | group |
|---|---|---|---|---|
| OPS-1a → **OPS-7** | model-pack publish flow (hash-at-publish vs wake-pack STAMP) — the zero-dependency half of OPS-1, split at intake per §4. *Intake note 2026-07-14: filed as satellite **OPS-7** — letter-suffix IDs are unparseable by scope-guard (numeric-only regex); §4 amended accordingly. OPS-1 narrowed to the firmware half, dormant until FW-1.* | M | 0.3 | — |

## Visibility rows (zero cost)

- **bridge DRV-37 + VWB-39** — BLOCKED; unblock: satellite's first conforming descriptor
  reaches the bridge (PROD-20 chain).
- **bridge DRV-38 [P1] + HW queue** (DRV-32/6/15/16, CORE-1, SCN-13, UI-15) — HW-GATED;
  DRV-38 heads the bench queue of the next HW-bearing sprint.
- **satellite FW-1** — class no-data (legal); unblock: DES-3 done + first board exists +
  a bench slot.
- **PROD-20** — satellite first-light chain; HW-GATED, no timing asserted.

## Cross-sprint declarations (§7)

- **voice ui-kit adoption + UI-16** — travel together (touch config-ui structure once);
  head sprint-02 riding `ui-kit-v1`; the trailing pin is version-tolerable by contract
  design. Voice files local IDs at intake (none exist yet — contributor-round finding).
- **bridge `ui` ui-kit adoption** — sprint-02, after OPS-13 + `ui-kit-v1`.
- All HW-GATED rows above (bench budget 0 — no pull-in offered).

Each carries a mandatory zero-cost carry-over row in the sprint-02 plan.

## Bench-slot ledger

0 budgeted · 0 consumed. Pre-booked ask for the next HW-bearing sprint: bridge DRV-38
rack replay first; satellite FS90 rail-isolation check + deck `[VERIFY]` measurements
(dossier-embedded, not ledger rows — bench planning can't be read off the satellite
ledger alone).

## Side-finds (contributor round; review-then-remediate — delegations to pull at intake, never fixed silently)

- **voice:** `ci.yml` step-name prose cites scope-v3 / contract-guard-v1 (actual: v5 /
  v2) — S-chore batch candidate; BUILD-14 task text still says `wb-user-reports`
  (renamed to `locveil/locveil-reports` 2026-07-11); config-ui's eslint-8 exposure to
  the ui-kit toolchain was unrecorded anywhere — now scoped via the cross-sprint
  adoption declaration.
- **bridge:** UI-8/OPS-13 duplicate scope — fold UI-8 at OPS-13 intake; OPS-13's
  ordering constraint lived only on the board — annotate at intake (decision 1 supplies
  the ruling); OPS-14/CORE-7 still cite long-landed BUILD-21 as gate — narrow the prose;
  WB7 redeploy after OPS-26 (retained `meta/driver` flip) is unrecorded — the
  close-deploy slot verifies it.
- **satellite:** D-17 deliberately makes cert approval a root CLI, not a page — the
  PROD-24 split design must reconcile any "satellite workbench panel" with it (gated on
  DES-5); DES-4's bridge `device-integration-v1.1`-tag wrinkle is live (only v1 exists);
  `process/sprints.md` §6's satellite post-DES-3 line is vacuous between DES-3 close and
  first FW code — commons doc finding, becomes scope only when a ledger task declares it
  (matters only if DES-3 is selected in a future sprint).

---

# sprint-01 — close (2026-07-14)

Closed the same day it was planned. Verification read-only per convention §6/§8; the
sprint file still asserts no task's status — verdicts below cite repo evidence.

## Shippable verdicts (repo@sha + one line)

| repo | @sha | verdict |
|---|---|---|
| commons | `2872628` | ✅ scope-guard + contract-guard green on every commit today (the close commit follows this sha); both sprint deliverable sets landed (PROD-24 arc, PROD-10 ①–④ + `ui-kit-v1` tag) |
| voice | `3bf39ce` | ✅ clean tree; vendored guards green at pinned tags (scope-v5, contract-guard-v2); **repin-check green — all pins @ owner-newest incl. catalog-v1.7**; suite 1415/7 journal-evidenced; TEST-20+BUG-42, QUAL-78 DONE. Caveat: QUAL-78's fix is not yet in a published image — rides the close-deploy dispatch |
| bridge | `5da5c96` | ✅ clean tree; guards green (contract-guard byte-identical to v2); `ui npm run check` green live; heavy gates (import-linter 6/6 · pyright 0 · pytest 725) CI-evidenced and unbroken since. UI-17 DONE (`docs/design/ui/workbench_split.md`; spawned UI-18/CORE-12/DOC-17), OPS-13 DONE (UI-8 absorbed), OPS-28 filed (posture decided jointly with voice BUILD-14, deliberately parked). Caveats: last armv7 UI image predates the vite-6 toolchain; post-OPS-26 WB7 redeploy still unrecorded |
| satellite | `91e7bee` | ✅ clean tree; **all four guards green**, esp32-site v1 surface intact (9 markers); OPS-7 DONE (verified live against HF upstream; ssh branch honestly flagged as awaiting a controller session); OPS-1 narrowed/dormant, DES-5 expanded, OPS-6 earmarked |

## The close-deploy slot (owner op — SCHEDULED, not run; deployable ≠ deployed)

1. **voice**: multi-arch image dispatch (bakes QUAL-78) → WB7 `git pull && ops/update.sh`
   → manual `/health` smoke.
2. **bridge**: image dispatch (bakes the vite-6 UI) → WB7 `update.sh` → flips the OPS-26
   retained `meta/driver` topic and finally puts the redeploy on the journal record
   (the planning side-find, discharged here).
3. Each repo journals its own deploy line at its local close (convention §8 — no
   coordinator-stamped refs).

## Row outcomes

All 14 selected items landed (13 executed + OPS-28 whose deliverable WAS the filing).
Incident displacements: none. Reserve spent: **0.1 of 3.6** (the split-ID convention
fix). Bench: 0/0.

## Carry-over rows → sprint-02 plan (mandatory, zero-cost)

- voice **UI-17** (config-ui → Workbench plugin + ui-kit adoption) + **UI-16** — travel
  together (declared at planning).
- bridge **UI-18** (Bridge Workbench plugin package, read-only cut) + **CORE-12**
  (staged-write API — PROD-4-gated, per the binding condition).
- HW-GATED standing set: satellite FW-1 · bridge DRV-38 + queue · PROD-20 chain.
- Owner-announced (not yet filed): the bridge remote-wireframe/layout session (operations
  UI re-zoning + D10 fluid implementation).
- Discovered-and-filed, for sprint-02 selection: **IMPL-1** (Workbench shell — all gates
  green) · **IMPL-2** (scope-guard UNREFERENCED check) · voice **ARCH-51** · bridge
  **DOC-17** · the **PROD-4 council** (now load-bearing: CORE-12 + auth + ARCH-45 wait
  on it).

# sprint-01 — review (realized vs planned)

| class | planned (rows · s-e) | landed | discovered in-window |
|---|---|---|---|
| S | 2 · 0.2 | 2 · 0.2 | +1 executed from reserve (split-ID fix, 0.1); +5 out-of-sprint S executions (pre-sprint delegations BUILD-37, DOC-13, DOC-16, OPS-27, OPS-5 — PROD-22/23 lineage) |
| M | 3 · 1.1 | 3 · 1.1 | +filed: voice ARCH-51, IMPL-2 |
| M–L | 1 · 0.5 | 1 · 0.5 | UI-17 spawned UI-18 + CORE-12 + DOC-17 |
| L | 4 · 4.0 | 4 · 4.0 | +filed: IMPL-1 |
| council | 2 · 1.5 | 2 · 1.5 (both converged in budgeted rounds) | +HK-10 born-decided (≈0) |
| XL / bench | 0 | 0 | — |
| **total** | **7.3** | **7.3 (100%)** | ≈9 new items filed, 0.1 s-e reserve spent |

## Calibration findings (feeds sprint-02 planning)

1. **Relative costs were exact**: every row landed at its planned class cost; both
   councils converged in exactly their budgeted rounds. The S/M/L/council currency is
   internally consistent.
2. **Absolute throughput is ~3–7 s-e per attended session** — the whole 7.3 s-e plan
   ran plan-to-close in ONE day of owner-attended work against a 12-session budget.
   HK-9's ~10× anchor (BUILD-36) reconfirmed at sprint scale: budget owner-attendance,
   not machine time, and expect a session to land far more than the "3–4 M or ~2 L"
   guide.
3. **Discovery is real but cheap to hold**: 14 landed items spawned ≈9 filed ones —
   the 30% reserve rationale confirmed — yet only 0.1 was *spent*; filing (with HK-10
   anchoring) absorbed the rest at near-zero cost.
4. **Deployable ≠ deployed worked**: both product caveats (QUAL-78 image, vite-6 image
   + OPS-26 flip) land exactly in the pre-reserved deploy slot instead of blocking the
   close.
