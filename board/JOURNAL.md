# Board journal — newest on top
> Older sections: board/archive/journal/2026-07-11_2026-07-12.md

## 2026-07-18 — IMPL-9: the rotation that refused — scope-guard v7.2

The owner-ordered journal rotation refused with "fewer than 2 dated sections" on a
journal carrying eight days — the DATED pattern wanted the date flush against the
heading marks, so the commons `## date — …` style parsed as zero sections; the
voice/bridge bullet style masked the bug because their dates ARE flush. One-character
class of fix (`\s*`), verified against the live journal (8 day sections), shipped as
scope-v7.2 / 1.4.1 with the STAMP bump in the same change — CONTENT-DRIFT would have
demanded it anyway, which is the day's now-familiar refrain: fifth self-catch. The
rotation itself follows in its own commit, per the discipline the fixed tool enforces.
contracts: scope-v7.2 cut (bug-fix minor); re-pin owed: voice, bridge, satellite
(advisory nags). docs: none — guard internals.

## 2026-07-18 — PROD-8 CLOSED: the loader arc completes — both consumers live on core-py-v1.1

Bridge's CORE-7 verified at close, condition by §5 condition: pin + owner STAMP
byte-identical to `core-py-v1.1`, importable copy in `utils/` equal to the pin with the
identity test wired, the driver axis live on `discover_providers("locveil_bridge.devices",
base_class=DevicePort)` through a `utils/entry_points.py` singleton (never `domain/`),
`class_loader.py` untouched since CORE-10, `validate_class_references` gone, and the
dump_catalog golden byte-identical — no contract movement, exactly as the council
scoped. With voice's ARCH-58 verified this morning, both consumers of the estate's
first vendored RUNTIME code are pinned at the same tag with the same three-way
byte-identity discipline, and bridge's pin hashes match voice's bit for bit. The arc's
recorded lesson is the v1→v1.1 packaging correction: a tag must carry its STAMP, and
the first strict pin proved it. Bridge filed CORE-13 + OPS-35 off its adoption
analysis (config-driven activation, slim images — deliberately not the voice-side
metadata quartet). **The parked logging extraction spins off as PROD-27, OPTIONAL and
trigger-driven** (owner ruling at close): bridge OPS-12 stays the authored reference,
voice ARCH-43 un-parks as the design task if it ever activates; PROD-8 closes on the
loader alone. docs: none — the package README and design doc are the integrator
surface, both current. contracts: none at close — the arc's surfaces carried their own
verdicts. (Journal is over high-water — rotation due, its own commit per discipline.)

## 2026-07-18 — IMPL-8 DONE: guard v3.1 ARTIFACTS-PATH — and it bit its own author first

The Option B ruling executed: every STAMP `artifacts` entry must be repo-root-relative
and resolve to a file at HEAD; bare names and ghost paths fail `ARTIFACTS-PATH` with no
relax escape (a shape error is never a mid-bump state), and bad entries are excluded
from the drift comparison so one mistake doesn't cascade into noise. The rollout
coupling the task recorded died before execution — bridge landed VWB-43 first
(`catalog-v1.8`, repo-root paths, zero warnings), so v3.1 rolls out to all four repos
with no sequencing care; their `[[tool]]` manifests start nagging from the tag. The
acceptance test wrote itself: the first live v3.1 run CONTENT-DRIFT-failed the guard's
OWN family — edited script, un-bumped stamp — forcing the 3→3.1 STAMP bump through the
exact discipline it enforces. Fourth self-catch of the day. Smoke suite: bare name,
ghost path, relax-immunity, drift-still-works — all correct. contracts:
contract-guard-v3.1 cut; re-pin owed: voice, bridge, satellite (one-commit quick tasks;
advisory nags until then). docs: none — STAMP note + registry row updated in place.

## 2026-07-18 — PROD-26 CLOSED: the hardening is live in all four repos — and it already earns its keep

Decided in the morning (HK-12), built by mid-day, adopted and verified by evening —
the fastest decision-to-org-wide-enforcement arc the estate has run. All three product
sweeps landed same-day and each was independently verified from commons: vendored
scripts byte-compared against the tags, block hashes exact, verdict cutovers set, hooks
staged, live guard + repin runs green, CI checked job-by-job (the PROD-25 lesson).
Satellite OPS-11/12/13 set the pace and improved on the plan twice (declared-ahead
device-integration family = a visible nag instead of a forgotten pin; the publish-tool
freshness gate). Voice BUILD-41/42/43 + DOC-14 cut the estate's fourth doc-canonical
contract (trace-format-v1, version-triple-tested) and answered BUILD-44 with teeth
(tagged-bumps-only + immutable /resolve/ URLs). Bridge OPS-32/33/34 + VWB-42 closed its
plugin CI hole — first live run failed on exactly the new job, proving the gate gates —
and cut device-integration-v1.1 STAMP-in-tree, applying the core-py packaging lesson
hours after it was learned. **Three real defects caught on day one:** the published
wake pack had already drifted on HF mutable refs; core-py-v1 couldn't satisfy a
conforming pin (→ v1.1); and bridge's bare-name catalog artifacts hide a
false-CONTENT-DRIFT trap — VWB-43 bridge-side, and commons **IMPL-8** filed at close
(owner pick: Option B, one canonical repo-root path form, loud ARTIFACTS-PATH failure;
rollout sequenced so bridge re-vendors v3.1 only after its VWB-43 catalog cut).
Residuals ride their recorded vehicles: workbench machine schemas at its next bump,
the docs-manifest 10-surface cap at its next bump. PROD-8 remains the only open thread
of the arc (bridge CORE-7 + the parked logging decision). docs: none — closure; the
execution items carried their own verdicts. contracts: none — the close moves no
surface (every surface cut during execution carried its own verdict).

## 2026-07-18 — PROD-8: core-py-v1.1 — packaging correction found by the first consumer pin

Voice's ARCH-58 pin run (the first live consumer of both `core-py` AND the new repin
tool) refused `core-py-v1` immediately: the tag was cut before the "PROD-8 amended"
commit added `contracts/core-py/STAMP.json`, so the v1 TREE carries no STAMP and a
pins-complete-and-verbatim pin (artifact + owner STAMP verbatim at ONE tag) cannot be
assembled from it. Exactly the class of gap HK-12's rules exist for — surface-with-the-
artifact says STAMP + tag land in the SAME change, and the amendment didn't re-tag.
Fix: **`core-py-v1.1`**, artifact bytes UNCHANGED from v1 (diff-verified), STAMP bumped
1→1.1 with the correction recorded in its note, registry + pointer README re-anchored.
A quiet vindication of the strict-pin ruling: convention-only discipline missed this;
the very first mechanical pin caught it.

## 2026-07-18 — PROD-26 item 4: the contract-triad block — commons build COMPLETE

The last commons-side piece of HK-12: the contract discipline finally gets what the
ledger triad has had since HK-2 — a pinned digest in every session's context. Four
invariants, ≤20 lines, dialect-free: surface-with-the-artifact (STAMP + tag + registry
in the SAME change — the rule whose absence seeded HK-12), pins-complete-and-verbatim,
contracts-verdict (with the FIRST-CONSUMED arm and `re-pin owed:`), and the §5 staleness
ladder. Source at `process/claude-blocks/contract-triad.md`, pinned into commons' own
CLAUDE.md, hash in `.scope-guard.toml`. Shipped at **`scope-v7.1`** — blocks version
with scope tags (HK-2 single-pin), and v7 was already published, so the additive minor
bump is the clean vehicle: script bytes unchanged, STAMP 7→7.1 in the same change, and
the new ORPHAN-TAG/CONTENT-DRIFT rules verified the bump discipline live. With that,
every PROD-26 commons deliverable exists: `repin-v1`, `contract-guard-v3`, `scope-v7.1`
(tool + block), the four sweep stamps, §5 + §7 process text. The entry stays OPEN by
owner ruling until voice, bridge, and satellite execute their sweeps and write their
IDs back — the product sweeps vendor exactly those three tags in one pass each.
contracts: scope-v7.1 cut (additive block release, STAMP 7→7.1); re-pin owed: voice,
bridge, satellite — the already-delegated PROD-26 sweeps. docs: none — block source +
CLAUDE.md pin + config hash; process/claude-md.md already documents the lane.

## 2026-07-18 — PROD-26 items 2/3/5: the guards learn to see omissions — v3 + v7 + stamps

The HK-12 diagnosis was "the guards verify coherence of what exists; omissions are
invisible" — this lands the cure. contract-guard v3 (3.0.0, `contract-guard-v3`) gains
the three existence rules: ORPHAN-TAG (a newer family tag than the STAMP records —
keyed to registered contracts so release tags can't false-positive), CONTENT-DRIFT
(`artifacts`-carrying STAMPs are byte-frozen at their tag — the satellite
device-integration scar becomes a commit-time FAIL; package-style contracts opt out by
not enumerating), and VENDORABLE-UNREGISTERED (explicit `vendorable_roots` config —
today's PROD-8 seed miss now fails the commit that makes it). Plus `--relax-tags`, the
mid-bump tolerance the repin-v1 landing painfully re-motivated hours earlier: the hook
warns on the bump commit's unavoidable tag-less state, CI stays strict. scope-guard v7
(1.4.0, `scope-v7`) gains CONTRACTS-VERDICT (spec: ledger-discipline §7 — "created,
bumped, or first consumed", owner bumps carry `re-pin owed:`; commons cut over today,
HK-12's own entry retro-carries the line per the HK-6 rollout precedent) and
UNKNOWN-PREFIX (the satellite DOC scar: a prefix missing from config now fails loudly
instead of silently not counting). Every rule smoke-tested on synthetic repos before
going live; both guards green on commons. The item-5 stamps rode along because
VENDORABLE-UNREGISTERED demands them: scope + contract-guard (first stamps of their
families, drift-checked, pre-stamp tags frozen history) and package-style ui-kit +
workbench at their existing v1.2 tags — the workbench machine schemas are recorded owed
at its next bump. Remaining commons build: the pinned contract-triad block (item 4).
contracts: scope STAMP @ scope-v7 + contract-guard STAMP @ contract-guard-v3 (first-cut,
new tags) + ui-kit/workbench package-style STAMPs @ existing v1.2 tags; re-pin owed:
voice, bridge, satellite — discharged by the already-delegated PROD-26 sweeps. docs:
none — process file §7 + registry/READMEs amended in place; no manifest node covers the
guard scripts (integrator surface, own READMEs).

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

