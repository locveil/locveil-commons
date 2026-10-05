#!/usr/bin/env python3
"""contract-graph — the org-wide contract graph as a generated VIEW (HK-13 rider, IMPL-18).

Reads, from the sibling checkouts on disk, exactly the two declarations HK-13 made the
single sources of the graph —

    owner side     contracts/<name>/STAMP.json      what each contract IS
    consumer side  .repin.toml + contracts/pins/<name>/PIN.json   who consumes it

— and writes process/contract-graph.md: owned surfaces, consumption edges with their
freshness, the vendored-tools manifest, and a diagram. The page is NEVER a source:
nothing reads it, nothing is decided from it, and it is regenerated, not edited.

    python3 contract_graph.py            regenerate the page
    python3 contract_graph.py --check    exit 1 when the committed page is stale

Local and offline by design (it compares against the siblings' on-disk STAMPs, not
against remote tags — staleness gating is repin's job). A sibling that is not on disk
is listed as absent; --check then skips (CI sees one repo).
"""

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path

REPOS = ("locveil-commons", "locveil-voice", "locveil-bridge", "locveil-satellite")
OUT = "process/contract-graph.md"


def _json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except (OSError, ValueError):
        return None


def _version(tag: str | None) -> tuple[int, ...]:
    m = re.search(r"-v(\d+(?:\.\d+)*)$", tag or "")
    return (tuple(int(x) for x in m.group(1).split(".")) + (0, 0, 0))[:3] if m else ()


def _freshness(pinned: str | None, current: str | None) -> str:
    if not pinned:
        return "never pinned"
    if not current:
        return "owner not on disk"
    old, new = _version(pinned), _version(current)
    if old == new:
        return "current"
    if not old or not new or old[0] != new[0]:
        return "TRAILS (major)"
    return "trails (minor)" if old[1] != new[1] else "trails (patch)"


def collect(base: Path) -> dict:
    owned: dict[str, dict[str, dict]] = {}   # repo -> family -> STAMP
    edges: list[dict] = []
    tools: list[dict] = []
    absent: list[str] = []
    for repo in REPOS:
        root = base / repo
        if not root.is_dir():
            absent.append(repo)
            continue
        owned[repo] = {}
        for stamp_path in sorted((root / "contracts").glob("*/STAMP.json")):
            stamp = _json(stamp_path)
            if stamp:
                owned[repo][stamp_path.parent.name] = stamp
    for repo in REPOS:
        root = base / repo
        if not root.is_dir():
            continue
        try:
            cfg = tomllib.loads((root / ".repin.toml").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            cfg = {}
        declared = set()
        for fam in cfg.get("family", []) or []:
            for dest in fam.get("dest", []) or []:
                path = str(dest.get("path", ""))
                holder = repo if not path.startswith("..") else Path(path).parts[1]
                if holder != repo:
                    continue  # a cross-repo dest is listed by the repo that holds the pin
                declared.add(fam["name"])
                pin = _json(root / path / "PIN.json") or {}
                edges.append({"consumer": repo, "family": fam["name"],
                              "owner": fam.get("owner_repo", "?"), "pinned": pin.get("tag"),
                              "conformance": pin.get("conformance") or dest.get("conformance"),
                              "stamped_by": fam.get("managed_by")})
        for pin_path in sorted((root / "contracts/pins").glob("*/PIN.json")):
            name = pin_path.parent.name
            if name in declared:
                continue  # an undeclared (legacy) pin: on disk but not in .repin.toml
            pin = _json(pin_path) or {}
            edges.append({"consumer": repo, "family": name,
                          "owner": pin.get("owner_repo", "?"), "pinned": pin.get("tag"),
                          "conformance": pin.get("conformance"), "stamped_by": None,
                          "undeclared": True})
        for legacy in sorted(p.name for p in (root / "contracts/pins").glob("*")
                             if p.is_dir() and not (p / "PIN.json").is_file()):
            edges.append({"consumer": repo, "family": legacy, "owner": "co-owned",
                          "pinned": None, "conformance": None, "stamped_by": None,
                          "legacy": True})
        for tool in cfg.get("tool", []) or []:
            tools.append({"repo": repo, "tool": tool.get("name"), "family": tool.get("family"),
                          "owner": tool.get("owner_repo", "?"),
                          "pinned": tool.get("pinned_tag"),
                          "hashed": bool(tool.get("sha256"))})
    for e in edges:
        e["current"] = (owned.get(e["owner"], {}).get(e["family"], {}) or {}).get("tag")
    for t in tools:
        t["current"] = (owned.get(t["owner"], {}).get(t["family"], {}) or {}).get("tag")
    return {"owned": owned, "edges": edges, "tools": tools, "absent": absent}


def render(g: dict) -> str:
    short = lambda r: r.removeprefix("locveil-")  # noqa: E731
    out = ["# The Locveil contract graph — GENERATED VIEW",
           "",
           "> **Generated by `packages/contract-graph/contract_graph.py` — never edit, never",
           "> cite as a source.** The sources are each owner's `contracts/<name>/STAMP.json`",
           "> and each consumer's `.repin.toml` + `PIN.json` (HK-13). Regenerate after a cut",
           "> or a re-pin; `--check` tells you when this page is stale. It shows declared",
           "> edges only — a surface consumed with no pin is invisible here by definition.",
           ""]
    if g["absent"]:
        out += [f"_Not on disk when generated: {', '.join(g['absent'])}._", ""]
    out += ["## Who consumes what", "", "```mermaid", "graph LR"]
    for repo in REPOS:
        if repo not in g["absent"]:
            out.append(f"  {short(repo)}[{short(repo)}]")
    seen = set()
    for e in sorted(g["edges"], key=lambda e: (e["owner"], e["consumer"], e["family"])):
        if e.get("legacy") or e["owner"] not in REPOS:
            continue
        key = (e["owner"], e["consumer"], e["family"])
        if key not in seen:
            seen.add(key)
            out.append(f"  {short(e['owner'])} -- {e['family']} --> {short(e['consumer'])}")
    out += ["```", "", "## Owned surfaces", "",
            "| Owner | Contract | Tag | Enumerated artifacts | Guard |", "|---|---|---|---|---|"]
    for repo in REPOS:
        for name, stamp in sorted(g["owned"].get(repo, {}).items()):
            arts = stamp.get("artifacts")
            if arts is None:
                shown = "_undeclared (legacy STAMP)_"
            elif not arts:
                shown = "_none (empty by declaration)_"
            else:
                shown = "<br>".join(f"`{a}`" for a in arts)
            guard = f"`{stamp['guard']}`" if stamp.get("guard") else "—"
            out.append(f"| {short(repo)} | `{name}` | `{stamp.get('tag')}` | {shown} | {guard} |")
    out += ["", "## Consumption edges", "",
            "| Consumer | Family | Owner | Pinned | Owner's current | State | Conformance |",
            "|---|---|---|---|---|---|---|"]
    for e in sorted(g["edges"], key=lambda e: (e["consumer"], e["family"])):
        if e.get("legacy"):
            state = "legacy pin — no PIN.json"
        else:
            state = _freshness(e["pinned"], e["current"])
            if e.get("undeclared"):
                state += "; not in `.repin.toml`"
            if e.get("stamped_by"):
                state += f"; stamped by {short(e['stamped_by'])}"
        conf = f"`{e['conformance']}`" if e.get("conformance") else "_none yet_"
        out.append(f"| {short(e['consumer'])} | `{e['family']}` | {short(e['owner'])} | "
                   f"`{e['pinned'] or '—'}` | `{e['current'] or '—'}` | {state} | {conf} |")
    out += ["", "## Vendored tools", "",
            "| Repo | Tool | Pinned | Owner's current | State | Bytes hashed |",
            "|---|---|---|---|---|---|"]
    for t in sorted(g["tools"], key=lambda t: (t["repo"], t["tool"] or "")):
        out.append(f"| {short(t['repo'])} | `{t['tool']}` | `{t['pinned']}` | "
                   f"`{t['current'] or '—'}` | {_freshness(t['pinned'], t['current'])} | "
                   f"{'yes' if t['hashed'] else 'NO'} |")
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2],
                        help="the locveil-commons checkout (default: this file's repo)")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 when the committed page differs from a fresh render")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    graph = collect(root.parent)
    page = render(graph)
    target = root / OUT
    if args.check:
        if graph["absent"]:
            print(f"contract-graph: siblings absent ({', '.join(graph['absent'])}) — skipped")
            return 0
        if not target.is_file() or target.read_text(encoding="utf-8") != page:
            print(f"contract-graph: {OUT} is STALE — regenerate: "
                  "python3 packages/contract-graph/contract_graph.py")
            return 1
        print(f"contract-graph: {OUT} is current")
        return 0
    target.write_text(page, encoding="utf-8")
    print(f"contract-graph: wrote {OUT} ({len(graph['edges'])} edges, "
          f"{sum(len(v) for v in graph['owned'].values())} owned surfaces)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
