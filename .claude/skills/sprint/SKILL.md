---
name: sprint
description: Plan or close a Locveil sprint — owner scoping page, keeper-contributor proposals with fresh dependency closures, a selection page with live dependency auto-pull and a "can is full" capacity gauge, landing as board/sprints/sprint-NN.md; close runs the per-repo shippable verdicts + the review stats loop. Args: "plan" (default), "close". Convention of record: process/sprints.md.
---

# The Locveil sprint loop (PROD-23)

Convention of record: `process/sprints.md` — read it if in doubt; this file is the
executable procedure. The sprint file `board/sprints/sprint-NN.md` is a **plan artifact**:
it lists task IDs and budgets and **never asserts a task's status** — per-repo ledgers own
status. The page artifact is an ephemeral view, never a record.

Modes: `plan` (default; also bare) · `close`. One sprint at a time — `plan` refuses while
a sprint file exists without a close section; `close` refuses without one.

## plan

### 1. Number and scoping round (round 0)

`NN` = next free number from `board/sprints/sprint-*.md` (zero-padded, `sprint-01` first).
Build the round-0 page from `scoping-template.html` (same directory): theme (a field, never
part of the name), expected **owner-attended sessions**, **bench/rack slots**, excluded
repos, reserve override (default 30%, 50% if the sprint will contain XL/HW), free notes.
Publish via the Artifact tool to the scratchpad as `sprint-NN.html` — **same file path
every round** (same URL), favicon `📆`, stable title. End the turn; the owner answers on
the page → *Copy my changes* → pastes a `sprint-reply sprint-NN round-0` block (grammar =
council-reply's, different verb).

### 2. Contributor round

Spawn the keeper agents **in parallel** (voice-keeper, bridge-keeper, satellite-keeper —
skip owner-excluded repos) in **contributor mode**: each proposes from its own ledger
`{id, gist, class, deps, travels-with, rank}` with the dependency closure computed
**fresh from repo reality** (never trust gate prose; flag stale gates as side-finds), plus
its repo's current shippable-definition line (§6 of the convention) and any HW/bench asks.
Effort classes and the no-data rule: convention §3.

The coordinator (you) then computes what no single keeper can:
- **PROD pulls** from `board/BOARD.md`: a selected PROD brings its written-back repo IDs;
  members that are blocked/unstartable become **visibility rows** (unblock condition, zero
  cost); a PROD without intake = one L row ("intake + execution").
- **Cross-repo closure** and **travels-with groups** → single atomic rows (a group row
  carries the sum cost; the cut-carrying member drags every cut-coupled member — §6).
- **Enabling councils**: a council-gated task auto-adds its council as a ≈0.5-session row.
- **Conflicts**: a PROD pull reaching an excluded repo → a conflict card, owner decides on
  the page (never silent either way). Rule of thumb for costs (session-equivalents baked
  into `data-cost`): S batched ≈0.1 · M ≈0.3 · L ≈1 · XL ≈2+ (flag owner-latency) ·
  council ≈0.5 · visibility/carry-over = 0 · attempt-slot → `data-bench="1"`, cost 0.
- **Split rows never mint letter-suffix IDs** ("OPS-1a" is a page display name only):
  the repo files a FRESH numeric ID at intake and records the display name in the task
  text — scope-guard's regex/aliases are numeric-only (convention §4, satellite finding
  sprint-01).

### 3. Selection round(s)

Build from `selection-template.html`: one row per selectable item/group (checkbox,
`data-cost`, `data-bench`, `data-deps` = other row ids), the recommended selection
pre-checked. The page's live JS enforces the convention: checking a row auto-checks its
dependency closure; unchecking auto-unchecks dependents; the **fill gauge** shows
cost vs usable capacity (sessions − reserve − **1 pre-reserved close-deploy slot**) and
goes red when the can is full; the **bench ledger** counts slots. Also on the page:
per-repo shippable definition lines, cross-sprint declarations (HW-GATED rows arrive
pre-declared cross-sprint; single-sprint inclusion is the owner's explicit toggle),
carry-over rows from the previous sprint file, conflict cards. Bump `{{ROUND}}` every
redeploy. Iterate on owner deltas; substantive scope questions may go back to the keepers
(SendMessage, context intact).

### 4. Land

On accept, write `board/sprints/sprint-NN.md`: header (theme, dates are the owner's
statement, budgets, reserve, excluded repos), per-repo shippable definitions, the selected
rows grouped by repo (ID · class · cost · group), visibility + carry-over rows,
cross-sprint declarations, bench-slot ledger. Then a `board/JOURNAL.md` entry, commit +
push, redeploy the page with the chip set to "planned". **No repo-side writes at plan
time** — repos learn about the sprint by reading commons, exactly like the board.

## close

1. Read the active sprint file. For each involved repo (= has a sprint-listed task ID),
   verify its **shippable definition** against repo reality (read-only: gate evidence in
   its journal/CI, its own guards `--check`, `make repin-check` where wired) — the
   deployability gate, never a `[release]` scope gate. The actual WB7 deploy is the
   owner's pre-reserved slot: confirm it's scheduled/done, never run it.
2. Append the **close section** to the sprint file: one `repo@<sha>` row + one-line
   verdict per involved repo; unfinished cross-sprint features → carry-over rows (they
   re-enter the next plan automatically); incident displacements made visible. No
   repo-side tags, ever (convention §8) — if the owner wants a repo-visible marker, the
   repo writes its own journal line at its own close.
3. **Review**: mine the involved repos' journals + ledgers for the sprint window; append
   the realized table (per class: planned vs landed vs discovered) — this feeds the next
   plan's calibration. Journal entry, commit + push, page chip → "closed".

## Discipline

- Mid-sprint cross-sprint declaration is the **owner's act only**, recorded in the sprint
  file with a journal note — never agent self-service (convention §7).
- Cost: one contributor round is three keeper spawns — don't re-spawn for page-only
  iterations; use SendMessage.
- Side-finds from contributor rounds (stale prose, missing tasks) are filed per
  review-then-remediate: repo-side finds delegate with write-backs; never fixed silently.
