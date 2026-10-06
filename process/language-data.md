# Language data — who contributes which words (PROD-18 / VWB-33, normative)

Decided by council PROD-18 round 1 (2026-10-06; voice + bridge + satellite keepers, owner
decided). Applies to every repo that feeds spoken or displayed words into the Locveil
voice path: bridge catalog config, voice donations, satellite device descriptors. This
file states OWNERSHIP only. **The machine rule — which surfaces are localized, the
required locales, the exemptions, the guard — lives in the bridge's pinned normative
guide `contracts/catalog/catalog-contract.md` ("Localization") and is never restated
here; on any disagreement that guide wins.**

## 1. The split

- **The catalog contributes the NOUNS.** Device `names`, device and room `aliases`, field
  `labels`, enum value `labels`. A device-integration descriptor (satellite-built devices)
  authors the same surfaces for its device, under the descriptor schema's own locale rule
  (`device-integration` convention, D3), which agrees with the catalog's floor by
  construction — a device that passes its descriptor conformance check never fails the
  catalog guard on labels.
- **Voice donations contribute the VERBS.** Phrases and lemmas per handler method, the
  intent names, the response templates. The catalog **never carries action labels**:
  `CatalogAction` names (`set`, `on`, `off`, …) are identifiers, not vocabulary.
- **The spoken noun of a capability is donation data.** «режим», «вентилятор»,
  «заслонка» are spoken because a donation lemma says so, not because a catalog field
  label does; field labels are display text (UI), value labels are match vocabulary.
- **Group tokens stay unlocalized identifiers** (`light`, `cover`, `fan`, …). Their spoken
  words live in donation choice surfaces (`group_noun.choice_surfaces`), where voice
  localizes them.
- **Donations may QUOTE catalog value labels** as classification phrases and examples
  («кондиционер на охлаждение»); at match time the catalog `values` table is the only
  vocabulary — a quoted phrase that stops matching a label is a stale donation, not a
  catalog defect.

## 2. What each author owes

- **Bridge (catalog config, device-integration schema):** names, aliases and labels per
  the guide's floor; a `unit` is a symbol (°C, %, dB), a `description` is developer-facing
  English — neither is spoken or localized; aliases are an authoring-checklist item,
  Russian first, never a required minimum.
- **Voice (donations):** every spoken verb and capability noun; a donation that needs a
  word the catalog does not carry adds a lemma, never asks for a catalog label.
- **Satellite (descriptors):** names and labels for its own device, nothing about verbs.

## 3. Pointers

- Machine rule + guard: bridge `contracts/catalog/catalog-contract.md` (pinned by voice
  and commons at `contracts/pins/catalog/`).
- Donation-side how-to: voice `docs/guides/howto-new-intent.md`.
- Descriptor rule: bridge `contracts/device-integration/convention.md` (D3).
- Decision record: `board/BOARD_DONE.md` PROD-18.
