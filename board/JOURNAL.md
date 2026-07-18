# Board journal — newest on top

## 2026-07-18 — PROD-26 item 1: repin promoted — `packages/repin/` @ `repin-v1`

The HK-12 centerpiece lands hours after the decision. Voice's BUILD-24 engine promoted
faithfully — registry-anchored newest-tag parsing, fetch-at-tag + sha256 + PIN.json with
mirrored owner-STAMP keys, multi-dest one-run writes — with the council's deltas built
in: topology moved wholesale into per-repo `.repin.toml` (the tool carries none), the §5
severity ladder as `--fail-on none|major|any` (pre-commit / ordinary CI / release gates),
remote-first tokenless `ls-remote` with satellite's stale-clone fallback (WARN + fetch
age) and never-network-required-to-commit degradation, untagged families drift-checked
locally and warn-skipped without a source, `check_only` for pins another repo's flow
stamps, cross-repo dest writes validated commons-only, and the `[[tool]]` vendored-tools
manifest so tag↔vendored-copy stops living in prose. 15 behavior tests on real throwaway
git repos, all green. Commons ate its own cooking in the same commit: `.repin.toml`
(catalog check_only under voice's multi-dest authority), a warn-only pre-commit stage,
and — per this very council's ruling — the owned surface `contracts/repin/` (STAMP v1
with `artifacts` list + registry row) cut in the SAME change as the tag, not after a
prompt. Live check green: catalog current at v1.7 over real ls-remote. Voice BUILD-43 and
the bridge/satellite sweeps can now vendor at `repin-v1`; guard v3/v7 are the remaining
commons build. contracts: repin STAMP v1 cut (new owned surface, tag `repin-v1`); no
consumer re-pins owed yet — adoption rides the PROD-26 sweeps. docs: none —
packages/README.md row added in the same change; the package README is the consumer doc
(guards precedent).

## 2026-07-18 — HK-12 DECIDED: convention-enforcement hardening (council, 2 rounds)

Seeded by the owner minutes after catching the PROD-8 contract-surface miss ("no new
contract?" — a repeated org-wide class). The council confirmed the diagnosis with paper
trails in every product repo — voice's WS protocol shipped unstamped and its catalog
consumed unpinned until HK-5; bridge's catalog-v1.7 false green and re-pin-owed journal
rot; satellite's four instances in six days plus LIVE drift caught during round 2 (its
registry cited contract-guard-v1 while running v2). Round 1 converged on the `contracts:`
verdict line as the strongest single control (it fires at every completion, catching the
en-passant bumps that skills never see) plus orphan-tag/content-drift/unknown-prefix guard
rules and a pinned triad block; the owner's round-1 amendment then made voice's `repin.py`
the centerpiece — promoted to commons `packages/repin/` with per-repo config, after bridge
verified all org repos are public (tokenless `ls-remote`, credential objection withdrawn)
and satellite set the offline floor (warn with fetch age, never network-required-to-
commit). Severity landed on bridge's three-case model — staleness fails CI only on
touch-the-family / release workflows / major-gap (per-repo configurable) — and §5 of
`process/contracts.md` was amended in this landing, superseding "never a push gate"
eye-open rather than by adverb. Wave B (central freshness job) dropped as redundant;
skills deferred. The candidate sweep stamps workbench + ui-kit + the shared tools,
earmarks voice's trace format and satellite's two future API surfaces (born-stamped),
defers eval, and puts the non-candidates on record. HK-12 filed born-decided; execution +
delegations: **PROD-26** (one sweep per repo). docs: none — normative change is a process
file; the dossier is ephemeral by convention.

## 2026-07-18 — PROD-8: the core-py skeleton is cut — `core-py-v1`

The last commons-side piece of the loader arc: `packages/core-py/` now exists, carrying
`entry_point_loader.py` against the agreed ARCH-42 design's §2 surface — `DynamicLoader`
class only (no module-level singleton; the shared artifact stays state-free),
`importlib.metadata`/py3.11 only (the pkg_resources compat branches did not travel),
faithful cache + BUG-36 failure-ledger semantics, and the three council-agreed deltas:
optional `base_class=` rejection into the ledger, `get_provider_class` loading a single
named entry point instead of materializing the whole group, and import-free
`list_registered`. One divergence-by-necessity from the voice original: the cache key
gains `base_class` (voice's string key predates the parameter — two same-namespace calls
with different base classes must not collide). Behavior suite: 23 tests, all green,
faking the EP mechanism duck-typed so semantics are pinned without throwaway
distributions. Distribution `locveil-core-py` 1.0.0, tag **`core-py-v1`**, flat-module
layout per the guards' precedent. Voice ARCH-58 and bridge CORE-7 are unblocked to vendor
at the tag (strict pin + byte-identity test — the estate's first vendored RUNTIME code).
**PROD-8 stays OPEN by owner ruling until both adoption write-backs arrive**; the
logging-extraction spin-off question is parked with it. docs: none — packages/README.md
planned-list refreshed to reality in the same change; no manifest node covers
`packages/core-py` (integrator surface, own README).

Amended same day off the owner's "no new contract?": the cut had skipped the owner-side
contract surface the pin convention presupposes — `contracts/pins/core-py/` in each
consumer must hold the owner's STAMP.json verbatim, which therefore has to exist.
`contracts/core-py/` landed in the docs-manifest cross-reference style (artifact keeps
its importable home in `packages/core-py/`; the folder holds STAMP + pointer README;
registry row added). STAMP `core-py` version "1" ↔ tag `core-py-v1` (the guard's
tag==contract-vVersion rule), and — first stamp of a new family — it already carries the
`artifacts` completeness list per the HK-5 forward requirement: exactly
`entry_point_loader.py`; tests/pyproject/README are owner-side tooling and never travel.
contract-guard green (sole warning is the pre-existing crossover-fixtures PIN-PENDING).

## 2026-07-17 — PROD-25 CLOSED: all three close conditions verified in live CI

The close was pure verification — the work had already happened in the consumer repos;
this session checked run histories and wrote the evidence back. Commons: run 29435212549
@ 8cb7880 executed the guard job green on the explicit-fetch workflow (two tag-naming
owned STAMPs → a passing `--check` proves tag resolution). Voice: run 29435718102 @
4175aeb (contains BUILD-39) ran the `contract-guard` job to success — every later green
CI was a path-skip, checked job-by-job. Bridge answered the entry's open question with
two live runs (29413490074, 29436060503, guard green right after the bare-checkout 3×
TAG-MISSING dispatch): **checkout@v6 does not share #1467's behavior — `fetch-tags:
true` genuinely works there.** §4 therefore gains a v6 footnote scoping the flag-form
ban to v4's shallow-SHA path and protecting bridge's working flag-on-v6 from being
"fixed" to the explicit form; the explicit step stays the prescription as the
checkout-version-proof fix class. Entry moved to BOARD_DONE. docs: none — process file
amended in place.

## 2026-07-17 — IMPL-7: the logo lands — packages/brand + kit `<Logo>` + Workbench top bar

The owner's browser design session delivered the identity (mark 2b + wordmark B, drawn
in the chrome's own 24px/stroke-2 language) and this session integrated it. The
delivery's own README flagged its two guesses and both were live defects — the
structure-wiring recipe pointed at a nonexistent token whose real namesake holds a
bare hue (`hsl(var(--lv-status-pristine))` = invalid CSS = invisible house outline),
and all four standalone fallback hexes sat ~20 chroma points off-token. Owner rulings
at integration: independent `packages/brand/` as the canonical, reuse-anywhere home;
fallbacks snapped to exact token renditions; **Latin wordmark universal — the Cyrillic
lockup question is closed as never**; the Workbench top bar carries the horizontal
lockup at the function-cluster width (the IMPL-1 gradient-square placeholder retires).
The kit component wires colors internally (`--primary`/`--muted-foreground`) so the
mis-wiring class dies at the API. Proven live: kit + workbench checks and builds
green, storybook stories screenshot-verified on dark. docs: stylebook (§10 added).

Amended same day off the owner's first live screenshot: "function cluster" was the
wrong reading of the placement ruling — the logo gets a dedicated top-bar region
exactly as wide as the **plugin-pages sidebar**, both consuming one `--wb-rail-w`
(13rem) so equality holds by construction and the tabs start flush with the content
area. Wireframe prose in workbench.md §3 carries the amendment; verified on the
running shell.

Second same-day amendment (owner: "why doesn't the workbench use the brand favicon?"
— it didn't, the adoption was parked and no ico existed): favicon.ico generated into
brand/ (multi-size, regen recipe documented), workbench adopts both forms via
byte-identical public/ copies, index.html icon links + serve.mjs `.ico` MIME landed,
both URLs verified 200 on the live shell. The IMPL-7 favicon follow-up is closed.

Org housekeeping, owner-requested, same shape as the 2026-07-13 library moves: the
microWakeWord training factory (Russian wake words «Ирина»/«Борис» for the ESP32
satellites) transferred `droman42/wakeword-training` → `locveil/wakeword-training`.
Name kept (library/tooling precedent — `locveil-*` is for product repos), visibility
stays PRIVATE, and unlike the PyPI libraries there was no publisher prework: the repo
has no CI and publishes nothing — its artifact channel is Hugging Face
(`droman42/microwakeword-irina-ru`), which is untouched by a GitHub transfer, so the
voice/satellite wake-pack pins (STAMPs reference the HF model, not the GitHub repo)
need no re-pin. Local remote re-pointed; living old-owner URLs fixed in the repo's own
`scripts/train_local.py` + `scripts/publish_hf.py` (@a1aa39f); historical
`results/run_*/irina.json` manifests deliberately untouched — history stays. The repo
remains a lightweight research spike: org membership does NOT mean the Locveil process
kit. docs: none — sibling-repo op, no commons manifest node describes it.

## 2026-07-16 — PROD-8 COUNCIL DECIDED: core-py loader scope + sequencing (2 rounds)

Convened PROD-8 (D-8 core-py bootstrap + the loader/logging extractions) as a council;
keepers voice + bridge (satellite skipped — not a core-py Python consumer). Both landed
support-with-conditions. Round 1 established the shared spine is **entry-points** (voice's
`get_*` methods are accessors/metadata, not a rival mechanism) and that **bridge authored the
logging scheme** (OPS-12 DONE; voice BUG-30 is the copy — settling the owner's "who's ahead"
hunch). The owner sent it back with three sharp questions; round 2 answered all and dissolved
the round-1 single-vs-two-axis crux: the voice `get_***_capabilities/platform` "~4 methods" are
the `EntryPointMetadata` build-time quartet (dependency-closure + the load-bearing arch gate),
orthogonal to discovery and staying voice-side; the bridge "second axis" is the *simple* by-name
config resolver, required because the offline catalog generator builds the voice-pinned golden
**without loading drivers**, and it stays bridge-local. **Decisions (accepted no-changes):**
(1) core-py loader = the **entry-point-group registry only**, auxiliaries stay local until a
second consumer; (2) config-based driver loading = **unify resolution, keep entry points** —
runtime config-path discovery REJECTED (breaks catalog generation); (3) the UI/panel
driver-availability gating (bridge is split-brained today: config pages show configured-but-
unloaded devices) is a **separate bridge task**, not a CORE-7 rider; (4) sequencing locks —
ARCH-50 ⟶ ARCH-42, skeleton after both, logging parked (loader-first). Delegations committed in
the PROD-8 entry: voice reconciles ARCH-42/ARCH-50 scope (+ dead `get_provider_capabilities` to
ARCH-50's sweep); bridge reconciles CORE-7 (fix its stale "BUILD-21" gate → PROD-8; fold the dead
`validation.py` cleanup) and files the new UI-gating task. PROD-8 stays open — the skeleton +
designs are unexecuted; the council set scope + sequencing only. docs: none — board + journal.

## 2026-07-15 — sprint-02 CLOSED: Workbench shell + config-ui port, all four repos shippable

`/sprint close` ran the per-repo shippable verdicts read-only (gate evidence in journals +
`--check` guards gating every committed HEAD). Verdicts: **commons@8cb7880** (IMPL-1 shell
+ IMPL-2 scope-v6 + HK-11 runtime-assembly council, plus discovery IMPL-4/5/6) ·
**voice@4175aeb** (port arc COMPLETE — UI-18/19/17/16; config-ui is now the Voice tab, the
standalone app is gone; image deploy DONE by the owner) · **bridge@c60a2bc** (UI-18 Bridge
plugin loads in the shell + DOC-17 done; suite 734 · pyright 0 · import-linter 6/6 · no
drift; both armv7 images build) · **satellite@5761e7d** (OPS-8 + incident-born OPS-9 done;
four guards green). Landed ≈ 7.2 of 7.3 selected s-e — a full clear of the selected work
bar one absorbed chore. **Superseded, not carried:** the satellite D-17 marker S-chore — the owner
overruled D-17's CLI-only reading and its amendment lands via the expanded DES-5 design, so
the standalone marker was absorbed. Discovery ran hot again (commons IMPL-4/5/6, bridge
LIB-1/2/3 eMotiva burst, satellite OPS-9) inside the 30% reserve; no incident-P1
displacement fired. The L-heavy voice port arc (4.0 s-e) landed inside estimate — UI-19,
flagged the sprint's largest execution risk, did not overrun. Close section + realized
velocity table appended to `board/sprints/sprint-02.md`. docs: none — planning artifact.

## 2026-07-15 — IMPL-2 DONE: the UNREFERENCED-evidence check ships (scope-v6)

HK-10's evidence-anchoring rule goes mechanical: scope_guard.py 1.3.0 adds the fourth
direction — an evidence doc on disk whose path and basename both appear nowhere in
active+DONE is flagged (`unreferenced = "error"|"warn"|"off"`, default warn; commons
runs error). Acceptance per the entry's own spec: commons clean with the
HK-10-anchored fixture_recorder.md passing, a synthetic orphan flagged, clean after
removal. Tagged scope-v6 (pyproject aligned from a stale 1.0.0 en route);
ledger-discipline §3/§6 updated to shipped-state; consumers adopt at their next re-pin
with warn keeping first runs honest rather than red. With this, EVERY commons sprint-02
row is done — the sprint's remaining work is bridge DOC-17, the two satellite chores,
voice UI-23 verification, and the close-deploy slot. docs: none — process file updated
in place.

## 2026-07-15 — IMPL-6 filed and done: backends reach plugins (workbench-v1.2)

The owner's first-controller-run question exposed the last contract gap: the prose
promised per-page backend targets since PROD-24, but contract-as-code v1 passed only
locale — plugins would have resolved fetches against the SHELL origin (localhost:6107)
instead of the WB7. Implemented as decided everywhere else in this arc: deployment
facts (absolute origins — IP AND port) live in the owner-edited workbench.config.json
per plugin and flow config → runtime-config → loader → PageProps.backends; build
artifacts stay deployment-blind. Ports pinned from repo reality: voice backend :8080,
bridge backend :8000 (both host-network on the WB7); CORS already wide open on both, so
the browser hits the controller directly — no proxying. Additive (old plugins ignore
the prop): workbench-v1.2, §4 amended, README recipe updated, demo About page renders
its backends map as proof. Config merged with the externally-mounted voice AND bridge
plugin dists — the shell now assembles demo + voice + bridge + the dormant satellite
slot. Repo-to-repo consumer note: plugins route every fetch through PageProps.backends
("api" = the conventional key). docs: none — design doc + README amended in place.

## 2026-07-15 — IMPL-5 filed and done: the bottom action-bar surface (ui-kit-v1.2 + workbench-v1.1)

Voice's port comment ("the two fixed bottom-0 action bars wait on a plugin-contract
bottom-slot surface that doesn't exist yet") was the first-consumer trigger IMPL-1
deliberately deferred to — filed as IMPL-5 and closed in one arc. The IMPL-4 pattern
reused wholesale: <ActionBar> in the kit registers into a module-scope bus (one
instance everywhere via the import-map singleton — usable from any depth of a plugin
tree, no prop drilling), the shell renders the single <ActionBarHost/> in normal flex
flow at its bottom slot, single-occupancy latest-wins with a dev warning, unmount
clears, standalone apps render their own host. The demo plugin now renders an ActionBar
+ fires a toast ACROSS the bundle boundary — the cross-bundle proof baked into the
repo. Tags: ui-kit-v1.2 (0.1.2, additive — plugin peers ^0.1 unaffected) +
workbench-v1.1 (contract addition, workbench.md §4 amended). Both packages + storybook
green; the serve smoke showed the voice plugin mounting from its real dist alongside
the demo. Voice now collapses ApplyChangesBar + the LocalizationsPage bar into
<ActionBar> at its port. docs: none — design doc amended in place.

## 2026-07-15 — IMPL-4 DONE: Toast + AlertDialog land in ui-kit 0.1.1 (ui-kit-v1.1)

The voice session's UI-19 filing closed same-day: the two stylebook-§7 standards
ui-kit-v1 didn't ship. The plugin-context Toast question the filing asked resolved
elegantly out of HK-11 itself — locveil-ui-kit is an import-map SINGLETON, so the
module-scope toast bus in use-toast is one shared instance across the shell and every
runtime-loaded plugin by construction: plugins call toast(), the shell renders the one
<Toaster/> (added to the workbench App in the same change), standalone apps render
their own. AlertDialog = full shadcn set on the tokens with the destructive recipe from
the status hues; feedback stories with RU content. Versioning honored the loader's
strict 0.x rule: 0.1.1 / tag ui-kit-v1.1 — additive, plugin peers ^0.1 keep matching,
zero refuse-churn. Verified: check clean, kit + storybook + workbench builds green.
Voice UI-21 ungated. Also absorbed from the same external burst: IMPL-3 (StatusChip
literal recipes — a real consumer find fixing my template-literal mistake), the voice
plugin mounted in workbench.config.json (the first real product plugin through the
import map), HK-11 write-backs complete (voice UI-17 corrections + UI-20 bundle-Monaco;
bridge UI-18 confirmed), and PROD-25's reopening — my fetch-tags one-liner was the dud,
satellite OPS-9 established the explicit-fetch fix, voice re-fixed the commons workflow.
docs: none — stylebook already names both standards.

## 2026-07-15 — PROD-25 reopening discharged: the explicit tag-fetch lands on commons + voice

The satellite session's "fetch-tags is a dud" finding (actions/checkout#1467) got its
third live confirmation exactly as predicted: voice's push-day run 29417879036 fired 4×
TAG-MISSING with the flag set and no tag refspec in the checkout log. Voice fixed as
BUILD-39 (explicit `git fetch --tags --depth=1 origin` per the satellite OPS-9
reference, plus an unrelated frontend-health repair — the Workbench-era sibling `file:`
deps need a side-by-side commons checkout in CI). Commons' own defective deliverable
(2) is re-fixed the same way, and §4's prescription re-worded: the flag-only form is
gone, the explicit step (or `fetch-depth: 0`) is the fix class, OPS-9 is the reference,
all three failing runs are cited. Left on the entry: bridge's checkout@v6 verification
of OPS-30, and green `contracts/**` runs on commons + voice. Reserve spend 0.1 (this).

## 2026-07-15 — IMPL-3: StatusChip was invisible to Tailwind — caught by the first real consumer

Voice's UI-18 kit adoption (the first consumer build to scan the kit's dist with a
lightningcss-minifying pipeline) failed on a `$` in generated CSS and exposed the real
defect underneath: `status-chip.tsx` assembled its variant classes via a template
literal, so Tailwind never saw the five real recipes whole (chips unstyled everywhere)
while happily extracting the `${h}` pseudo-candidate into consumer CSS. Fixed
found-and-fixed as **IMPL-3**: a fully-literal class map per variant, values exactly
the council-ratified recipe; kit green, dist clean, voice's build is the live proof.
Lesson for kit authors on record: className strings must be statically whole — the
extractor is the contract. Reserve spend 0.2 of 3.6.

## 2026-07-15 — PROD-25 commons half executed: contract-guard CI checkouts get tags

The bridge session's filing (off its OPS-30) found commons' own contract-guard workflow
latently broken — TAG-MISSING resolves owned STAMP tags via `git tag -l`, and a default
actions/checkout is tag-less, so the rule could never pass on the next `contracts/**`
push. Executed under sprint-02 discovery reserve, same day: `process/contracts.md` §4
now states the CI-checkout requirement (fetch-tags: true; shallow fine) with the
false-alarm failure signature named, and the commons workflow carries the fix. The
voice + satellite delegations stand (their fix rides the contract-guard-v2 re-pins);
write-back slots open on the entry. Reserve spend now 0.1 (this) of 3.6. docs: none —
process file amended in place.

## 2026-07-15 — IMPL-1 DONE: the Workbench shell lives (workbench-v1)

`packages/workbench` = locveil-workbench 0.1.0, the first IMPL-prefix completion. The
shell implements HK-11 natively rather than around it: the shell's own build
externalizes the singleton set and ships vendor ESM bundles behind the import map, so
shell and plugins share one react BY CONSTRUCTION — the 4 kB react-dom-client vendor
bundle is the proof the re-export chain held. Chrome per the ratified wireframe (tabs +
status dots, RU/EN, theme toggle, the Material BugReport glyph delegating to the active
plugin's reportHook, both reserved slots); contract as code exported types-only at
`locveil-workbench/contract`; loader with strict refuse-and-surface, style injection,
and dormant slots that trigger zero activity and render their conjunctive gate; a
serve script that mounts owner-config locations and generates the runtime config; and
an in-tree demo plugin built exactly the way voice UI-17 and bridge UI-18 will build
(externals + build-emitted fragment) proving the loading path end-to-end over HTTP.
Verified: 0 vulns, check clean, all three builds, full HTTP path (runtime-config →
fragment → entry → styles → vendor → SPA fallback); browser render is one `npm run
serve` away. Sprint-02: the commons chain (council 0.5 + shell 1.0) is done at planned
cost; remaining rows are the voice port arc, bridge UI-18 + DOC-17, satellite OPS-8 +
marker. docs: none — package README is the consumer doc.

## 2026-07-15 — PROD-25 filed: CI checkouts must fetch tags for contract-guard

Filed by the bridge session off bridge OPS-30. contract-guard-v2's TAG-MISSING rule
reads tags via `git tag -l`, but the default `actions/checkout` clone carries none — the
bridge's path-gated guard job had been failing since the OPS-27 re-pin push itself
(unnoticed; re-exposed by the first workflow_dispatch, a 3× false alarm with all tags
present on origin). One-line fix class: `fetch-tags: true` on the guard job's checkout;
bridge already fixed (OPS-30, the reference). Sweep at filing: commons' own
contract-guard workflow is latently broken NOW (v2 source + two tagged owned STAMPs +
bare checkout — fires on the next contracts/** push); voice + satellite are at v1 and
inherit the gap at their v2 re-pin, so their checkout fix rides the re-pin delegation.
Deliverables on the entry: process/contracts.md §4 amendment + the commons workflow fix
+ the two delegations. docs: none — board filing only.

## 2026-07-15 — HK-11 DECIDED: Workbench runtime assembly = native ESM + import map

The sprint-02 planned council, one round to convergence — all three keepers backed the
same mechanism independently: native ESM dynamic import behind a shell-served import
map, with Module Federation rejected for coupling build tooling across repos (the
vite-majors-per-consumer ruling's enemy) and iframes for amputating the contract. The
design assembled itself from keeper contributions: bridge supplied the manifest
reconciliation (shell config = locations + dormant slots only; each plugin's dist
carries its own BUILD-EMITTED fragment — cross-repo-source-of-truth by construction)
and the strict refuse-and-surface compat rule; voice verified the hard cases (Monaco
is moot for bundling — it loads from CDN at runtime, itself a privacy side-find voice
now owns; router is the one real coupling → externalized, pinned major 6, both repos
already on identical 6.30.4) and won plugin-local i18n; satellite locked dormant slots
as pure metadata (no location, zero shell activity, conjunctive gates) and got its
commons-side-panel exception finally made citable. Owner rulings: all recommendations
stood; q5 = the standalone config-ui app RETIRES at voice UI-17 (DoD re-anchored to the
plugin build in the same change); and the harmonization question answered on record —
NO shared vite version required, the boundary is bundler-blind runtime ESM, peer majors
are what must match and the manifest enforces them mechanically. workbench.md §4
amended in place; HK-11 filed born-decided; delegations to voice (UI-17 corrections +
the Monaco task) and bridge (UI-18 refinement + workbench_split.md amendment) committed
in the entry. IMPL-1 unblocked — the sprint's commons chain is now
council✓ → shell. docs: none — design record amended in place.

## 2026-07-15 — sprint-02 PLANNED: the Workbench arc (shell + full config-ui port)

Second run of the sprint machinery: scoping + two selection rounds, the second REDONE
mid-flight on the owner's flag that bridge had closed a burst of eMotiva tech debt —
the bridge keeper's delta (SendMessage, context intact) absorbed 7 closures (LIB-1/2/3
= the new LIB workstream + pymotivaxmc2 0.8.0 on PyPI, OPS-29, SCN-18, DRV-39 with
DRV-40 folded), moved the shippable line to pytest 734, rewrote DRV-38 [P1] as the
validation replay of the fresh fail-closed stack, and flagged the WB7 as running
pre-DRV-39 code — whence decision 5: the bridge deploy runs EARLY in-sprint, safety-
relevant, with the fail-closed/`force` briefing and the OPS-26 verify folded in.
Selected 7.3/7.4 (12 sessions, 30% reserve, bench 0): the commons Workbench arc
(runtime-assembly COUNCIL per owner directive — seeds as the next HK, amends
workbench.md §4, IMPL-1 depends on it; IMPL-1 shell; IMPL-2), voice's port arc split
per §4 from the XL-in-disguise "fully ported" (fresh IDs UI-18 foundation / UI-19 port
body / UI-17 narrowed to plugin conversion, + UI-16 riding its declared travel-with),
bridge UI-18 (read-only plugin cut — the two-real-plugins rule wants it beside the
voice port) + DOC-17, satellite OPS-8 + the D-17 marker chore. Owner decisions
recorded: ARCH-50 explicitly deferred (not starved), bench stays 0 with the DRV-38
attempt-slot offered and declined, no XL selected (DES-5 and the bridge wireframe
session wait), PROD-4 council deferred again — all write-gated work stays dormant.
docs: none — planning artifacts only.

## 2026-07-14 — sprint-01 CLOSED: 7.3/7.3 landed, plan-to-close in one day

The first sprint of the HK-9 machinery closed the day it was planned. Read-only
verification against all three shippable definition lines: voice @3bf39ce (guards green
at pinned tags, repin-check green with every pin at owner-newest incl. catalog-v1.7,
suite 1415/7 journal-evidenced), bridge @5da5c96 (guards green, ui check green live,
heavy gates CI-evidenced unbroken; UI-17 DONE with workbench_split.md spawning
UI-18/CORE-12/DOC-17; OPS-13 DONE with UI-8 absorbed), satellite @91e7bee (all four
guards green, OPS-7 DONE verified live, ssh branch honestly flagged). All three:
SHIPPABLE. The two product caveats — voice's QUAL-78 fix not yet in a published image,
bridge's vite-6 UI image + the still-unrecorded post-OPS-26 redeploy — land exactly in
the pre-reserved close-deploy slot (owner op, scheduled not run; deployable ≠ deployed
held). Realized table: 7.3 of 7.3 session-equivalents, every row at its planned class
cost, both councils in budgeted rounds, reserve spend 0.1 of 3.6, ≈9 items discovered
and filed. Calibration headline for sprint-02: relative costs are exact but absolute
throughput ran ~3–7 s-e per attended session — HK-9's ~10× anchor reconfirmed at sprint
scale. Carry-overs pre-staged for sprint-02: voice UI-17+UI-16, bridge UI-18+CORE-12,
the HW set, IMPL-1/IMPL-2, the now-load-bearing PROD-4 council, and the owner-announced
bridge remote-wireframe session. Close section + review appended to
`board/sprints/sprint-01.md`; page chip → closed. docs: none — sprint/journal
artifacts only.

## 2026-07-14 — satellite intake finding: split rows must not mint letter-suffix IDs

Satellite executed its sprint-01 intake (their a181f5d + be84ea4): the OPS-1 split
landed as **OPS-7** (model-pack publish flow, PROD-16 amendment absorbed, execution
questions recorded) + OPS-1 narrowed to the firmware half, dormant until FW-1. The
wrinkle they caught and correctly reported upstream instead of fixing silently: the
sprint coordinator pre-named the split half "OPS-1a", and scope-guard's declaration
regex + aliases table are numeric-only BY DESIGN — the row parsed as prose (the guard's
own per-prefix count exposed it). Their resolution is now the convention:
`process/sprints.md` §4 amended — split halves get FRESH NUMERIC IDs at intake,
letter-suffix labels are sprint-page display names only, recorded in the fresh task's
text for traceability; the /sprint skill gained the same rule. This was the
coordinator's own deviation from §4's existing "no new syntax" clause, so the fix is
remediation, not a new decision; teaching the guard suffixes was rejected (parser +
aliases complexity for zero benefit). Sprint file annotated (OPS-1a → OPS-7).
Discovered work, S-class, first draw on the sprint's reserve (0.1). docs: none —
process convention + sprint artifacts; no manifest node touched.

## 2026-07-14 — PROD-10 ④ ui-kit-v1 LANDED; PROD-10 CLOSED (all four stages in one day)

`packages/ui-kit` = `locveil-ui-kit` 0.1.0, tagged **ui-kit-v1**: 17 radix-based
primitives on the council's tokens — including StatusChip/StatusDot implementing the D8
recipes with the tested-stays-blue pill contract, and an Icon component that OWNS sizing
(16/20px; the extraction's `!w-*` override pattern is structurally impossible now) —
plus the tailwind preset, version-agnostic ESM + types (deps externalized; vite majors
per-consumer, honored), eslint-9 flat config, and the Storybook workbench with a
dual-theme toolbar whose assembly story is the council's round-2 mock rebuilt on the
real components. Verified end-to-end: install (0 vulnerabilities), typecheck + lint,
lib build, storybook build. One build wrinkle caught live: vite's emptyOutDir wiped
tsc's declarations — build order flipped. Deployment-class ruling recorded from the
owner Q&A: ONE kit for workbench AND operations; the future controller-UI council adds
token sections/profiles (island retune, touch density), never a second kit; bridge
composites stay bridge-owned, built ON the kit. PROD-10 moved to BOARD_DONE — write-backs
voice UI-17 + bridge UI-17 both on record via PROD-24; delegated adoption executes
cross-sprint as declared. Sprint-01: c-uikit realized at its planned 1.0 — the entire
PROD-10 backbone (①②③④, 4.0 planned) landed on planning day; remaining sprint rows:
bridge UI-17 execution, satellite OPS-1a. docs: stylebook — node covers the ui-kit
surface; the package README is the consumer doc.

## 2026-07-14 — PROD-10 ②+③: style council decided, tokens + stylebook + ui-style landed

The style council ran exactly as designed — two rounds of rendered choices, zero design
vocabulary asked of the owner. Round 1 (nine cards, all real workbench slices with
config-ui's actual RU content): owner seeded "blued steel, island stays black-ish" and
picked steel-A «Воронение» neutrals, then diverged from the recommendations into a
coherent monochrome-metallic identity: STEEL-BLUE accent (over the incumbent amber),
SPLIT icons (lucide stroke in chrome, Material filled stays inside the island — the
backend manifest contract untouched), 0.75rem chrome radius (rounder than stock);
compact density, system type stack, status tokens and all three confirmations (dual
theme, shadcn/radix, fluid-remote) accepted as recommended. Two owner notes recorded:
the island ships as-is AND the remote wireframe/layout rework — including D10's fluid
implementation — happens in a dedicated bridge-project session (bridge files it at that
intake). Round 2 (the assembly — one full mock, both themes, all picks applied): accepted
first pass; accent = polished dark calibration; the one collision the choices created
(tested-chip blue vs accent blue) resolved by owner ruling KEEP BLUE — the pill shape
carries the status-vs-interaction distinction. ③ transcribed the outcome:
`packages/ui-kit/tokens/locveil.css` + `.json` (the package seed), the stylebook
(`docs/design/ui/stylebook.md`) with a new `ui-kit` manifest surface + `stylebook` node,
and the `ui-style` skill as the executable half (already registered in-session).
frontend-design + skill-creator installed by the owner. Sprint: c-council realized at
1.0 (2 rounds, no reserve draw), c-stylebook at its planned 1.0 same day. Next: ④
ui-kit-v1 — fully unblocked (OPS-13 done, shell contract decided, tokens decided).
docs: stylebook (new node; manifest gains the ui-kit surface).

## 2026-07-14 — PROD-10 ① extraction landed: token inventory + divergence list

The sprint's critical-path head, executed with the owner's evidence-tier ruling (remote
pages + remote scan = the only approved taste; appliance pages and all of config-ui =
inventory only; even the remote's rigid layout is non-sacred — zoning yes, geometry no).
Two miners over the repos + the scan read directly. Headline finds, both
assumption-breaking: (1) bridge `ui/` is a stock shadcn/ui install in all but name —
full CSS-variable semantic theme at DEFAULT values (adopted, never chosen), cn()/cva,
components/ui/ — so the Locveil tokens file is "fill in the variables", not invent a
system; (2) @mui/material + emotion have zero imports — the MUI-vs-Tailwind divergence
everyone assumed does not exist; the only Material reality is the icon set, whose names
are a backend layout-manifest CONTRACT (icon-family change = mapping layer, D1). The
approved tier-1 system is the dark remote island: #2a2a2a metal shell, white-alpha
surface ladder, rounded-square ghost buttons, amber attention, green/red power
semantics, 200ms motion, px radius ladder 24/16/12/8 — extracted into
`docs/design/ui/token-inventory-draft.md` with file:line evidence. The stiffness is
documented as mechanism (fixed 320×850 container, two hand breakpoints, scale-75
NavCluster hack, runtime <style> blob) → fluid-rebuild requirement D10.
`docs/design/ui/divergence-list.md` = the stage-② council agenda: D1 icons
(material/lucide/split), D2 amber-vs-blue accent, D3 neutrals+primary (candidate: derive
from the island's warm greys), D4 dark-mode policy, D5 chrome radius, D6 type stack
(system vs Cyrillic-complete webfont, offline-first constraint), D7 density, D8 semantic
status tokens (the one near-deliberate config-ui system, preserved), D9 shadcn adoption
(verdict: strong yes), D10 fluid remote. Both artifacts anchored by PROD-10 (HK-10
rule). Tooling prep: anthropics/skills cloned; the frontend-design + skill-creator
install into .claude/skills/ was permission-gated — owner runs the cp (command in the
session log). Next: build the style-council round-1 page from D1–D10. docs: none —
design/evidence artifacts, anchored by PROD-10; no manifest node touched.

## 2026-07-14 — HK-10 DECIDED: evidence anchoring + the IMPL prefix; IMPL-1/IMPL-2 filed

Born-decided owner rulings, triggered by the question "where is the Workbench shell's
implementation task?" — answer at the time: nowhere, just the design doc. Ruling 1:
every design AND review doc must be referenced by at least one ledger entry (open task
while scope is unexecuted; completion entries anchor executed docs) —
`process/ledger-discipline.md` gains §6, commons `[evidence] dirs` gains `docs/review`,
and the missing mechanical direction (doc on disk, zero ledger references) is filed as
IMPL-2 (scope-guard UNREFERENCED check, next scope-vX cut, consumers adopt on re-pin).
The decision-time sweep found exactly one true orphan proving the point:
`fixture_recorder.md`, pre-board and implemented, now anchored by the HK-10 entry.
Ruling 2: commons-local implementation work gets the IMPL prefix (registered in
`.scope-guard.toml`, new `## IMPL` board section; IMPL collides with no product
workstream, unlike BUILD/CORE). First filings: IMPL-1 — Workbench shell v1
(`packages/workbench`, implements `docs/design/workbench.md` §3–4, gated on ui-kit-v1,
plugin content via the two UI-17s, sprint-02 candidate; simultaneously the design doc's
anchoring task per ruling 1) and IMPL-2 (above). Sprint-01 note: both IMPL tasks are
new-scope discoveries — reserve items if pulled in, else sprint-02 rows. docs: none —
process file updated in place; no manifest node invalidated.

## 2026-07-14 — PROD-24 CLOSED: all three write-backs in, entry moved to BOARD_DONE

Filed, council-decided, design-doc'd, delegated, and closed within one day. The three
repos pulled their delegations and wrote back: voice — **ARCH-51** (satellite-local
config endpoint design) + **UI-17** (config-ui → Workbench plugin, the grown sprint-02
adoption task); bridge — **UI-17** (its own serial — the repos coincidentally minted the
same ID; cross-repo references must say "bridge UI-17" / "voice UI-17", which bridge's
entry itself flags); satellite — **DES-5 expanded in place** (broker, verb vocabulary,
workstation operator credential; its reconciliation mapped today's CLI `revoke` to the
board's `reject-pending`) + **OPS-6** (the ansible-rework earmark). All five IDs verified
present in the sibling ledgers before the move (the board never asserts their status —
they were verified to EXIST, nothing more). Close condition per board convention:
commons deliverable landed (`docs/design/workbench.md`) + all delegations have local IDs
written back. Sprint-01 note: both PROD-24 rows (split doc M·0.5 + shell council
council·0.5) realized at their planned cost on planning day. What PROD-24 leaves behind:
the Workbench design doc as the normative UI-split reference, the PROD-4 item (4)
amendment (write convention + auth, now load-bearing for sprint-02), and the dormant
reserved-verbs table waiting on DES-5. docs: none — ledger/journal move only; the design
doc's verdict was recorded at its own landing.

## 2026-07-14 — PROD-24: deploy-split design doc landed (`docs/design/workbench.md`)

The sprint-01 `c-split` row, executed as transcription of the decided council:
`docs/design/workbench.md` codifies the three-plus-one UI classes, the full per-surface
classification table, the shell spec around the checked-in wireframe
(`docs/design/ui/workbench-wireframe.png`), the plug-in contract v1 (runtime-registrable
pages, per-page backend targets, status slot, dormant gates), the DEV-PHASE
config-ownership/staged-write model with the owner's productization deferral quoted and
PROD-4 named as the convention home, the satellite reserved-verbs table with named
gates, the v1 auth posture (trusted-LAN documented, guard slot reserved, no write API
before PROD-4), the deferred reporter, sequencing/non-goals, and change control
(commons owns shell+contract; products own plugin content). One design decision made
here rather than left open: the dev-phase plugin consumption mechanism = `file:`
dependencies on sibling repos' BUILT plugin packages (the eval framework's sibling-path
pattern; honors the bridge's no-TS-source-imports condition), final distribution
deferred to productization like the write model. PROD-24 stays [>] on the three
write-backs (satellite DES-5 expansion, voice endpoint + adoption growth, bridge
UI-17). docs: none — contributor-facing design record; the commons manifest carries no
design-doc class (its nodes are front-door/contributor/reference), and no existing node's
coverage is invalidated by this addition.

## 2026-07-14 — PROD-24 shell council DECIDED: the Workbench wireframe + plug-in contract

Tenth council, two rounds, all three keepers, seeded from the PROD-24 entry plus the
owner's hand-drawn wireframe. The sketch survived intact: shell chrome (logo · one tab
per plugin · Material BugReport problem-button) + sidebar of the active plugin's pages +
content area; repo = plugin; React 18 SPA in commons `packages/workbench`. Round 1
produced the classification table (voice config-ui → workbench with voice's operations
column empty by design; bridge `ui` + appliance pages stay operations, the three setup
pages → workbench; landing page = third class) and three conflicts. Round 2's headline:
the owner OVERRULED the CLI-only reading of satellite D-17 — cert CLI functionality must
be replicated in the UI — and the satellite keeper absorbed it without breaking the
privilege boundary: one controller-side privileged broker, CLI and page as peer clients,
D-17 second amendment via an expanded DES-5 (which also inherits the workstation
operator-credential design and the ansible-rework OPS earmark). The three keepers then
converged independently on ONE write model: staged proposals via controller APIs +
explicit human promotion to the canonical repo (bridge), ownership classes separating
repo-owned from device-owned targets (voice), narrow-verb broker for privileged ops
(satellite) — landed as the DEV-PHASE convention with the owner's explicit ruling that
the final design defers to a further productization step; the convention's home is
PROD-4 item (4), whose "bridge needs none" claim this council falsified (amended in
place). Reporter pipeline deferred out of v1 (button stays; PROD-19 owns the fallback).
Bonus reality from the keepers: voice's desktop satellite runs the exact same CSR flow
and becomes the provisioning page's test target; config-ui's destiny is 6 pages (Overview
+ own top bar retire into chrome, a per-plugin status slot preserves health visibility).
Delegations committed in the entry: satellite DES-5 expansion, voice satellite-config
endpoint design + adoption-task growth, bridge UI-17 growth + planned-docs DOC follow-up.
Remaining commons deliverable: the deploy-split design doc (sprint-01 row) codifying it
all. docs: none — board/journal artifacts only; the design doc (with its manifest node)
is the follow-on deliverable.

## 2026-07-14 — sprint-01 PLANNED: first run of the /sprint machinery (PROD-23)

Three rounds on one page URL: scoping (round 0), two selection rounds. All three keepers
ran in contributor mode with fresh dependency closures — the round found PROD-10 had
ZERO intake anywhere (no voice or bridge task mentioned ui-kit; the owner's
controller-vs-workstation split was unfiled everywhere). Theme: ui-kit package +
stylebook (PROD-10) + first-sprint calibration; 12 sessions, 30% reserve, 0 bench slots,
no exclusions → usable 7.4, selected 7.3. Landed `board/sprints/sprint-01.md`. Decisions:
OPS-13 runs first and ui-kit targets eslint-9/vite-6 (HK-7 must-not-run-twice honored);
CORE-8 rides with PROD-4 (sprint-02 council candidate); UI class naming decided —
**operations / workbench**, the workstation shell is the **Locveil Workbench**. The
owner's round-1 comment (wireframe + how repos plug panels into the shell) was new
scope, not implicit: filed as **PROD-24** (deploy-split design doc + shell council;
PROD-10 ④'s component boundaries consume its output; must reconcile satellite D-17's
CLI-not-page ruling). Round-1 raw pick ran 9.0/7.4 — rebalanced by declaring voice
ui-kit adoption + UI-16 cross-sprint (travel together into sprint-02 riding ui-kit-v1)
and trimming the style council to 2 budgeted rounds. Keeper side-finds recorded in the
sprint file for pull-at-intake: voice ci.yml guard-version prose + BUILD-14 old repo
name; bridge UI-8 fold, OPS-14/CORE-7 stale BUILD-21 gates, unrecorded post-OPS-26
redeploy (close-deploy slot verifies); satellite DES-4 v1.1-tag wrinkle + the sprints.md
§6 post-DES-3 vacuity note. First calibration sample for §8's realized table comes at
close. docs: none — planning artifacts only (board ledger + sprint file; no user-facing
docs surface changed).

## 2026-07-14 — PROD-23 CLOSED: /sprint skill built, both HK-9 side-finds executed

Closed the same day it was filed. The skill (`.claude/skills/sprint/`) is the council
pattern extended with live math: the selection page's rows carry cost/bench/deps data,
checking a row auto-pulls its dependency closure, and the fill gauge computes usable
capacity as sessions minus reserve minus the pre-reserved close-deploy slot — "the can
is full" is now a red bar, not a judgment call. Scoping and selection pages share the
council's delta-only Copy machinery under a `sprint-reply` grammar. Both side-find
delegations executed directly (owner instruction, quick-task precedent): voice DOC-13 —
the stale-gate sweep found FOUR stale gates, not two (ARCH-42/43 AND BUILD-18 all still
"gated on BUILD-21", closed 2026-07-11 — re-anchored to commons PROD-8/PROD-4; UI-4's
Gate-2 block discharged since the remediation core is fully DONE; the sequencing block's
"QUAL-29 remains" corrected); bridge DOC-16 — VWB-39's dep line re-anchored (VWB-38's
artifact exists since 2026-07-12; the implementation dependency is DRV-37, not "DRV-36's
implementation"). The QUAL-82→VWB-33 gate checked and verified LIVE — the audit
distinguishes stale from standing. Both repos' guards green; write-backs on the entry.
docs: contributing (the Sprints process row).

## 2026-07-14 — HK-9 DECIDED: sprint planning convention landed, /sprint skill filed as PROD-23

Ninth council, two rounds, all three keepers, accepted (no-changes) both rounds after
one owner delta. Round 1 settled the mechanics: capacity in owner-attended sessions +
a separate bench-slot budget (the calibration table killed calendar estimates —
BUILD-36's own keeper predicted 4.5–5 days, reality was 2h45m), S/M/L/XL classes with
no-data legal for satellite HW, 30/50% discovery reserve, a commons sprint file that
lists IDs but never asserts status, deps computed fresh per sprint (the audit found
live stale gate prose in both product ledgers — the reason a standing deps: field
waits for v2), travels-with groups as atomic rows, refusal-grade HW gates. Round 2
took the owner's philosophy additions and the keepers converged hard: the shippable
invariant binds each repo's EXISTING deployability gates via per-repo definition lines
(nothing invented; deploy itself = one pre-reserved owner slot), cut atomicity rather
than group confinement, HW-GATED members cross-sprint by default with mandatory
carry-over rows, plain sprint-NN naming (all three independently flagged date/release
shapes as pre-empting the parked release-numbering council), and SHA-in-sprint-file
over repo-side sprint tags — voice put the principle best: tags mark what a repo
asserts about itself; sprint participation is a planning fact, and planning facts
live commons-side. Landed: `process/sprints.md` (normative), PROD-23 (build /sprint;
carries the two S-class side-find delegations to voice and bridge), HK-9 →
BOARD_DONE. docs: none — process convention + board artifacts only.

## 2026-07-14 — BUILD-36 tail confirmed live: the HK-8 migration is fully deployed

Commons verification of the WB7 cutover: voice's journal records the scripted sequence
(git pull → `cutover-env-locveil-voice.sh` .env token-key rename → update.sh →
`/health` smoke) on image v20260713-a946dab, code == HEAD, no breakage-BUG; and a live
probe from here confirms `/health` → healthy, v0.5.2 — the renamed image family
answering on the controller, which also proves the `LOCVEIL_VOICE_*` env cutover
end-to-end (boot consumes the config-file key). With this, the ENTIRE HK-8 arc is
deployed reality in every repo and on the controller. One residual observation, not a
bounce: the hand-edited secrets key's soft-fail path (reports silently off on a typo)
is not exercised by a /health smoke — one «сообщи о проблеме» utterance through the
controller would prove the reports pipeline post-rename; owner's call, zero urgency.
docs: none — board only.

## 2026-07-14 — PROD-22 CLOSED: contract-guard-v2 vendored everywhere — the rule caught two more on arrival

The re-vendors executed directly by the commons session on owner instruction, filed
under each repo's own discipline (voice BUILD-37, bridge OPS-27, satellite OPS-5 —
satellite added to the delegation list at execution; the bridge-filed original named
two repos, the guard has three consumers). The story is the rule's instant payoff:
TAG-MISSING fired in bridge AND satellite — both had stamped `docs-manifest-v1`
without ever creating the tag, the 2nd and 3rd instances of the false green the bridge
caught manually at catalog-v1.7. Tags created at each STAMP's landing commit, pushed.
Voice was fully clean. Every guard green in all four repos; the satellite's three-stage
hook (scope + contract + its own surface checks) made a nice showing. Two small craft
notes: both product-ledger insertions initially landed past a section header (MISFILED,
caught by each repo's own scope-guard within seconds — the guards disciplining the
coordinator again), and voice's remote flagged a bypassed branch-protection rule on
push (owner-auth bypass; worth an owner glance at whether main-protection is intended
to bind these sessions). docs: none — board only.

## 2026-07-13 — PROD-21 CLOSED: both HK-8 migrations verified; the bounce loop worked both ways

Voice's bounce fixes verified: 8/8 discovery_paths flipped, zero IRENE_* left in the
config tree, the env-override syntax examples now teach the live LOCVEIL_VOICE_ form.
The demanded tripwire proof delivered more than asked: it DISPROVED the bounce's own
"boot-breaking" severity — IntentHandlerManager discovers from a hardcoded namespace
and never reads config discovery_paths; the field is plumbed but dead (all 8 handlers
resolved against the stale value, x86_64 boot healthy). Flipped anyway for config
honesty; dead-field removal flagged voice-side as a separate call. So the verification
loop corrected the executor AND the verifier in one round — the record stays honest in
both directions. PROD-21 closed with both repos structurally identical
(backend/src/locveil_* + root config/ + root docker/), catalog at v1.7 in both pin
copies, contract-guard-v2 pending consumer re-vendors (PROD-22). BUILD-36's tail (arm
images, scripted WB7 cutover) rides the voice ledger. Also noted: voice filed ARCH-49 —
the quiet-ledger window HK-8 executed inside is closing exactly on schedule.
docs: none — board only.

## 2026-07-13 — BUILD-36 verification: BOUNCED on the 8 discovery_paths lines

Second bounce in the board's life, and it validates the model-choice reasoning: the
Opus-executed BUILD-36 is clean on everything the machinery can see (layout, zero
`irene` imports, 175 pyproject refs, aliases, `config/` singular, docs sweep, even the
opportunistic v1.7 catalog re-pin) — and missed exactly the string-as-data class the
keeper flagged as the hard part: all 8 config files still say
`discovery_paths = ["irene.intents.handlers"]` against renamed `locveil_voice.*` groups
(boot finds no intent handlers), plus stale `IRENE_*` env comments sitting precisely
where the operator reads during the cutover's one hand-edited step. No test can catch
either; only boot verification (still running when verified) or a reader. Bounce text
committed in PROD-21 with two precise asks + one tripwire-proof request; the runtime
`irene.toml` filename noted as legal deployment identity. docs: none — board only.

## 2026-07-13 — PROD-21 bridge share VERIFIED (Opus execution); PROD-22 filed by bridge and EXECUTED

The first Opus-executed delegation, verified against the HK-8 checklists: **CORE-10** —
`src/locveil_bridge/` renamed, ZERO living `wb_mqtt_bridge` refs in code/toml, scripts
`locveil-catalog`/`locveil-openapi` live with `wb-api` retired, import-linter 6/6 under
the new name, catalog-v1.7 STAMP + UI types + contract openapi all carrying the new
module names; **CORE-11** — `config/` at repo root (update.sh rsyncs `../config`),
`docker/Dockerfile.{backend,ui}`; **OPS-26** — executed same cycle,
`driver_name="locveil-bridge"` live. Unit suite 625/625; both guards green. One cosmetic
fleck accepted, not bounced: 3 inert `sys.path.insert` lines survive in tests (one WAS
on the checklist; all point at a directory with no importable package — zero effect;
bridge cleans opportunistically). **The round's real prize: bridge caught a FALSE GREEN
in commons' own tool and filed PROD-22** — the catalog-v1.7 STAMP passed contract-guard
while the tag it named didn't exist (owner created it manually). Commons executed
same-day: contract-guard 1.1.0 adds `TAG-MISSING` (owned STAMP's tag must resolve as a
local git tag object; remote push out of scope), functional-tested, tagged
**`contract-guard-v2`**. Bridge + voice re-vendor on their write-backs. Model note for
the record: Opus handled the mechanical delegation cleanly — the checklist+guard
machinery did exactly the job it was built for. Voice's BUILD-36 still in flight.
docs: none — tool README updated (not a manifest node); board/ledger otherwise.

## 2026-07-13 — HK-8 DECIDED: Python layout & naming convention → PROD-21

Three rounds, and the measurement discipline paid for itself twice. Round 1's asymmetric
proposal (move voice's layout, rename only bridge) died against two owner corrections —
voice IS multi-component, and "if we rename at all, we rename everything" — plus a format
mandate that reshaped keeper output for good: human-interpretable blast radius tables.
Round 2 vindicated the mandate: forced to re-price its "minefield" under deployment
reality, the voice keeper found its own three alarms hollow (zero external plugins; the
deployed config is DERIVED — update.sh overwrites it from the repo; prod state on a bind
mount, not ~/.cache) and withdrew opposition — uniform rename signed at an honest
~4.5–5-day one-churn price. Round 3 leveled the bridge config tree to root (conceded:
"the asymmetry was historical, not principled" — ~3 hours, no contract cut) and
consolidated its Dockerfiles to root docker/ (per-component files RIGHT for bridge by
OPS-11's arch-identical finding, per-arch RIGHT for voice by its ML profiles — location
mandated, file axis dialect); eval_commons stays under the principled rule the owner
ratified. End state: voice and bridge become structurally identical
(backend/src/locveil_*/ + backend/tests/ + UI peer + product data at root incl. config/
singular + docker/), satellite and core-py inherit via the template. Landed:
process/python-layout.md, PROD-21 (voice BUILD-36; bridge CORE-10/CORE-11/OPS-26, all
with keeper checklists as reconciliation baselines), template/CONTRIBUTING/process-README
pointers, HK-8 → DONE. Craft note recorded: never queue additions to a mid-flight
keeper — the message stranded silently; re-engage on notification. docs: contributing.

## 2026-07-13 — asyncwebostv + pymotivaxmc2 moved into the locveil org (owner libraries)

Org housekeeping, owner-decided after a CI analysis: the two owner-authored PyPI
libraries the bridge depends on (`asyncwebostv==0.4.0`, `pymotivaxmc2==0.7.0`, exact
PyPI pins — consumption unchanged by design) transferred `droman42/*` → `locveil/*`.
Sequence per the runbook: PyPI trusted publishers for the `locveil` identities added
BEFORE transfer (both workflows publish via OIDC trusted publishing — no tokens, no
secrets to migrate; the old `droman42` publisher entries get removed after each
library's first successful org-side release), org Actions policy verified by owner,
transfers executed, local remotes re-pointed, living old-owner references fixed in the
same pass (archives/CHANGELOG untouched — history stays; the `droman42/py-dev-gates`
composite-action refs deliberately untouched: it is public, callable cross-owner, and
its own move is EXPLICITLY DEFERRED by owner decision). Post-transfer CI validated
live: asyncwebostv's org-side run green, pymotivaxmc2's in progress at journal time.
Libraries stay lightweight — org membership does NOT mean the Locveil process kit;
they keep their own lifecycle. Residual: the first `v*` release of each validates the
new trusted-publisher binding end-to-end. docs: none — sibling-library op, no commons
manifest node describes it.

## 2026-07-13 — PROD-10 amended: the design-phase shape (sketch-to-stylebook pipeline)

Out-of-council owner discussion, recorded onto the entry: the owner is not a UI
professional and expresses intent by sketch and plain words — and the record shows that
works (the bridge remote UI was built from a scanned paper drawing,
`docs/design/ui/remote.png` → `RemoteControlLayout.tsx`; the sketch carried zoning and
hierarchy completely). PROD-10's design phase is therefore shaped as: (1) extraction —
reverse-engineer the implicit token system from the two shipped UIs + the scan;
(2) a style council eliciting preferences via RENDERED A/B dossier pages (clicks become
tokens; no design vocabulary required from the owner); (3) codification — tokens →
stylebook (manifest node) → ui-kit on the tokens → a `ui-style` skill as the executable
half, versioned with the package. Tooling prep noted: frontend-design + skill-creator
skills, Storybook as workbench. Standing rule recorded: owner sketches are first-class
input. docs: none — board entry amendment only.

## 2026-07-12 — HK-7 DECIDED: the open-task triage → PROD-4 reframed, PROD-18/19/20 filed

The board finally metabolized the pre-board backlog. Two keepers swept 63 open tasks
complete (voice 26, bridge 37) and the strongest finding was restraint: ~51 stay
repo-local, 5 already ride correctly, and the entire cross-repo residue fits in one
reframe and three entries. The reconciliation catches were the story — BUILD-28's board
seed had silently misfired ("seeded when BUILD-21 lands"; it landed, nothing happened);
VWB-33/VWB-34 have been asking for the board by name since before it existed; BUILD-14's
claimed bridge twin turned out not to exist; the master→profiles gate was STILL filed
nowhere (voice now files it regardless); and voice carries two open tasks about the same
flaky test with contradictory measurements. Owner rulings: PROD-4 reframed in place to
deployment coordination (readiness contract as named dependency — health-gated compose
over a lying /health would be fiction; CORE-8 secrets posture joins, the committed
broker password's rotation is a near-term op); PROD-18 with the one-cut-one-re-pin
binding condition; PROD-19 small; PROD-20 as the round's one flip — the owner chose
board visibility for the satellite first-light burst over repo-to-repo silence
(HW-GATED, no timing asserted). BUILD-13 stays voice-published. PROD-10 gained its
sequencing note. Product sessions pull the reframed/new delegations at their leisure —
nothing here is release-gated. docs: none — board/ledger artifacts only.

## 2026-07-12 — PROD-17 CLOSED: all three delegations verified; commons executes its own piece

The docs convention went org-wide in one afternoon. Verified: **voice** (DOC-11/12,
BUILD-35) — the :6000 quartet and the WS example are gone (the two remaining grep hits
were `sample_rate: 16000`), QUICKSTART's post-split mislabel fixed, manifest + 8/8
coherence test, dialect updated with `ops/INSTALL.md` in scope, guard v5 byte-identical
(voice chose the stricter `docs_verdict_since = 2026-07-12`); **bridge** (DOC-13/14/15,
OPS-24) — ADRs dissolved and archived with banners, the 0006 dependency policy lives in
CONTRIBUTING with OPS-19 re-pointed, NINE diagrams verified (four beyond the flagged
five), and the OpenAPI description scrub was correctly treated as a contract cut:
**catalog-v1.6** tagged; **satellite** (OPS-4, all three items) — a 7-node manifest with
3 pending-gate slots naming their gates ("FW-1 first light", "first board reaches
bench-verified"), its first CONTRIBUTING.md, the provisioning README stripped of
tracking refs and the `.pio` line. **First live catch by the HK-5 staleness gate:**
voice's `repin-check` reports both catalog pins trailing v1.6 — exactly the designed
release-time lane; the next `make repin CONTRACT=catalog` clears both copies in one run.
Commons then executed its own piece: `docs/manifest.json` (4 nodes) +
`contracts/docs-manifest/` @ docs-manifest-v1 + registry row + CONTRIBUTING.md +
`eval/tests/test_docs_manifest.py` — whose first two runs FAILED on commons itself
(schema rejected `$comment`; contract-guard demanded the registry row): the machinery
biting its author twice before passing 46/46. PROD-17 moved to DONE with its verdict
line. docs: contributing, contracts-registry.

## 2026-07-12 — HK-6 DECIDED: user-facing docs convention + the docs manifest → PROD-17

Two rounds, three keepers, and the owner's mid-council invention became the centerpiece.
Round 1 root-caused the docs-rule failure with unanimous precision: the only LAW with
zero mechanical enforcement and no artifact slot recording the verdict — live exhibits on
every side (voice's port-6000 quartet, missed by a commit that claimed to fix it;
bridge's REL-4 fixing 11 of ~22 docs at the release gate; the satellite's provisioning
README hardcoding the PlatformIO path its own DES-3 defers) — plus the template bug: the
rule never reached the satellite at all. Round 2 engineered the owner's docs-manifest
idea into machinery: a repo-internal contract (`docs/manifest.json` + STAMP @
docs-manifest-v1) whose coherence test makes the node policy a FAILING TEST instead of an
approval; pending-gate slots let the hardware repo sign the same floor without fiction;
surface→glob maps turn a diff into candidate nodes at completion time (the
false-positive machine relocated to where a false positive costs one dismissal clause);
`docs: none` became falsifiable; CONTRIBUTING.md moved INSIDE the manifest after
bridge's own drifted stale in under 24 hours outside the old rule's scope. Owner
rulings: ADRs abolished (one bridge dissolution task — 0006 is the only load-bearing
one), org README folds into PROD-9, no Russian docs today, operator docs in scope, floor
only where the capability exists, docs-review tasks fileable any time with commons-filed
ones fanning out org-wide. Landed same day: `process/user-docs.md` +
`manifest.schema.json`, **scope-guard 1.2.0 tagged `scope-v5`** (docs-verdict presence
rule, functional-tested; shared-invariants block gains the invariant, commons re-pinned
with `docs_verdict_since = 2026-07-13`), template seeds (skeleton manifest, CONTRIBUTING
stub, config key), HK-6 → DONE carrying the first verdict line written under its own
rule, PROD-17 with three delegations. Commons' own manifest + CONTRIBUTING remain
commons follow-up work under PROD-17.

## 2026-07-12 — PROD-16 satellite delegation VERIFIED (3/3) → PROD-16 CLOSED

The last write-back, verified: satellite's pins were **born stamped** — the parallel
voice session had tagged `ws-protocol-v1`/`wake-pack-v1` before the satellite pulled, so
the interim commit-pin step collapsed; both pins are strict, COMPLETE, and byte-identical
at their tags (checked against the tag contents directly). Conformance pointers honestly
respect the phase gates (FW conformance lands with FW-1 after DES-3 — no consuming code
exists yet, exactly the keeper's HK-5 condition). Bonus deliverables beyond the
delegation: satellite stood up its own **`esp32-site-v1`** owned surface (STAMP + tag
over the Plane-B template voice pinned pre-tag — voice's PIN fills version/tag at its
next re-pin), and its DES-4 intake caught that `device-integration-v1`'s tagged STAMP is
pre-convention (the core fix was post-tag) — the `v1.1` request routes repo-to-repo at
descriptor authoring, correctly. Guard byte-identical, 0 warnings, hook + path-gated CI;
stale README line fixed; OPS-1 amended with hash-at-publish. Write-back: OPS-3 + DES-4/
OPS-1 amendments (satellite `fcc6989`). **With all four delegations verified and every
write-back in, PROD-16 moved to `BOARD_DONE.md`** — decided, delegated, executed across
four repos, verified, and closed in ONE day. The org runs one contract convention:
eight family tags live, contract-guard everywhere, conformance in every CI. Recorded
residuals: crossover-fixtures strict PIN (next fixtures task), device-integration v1.1
(repo-to-repo), STAMP `artifacts` list + completeness rule (contract-guard v1.1).

## 2026-07-12 — PROD-16 voice follow-up (BUILD-34) VERIFIED and accepted (4/4)

The completeness ruling's first instance, verified: voice's `contracts/pins/catalog/`
holds the FULL `catalog-v1.5` set, all three artifacts byte-identical to the bridge's
tagged copies; strict PIN.json pointing at the new conformance test. `repin.py` now
carries both targets — one `make repin CONTRACT=catalog` stamps the local pin AND the
commons crossover pin at the same tag (divergence impossible by construction).
`test_catalog_contract_conformance.py` (5/5 live) binds `parse_catalog` and the emitted
`CanonicalActionRequest`/`RoomCanonicalRequest` wire bodies to the pinned schemas in
voice's normal CI — the push-time gap the voice keeper flagged in HK-5 is closed; the
commons crossover suite stays the release-cadence deep gate. Registry states the
division of labor; contract-guard on voice: 0 warnings. Write-back: BUILD-34
(voice `a51f709`). PROD-16 now waits only on the satellite delegation (in progress).

## 2026-07-12 — PROD-16 follow-up delegation to voice: the local COMPLETE catalog pin

Owner decision closing the pin-placement discussion: voice adds a local catalog pin —
COMPLETE per the same-day ruling (full `catalog-v1.5` artifact set, never a usage
subset), maintained by the same `repin.py` run that stamps the commons crossover pin
(one command, both copies, same tag — divergence impossible by construction), plus a
fast named conformance test in voice's normal CI binding its emitted-command shapes to
the pinned schemas. Division of labor now explicit: the commons pin remains the shared
crossover copy both product suites bind to (release-cadence deep gate); the voice pin
is the hermetic push-time stub (the protobuf property the owner asked for). Delegation
committed in the PROD-16 entry; voice files a local ID and writes it back.

## 2026-07-12 — PROD-16 ruling: pins are always COMPLETE (the IDL principle)

Owner ruling from the post-verification discussion of voice's catalog consumption,
landed in `process/contracts.md` §2: a pin is the owner's FULL tagged artifact set,
byte-identical — like a protobuf/IDL definition, you take the whole interface; what the
consumer uses never shapes the pin. This retracts the coordinator's "subset pin via the
files map" reading before it reached any tree — audit confirms every existing pin
(catalog ×1, report-protocol ×2, crossover-fixtures, esp32-site) already carries its
owner's complete set. Forward requirement recorded: from each contract's next bump the
owner STAMP enumerates its `artifacts` list, making completeness machine-checkable
(contract-guard v1.1 rule, not built yet). Noted, self-healing: the report-protocol
STAMP sidecar postdates the v1 tag, so pins carrying it hold one file the literal tag
lacks — aligns at v2. Still OPEN (owner has not decided): whether voice adds a local
COMPLETE catalog pin + in-repo conformance test to close its push-time schema gap, or
accepts release-cadence conformance via the crossover suite + repin-check.

## 2026-07-12 — PROD-16 voice delegation VERIFIED and accepted (5/5); PROD-7 closed as absorbed

Voice's five tasks verified against the convention, all clean. **ARCH-47**: tag
`ws-protocol-v1` + `contracts/ws-protocol/` STAMP (version + doc pointer + code-constant
pointer — no doc hash, as conditioned); the doc opens with "Protocol version: 1";
`WS_PROTOCOL_VERSION = "1"` in `irene/core/ws_protocol.py` feeds both the satellite link's
`register` and the server ack; the version-triple test exists and passes; `register` now
reports `protocol_version` + `firmware_version` + `wake_pack_version`. **Wake pack**:
exemplary sidecar stamp over the UNMODIFIED HF pack — per-file URL + sha256, with bump
semantics written down (add word = minor; replace published file = major, flashed hashes
stop verifying). **BUILD-24**: `scripts/repin.py` + `make repin`/`repin-check`; the first
scripted re-pin ran same-day INTO commons — catalog pin now strict (files hashes, family
tag) and the PROD-14-era openapi staleness is CLEARED (byte-identical again; commons
guard down to 1 by-design warning). **BUILD-32/33**: voice `contracts/` on the uniform
shape (pins: report-protocol, esp32-site; registry cross-references the commons-held
catalog/fixtures pins with rationale); guard byte-identical @ contract-guard-v1, hook +
path-gated CI, 0 warnings. **BUILD-26**: `ui-openapi` stamped as a repo-internal
generated contract — the STAMP versions the convention surface, not each regen; drift
guard in CI. Conformance tests run live: 16/16. **PROD-7 closed as absorbed by
PROD-16** — its entire scope (bridge tagging, voice scripted re-pin + staleness gate)
delivered under the rescoped VWB-29/BUILD-24; family tags superseded the old
`contract-vN` naming. Remaining on PROD-16: the satellite delegation.

## 2026-07-12 — PROD-16 bridge delegation VERIFIED and accepted in full (4/4, no bounce)

Commons verification of the bridge claim against the HK-5 convention, item by item.
**VWB-29** (the owner-side cut): `contracts/catalog/` layout ✓, STAMP carries the full
core + build extras ✓, tag `catalog-v1.5` sits on the cut commit ✓, `CONTRACT_VERSION`
constant lives in `presentation/api/catalog.py` and feeds both the stamp writer and the
drift-guard test ✓, registry README direction-labeled ✓, catalog README changelog KEPT
and continued with an honest v1.5 note ("changed no contract surface — it is the
convention cut") ✓. **VWB-40** (pin relocation): went STRICT immediately — full PIN.json
with `files` hashes, conformance pointer, and a lineage-honest `pinned_by` ("bytes
unchanged, tag-verified at both") ✓; the reports-repo lens was re-taught the new path in
`locveil-reports@ce1db63` ✓. **VWB-41**: committed `example.descriptor.json` +
schema-validation test — the model layout's own gap closed ✓. **OPS-23**: vendored
`contract_guard.py` byte-identical to `contract-guard-v1`, hook + path-gated CI, runs
**green with 0 warnings** (first repo to hit zero) ✓. Conformance suite run live:
18/18 across the three contract test files. One pre-existing divergence re-confirmed,
not new: the commons catalog pin's `openapi.json` is one rev stale (the VWB-35
schema-default drop, flagged at PROD-14 close) — rides BUILD-24 as recorded. Golden is
byte-identical, so the voice re-pin stays ordinary. Remaining on PROD-16: voice and
satellite delegations.

## 2026-07-12 — PROD-16 commons execution COMPLETE: contract-guard v1 + the restructure

Same-session follow-through on the HK-5 decision. Landed: **contract-guard 1.0.0**
(`packages/contract-guard/contract_guard.py`, stdlib-only, --check only; layout/registry/
STAMP-core/PIN-core/sha256/version-consistency checks; legacy pins degrade to warnings
until their next re-pin) tagged **`contract-guard-v1`**, wired into `hooks/pre-commit`
(after scope-guard) and a new path-gated `contract-guard` CI job. Commons `contracts/`
restructured to the uniform shape: catalog pin → `contracts/pins/catalog/` (regime-1
semantics preserved, per-pin README), fixtures → `contracts/pins/crossover-fixtures/`,
and commons' own **report-protocol machine core moved home** to
`contracts/report-protocol/` with its STAMP sidecar (tag `report-protocol-v1` untouched;
consumers hold verbatim copies — zero consumer impact). Registry README rewritten as the
direction-labeled index; CLAUDE.md regime text updated. Eval re-point turned out to be
FOUR path sets, not three — reconnaissance had missed `test_device_command_eval.py`;
found by running the suite, fixed, **40/40 green**. contract-guard runs green with
exactly 3 by-design warnings (catalog PIN legacy until BUILD-24; fixtures PIN pending
its next fixtures task). One cross-repo find written into the voice delegation: voice's
`eval/Makefile` + `device.promptfooconfig.yaml` reference the old commons contracts
paths — re-point rides BUILD-24 or the voice restructure task. Bridge/voice/satellite
delegations now unblocked to pull.

## 2026-07-12 — HK-5 DECIDED: the contract convention → PROD-16 (`process/contracts.md`)

The first parked seed convened, the first three-keeper council (satellite-keeper's debut —
it stale-flagged its own repo's README on arrival). One keeper round sufficed: the
inventories agreed on the diagnosis before the argument started. Corrections to the brief:
catalog is v1.4 not "1.5" (no version field, no `contract-vN` tags exist; voice's
15-clause prose `contract_patch` accumulator is the symptom), "PROD-7 in flight" was
optimistic (VWB-29 + BUILD-24 both unbuilt — which turned the redo into a near-free
coordinated cut), and commons self-flagged: `report-protocol.json` carries no in-artifact
version either. Unanimous core: two-layer enforcement — a thin vendored coherence checker
(`contract_guard.py`, commons regime 2, `contract-guard-vN`; scope-guard stays
ledger-only — satellite's decoupling argument beat voice's mild extension preference)
plus per-repo conformance tests, with owner-side guards mandatory from day one (the
bridge's own model layout, device-integration, lacked one — honest self-audit). Owner
rulings: uniform layout enforced IMMEDIATELY (`contracts/<name>/` owned +
`contracts/pins/<name>/` consumed + direction-labeled registry README; bridge's
grandfathering plea overruled); first tag `catalog-v1.5` — and a mid-landing correction
worth recording: README changelogs STAY as narrative, the STAMP + tag are the
machine-readable authority ("the stamp defines, the changelog narrates"); staleness never
a push gate (runtime version-reporting + release-time re-pin only). ARCH-47 ungated.
Landed: `process/contracts.md` (normative), PROD-16 with three delegations + the
commons execution list (contract-guard v1, commons restructure, eval re-point,
report-protocol STAMP), HK-5 moved from parked to DONE.

## 2026-07-12 — HK-5 parked: contracts-in-general council (owner seed)

Owner decision from the PROD-15 aftermath: voice ARCH-47 (the WS version stamp / wake-pack
pin surface) is NOT executed standalone — it rides the next council round, which will take
on the contract surfaces in general (five dialects and counting; seed text in the new
BOARD.md `## HK` parked-seeds section). Voice annotated ARCH-47 as gated the same day. This
is the first parked HK seed, exercising the "deferred council parks its entry here"
convention.

## 2026-07-12 — PROD-15 CLOSED — the satellite repo is real; cross-repo-board block @ scope-v4

The fastest board arc yet: decided (HK-4), delegated, executed on all three sides, and
closed in one day. Close condition: commons deliverables shipped with the decision; voice
wrote back BUILD-22 + ARCH-47; bridge wrote back DRV-34/35/36 + VWB-38/39; the satellite
born backlog is filed under local IDs in the new repo's own ledger. With a fourth sibling
on disk, the `cross-repo-board` shared block was amended to name `../locveil-satellite`:
source edit in `process/claude-blocks/`, tagged **scope-v4**, hashes re-pinned same day in
all four CLAUDE.mds (commons, voice, bridge, satellite); the new-repo-template examples
bumped to the new tag. `shared-invariants` is content-unchanged (its markers keep their
scope-v3 provenance).

## 2026-07-12 — PROD-15 voice delegation consumed — voice IDs written back

Voice pulled the delegation same-day, reconciled it (org repo confirmed created — owner
action done; the two reversals vs its frozen BUILD-22 text caught and recorded: nginx tree
moves, ARCH-23/ARCH-44 export-close), and filed locally: **BUILD-22** redefined in place
(items 1–5) + new **ARCH-47** (item 6 — the WS version-stamp / wake-pack pin / `register`
version-reporting surface). IDs written back into the entry. Bridge IDs still pending;
the entry stays open until they land and the delegated work needs no commons-side action.

## 2026-07-12 — HK-4 DECIDED: locveil-satellite bootstrap (four rounds) → PROD-15

The satellite repo gets its bootstrap decision — D-6/D-7 executed with dated amendments,
the first four-round council, and the first with a coordinator-only round. Both keepers
opened support-with-conditions and earned their keep in round 1: voice flagged that
brief item 3 was already-decided ground (QUAL-19 review done, DELETE verdict recorded),
bridge flagged the ESP8266 half-story (HVAC drivers are shipped bridge code, not movable
estate) and inverted the owner's doc-freshness assumption (the new general doc downgrades
bench-CONFIRMED facts to VERIFY — harmonize claim-by-claim). Net movable set: two voice
tasks + one bridge task + two folders. Owner pushbacks drove real design: round 2's
"build-time wake word" resolved as flash-time partition pin of voice's unmodified pack
(voice's own D-12 line held); rooms stayed provisioning-time (registry authoritative)
with a build-seed compromise; round 3 replaced WB-passthrough with a new descriptor-native
**EspManagedDevice** driver, went fully design-time on the contract (latency static — the
DRV-29 window was always firmware constants), and retired FR-1's single image after the
GPIO14 double-booking vindicated the owner's bench knowledge. Round 4 triaged the owner's
browser-researched toolchain: adopt the knowledge-side MCPs day one, defer BOTH execution
commitments (skidl-skills, PlatformIO) to mandatory satellite design tasks — the
PIO-platform-vs-latest-IDF tension is a fact-check (DES-3), not a blind bet. Landed:
PROD-15 (board umbrella + voice/bridge delegations + satellite born backlog DES-1..4,
OPS-1..2), D-6 amendment in `docs/design/productization.md` (nginx Plane B moves,
tether-cuts named; rest of the STAYS list reconfirmed), HK-4 → `BOARD_DONE.md`,
satellite-keeper agent authored. Council craft: the cancelled PROD-4 round's keeper
inventories fed straight into round 1 as promised; keeper cost was skipped in round 4
where no cross-repo stakes existed.

## 2026-07-11 — PROD-4 council convened and CANCELLED at round 1, no decision

Owner cancelled before answering the form — the round surfaced that the entry's purpose
(codify the hand-converged per-repo ops pattern) is not the owner's actual concern:
**deployment coordination** ("deployment and startup of the images is not coordinated is
a mess" — BUILD-28 territory, owned by no PROD entry) and a **bigger topic on contracts
in general** still forming. The PROD-4 entry stands untouched, `[ ]`, as if the council
had not convened. Session notes worth keeping: both keepers produced full ops inventories
and found the entry stale in 5+ places (units require more than the entry claims;
start-period is dialect not constant; `.env` lives in the runtime tree; both pre-named
delegation intakes worded around retired mechanisms; several proven patterns omitted);
voice identified the smoke's "systemic config issue" as BUILD-31's root cause — no gate
forces config-master→deployment-profiles reconciliation — and that follow-up is **still
filed nowhere**. To be continued when the owner's contracts framing is ready.

## 2026-07-11 — PROD-14 + PROD-6 CLOSED: the inbox story lands end to end

Bridge's delegation verified and ACCEPTED in full (VWB-35 re-point with the schema-default
drop + fail-fast validator + regen chain, VWB-36 lens re-review — including an honest
ID re-serial when the pre-named VWB-30 turned out consumed, VWB-37 protocol pin +
conformance 5/5, spool trivially drained — verified: no spool dir was ever created).
Voice's was accepted earlier today after one bounce round (ARCH-46: the §5/§7 lift-out).
With commons-side deliverables done and all delegation IDs written back, both entries
moved to `BOARD_DONE.md`. All three protocol writers are now pin-validated against
`report-protocol-v1`; the full loop is live and smoke-proven (ticket #3). Residuals, all
non-blocking: org base-permissions check (owner), ticket #3 close via `/inbox` (owner),
and one recorded flag — bridge's `openapi.json` changed, so the voice-side contracts pin
is one rev stale, riding the normal re-pin cadence (PROD-7 / BUILD-24). The verification
pattern itself (claim → check against the council agreement → bounce precise asks →
re-verify) got its first full exercise today and both product sessions closed the loop
same-day. Next council candidate, owner-flagged twice today: PROD-4 (ops spec).

## 2026-07-11 — ARCH-46 verification: four items accepted, the doc restructure bounced

First bounce-back in the board's life. Owner asked commons to verify voice's
completion claim against the HK-3 agreements, lens ownership specifically. Verified DONE:
the `lens-voice.md` co-ownership re-review (`locveil-reports@1ca251e`) is a genuine
VWB-26-pattern pass — every repo claim checked, one real stale claim found and fixed (the
eval-commons catalog-comparison step, reworded to something the triage checkout can
actually do); slug sweep clean; ping-pong guard + affirmative wording in the skill;
`wb7.env` at :8080; pin + conformance test 11/11; all seven canonical profiles carry
`[reports]` (BUILD-31). BOUNCED (owner decision): the ARCH-30 doc restructure — delivered
as a commons-ownership header over an intact body, leaving §5 (envelope) and §7 (triage
choreography) as full second copies of the shared vocabulary, which `problem-reports.md`
§1 forbids. The bounce text is committed in the PROD-14 entry per board-as-outbox;
ARCH-46 stays open voice-side until §5/§7 become pointers. Bridge delegation still in
progress.

## 2026-07-11 — PROD-14 phase 1 COMPLETE: end-to-end smoke green on the renamed pipeline

Owner finished the credential cutover (device PATs everywhere incl. the controller, Claude
App installed on the org — the claude.ai "organization settings" plan message was a red
herring; the GitHub-side install verified). Plumbing check first: an owner comment on
closed ticket #2 → triage ran SUCCESS (both codebases check out at `locveil/*`,
CROSS_REPO_TOKEN present) and the follow-up bot event was correctly skipped (§7.5).
Then the real smoke through the controller (REST `/execute/command`, two turns,
`room_alias=kitchen` — bare web sessions don't share the capture window): «сообщи о
проблеме» → «Опишите проблему…» → test description → `report_status: sent` (direct
delivery, no spool) → ticket #3 filed protocol-correct (`[voice]` prefix, labels per the
pin) → triage flipped `new`→`needs-owner`, confirmed delivery + bundle + report-id,
recommended close. Event fan-out note: filing with 3 labels spawns 4 workflow runs; the
concurrency group collapsed them to ONE executed run (3 cancelled unstarted, bot-comment
follow-ups skipped) — by design, cosmetically quietable in the delegation tail. Voice-side
finds for the delegation: voice Claude fixed a systemic config issue live (owner: to be
addressed together later); `[reports]` must land enabled in the canonical WB7 profile
config (hand-edit dies at next `update.sh` rsync); `eval/profiles/targets/wb7.env` port
6000 is stale (live API is :8080). Remaining on PROD-14: org base-permissions check
(owner), the voice + bridge delegations, owner close of ticket #3 via `/inbox`.

## 2026-07-11 — PROD-14 phase 1 mostly executed: the repo IS locveil/locveil-reports

Owner re-minted the cross-repo PAT under the org (secret updated — the triage fix-PR path
is live again after five dead days) and green-lit the transfer; the commons session
executed it via the API (transfer + rename in one call). Verified surviving: both Actions
secrets, issues, labels; local remote re-pointed (no venv to brick — the PROD-2 trap
doesn't apply here). The reports-repo protocol consumption followed immediately
(`locveil-reports@676091f`+`ef0b3d4`): `report-protocol.pin.json` vendored at
`report-protocol-v1`, `bootstrap.sh` now GENERATES labels from the pin, new
`protocol-check` CI compares live labels to the pin (first run failed honestly — the
default workflow token lacked `issues: read`; fixed, now green), README pointer flipped
from voice's design doc to `process/problem-reports.md`, post-transfer self-references
swept. Remaining owner steps: org policy checks, Claude App coverage of the private repo,
device PAT + WB7 `.env`×2 + config slugs, end-to-end smoke. Product delegations (voice,
bridge) still await intake.

## 2026-07-11 — HK-3 decided: the inbox story (PROD-14 filed, PROD-6 rescoped, report-protocol-v1)

Third council, first MULTI-ROUND one (two owner rounds; keepers continued via session
messages with context intact). Topic: move `wb-user-reports` → `locveil/locveil-reports`,
consequences for the GitHub-resident triage Claude, PAT survival, and the twin `/inbox`
skills. Sharpest findings: **the cross-repo triage PAT is presumed dead since the
2026-07-11 code-repo org move** (fine-grained under `droman42`; fine-grained PATs are
resource-owner-scoped; last triage ran 2026-07-06) — re-mint required regardless of the
move; both device PATs die AT the move; both collectors verifiably fail safe (durable
spool + retry) so the window loses nothing but must stay short; the GitHub Claude has no
CLAUDE.md by design (workflow prompt + lens files ARE its brain) and those were stale.
**Phase 0 executed mid-council** (`wb-user-reports@15d788b`): 16 stale
`droman42/wb-mqtt-*` refs → `locveil/locveil-*` + live label descriptions; ticket #2
verified closed-complete (round-1 misread corrected). Round 2 (owner: "smells like a new
contract — which form, who owns the truth"): keepers converged unanimously — **commons
owns**; voice ceded ARCH-30-era ownership explicitly ("nobody serves the inbox"); bridge
declined ownership and vetoed the ungoverned reports repo. Form: two-part truth — tiny
machine core `process/report-protocol/report-protocol.json` (labels, lenses, typed state
machine + ping_pong_max, prefixes, bundle path, handover schema, slug registry), tagged
**`report-protocol-v1`**, pinned + test-validated by all three writers (reports bootstrap
GENERATES labels from it); judgment/policy stays prose in `process/problem-reports.md`
(PROD-6's scope, rescoped to own both + tagging authority). No `contract-vN` regime-1
ceremony (cadence: 3 changes ever) and no SKILL.md pinned block in v1. Owner's final
extension check ("feature requests through the same channel") PASSED and shaped v1:
ticket TYPE is a first-class core dimension. Skills stay per-repo (genuine dialect).
Landed: spec + core + tag, PROD-14 (phase-1 owner checklist + both delegations),
PROD-6 rescope, HK-3 → BOARD_DONE, this entry.

## 2026-07-11 — Council/HK reconciliation: the tooling catches up with its own convention

Owner asked whether the HK-N rules actually exist as written invariants. Finding: the
filing rule existed (`ledger-discipline.md` §5 + board conventions, landed at HK-1) but
the council tooling predated it — `SKILL.md`'s id-assignment heuristic (count `## HK-`
journal headings) was broken (journal headings are dated; it always returns 0 and would
have re-assigned HK-1 for HK-2 — the session worked around it silently), and
`process/council.md` never stated the filing rule. Fixed: SKILL.md + council.md now derive
the next `HK-N` from the board ledgers (`BOARD.md` + `BOARD_DONE.md`, the set scope-guard
enforces) and state born-decided → `BOARD_DONE.md` filing; commons CLAUDE.md gains the
`hk-ids-from-the-board` invariant (commons-local prose, NOT in the shared blocks — product
repos never assign HK ids).

## 2026-07-11 — PROD-5 CLOSED: bridge delegation consumed (OPS-16) — all three repos harmonized

The bridge session pulled the PROD-5 delegation (pre-assigned OPS-16, flagged REDEFINE),
verified it per its `task-start-reconciliation` — all three staleness counts confirmed real
(deleted `check_scope.py` reference, dead separate-drift-guard-script plan, the superseded
split-in-two rename) — got owner approval for the redefine, and executed the full adoption:
both blocks inserted byte-identical at `scope-v3` (hashes match this repo's pins; tamper
test fails correctly with CLAUDE-BLOCK drift), CLAUDE.md net-shrank 175 → 164 lines (~55
duplicated mechanics lines out; shared invariants kept as dialect-only bullets), the false
sovereignty preamble + retired uncommitted-intake clause rewritten (commons acknowledged as
co-owned ground), `config-master-canonical` → `config-master-tree`, `[claude]` live in its
`.scope-guard.toml`, `CLAUDE.md` added to its CI ledger filter. With voice BUILD-23
confirmed earlier today, **both consumptions are in — PROD-5 closes** (entry moved to
`BOARD_DONE.md` in this change). All three repos now carry the same pinned blocks at one
tag; the "sessions search for the board process" gap HK-2 named is shut.

## 2026-07-11 — PROD-5 voice delegation consumed (BUILD-23) — voice on scope-v3

The voice session pulled the PROD-5 delegation and executed it as **BUILD-23** (the
pre-assigned ID), narrowed at intake exactly as the delegation specified (drift-guard-script
wording dead; scope-guard's `claudemd` rule is the guard). Voice CLAUDE.md now carries both
pinned blocks at `scope-v3` (byte-identical, tamper-tested red/green), net-shrank 165→160
lines (the six long-form shared invariants out, voice dialect condensed to one
`ledger-dialect` bullet), re-pinned the tool to 1.1.0, rewrote the retired pre-board intake
bullet, renamed `config-master-canonical`→`config-master-file` (legend row added), added
`CLAUDE.md` to the CI `ledger` filter, and recorded the BUILD-22 template dependency.
Pushed; the voice `ledger-guard` CI validates the blocks remotely. PROD-5 now waits only on
bridge OPS-16 to confirm.

## 2026-07-11 — HK-2 decided: CLAUDE.md harmonization (executes PROD-5)

Second council session, bare seed, one keeper round + one owner round. Topic: where shared
rules live, how product Claudes access them, how they learn the board process, how new
repos get seeded. Keepers' unanimous finding: **the topic IS the parked PROD-5 — execute
it, don't re-design it.** Root cause of the owner's "sessions search for the board
process" complaint found and named: neither product CLAUDE.md mentions the board AT ALL,
and both still teach the retired pre-board uncommitted-intake mechanism inside
`cross-repo-source-of-truth`; bridge's preamble also still claims invariant sovereignty
that `ledger-discipline.md` took over at HK-1. Both keepers independently converged on the
same mechanism: **pinned digest blocks between markers + pointers** (bare pointer fails
offline enforcement — hooks/CI/cloud-triage run without siblings; full prose fails the
token budget), enforced by a `claudemd` hash rule in scope-guard (one tool, one hook, one
pin — `scope-v3`), with the hard criterion that adoption must NOT grow a product CLAUDE.md
(each currently duplicates 20–55 lines of ledger mechanics that come out). Owner accepted
all recommendations: single scope-vX pin; `config-master-canonical` renames apart both
sides (`config-master-file` / `config-master-tree`); commons authors
`process/new-repo-template/` and voice BUILD-22 instantiates it; immediate execution.
Deferred by owner: the session-start **inbox story** — "much bigger, the next HK
exercise". Landed: `process/claude-md.md` (normative), PROD-5 → `[>]` with delegations
(voice BUILD-23 narrowed, bridge OPS-16 redefined — its text referenced the deleted
`check_scope.py`), HK-2 filed to `BOARD_DONE.md`, this entry. Executed same session
(`1786f91`, tag `scope-v3`): `process/claude-blocks/` (both digest sources),
`process/new-repo-template/` (CLAUDE.md skeleton + starter config + hook + CI template +
ledger/journal shapes), scope-guard 1.1.0 with the `[claude]` hash rule +
`--hash-blocks`, commons' own adoption (blocks + config + CI filters + the overdue
`process/README.md` fix), CI convention in `ledger-discipline.md` §4. Verified: green on
commons; tampered block and missing markers both fail correctly. PROD-5 stays `[>]` until
BUILD-23/OPS-16 confirm consumption.

## 2026-07-11 — PROD-13 CLOSED: the discipline is live in all three repos

Both delegations executed same-day and wrote back (voice **BUILD-30**, bridge **OPS-22**);
commons-side deliverable was already done, so the entry moves to `BOARD_DONE.md` — the
first close performed *under* the discipline it created, gated by its own pre-commit hook.
Full arc: decided as HK-1 in the first live council, executed commons-side (scope-guard +
BOARD split + CI/hooks, `scope-v1`), consumed by both products — whose first real rotation
caught a v1 `--rotate journal` bug (archives written character-per-line; scratch tests
missed it), fixed commons-side as **scope-v2** with both consumers re-pinning. Regime 2
worked exactly as designed under a concurrent two-session collision: one fix in commons,
consumed by re-pin, no forked copies. All three repos now run the union checker green with
committed hooks + `ledger-guard` CI; both product journals rotated under their watermarks;
voice's DONE ledger rotated with all archived IDs resolvable.

## 2026-07-11 — PROD-13 voice delegation consumed (BUILD-30) — both delegations now written back

The voice session pulled the PROD-13 delegation, verified it per its
`task-start-reconciliation` (both advertised pre-existing findings confirmed real: the
unsorted DONE I18N section and the DONE ledger over the 4000-line ceiling), filed it as
**BUILD-30**, and executed the full cutover (vendored tool + `.scope-guard.toml`,
`check_scope.py` retired, `ledger-guard` CI re-pointed, committed pre-commit hook live,
invariant text + gate wording updated, DONE-ledger rotation adopted, journal 1510→708 and
DONE 4273→1930 rotated losslessly). Voice's first rotation attempt hit the same v1
`--rotate journal` bug **concurrently** with the bridge (its corrupted first-pass commits
were rebuilt; nothing had been pushed) — the sessions collided mid-fix on this repo, and
the bridge's scope-v2 landed first; voice re-pinned to it. Regime 2 held: one fix,
commons-side, consumed by re-pin on both sides. With both local IDs written back,
PROD-13's remaining board action is closing the entry (commons-side deliverable already
done) — left to the commons session that owns the entry, since it was active in this
working copy at the time.

## 2026-07-11 — PROD-13 bridge delegation consumed (OPS-22); scope-v2 tagged (rotation bugfix)

The bridge session pulled the PROD-13 delegation, verified it per its
`task-start-reconciliation`, filed it as **OPS-22**, and executed the cutover (vendored
tool + `.scope-guard.toml`, `check_scope.py` retired, `ledger-guard` CI re-pointed,
committed pre-commit hook live, invariant text updated). The first real `--rotate journal`
run then caught a v1 defect: **archives were written character-per-line** (in
`rotate_journal`, the section body was double-indexed after unpacking — `s[1]` on the
already-unpacked day-lines list — so `"\n".join` iterated a string; the kept-sections
rewrite had the same bug, silently truncating the journal). No history lost — the journal
is git-tracked and was restored. Fixed here (2-line fix), validated against a copy of the
bridge tree with a line-by-line Counter diff (1625 → 989 kept + 635 archived + pointer,
zero lines missing), tagged **scope-v2** (1.0.1). Also made the docs honest: v1's
README/spec said hooks run `--check` but no such flag existed (the bare invocation was the
check) — v2 adds the explicit `--check` flag (mutually exclusive with `--rotate`). Both
PROD-13 delegations re-pointed at scope-v2; **voice must pin scope-v2, not v1** — its
overdue journal rotation (1510 lines) would have hit the same bug. Bridge ID written back;
voice ID still pending.

## 2026-07-11 — HK-1 decided: ledger/journal discipline harmonized (files PROD-13)

First live council session (PROD-12's shakedown) — bare seed, topic typed into the round-0
dossier, decided in one keeper round + one owner round. Topic: harmonize ledger/journal
discipline across the repos and migrate `check_scope.py` to commons. Keeper reconciliation
corrected the brief: **neither script is a superset** (bridge adds DUPLICATE/MISPLACED/
ALIAS/tombstones; voice has UNINDEXED-review + evidence-index `[x]` semantics — and the
triad itself originated in voice, DOC-12), voice CI-gates its checker just like bridge,
pre-commit hooks exist nowhere, bridge's DONE doesn't rotate, and **both journals sit over
their own ~1500-line high-water today** (voice 1510, bridge 1625) — manual rotation
demonstrably drifts. Both keepers: support-with-conditions; conditions unanimous (union
rule set, per-repo config, pinned consumption, check-vs-rotate split, archived-ID
resolution). Owner accepted all recommendations; amendments: PROD-13 executes immediately;
required-task-tags in v1 but to be revisited in a future release-numbering/sprints
housekeeping round; **HK-N becomes a tracked board prefix** — council topics are
born-decided and file directly into `BOARD_DONE.md`. Rename question (brief point 5):
dropped — naming is config. Landed: `process/ledger-discipline.md` (normative), PROD-13
on the board with voice+bridge delegations, this entry. Executed same session:
`packages/scope-guard/` (union tool, `locveil-scope-guard`, tag `scope-v1`), the
BOARD/BOARD_DONE split (PROD-1/2/3/12 + HK-1 moved), commons `.scope-guard.toml` +
`ledger-guard` CI + committed pre-commit hook (`hooks/`). Verification: commons green;
bridge green (+ true overdue-journal warning); voice run surfaced **two true pre-existing
findings its own checker could not see** — the DONE I18N section is unsorted (the old
`[A-Z]+` ordering regex never matches `I18N`) and RELEASE_PLAN_DONE.md exceeds the
4000-line hard ceiling — both folded into the voice delegation. Rotation verified on
scratch copies: bridge journal 1625→698 lines (whole days, pointer updated), voice DONE
4273→1930 with all 125 archived IDs still resolvable (zero false orphans).

## 2026-07-11 — PROD-12: the council built (skill + keepers + dossier + convention)

Owner-designed over three analysis rounds, filed and built same day. Deliverables:
`.claude/skills/council/SKILL.md` (the procedure: seed → parallel keeper round →
synthesis → dossier publish → paste-back delta → iterate → land on the board),
`.claude/skills/council/dossier-template.html` (theme-aware page with the decision form,
dirty-field delta serializer, localStorage drafts, clipboard Copy with fallback),
`.claude/agents/{voice,bridge}-keeper.md` (read-only partisan lenses that load their repo's
CLAUDE.md/ledger/journal and reconcile seeded claims before arguing), and
`process/council.md` (the normative convention: terminal-equivalence of decisions,
paste-is-the-channel, one-channel-per-round, PROD-only seeding v1, `council-reply` format
v1). CLAUDE.md and process/README gained pointers. Not yet exercised live — the first real
topic shakes it down; the satellite keeper joins when BUILD-22 creates that repo.

## 2026-07-11 — Controller cutover CONFIRMED: the deployment is fully Locveil

Owner made the 9 new GHCR packages public (org policy initially blocked Public — fixed via
org Settings → Packages → allow public package creation) and ran both
`ops/migrate-to-locveil.sh` scripts on the WB7 successfully. The controller now runs
`locveil-voice`, `locveil-bridge`, `locveil-bridge-ui` from `/mnt/data/locveil-*-config`
under `locveil-{voice,bridge}.service` — zero `wb-mqtt` naming left anywhere in the product
estate (repos, images, containers, units, runtime trees, package names). The re-pointing arc
(PROD-2 + its BUILD-29/OPS-21 residue) is fully closed. Next natural board item: the
single-compose-with-startup-order design (voice BUILD-28's cross-repo intent).

## 2026-07-11 — Deployment-identity rename executed repo-side (voice BUILD-29 + bridge OPS-21)

Owner decision: complete the re-pointing down to the metal — the controller must run new
images with zero `wb-mqtt` leftovers, including the `/mnt/data/mqtt-*-config` runtime trees →
`locveil-*-config`. Both repos executed the coordinated rename in one session
(`locveil-voice@0aca2f7`, `locveil-bridge@bba68c9`): images (`locveil-voice-*`,
`locveil-voice-ui`, `locveil-bridge`, `locveil-bridge-ui` — UI name = owner pick), containers,
systemd units (`locveil-{voice,bridge}.service`), runtime trees, clone paths, INSTALL flows;
bridge also renamed its Python distribution (`locveil-bridge`, import package kept); voice
regenerated its API contract chain (description strings; config-ui gates green). Each repo
ships a one-time `ops/migrate-to-locveil.sh` for the controller cutover (runtime tree moves
with state/models/.env intact). Sequencing: CI publishes dispatched (runs watched); owner then
flips the new GHCR packages PUBLIC and runs the two migration scripts on the WB7. Voice also
surfaced a pre-existing order-dependent test flake → voice BUG-42.

## 2026-07-11 — PROD-2 CLOSED: bridge re-point executed (`locveil-bridge@bd256d8`, OPS-20)

The first board-as-outbox round-trip completed exactly as D-5 designed it: the bridge session
pulled the PROD-2 delegation, verified it per its `task-start-reconciliation` (the `.venv`
shebang warning proved out verbatim), filed it as **OPS-20**, executed (eval re-point green —
cli 4/4, backend suite 698 post venv-rebuild; sweep; container user; GHCR refs), and wrote
the ID back. PROD-2 is `[x]`; the uncommitted-sibling-filing mechanism is now fully retired.
Standing residue: the coordinated deployment-identity rename (voice BUILD-29 + bridge OPS-21,
owner-gated, likely one joint session with the BUILD-28 single-compose design), and each repo
needs one CI publish before its next controller `update.sh`.

## 2026-07-11 — PROD-2: voice re-point delegation EXECUTED (`locveil-voice@d0c0755`)

The voice BUILD-21 tail landed: eval refs re-pointed to `../../locveil-commons/eval` (gates
green from the new paths — cli 5/5, device tier-1 48/48), operative name sweep, `domovoy` →
`locveil` container user, GHCR pull refs → `ghcr.io/locveil/*`, productization pointer swap;
BUILD-21 closed in the voice ledger, residual deployment-identity rename filed there as
BUILD-29. Two operational notes: (a) the owner must run one voice CI publish before the next
controller `update.sh` (compose now pulls `ghcr.io/locveil/*`, which doesn't exist until the
first org-side publish); (b) the local dir rename bricks a repo's `.venv` (absolute
console-script shebangs) — the voice venv was rebuilt with `uv sync --all-extras`; the bridge
delegation now carries the same warning for `backend/.venv`. PROD-2 remains `[>]` until the
bridge writes its local ID back.

## 2026-07-11 — BUILD-21 commons bootstrap (PROD-2 restructure + PROD-3 board)

Owner had completed the rename chain (GitHub org `locveil`, repos `locveil-commons` /
`locveil-voice` / `locveil-bridge`, local dirs + remotes) and, earlier the same day, the
PROD-1 name lock (Locveil; .com/.ru registered, org claimed, .io dropped, .eu pending ID
verification). This session executed the commons side of voice BUILD-21:

- **D-2 restructure**: eval framework moved to `eval/` via `git mv` (package `eval_commons`,
  `shared/`, `examples/`, `tests/`, pyproject, uv.lock, ARCHITECTURE.md, its README);
  `board/`, `process/`, `packages/`, `site/` created. `contracts/` and `docs/design/` stay
  at root. Distribution renamed `eval-commons` → `locveil-eval` (import name unchanged);
  uv.lock regenerated; test `contracts/` anchors repointed (`parents[2]`). Suite green from
  the new home: 40 passed (`cd eval && uv run --all-extras --with pytest --with jsonschema
  pytest tests/ -q`).
- **Name sweep** of repo-owned files (code comments, examples, shared YAML, docs,
  contracts/README). NOT swept, by design: the pinned artifacts + `PIN.json` +
  `crossover_fixtures.json` (new names arrive with the next re-pin / fixture re-author) and
  the dated records (`productization_roadmap.md`, body of the migrated decision record).
- **PROD-3 board bootstrap**: `BOARD.md` (conventions + §3 seed backlog as PROD-1..11),
  this journal, new commons CLAUDE.md (session discipline, ownership regimes, tag scheme),
  root README rewritten as the umbrella; old README/ARCHITECTURE live on under `eval/`.
- **Decision record migrated**: `docs/design/productization.md` copied verbatim from
  `locveil-voice@92d1abd` with a migration + name-lock header; the voice-side pointer swap
  is delegated in PROD-2.

Open tails: PROD-2 delegations to voice (BUILD-21 tail: eval-ref re-point + pointer swap)
and bridge (first board-as-outbox delegation, ID pending write-back); `locveil.eu` owner
action in PROD-1.
