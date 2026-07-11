#!/usr/bin/env python3
"""Join a promptfoo eval output with the human gold labels → agreement + Cohen's κ.

Usage: python3 score.py out.json

Confident labels feed raw agreement and Cohen's κ; `borderline` cases are excluded
from both and reported separately (the human declared either verdict acceptable).
"""
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent


def main(out_path: str) -> int:
    gold = yaml.safe_load((HERE / "gold_labels.yaml").read_text())["labels"]
    results = json.loads(Path(out_path).read_text())["results"]["results"]

    verdicts = {}
    for r in results:
        case = r["testCase"]["description"]
        verdicts[case] = "pass" if r["success"] else "fail"

    confident = {k: v for k, v in gold.items() if v in ("pass", "fail")}
    borderline = {k for k, v in gold.items() if v == "borderline"}

    agree = 0
    disagreements = []
    n_pp = n_pf = n_fp = n_ff = 0  # human × judge contingency
    for case, human in sorted(confident.items()):
        judge = verdicts.get(case)
        if judge is None:
            print(f"MISSING judge verdict for {case}")
            return 2
        if human == judge:
            agree += 1
        else:
            kind = "FALSE-ACCEPT" if judge == "pass" else "FALSE-REJECT"
            disagreements.append(f"  {case}: human={human} judge={judge}  [{kind}]")
        n_pp += human == "pass" and judge == "pass"
        n_pf += human == "pass" and judge == "fail"
        n_fp += human == "fail" and judge == "pass"
        n_ff += human == "fail" and judge == "fail"

    n = len(confident)
    po = agree / n
    # Cohen's κ, binary
    p_human_pass = (n_pp + n_pf) / n
    p_judge_pass = (n_pp + n_fp) / n
    pe = p_human_pass * p_judge_pass + (1 - p_human_pass) * (1 - p_judge_pass)
    kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0

    print(f"confident cases : {n} (of {len(gold)}; {len(borderline)} borderline excluded)")
    print(f"raw agreement   : {agree}/{n} = {po:.0%}")
    print(f"Cohen's kappa   : {kappa:.3f}")
    print(f"contingency     : PP={n_pp} PF={n_pf} FP={n_fp} FF={n_ff} "
          f"(false-accepts={n_fp}, false-rejects={n_pf})")
    if disagreements:
        print("disagreements:")
        print("\n".join(disagreements))
    print("borderline verdicts (either acceptable):")
    for case in sorted(borderline):
        print(f"  {case}: judge={verdicts.get(case)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
