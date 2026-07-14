# Locveil sprint planning — the convention (HK-9)

Decided by council **HK-9** (2026-07-14, two rounds; arc in `board/BOARD_DONE.md`). This
file is normative; the `/sprint` skill (PROD-23) is its executable half. A sprint is a
planning artifact over the existing ledgers — it never replaces them and never asserts
task status.

## 1. Artifacts

- One file per sprint: `board/sprints/sprint-NN.md` in commons. It lists task IDs,
  classes, groups, per-repo shippable definitions, cross-sprint declarations, bench
  slots, and (at close) `repo@sha` rows + realized stats. **It never asserts a task's
  status** — the per-repo ledgers own status (the board rule, generalized).
- Zero repo-side churn: no new ledger fields, no new required task tags (the HK-1
  required-task-tags earmark is resolved: none), no new scope-guard rules in v1. Sprint
  rows are plain prose; IDs are pointers.

## 2. Capacity

- **Currency = owner-attended sessions**, plus a **separately budgeted bench/rack-slot
  count** for hardware work. Never calendar effort, Claude-hours, or raw task counts —
  calibration evidence (BUILD-36: predicted 4.5–5 focused days by its own keeper,
  realized 2h45m; ~10×) shows owner attendance and review latency bound throughput, not
  machine time.
- The owner states both budgets at scoping (guide: 3 weeks ≈ 12–15 sessions; an attended
  session lands 3–4 M-tasks or ~2 L; an unattended day lands ≈ nothing).
- **One owner slot per sprint is pre-reserved for the close deploy** (§6) before filling.

## 3. Effort classes

`S` chore ≤1 h, batchable · `M` 0.5–2 h · `L` one full session (arc / delegation batch) ·
`XL` interactive design across 2–4 sessions, bounded by owner review latency ·
`attempt-slot` (bench budget only; success = attempt made and journaled) ·
`no-data` — a **legal** estimate where no samples exist (satellite PCB/FW); forcing a
number there is fabrication.

## 4. Selection

- Contributor agents (the keepers, in contributor mode) propose per repo:
  `{id, gist, class, deps, travels-with, rank}` — dependency closures computed **fresh**
  from repo reality each sprint (prose gates rot; the stale "Gated on BUILD-21" entries
  are the proof). A standing `deps:` ledger field is v2 hardening, only if sprints recur.
  Partial dependencies = split the task (design-then-implement already splits); no new
  syntax.
- The coordinator alone computes PROD pulls and **cross-repo** closure (a single repo
  agent cannot see the other ledgers). Artifact-shaped deps at repo boundaries are
  normal (`satellite:DES-4#descriptor`).
- Selecting a PROD pulls its written-back repo IDs; **blocked / unstartable members enter
  as visibility rows** carrying an unblock condition, not effort. A PROD without intake
  yet enters as one L ("intake + execution").
- **Travels-with groups are single selectable rows** — silent partial picks forbidden;
  overrides explicit (PROD-18 one-cut rule; DRV-37 + VWB-39 + deck-vocab-cut travel
  together).
- **Planned councils are first-class items** ≈ 0.5 day; selecting a council-gated task
  requires scheduling the enabling council in the same sprint.
- A PROD pull reaching an owner-**excluded** repo is surfaced to the owner interactively
  during selection — never silently included, never silently dropped.

## 5. Discovery reserve

30% of capacity by default, 50% when the sprint contains XL or HW items (discovery is
not conserved: closing tasks spawns tasks). Incident-born tasks (P0/P1) auto-enter,
displace reserve first; displacement stays visible in the sprint file.

## 6. The shippable invariant

**Every sprint closes with each involved product repo shippable**, unless a feature is
declared cross-sprint (§7).

- **Shippable = deployABLE, bound to each repo's own existing gates** — declared as a
  per-repo definition line in the sprint file at planning; never one invented universal
  definition. Current definitions: voice — CI gates green + multi-arch image build
  (baked component gate) + WB7 `update.sh` + `/health` smoke path ready; bridge —
  standing gate list + both armv7 images build + contract-guard clean; satellite
  (pre-first-light) — all four guards green + the provisioning surface intact
  (post-DES-3: firmware builds + publishable per its OPS-1 flow). The invariant binds
  the *deployability* gate, never a repo's `[release]` scope gate.
- **Deployable vs deployed:** the actual WB7 deploy is an owner op — the pre-reserved
  owner slot (§2). Sprint close requires deployable; the deploy is scheduled, not
  implied.
- **Cut atomicity, not group confinement:** a contract cut is atomic within one change
  (contracts convention); design may land in sprint N and implementation+cut in N+1
  with the repo shippable throughout. The sprint-level rule: **if a sprint selects the
  cut-carrying member of a travels-with group, every cut-coupled member lands in that
  sprint.** A trailing sibling pin across a boundary is version-tolerable by contract
  design; the owner pulls the re-pin into the same sprint when the product-level bar
  demands it.
- Sprint close runs each repo's **repin-check** (release-time checks asked at a
  recurring moment; caps pin staleness at one sprint). Verdicts live in the repo
  journals; the sprint file records the one-line outcome (§8).

## 7. Cross-sprint features

- Declared **at planning, in the sprint file only** — ledgers never carry sprint
  membership. **HW-GATED and blocked members are cross-sprint by default,
  auto-declared** (the natural satellite case); single-sprint inclusion is the owner's
  explicit override.
- A cross-sprint feature carries a **mandatory zero-effort carry-over row** in every
  subsequent sprint until done — visibility, and the moment where bench availability is
  re-checked each planning session.
- Mid-sprint declaration is allowed when discovery shows a feature won't land — but it
  is the **owner's act only** (never agent self-service; otherwise cross-sprint becomes
  an escape hatch from the invariant), recorded in the sprint file with a journal-grade
  note. Sprint review audits declarations; it never originates them.

## 8. Naming, close, and review

- **Names are plain `sprint-NN`** (ordinal). The theme is a field inside the file, never
  in the identifier (slugs rot when scope shifts). Date-based or release-shaped names
  are forbidden here: they pre-empt the parked release-numbering council (D-11 reserves
  calver shapes). **Sprint close ≠ release cut**; any coupling waits for that council.
- **Involved repo = has a sprint-listed task ID** (not "received any commit" — re-pins
  and write-backs touch repos incidentally). Excluded repos have no row.
- **Close labeling = SHA-in-sprint-file:** one row per involved repo,
  `repo@<sha>` + a one-line close verdict (gates + repin-check outcome). No repo-side
  sprint tags — product tag namespaces are load-bearing, guard-checked contract
  machinery, and "participated in sprint N" is a planning fact; planning facts live
  commons-side (the PIN.json `owner_commit` / board `repo@sha` pattern). If a
  repo-visible marker is ever wanted, the repo writes a dated journal line at its own
  local close — never a coordinator-stamped ref.
- **Sprint review** ends the sprint: retro mines the journals and appends a realized
  velocity table to the sprint file — the stats loop that keeps §2's calibration fresh
  for the next planning round.
