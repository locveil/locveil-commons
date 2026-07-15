# Contracts — the general convention (HK-5 / PROD-16, normative)

Decided by council HK-5 (2026-07-12, one keeper round — the first with all three product
keepers; positions/synthesis in `board/JOURNAL.md`). Applies to **every Locveil repo**.
On disagreement with per-repo text, this file wins. Companion conventions:
`ledger-discipline.md` (the scope kit), `claude-md.md` (pinned prose blocks).

## 1. What is a contract

A **contract** is any artifact one party generates/authors and another party consumes by
**pinned copy**, where silent drift breaks the consumer. Classes, with their mechanics:

| Class | Example | Version carrier | Owner-side guard | Consumer-side gate |
|---|---|---|---|---|
| Generated artifact | bridge catalog golden/openapi | STAMP.json + tag | drift guard (regen + compare in CI) | conformance test vs pin |
| Hand-written doc | voice `websocket-api.md` | doc header line + STAMP.json + tag | version-triple test (doc header == served code constant == STAMP) | pin + conformance test |
| Machine schema | `device-descriptor.schema.json`, `report-protocol.json` | STAMP.json + tag | schema check + committed validating example fixture | conformance test vs pin |
| Binary pack | wake-word pack | sidecar STAMP (third-party formats never forked) + content hashes | hash manifest at publish | flash/load-time hash verification |
| Prose/process block | pinned CLAUDE.md blocks, scope kit | `scope-vN` markers | commons source of truth | **block-pin**: sha256 in `.scope-guard.toml`, breaks commit + CI |
| Repo-internal generated | voice `config-ui/openapi.json` (BUILD-26) | STAMP + code constant, no tag needed | drift guard | same-repo consumer test |

Prose contracts get **pin-integrity enforcement and nothing more** — a prose contract
cannot be semantically build-broken, only drift-detected. The block-pin style is canonical
for them; they are listed in the registry (§3) as cross-references, never relocated.

**Not contracts:** per-instance config inputs validated *against* a pinned schema (e.g.
bridge `backend/config/descriptors/*.json`). They are config; the pin they validate
against is the contract.

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
  complete set, not a selection. (Machine check, forward requirement: from each
  contract's next bump its STAMP.json enumerates the artifact set in an `artifacts`
  list, so contract-guard can verify pin completeness — a contract-guard v1.1 rule.)
- `PIN.json` fields: `{contract, version, tag, owner_repo, owner_commit, pinned_by,
  pin_date, files: {<path>: <sha256>}, conformance: <pointer to the local test>}`.
- **STAMP.json core** (owner-side): `{contract, version, tag, date, owner_repo}` +
  contract-specific extras. Field names are fixed; extras are free.

## 3. Versioning and tags

- **Family-named tags**: `<family>-vN` or `<family>-vN.M` — `catalog-v1.5`,
  `ws-protocol-v1`, `report-protocol-v1`, `device-integration-v1`, `wake-pack-v1`,
  `contract-guard-v1`. Never a bare `contract-vN` (families, not a global counter).
- **The stamp defines, the changelog narrates** (owner ruling, HK-5 q4 + correction):
  README changelogs STAY as the human narrative record; from a family's first tag onward
  the STAMP + tag are the machine-readable version authority — no version exists that is
  not in a stamp. Pre-tag prose lineages (catalog v1.1–v1.4) are frozen history, not
  retro-tagged.
- Major = breaking; minor = additive (STAMP `version` + `date` bump, new tag).
  **Instance-data revisions** (e.g. a descriptor's bench-confirmed `confirm_latency_ms`)
  bump the instance artifact, never the convention version.
- **Content hashes are not versions.** A golden's content hash may move on config changes
  with zero contract change; the two must never be conflated.

## 4. Enforcement — two layers, both break CI

**Layer 1 — coherence (generic): `contract_guard.py`.** Single stdlib file at
`packages/contract-guard/` (regime 2), distribution `locveil-contract-guard`, tags
`contract-guard-vN`, **vendored per consumer at a pinned tag** exactly like scope-guard;
runs in pre-commit hooks and a path-gated CI job; `--check` only.
**CI checkout requirement (PROD-25, 2026-07-15):** a CI job running contract-guard v2+
must give its checkout tags — `actions/checkout` with `fetch-tags: true` (shallow stays
fine; the TAG-MISSING rule only needs the tag ref, resolved via `git tag -l`). The
failure signature of a tag-less checkout is a false `TAG-MISSING` alarm on every owned
STAMP that names a tag, with nothing wrong in the contracts (bridge run 29317709478 was
the live case). The fix rides each consumer's contract-guard-v2 re-pin. It verifies what is
generic and LOCAL: registry/layout shape, STAMP core present and well-formed, PIN.json
well-formed, sha256 of local pinned copies match PIN.json, version-string consistency
(STAMP vs markers vs registry). It never checks semantics and never reaches across repos.
scope-guard stays ledger-only — the two tools version independently.

**Layer 2 — conformance (semantic, per-repo tests).** Every OWNED contract ships an
owner-side guard from day one (drift guard, or schema check + committed example fixture —
no unguarded model layouts). Every CONSUMED pin has a named conformance test
(`test_<family>_pin.*` / `test_<family>_conformance.*`) wired into the repo's normal CI
suite, asserting the consuming code actually honors the pinned surface. The VWB-37 and
`test_contracts_golden.py` patterns are the reference implementations.

**Pin == tag bytes** is checked at **re-pin time** by the re-pin flow (the tooling fetches
the tag and records hashes into PIN.json) — not in CI, which cannot see sibling repos.

## 5. Staleness — never a push gate

Conformance gates are hermetic and run on push. **Staleness** (my pin vs the owner's
newest tag) is cross-repo and runs:

- **at runtime**, via version-reporting surfaces — the satellite `register` message
  (protocol + pack versions), the device `meta/locveil` retained stamp
  (`{app, fw, descriptor, convention}`), the bridge's retained catalog-version topic —
  surfaced as visible flags (registry/config-ui), never auto-fetch;
- **at release/re-pin time**, via the generalized `make repin` flow (PROD-7 lineage:
  scripted fetch-at-tag + PIN stamp + staleness report), optionally scheduled.

A hard cross-repo staleness gate on push is forbidden — it breaks CI hermeticity and
couples a repo's commits to sibling availability.

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
