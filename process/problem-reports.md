# Problem reports — normative spec + protocol governance (HK-3 / PROD-6 / PROD-14)

Decided by the third council session (HK-3, 2026-07-11). **Commons owns the shared inbox
truth** — voice ceded the ARCH-30-era ownership (an accident of building first; the old
reports-README pointer to `locveil-voice/docs/design/problem_reports.md` flips here at the
PROD-14 move). Per-repo docs (`locveil-voice/docs/design/problem_reports.md`,
`locveil-bridge/docs/design/problem_reports_bridge.md`) remain each side's implementation
design and defer to this spec for everything shared.

## 1. The two-part truth (what lives where)

- **Machine core — [`contracts/report-protocol/report-protocol.json`](../contracts/report-protocol/report-protocol.json)** (home since PROD-16; STAMP + per-contract README alongside)**:**
  the wire-visible surface only — slug registry, labels {name, color, description}, lens
  enum, ticket types with per-type title prefixes / envelope required-fields / state
  buckets + transitions, `ping_pong_max`, bundle path template, handover-comment header +
  fields. Versioned with prefixed tags **`report-protocol-vN`**. A label mismatch makes
  tickets silently invisible to queue queries — that is why this part is a CONTRACT.
- **This prose spec:** semantics, triage judgment, leak fence, retention/redaction/rate
  policy — the parts that degrade gracefully and change by owner decision. Policy edits
  here do NOT bump the protocol version; only machine-core changes do.
- **Boundary rules:** the core stays tiny (bridge's condition — every vN bump costs a
  consumer fan-out; judgment content never migrates in). The bridge's evidence-envelope
  schema (`GET /reports/evidence`) is bridge-generated contract surface — this spec and
  the core **reference it, never restate it** (`cross-repo-source-of-truth`).

## 2. Consumption (pin + validate; never sibling-read)

Consumers PIN a copy of the machine core at a tagged version and VALIDATE against the pin
— CI has no sibling checkout (the HK-2 constraint), so live reads protect nothing:

- **locveil-voice / locveil-bridge:** vendor the pinned JSON; one unit test each asserting
  the collector's emitted labels, title prefix, and bundle path against the pin (bridge's
  writer surface today is unvalidated hardcodes — `service.py:210/216`; voice's collector
  equally). The `/inbox` skills and `problem-report-inbox` invariants cite the pin's slug.
- **locveil-reports:** the FIRST consumer, not the owner — `bootstrap.sh` GENERATES its
  labels from the pinned core, and a trivial CI check compares live labels to it. (The
  reports repo is deliberately the org's least-governed repo; normative truth for a
  household-data pipeline does not live there.)
- **Propagation:** rare by design (the shared vocabulary changed 3× in its life). On a
  bump: commons edits + tags `report-protocol-vN` → board fan-out → each consumer re-pins
  under its own ledger ID. No automated cross-repo staleness gate at this cadence; the
  escape hatch stays same-day cheap (scope-v2 precedent).

## 3. Choreography semantics (normative prose over the core's enums)

- **Filing:** one report = one issue (type label + lens label + `new`) + one bundle commit
  at the core's `bundle_path`. The issue body is the distilled envelope — triage usually
  needn't open the tarball.
- **Triage outcomes** (each run ends in exactly one): fix → PR on the lens's code repo,
  label `fix-pr-open` · handover → flip the lens label + post the handover comment (the
  receiving lens reads THAT first, not the raw bundle) · unclear/not-a-bug → `needs-owner`
  with the analysis AND a drafted reporter reply in the reporter's language.
- **Ping-pong guard:** a ticket already handed over once in EACH direction escalates to
  `needs-owner` instead of bouncing (`ping_pong_max` lives in the core).
- **Terminal state:** the OWNER closes every ticket (via `/inbox`); the outcome bucket
  label stays on the closed issue as the record.
- **Leak fence (absolute):** anything written to the public repos — PRs, branches,
  commits — describes defects technically; never quotes logs, room/device names, user free
  text, or config values. Household data appears only inside the private reports repo.
- **Loop safety:** triage ignores the bot's own events, is label-gated on the type label,
  one concurrent run per ticket.

## 4. Policy (PROD-6 scope)

- **Retention:** raw bundles die after 30 days (scheduled prune); issues + distilled
  summaries persist. Privacy decays by default; triage history does not.
- **Privacy boundary:** the reports repo is private, and after the PROD-14 org transfer
  that boundary is the ORG's access policy — base member permission `none`, membership
  owner-only. Redaction inside bundles stays per-collector (each side's design doc), under
  the invariant that bundles never leave the private repo.
- **Rate/abuse:** collectors throttle at the source (one report per capture dialog; spool
  on delivery failure — never drop, never flood). Delivery failures spool durably and
  retry; a stalled spool is a defect to surface, not a silent state.
- **Model policy:** triage pins one strong model in ONE place (the workflow env — D-11).

## 5. Governance

- **Lens files are co-owned:** `.github/claude/lens-voice.md` / `lens-bridge.md` live in
  the reports repo but their triage-against-the-code content belongs to the respective
  product repo (VWB-26 precedent) — product repos re-review them when their repo reality
  shifts (the PROD-14 delegations carry the first pass).
- **The slug registry is the core's `repos` object** — the ONLY place repo slugs are
  normatively written. Skills, invariants, configs, and lens files carry copies that the
  consumption tests + sweeps keep honest; a future rename is a core bump + re-pins.

## 6. Extension-proofing (HK-3 owner check: "feature requests through the same channel")

The design holds. `types` is a first-class dimension of the core: a future
`feature-request` type adds its own label, prefixes, `bundle_required: false` (no logs
needed), and a lighter transition set (likely `new → needs-owner → filed-as-task`) as a
**`report-protocol-v2` bump** — old devices keep filing valid v1 problem-reports during
rollout precisely BECAUSE consumers pin. Lens machinery, handover, leak fence, `/inbox`
queues, and the triage workflow extend unchanged; "report" in this spec means any
user-originated ticket. What a new type must bring: its label in `labels`, its entry in
`types`, a triage-outcome section in the lens files, and a consumer fan-out.
