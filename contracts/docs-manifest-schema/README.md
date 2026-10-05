# docs-manifest-schema — the docs-manifest vocabulary (owned)

The machine-readable vocabulary every Locveil repo's `docs/manifest.json` validates
against (HK-6/PROD-17; convention: `../../process/user-docs.md` §4). The artifact keeps
its home — **`../../process/user-docs/manifest.schema.json`** — per the stays-in-home
rule (`../../process/contracts.md` §2); this folder holds the STAMP and this pointer.

- **What is the contract, what is not (HK-13 q5):** the SCHEMA is the contract. A repo's
  own `docs/manifest.json` is instance data validated against it — never stamped, edited
  freely with the docs it describes (`process/contracts.md` §1, "Not contracts"). The
  per-repo internal `docs-manifest` stamps HK-6 created are retired; their
  `docs-manifest-v1` tags remain as frozen history.
- **Consumers:** every product repo pins this family at `contracts/pins/docs-manifest-schema/`
  and points its manifest coherence test at the pinned copy (hermetic — no sibling
  checkout, no hand-mirrored vocabulary). Commons validates its own manifest against
  the artifact in place.
- **Owner guard:** `eval/tests/test_docs_manifest.py` (schema is well-formed JSON Schema
  and commons' own manifest validates against it; manifest ↔ tree coherence).
- **Version authority:** `STAMP.json` + tag. Additive vocabulary = minor; a reshape that
  invalidates existing manifests = major; bytes-only = patch.
