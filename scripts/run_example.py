#!/usr/bin/env python3
"""Run an offline case or score externally captured model/system responses."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fde_skills.reference_app import evaluate, respond  # noqa: E402


def run(case_dir: Path, variant: str, predictions_path: Path | None = None) -> dict:
    knowledge = json.loads((case_dir / "knowledge.json").read_text(encoding="utf-8"))
    cases = [
        json.loads(line)
        for line in (case_dir / "eval.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if predictions_path:
        predictions = {}
        for line in predictions_path.read_text(encoding="utf-8").splitlines():
            item = json.loads(line)
            if item["id"] in predictions:
                raise ValueError(f"Duplicate prediction ID: {item['id']}")
            predictions[item["id"]] = item["response"]
    else:
        predictions = {c["id"]: respond(c["request"], knowledge, variant) for c in cases}
    return evaluate(cases, predictions)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("case", help="Directory or case name under examples/")
    p.add_argument("--variant", choices=["baseline", "guarded"], default="guarded")
    p.add_argument(
        "--predictions", type=Path, help="JSONL: {id, response: {status, sources, answer}}"
    )
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    case = Path(args.case)
    if not case.is_dir():
        case = root / "examples" / args.case
    try:
        report = run(case, args.variant, args.predictions)
        text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
        print(f"{case.name}: {report['passed']}/{report['total']}; gate={report['release_gate']}")
        return 0 if report["release_gate"] else 1
    except (OSError, ValueError, KeyError) as exc:
        print(f"Example failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
