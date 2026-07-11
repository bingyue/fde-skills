#!/usr/bin/env python3
"""
capability_match.py — 需求-产品能力语义匹配

将客户需求与腾讯云产品能力进行匹配，输出覆盖矩阵和置信度评分。

用法：
    python capability_match.py --needs needs.json --capability-map references/capability-map.md --output matched.json
    python capability_match.py --needs-text "客户需要智能补货预测" --capability-map references/capability-map.md
"""

import argparse
import json
import re
import sys
from pathlib import Path


def load_needs(path: str = None, text: str = None) -> list[dict]:
    """Load needs from JSON file or text."""
    if text:
        return [{"id": f"N{i+1}", "description": t.strip(), "category": "unknown"}
                for i, t in enumerate(text.split(";")) if t.strip()]
    if path:
        with open(path) as f:
            return json.load(f)
    return []


def load_capability_map(path: str) -> list[dict]:
    """Parse capability-map.md into structured capabilities."""
    capabilities = []
    content = Path(path).read_text(encoding="utf-8")

    # Parse the quick-match table at the bottom
    table_pattern = re.compile(
        r'\|\s*\*\*(.+?)\*\*\s*\|\s*["\u201c](.+?)["\u201d]\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|'
    )
    for match in table_pattern.finditer(content):
        capabilities.append({
            "pain_category": match.group(1).strip(),
            "typical_expression": match.group(2).strip(),
            "recommended_products": [p.strip() for p in match.group(3).split("+")],
            "solution_pattern": match.group(4).strip(),
        })

    # Parse individual product tables
    product_pattern = re.compile(
        r'\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|'
    )
    for match in product_pattern.finditer(content):
        name = match.group(1).strip()
        if name in ("产品", "能力", "维度", "#"):
            continue
        desc = match.group(2).strip()
        scenario = match.group(3).strip()
        if desc and scenario and len(desc) > 5:
            capabilities.append({
                "product_name": name,
                "description": desc,
                "scenario": scenario,
            })

    return capabilities


def keyword_match_score(need_text: str, capability: dict) -> float:
    """Simple keyword-based matching score (0-1)."""
    need_keywords = set(re.findall(r'[\u4e00-\u9fff]+', need_text))
    cap_text = " ".join(str(v) for v in capability.values())
    cap_keywords = set(re.findall(r'[\u4e00-\u9fff]+', cap_text))

    if not need_keywords or not cap_keywords:
        return 0.0

    overlap = need_keywords & cap_keywords
    score = len(overlap) / max(len(need_keywords), 1)
    return min(score, 1.0)


def match_needs_to_capabilities(needs: list[dict], capabilities: list[dict]) -> list[dict]:
    """Match each need to best capabilities."""
    results = []

    for need in needs:
        need_text = need.get("description", "")
        matches = []

        for cap in capabilities:
            score = keyword_match_score(need_text, cap)
            if score > 0.1:
                matches.append({
                    "capability": cap,
                    "confidence": round(score, 2),
                })

        # Sort by confidence, take top 3
        matches.sort(key=lambda x: x["confidence"], reverse=True)
        top_matches = matches[:3]

        # Determine coverage status
        best_score = top_matches[0]["confidence"] if top_matches else 0
        if best_score >= 0.6:
            coverage = "full"       # ✅
        elif best_score >= 0.3:
            coverage = "partial"    # ⚠️
        else:
            coverage = "gap"        # ❌

        results.append({
            "need_id": need.get("id", ""),
            "need_description": need_text,
            "coverage": coverage,
            "best_confidence": best_score,
            "matched_capabilities": top_matches,
        })

    return results


def format_output(results: list[dict], fmt: str = "markdown") -> str:
    """Format results as markdown or JSON."""
    if fmt == "json":
        return json.dumps(results, ensure_ascii=False, indent=2)

    lines = ["# 能力匹配结果\n"]
    lines.append("| # | 需求 | 覆盖度 | 置信度 | 匹配能力 |")
    lines.append("|---|------|:-----:|:-----:|---------|")

    coverage_map = {"full": "✅", "partial": "⚠️", "gap": "❌"}
    full_count = partial_count = gap_count = 0

    for r in results:
        symbol = coverage_map[r["coverage"]]
        if r["coverage"] == "full":
            full_count += 1
        elif r["coverage"] == "partial":
            partial_count += 1
        else:
            gap_count += 1

        cap_names = []
        for m in r["matched_capabilities"]:
            cap = m["capability"]
            name = cap.get("product_name", cap.get("pain_category", "—"))
            cap_names.append(name)

        lines.append(
            f"| {r['need_id']} | {r['need_description'][:40]} | {symbol} | "
            f"{r['best_confidence']:.2f} | {', '.join(cap_names[:3])} |"
        )

    total = len(results)
    lines.append(f"\n## 覆盖度统计")
    lines.append(f"- ✅ 完全满足：{full_count}/{total} ({full_count/max(total,1)*100:.0f}%)")
    lines.append(f"- ⚠️ 部分满足：{partial_count}/{total} ({partial_count/max(total,1)*100:.0f}%)")
    lines.append(f"- ❌ 不满足：{gap_count}/{total} ({gap_count/max(total,1)*100:.0f}%)")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="需求-产品能力匹配")
    parser.add_argument("--needs", help="需求JSON文件路径")
    parser.add_argument("--needs-text", help="需求文本（分号分隔）")
    parser.add_argument("--capability-map", default="references/capability-map.md",
                        help="能力地图Markdown路径")
    parser.add_argument("--output", help="输出文件路径")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    needs = load_needs(args.needs, args.needs_text)
    if not needs:
        print("Error: No needs provided. Use --needs or --needs-text.", file=sys.stderr)
        sys.exit(1)

    capabilities = load_capability_map(args.capability_map)
    results = match_needs_to_capabilities(needs, capabilities)
    output = format_output(results, args.format)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Output written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
