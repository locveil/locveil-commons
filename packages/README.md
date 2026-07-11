# packages/ — co-owned shared code (ownership regime 2: commons owns, products pin versions)

Code moves in only under the **rule of two** — the second consumer must be real and
committed, nothing speculative (D-8). Each package versions independently via prefixed tags
(`core-py-vX`, `ui-kit-vX`) with its own `pyproject.toml`/`package.json`; the eval framework
lives at `../eval/` (tag `eval-vX`) for historical continuity.

Planned (see `../board/BOARD.md`):

- **core-py** — PROD-8: the dynamic code loader (voice-owned today; ownership flips on
  extraction) and the logging scheme (retires the BUG-30/OPS-12 hand-copy pair).
- **ui-kit** — PROD-10 (next release): stylebook + shared React components for the two
  config UIs.
