# sprint-02 — plan

Planned 2026-07-15 via `/sprint` (convention `process/sprints.md`). Round 0 scoping +
two selection rounds (round 2 redone mid-flight to absorb the bridge eMotiva
debt-closure burst). This file lists task IDs, classes and budgets — **it never asserts
a task's status**; per-repo ledgers own status.

## Header

- **Theme:** Workbench shell (IMPL-1) + config-ui ported to new ui-kit
- **Dates:** owner stated none — capacity is session-denominated (opened 2026-07-15)
- **Budgets:** 12 owner-attended sessions · discovery reserve 30% (3.6) · 1 close-deploy
  slot pre-reserved · **usable 7.4** · bench/rack slots **0**
- **Excluded repos:** none
- **Selected:** 7.3 session-equivalents · bench 0/0
- Calibration input (sprint-01): relative S/M/L costs exact; ~3–7 s-e landed per
  attended session.

## Decisions at planning

1. **ARCH-50 explicitly deferred** (owner, round-2 card): voice's only `[release]`-gate
   task sits out sprint-02 by owner deferral — recorded so it reads as a decision, not
   starvation. Sprint-03 candidate.
2. **Bench stays 0** (owner, round-2 card): the DRV-38 `[P1]` replay — now the
   validation of the freshly-landed DRV-39 fail-closed stack — stays cross-sprint. On
   record: three eMotiva wedges in five days; a fourth auto-enters as incident-born P1
   and displaces reserve (§5).
3. **Runtime assembly runs as a COUNCIL** (owner, round 2 — "this should be a
   council"): how the Workbench assembles from multiple repos at runtime. Seeds per
   `hk-ids-from-the-board` when convened; its decision amends `workbench.md` §4 via its
   change control; IMPL-1 depends on it. Keeper conditions already on record: plugin
   bundles stay repo-built + version-stamped; embedded openapi types never become
   commons-side schema pins; pinning-if-chosen is a deliberate contracts-convention act
   (new tag family); the assembly never reaches into the satellite tree (tags only).
4. **No XL selected** (satellite DES-5, bridge UI-19 wireframe session both deferred) —
   the 30% reserve stands without override; both are sprint-03 candidates.
5. **The bridge deploy runs EARLY in-sprint, not at close** (safety): the WB7 runs
   pre-DRV-39 code against a device that wedged three times in five days. The early
   deploy ships the fail-closed stack + vite-6/docker-context images, folds in the
   still-unjournaled OPS-26 retained-topic verify, and comes with the briefing note
   that fail-closed REFUSES commands while settling (`force` = operator escape hatch).
   The pre-reserved close slot still does the final verify pass.
6. **PROD-4 council deferred again** — CORE-12, CORE-8, ARCH-45 and all write APIs
   remain gated; bridge UI-18's write verbs stay dormant (consistent with its read-only
   cut).

## Per-repo shippable definitions (§6, keeper re-verified)

- **voice** — unchanged (ci.yml gate set + multi-arch dispatch + WB7 update path +
  `/health` smoke). Sprint-02 condition: the ci.yml config-ui gate survives the plugin
  restructure — `config-ui-stays-functional` binds at every intermediate cut.
- **bridge** — standing gates (**pytest 734** post-eMotiva-burst · pyright 0 ·
  import-linter 6/6 · no contract drift) + both armv7 images from the root `docker/`
  context + contract-guard v2 + repin-check at close. With UI-18 selected the line
  grows: `workbench-plugin/` check + lib build.
- **satellite (pre-first-light)** — all four guards green + provisioning surface
  intact. An in-sprint `esp32-site` bump (none planned) must be a proper tag+STAMP cut.

## Selected rows

### commons

| ID | gist | class | cost | group |
|---|---|---|---|---|
| (council; HK-N at seed) | **Runtime-assembly council**: multi-repo Workbench assembly at runtime (loadable plugin bundles vs dev-phase `file:` rebuild); amends workbench.md §4; keeper conditions on record (decision 3) | council | 0.5 | Workbench arc |
| IMPL-1 | Workbench shell v1: chrome (tabs, locale + theme toggles, BugReport button, status slots, auth-guard slot), plugin contract AS CODE (early slice — both plugin rows compile against it), registry, assembly per the council | L | 1.0 | Workbench arc |
| IMPL-2 | scope-guard UNREFERENCED-evidence check (HK-10 goes mechanical) + next scope-vX tag | S/M | 0.3 | — |

### locveil-voice (the port arc — §4 split; fresh numeric IDs filed at intake, display names recorded in task text)

| ID | gist | class | cost | group |
|---|---|---|---|---|
| voice UI-18 (new) | kit-first foundation: eslint-9 flat + ui-kit-v1 dep + preset/tokens + swap the 9 hand-built primitives; standalone app stays green; ci.yml guard-version prose fix batches in | L | 1.0 | port arc |
| voice UI-19 (new) | full port body: 35 composites + 7 pages onto kit primitives (~32k lines) — flagged as the sprint's largest execution risk | L+ | 1.5 | port arc |
| voice UI-17 (narrowed) | plugin conversion: Voice plugin mount (i18n bundles, per-page backend targets, report hook), 6-page cut, Header/Overview retirement, status slot, built-artifact packaging; needs IMPL-1's contract frozen, not the shell finished; PROD-24 write-back ID preserved | L | 1.0 | port arc |
| voice UI-16 | schema-driven sections/widgets + spaCy-attr i18n (declared travel-together with UI-17; backend half respects the hexagon) | M–L | 0.5 | port arc |

### locveil-bridge

| ID | gist | class | cost | group |
|---|---|---|---|---|
| bridge UI-18 | Bridge Workbench plugin, read-only v1 cut: skeleton + descriptor + voice-readiness live; setup shells with verbs dormant under the PROD-4-auth gate; existing backend surfaces only — no contract cut; milestone-tag hygiene at intake | L | 1.0 | Workbench arc (two-real-plugins) |
| bridge DOC-17 | planned-pages status sweep + 15 stale-titled .dot diagrams + PNG regen | M | 0.3 | — |

### locveil-satellite

| ID | gist | class | cost | group |
|---|---|---|---|---|
| satellite OPS-8 (new) | verify `publish_model_pack.py` ssh branch live against the WB7 (OPS-7's flagged-not-asserted tail); files at intake; execution rides a controller session | S | 0.1 | — |
| satellite (new S-chore) | pending-amendment marker at the two D-17 spots in `esp32_satellite.md` (doc currently asserts the overruled CLI-only ruling); DES-5's sweep replaces it later | S | 0.1 | — |

## Visibility / carry-over rows (zero cost)

- **bridge DRV-38 `[P1]`** — REWRITTEN post-burst: rack replay validating the DRV-39
  fail-closed stack (expect *refused*, not held) + DRV-32 CEC re-check. Cross-sprint by
  owner decision 2; heads the next HW-bearing sprint's bench.
- **bridge DRV-37 + VWB-39** — blocked on the first conforming descriptor (PROD-20).
- **HW queue rest**: DRV-32 full scope, DRV-6/15/16, CORE-1, SCN-13, UI-15.
- **satellite FW-1 (+ dormant OPS-1)** — no-data; DES-3 + first board + bench.
- **satellite OPS-6** — earmark, blocked on DES-5 (+ PROD-4 auth).
- **PROD-20** — first-light chain, HW-GATED.
- **Explicitly deferred, sprint-03 candidates**: voice ARCH-50 (decision 1) · satellite
  DES-5 (XL) · bridge UI-19 wireframe session (XL, owner-attended) · PROD-4 council
  (decision 6) · voice ARCH-51 · BUG-37+39 · BUILD-14⇄OPS-28 pair · bridge quality
  queue (UI-10/11/12, chores, VWB-31).

## Bench-slot ledger

0 budgeted · 0 consumed (owner decision 2 — the DRV-38 attempt-slot was offered and
declined). Standing ask for the next HW-bearing sprint: DRV-38 replay first, then the
satellite bench items (FS90 rail isolation, deck [VERIFY] measurements).

## Deploy ops (owner)

- **EARLY in-sprint: bridge deploy** (decision 5) — DRV-39 stack + images + OPS-26
  retained-topic verify + fail-closed briefing.
- **Close slot**: voice image dispatch (bakes QUAL-78) + WB7 deploy + `/health` smoke;
  final bridge verify; satellite OPS-8 ssh check piggybacks whichever controller
  session comes first.

## Side-finds (filed per review-then-remediate at intake)

- **voice**: ci.yml guard-version prose (batches into voice UI-18); plugin-bundle
  publishing/standalone-container fate → runtime-assembly council + voice UI-17 intake.
- **bridge**: UI-18 + CORE-12 missing milestone tags (REL-1 rule) — tag at intake;
  action_plan.md header date stale; UI-18 gate prose can name IMPL-1 concretely.
- **satellite**: D-17 prose (selected as the S-chore row); DES-4 v1.1 wrinkle confirmed
  live, not stale.
