# Contracts — the general convention (HK-5 / PROD-16, normative)

Decided by council HK-5 (2026-07-12, one keeper round — the first with all three product
keepers; positions/synthesis in `board/JOURNAL.md`). Applies to **every Locveil repo**.
On disagreement with per-repo text, this file wins. Companion conventions:
`ledger-discipline.md` (the scope kit), `claude-md.md` (pinned prose blocks).

Amended by HK-12 (§5, 2026-07-18) and **HK-13** (2026-10-05, two keeper rounds: §2
declared artifacts + reserved names, §3 three-level versions, §4 un-gated guards + the
v4 rule set, §5 release severity). HK-13 rules are normative from the landing; the ones
marked **(v4)** / **(repin v2)** become machine-enforced when a repo vendors
contract-guard v4 / repin v2 (execution: PROD-28) and bind by review until then.

## 1. What is a contract

A **contract** is any artifact one party generates/authors and another party consumes by
**pinned copy**, where silent drift breaks the consumer. Classes, with their mechanics:

| Class | Example | Version carrier | Owner-side guard | Consumer-side gate |
|---|---|---|---|---|
| Generated artifact | bridge catalog golden/openapi | STAMP.json + tag | drift guard (regen + compare in CI) | conformance test vs pin |
| Hand-written doc | voice `websocket-api.md` | doc header line + STAMP.json + tag | version test (doc header == STAMP; served code constant == the MAJOR, §3) + whole-file byte-lock (§2, HK-13) | pin + conformance test |
| Machine schema | `device-descriptor.schema.json`, `report-protocol.json` | STAMP.json + tag | schema check + committed validating example fixture | conformance test vs pin |
| Binary pack | wake-word pack | sidecar STAMP (third-party formats never forked) + content hashes | hash manifest at publish | flash/load-time hash verification |
| Prose/process block | pinned CLAUDE.md blocks, scope kit | `scope-vN` markers | commons source of truth | **block-pin**: sha256 in `.scope-guard.toml`, breaks commit + CI |
| Repo-internal generated | voice `config-ui/openapi.json` (BUILD-26) | STAMP + code constant, no tag needed | drift guard | same-repo consumer test |

Prose contracts get **pin-integrity enforcement and nothing more** — a prose contract
cannot be semantically build-broken, only drift-detected. The block-pin style is canonical
for them; they are listed in the registry (§3) as cross-references, never relocated.

**Not contracts:** per-instance config inputs validated *against* a pinned schema (e.g.
bridge `backend/config/descriptors/*.json`). They are config; the pin they validate
against is the contract. **The per-repo `docs/manifest.json` is instance data too
(HK-13, reversing the HK-6 per-repo internal `docs-manifest` contracts):** the contract
is the commons-owned schema, family `docs-manifest-schema`, pinned by every product; the
internal `contracts/docs-manifest/` STAMPs retire (their `docs-manifest-v1` tags stay as
frozen history).

## 2. Ownership, layout, directions (owner ruling: uniform, immediate)

Every repo's `contracts/` has ONE org-wide shape, **enforced immediately** — no
grandfathering (HK-5 q3):

```
contracts/
  README.md              ← the REGISTRY: every contract this repo OWNS and every pin it
                           CONSUMES, direction-labeled, one line + link each
  <name>/                ← OWNED surface: README.md (normative guide) + artifact(s)
                           + STAMP.json
  pins/<name>/           ← CONSUMED pin: verbatim artifact copy + owner's STAMP.json
                           verbatim + PIN.json (consumer-side metadata)
```

- Owned surfaces that legitimately live elsewhere (a hand-written doc that is also a
  user guide; the scope kit in `packages/`) keep their home; their `contracts/<name>/`
  folder holds STAMP.json + README pointing at the artifact. The registry indexes
  everything regardless of where bytes live.
- A pin is **always an artifact copy** — never a bare commit reference (nothing to hash,
  nothing CI can gate on).
- A pin is **always COMPLETE** (owner ruling 2026-07-12): the owner's full tagged
  artifact set, byte-identical — the IDL principle: you take the whole interface
  definition; what the consumer *uses* is its own business and never shapes the pin.
  There is no subset/"sub-pin" concept; the `PIN.json` `files` map enumerates the
  complete set, not a selection.
- **Every STAMP declares `artifacts` (HK-13; supersedes the HK-5 forward requirement and
  the HK-12 opt-in).** The list is ONE declaration with two readers: it is what consumers
  pin — repin takes the pin file set from the owner's STAMP at the tag **(repin v2)**; a
  consumer-side `files` list survives only as the fallback for tags cut before the owner
  enumerated — and it is what CONTENT-DRIFT byte-locks. `STAMP.json` itself is always an
  implicit member: it travels with every pin and must equal its own bytes at its tag
  **(v4)**. An **empty** list is legal only together with a named guard pointer that
  resolves (drift test, coherence test, hash manifest) — the shapes are the binary-pack
  sidecar (the STAMP is the whole pinned set), repo-internal generated artifacts whose
  regenerate-and-compare test is the stronger check, and package-style contracts. A
  missing key is a legacy STAMP: WARN until that contract's next cut, never a hard fail
  on re-vendor day **(v4)**.
- **Doc-canonical contracts enumerate the whole file** (owner ruling HK-13 q3): an edit
  to the guide cuts a patch (§3). An owner who finds the lock too wide splits the file;
  there is no marked-region mechanism.
- **Reserved names (HK-13).** In a pin folder two file names belong to the consumer:
  `PIN.json` (written by repin) and `README.md` (an optional hand-written note — why the
  pin exists, local conformance; never a manual re-pin recipe). Every other file is the
  owner's bytes under the owner's file name; pins stay FLAT (file names, not paths). An
  owner therefore never enumerates a file named `README.md` or `PIN.json`, and never two
  files with the same name — it fails in the owner's repo, at commit **(v4)**. Normative
  prose a consumer must hold lives in a named guide file that IS enumerated
  (`catalog-contract.md`, `convention.md`); the owner's README stays an unlocked index,
  changelog and how-to. A file in a strict pin folder that is neither reserved nor
  listed in `PIN.json` fails **(v4)**.
- **Pointers resolve; registry versions agree (HK-13 riders).** Every pointer field in a
  STAMP, PIN or `.repin.toml` that names a repo file (`conformance`, `code_constant`,
  guard pointers) must resolve to a file; a `<family>-vX` string in a registry README
  must equal the STAMP's or PIN's tag **(v4)**.
- `PIN.json` fields: `{contract, version, tag, owner_repo, owner_commit, pinned_by,
  pin_date, files: {<path>: <sha256>}, conformance: <pointer to the local test>}`.
- **STAMP.json core** (owner-side): `{contract, version, tag, date, owner_repo}` +
  contract-specific extras. Field names are fixed; extras are free.

## 3. Versioning and tags

- **Family-named tags**: `<family>-vX.Y.Z` — **always three parts from HK-13 on**
  (owner ruling, round 2): `catalog-v1.10.0`, `ws-protocol-v1.0.1`. Tags cut before
  HK-13 (`catalog-v1.5`, `ws-protocol-v1`, `contract-guard-v3.1`) are frozen as they
  are — never renamed or re-cut; the tools order mixed forms correctly
  (`v1` < `v1.0.1` < `v1.1.0`). Never a bare `contract-vN` (families, not a global
  counter).
- **The stamp defines, the changelog narrates** (owner ruling, HK-5 q4 + correction):
  README changelogs STAY as the human narrative record; from a family's first tag onward
  the STAMP + tag are the machine-readable version authority — no version exists that is
  not in a stamp. Pre-tag prose lineages (catalog v1.1–v1.4) are frozen history, not
  retro-tagged.
- **Three levels (HK-13 q2):** **major** = breaking; **minor** = the surface changed
  (additive — including the pinned set gaining a file); **patch** = enumerated bytes
  moved and the surface did not (an editorial fix to a locked guide, a regenerated
  sample, STAMP metadata). Every level is a STAMP `version` + `date` bump and a new tag
  in the same change. **Instance-data revisions** (e.g. a descriptor's bench-confirmed
  `confirm_latency_ms`) bump the instance artifact, never the convention version.
- **Runtime-served versions carry the MAJOR only** (`protocol_version`,
  `trace_version`, a device's reported convention): they state wire compatibility, so a
  minor or patch cut never changes what a fielded device or a saved file compares.
- **Content hashes are not versions.** A golden's content hash may move on config changes
  with zero surface change; the two must never be conflated — since HK-13 such a refresh
  of an enumerated golden is a patch cut, never a minor.

## 4. Enforcement — two layers, both break CI

**Layer 1 — coherence (generic): `contract_guard.py`.** Single stdlib file at
`packages/contract-guard/` (regime 2), distribution `locveil-contract-guard`, tags
`contract-guard-vN`, **vendored per consumer at a pinned tag** exactly like scope-guard;
runs in pre-commit hooks and in CI **on every push, with no path gate** (HK-13 — owned
artifacts mostly live outside `contracts/`, so a gated job never ran for the edit the
drift rule exists to catch; the HK-5 "path-gated" wording is superseded); `--check` only.
**CI checkout requirement (PROD-25, 2026-07-15; AMENDED same day — the original
`fetch-tags: true` prescription is a dud):** a CI job running contract-guard v2+ must
give its checkout tags, and the flag alone **never works**: `actions/checkout`'s
`fetch-tags: true` only drops `--no-tags` from a fetch that names a single commit, and
git tag auto-following cannot see tags pointing at unfetched commits
(actions/checkout#1467; proven live three times — satellite run 29414821199, commons
run 29414186194, voice run 29417879036, each with the flag set and no tag refspec in
the checkout log). The fix class is an **explicit step after checkout**:
`git fetch --tags --depth=1 origin` (shallow stays shallow; the TAG-MISSING rule only
needs the tag ref, resolved via `git tag -l`) — or `fetch-depth: 0` where full history
is acceptable. Reference: satellite OPS-9 (verified from checkout's exact
clone-procedure replica AND live green, run 29415097500). The failure signature of a
tag-less checkout is a false `TAG-MISSING` alarm on every owned STAMP that names a tag,
with nothing wrong in the contracts (bridge run 29317709478 was the first live case).
**v6 footnote (PROD-25 close, 2026-07-17):** the dud is checkout@v4's shallow-SHA
path — on `actions/checkout@v6` the flag DOES deliver tags, proven live twice on the
bridge (runs 29413490074 and 29436060503, guard green immediately after a bare-checkout
3× TAG-MISSING failure). The explicit step stays the prescription because it is
checkout-version-proof; the bridge's `fetch-tags: true` on v6 is the recorded working
exception — do not "fix" it to the explicit form.
The fix rides each consumer's contract-guard-v2 re-pin. It verifies what is
generic and LOCAL: registry/layout shape, STAMP core present and well-formed, PIN.json
well-formed, sha256 of local pinned copies match PIN.json, version-string consistency
(STAMP vs markers vs registry). It never checks semantics and never reaches across repos.
scope-guard stays ledger-only — the two tools version independently.

**Layer 2 — conformance (semantic, per-repo tests).** Every OWNED contract ships an
owner-side guard from day one (drift guard, or schema check + committed example fixture —
no unguarded model layouts). Every CONSUMED pin has a named conformance test
(`test_<family>_pin.*` / `test_<family>_conformance.*`) wired into the repo's normal CI
suite, asserting the consuming code actually honors the pinned surface. The VWB-37 and
`test_contracts_golden.py` patterns are the reference implementations. **Layer 2 must
run whenever a contract moves (HK-13):** a suite that is path-gated in CI includes
`contracts/**` and every enumerated artifact path in its trigger, or runs ungated — a
commit touching only a pin, a STAMP or a locked guide that runs no conformance test
contradicts "both break CI" (found live in voice; commons ran no layer-2 suite in CI at
all).

**Pin == tag bytes** is checked at **re-pin time** by the re-pin flow (the tooling fetches
the tag and records hashes into PIN.json) — not in CI, which cannot see sibling repos.
**Pin completeness** is checked locally on every run **(v4)**: the pin's files must
cover the `artifacts` list of the owner STAMP it carries.

## 5. Staleness — the severity ladder (HK-12, 2026-07-18; supersedes "never a push gate")

Conformance gates are hermetic and run on push. **Staleness** (my pin vs the owner's
newest tag) is cross-repo; the org mechanism is the shared **repin** tool (commons
`packages/repin/`, tags `repin-vN` — the promoted voice BUILD-24 engine; per-repo family
config, vendored per the scope-guard model). Severity, org-normative:

- **pre-commit: WARN-only, never blocks.** `repin --check` remote-first via tokenless
  `git ls-remote --tags` on the owner's public URL; on network failure it falls back to
  the on-disk sibling's tags with a WARN carrying fetch age. Never network-required-to-
  commit (offline bench sessions are normal operation); missing sibling = skip-silent.
- **ordinary push CI: staleness never fails the build**, EXCEPT three narrow cases:
  1. **touch-the-family** — the commit touches `contracts/pins/<family>/**` or that
     family's named conformance test while the pin trails: working against a stale pin
     is an error NOW, and the failing commit is about the pin itself (§5's original
     anti-coupling reason is preserved);
  2. **release/deploy workflows** — the REL flow / image-build dispatch fails on a
     **minor or major** family gap; patch gaps and vendored-tool (`[[tool]]`) gaps WARN
     (HK-13 q6, superseding "hard-fail on any": a commons tool tag must never block a
     hotfix image, and a bytes-only cut voids no conformance assumption) **(repin v2)**;
  3. **major-version gap** — a pin trailing a MAJOR family version fails (conformance
     assumptions void). Severity per-repo configurable: a pre-first-release repo may
     hold it advisory (recorded: satellite, until FW first light).
- **at runtime**, unchanged: version-reporting surfaces — the satellite `register`
  message (protocol + pack versions), the device `meta/locveil` retained stamp
  (`{app, fw, descriptor, convention}`), the bridge's retained catalog-version topic —
  surfaced as visible flags (registry/config-ui), never auto-fetch.

**Touch-the-family is implemented once, inside repin (HK-13)**, from the consumer's
`.repin.toml` — the family's `dest` paths and its `conformance` path (a real file path,
not prose) against a diff base — never as hand-written per-repo workflow filters; an
absent cross-repo destination (a sibling not checked out in CI) is skipped, not counted
never-pinned. `[[tool]]` entries record the vendored file's path and sha256, so the copy
is verified against its recorded tag **(repin v2)**. Satellite takes touch-the-family as
a hard failure from FW-1a start, ahead of its carve-out (its own offer).

The fix for staleness is always a **deliberate re-pin** (a ledger task), never an
auto-fetch. Untagged families skip-with-warning in CI mode. Recorded assumption: the
tokenless CI path rests on the org repos being PUBLIC — a visibility flip re-opens the
mechanism decision (HK-12). Repos not yet vendoring repin keep the pre-HK-12 behavior
(release-time `--check` only) until their adoption task lands (PROD-26).

## 6. The coordinated cut (execution order, PROD-16)

1. Commons: this spec; `contract_guard.py` v1 tagged `contract-guard-v1`; commons
   restructure (`contracts/pins/catalog/` etc.; `report-protocol` → `contracts/
   report-protocol/` with STAMP sidecar — tag v1 untouched, consumers hold copies); eval
   re-point (3 hardcoded paths).
2. Bridge: catalog → `contracts/catalog/` + `CONTRACT_VERSION` constant + STAMP core +
   first tag **`catalog-v1.5`** (README changelog kept and continued); registry README;
   consumed pins relocate NOW (`report-protocol` pin + paths in tests/lens teaching);
   device-integration example fixture + owner guard.
3. Voice: re-pin against final layout (BUILD-24 born right); ARCH-47 ships
   `ws-protocol-v1` + wake-pack sidecar stamp + `register` version fields; contracts/
   restructure to the pins shape.
4. Satellite: WS commit-pin → artifact-copy pin now, stamped pin when `ws-protocol-v1`
   lands; vendor contract-guard; CI job; DES-4 mirrors device-integration per this shape.

Consumers adopt contract-guard as it tags; a rule change here never moves a consumer
until it re-pins (the scope-guard consumption model, verbatim).
