"""`eval-fixture-record` — record conformant voice fixtures for the WS-audio system tests.

Worklist is derived from a promptfoo YAML (the single source of truth); fixtures are recorded
interactively and written as 16 kHz/mono/PCM16 WAV. See `docs/design/fixture_recorder.md`.

    eval-fixture-record --from-yaml ws.promptfooconfig.yaml            # record all missing
    eval-fixture-record --from-yaml ws.promptfooconfig.yaml timer_10min  # one, by key
    eval-fixture-record --from-yaml ws.promptfooconfig.yaml --list      # show worklist
    eval-fixture-record --devices                                       # list input devices
    eval-fixture-record --free scratch --base-dir fixtures             # freeform WAV
"""
from __future__ import annotations

import argparse
import os
import sys
from typing import List, Optional

from .worklist import FixtureJob, key_for, missing_jobs, resolve_worklist


def _load_mic(config_path: Optional[str]):
    """Parse the machine-local mic `.env` (REC_*) → a `Mic`. Defaults give native-16k mono."""
    cfg = {}
    if config_path and os.path.exists(config_path):
        with open(config_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.split("#")[0].strip()

    from .capture import resolve_device
    from .session import Mic

    return Mic(
        device=resolve_device(cfg.get("REC_INPUT_DEVICE")),
        rate=int(cfg.get("REC_CAPTURE_RATE", 16000)),
        channels=int(cfg.get("REC_CAPTURE_CHANNELS", 1)),
        countdown_s=float(cfg.get("REC_COUNTDOWN_S", 1)),
    )


def _print_list(jobs: List[FixtureJob], base_dir: str) -> None:
    for j in jobs:
        present = os.path.exists(os.path.join(base_dir, j.path))
        print(f"  [{'x' if present else ' '}] {j.key:<22} {j.path}")
        print(f"      say: {j.prompt or '(none)'}")
        if j.used_by:
            print(f"      used by: {', '.join(j.used_by)}")


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(prog="eval-fixture-record", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("keys", nargs="*", help="fixture keys to record (default: all missing)")
    p.add_argument("--from-yaml", help="promptfoo YAML to derive the worklist from")
    p.add_argument("--base-dir", help="dir audio paths are relative to (default: dir of --from-yaml)")
    p.add_argument("--config", help="machine-local mic config (.env with REC_* keys)")
    p.add_argument("--free", metavar="NAME", help="freeform record to <base-dir>/NAME.wav")
    p.add_argument("--seconds", type=float, help="fixed-duration capture instead of press-Enter")
    p.add_argument("--force", action="store_true", help="re-record fixtures that already exist")
    p.add_argument("--list", action="store_true", help="print the worklist and exit")
    p.add_argument("--devices", action="store_true", help="list input devices and exit")
    args = p.parse_args(argv)

    if args.devices:
        from .capture import list_devices
        print(list_devices())
        return 0

    # ── freeform: no YAML, just record an arbitrary named WAV ──────────────────────────
    if args.free:
        base = args.base_dir or "."
        name = args.free if args.free.endswith(".wav") else args.free + ".wav"
        out = os.path.join(base, name)
        job = FixtureJob(key=key_for(out), path=name, prompt=None, used_by=[])
        from .session import record_one
        return 0 if record_one(job, out, _load_mic(args.config), seconds=args.seconds) else 1

    if not args.from_yaml:
        p.error("need --from-yaml (or --free NAME)")
    base = args.base_dir or os.path.dirname(os.path.abspath(args.from_yaml))

    try:
        jobs = resolve_worklist(args.from_yaml)
    except ValueError as exc:  # conflicting reference text across cases
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.list:
        _print_list(jobs, base)
        return 0

    if args.keys:
        wanted = set(args.keys)
        unknown = wanted - {j.key for j in jobs}
        if unknown:
            p.error(f"unknown fixture keys: {', '.join(sorted(unknown))}")
        selected = [j for j in jobs if j.key in wanted]
    elif args.force:
        selected = jobs
    else:
        selected = missing_jobs(jobs, base)

    if not selected:
        print("nothing to record — all fixtures present (use --force to re-record).")
        return 0

    mic = _load_mic(args.config)
    from .session import record_one
    saved = 0
    for j in selected:
        out = os.path.join(base, j.path)
        if os.path.exists(out) and not args.force and not args.keys:
            continue
        if record_one(j, out, mic, seconds=args.seconds):
            saved += 1
    print(f"\ndone — {saved} fixture(s) saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
