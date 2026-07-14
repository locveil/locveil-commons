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
