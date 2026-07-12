"""Generate promptfoo test cases from the crossover fixtures (TEST-18 Slice B).

One fixture → one test case: the utterance is the prompt, the fixture's `expect` rides as a
test var for the shared assertion, and `metadata` carries fixture id / tier / kind so runs
can filter (`--filter-metadata tier=1`, `--filter-metadata kind=actuate`). The fixture file
stays the single source of truth — cases are GENERATED, never hand-edited.

Usage:  python -m eval_commons.fixtures_to_tests contracts/pins/crossover-fixtures/crossover_fixtures.json > tests.yaml
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def generate(fixtures_path: Path) -> str:
    doc = json.loads(fixtures_path.read_text(encoding="utf-8"))
    lines = [
        f"# GENERATED from {fixtures_path.name} (catalog {doc.get('catalog_version')}) — do not edit.",
        f"# Regenerate: python -m eval_commons.fixtures_to_tests {fixtures_path}",
    ]
    for fixture in doc["fixtures"]:
        utterance = fixture["utterance"]["ru"]
        room = (fixture.get("context") or {}).get("room") or ""
        expect = fixture["expect"]
        description = f"{fixture['id']} (t{fixture['tier']}, {expect['kind']}): {utterance}"
        lines += [
            f"- description: {json.dumps(description, ensure_ascii=False)}",
            "  vars:",
            f"    utterance: {json.dumps(utterance, ensure_ascii=False)}",
            f"    room: {json.dumps(room, ensure_ascii=False)}",
            f"    expect: {json.dumps(expect, ensure_ascii=False)}",
            "  metadata:",
            f"    fixture: {fixture['id']}",
            f"    tier: \"{fixture['tier']}\"",
            f"    kind: {expect['kind']}",
        ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="crossover fixtures → promptfoo tests YAML")
    parser.add_argument("fixtures", type=Path, help="Path to crossover_fixtures.json")
    args = parser.parse_args()
    sys.stdout.write(generate(args.fixtures))


if __name__ == "__main__":
    main()
