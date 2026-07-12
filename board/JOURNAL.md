# Board journal — newest on top

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
