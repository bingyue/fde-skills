#!/usr/bin/env python3
"""
gap_analysis.py — 需求-能力差距分析

对capability_match.py的匹配结果进行差距标记和缓解策略推荐。

用法：
    python gap_analysis.py --matched matched.json --output gap_report.md
"""

import argparse
import json
import sys
from pathlib import Path


MITIGATION_STRATEGIES = {
    "gap": [
        "寻找合作伙伴补位（ISV/SI生态）",
        "评估产品路线图中是否已规划该能力",
        "考虑开源方案+腾讯云基础设施组合",
        "缩减该需求范围至可覆盖的部分",
    ],
    "partial": [
        "通过定制开发补齐差距",
        "使用MCP连接器对接第三方工具",
        "通过Prompt Engineering优化AI效果",
        "分阶段交付：先覆盖核心，后续迭代补齐",
    ],
}


def load_matched(path: str) -> list[dict]:
    """Load matched results from capability_match.py output."""
    with open(path) as f:
        return json.load(f)


def analyze_gaps(matched: list[dict]) -> dict:
    """Analyze gaps and generate mitigation strategies."""
    report = {
        "summary": {"full": 0, "partial": 0, "gap": 0, "total": len(matched)},
        "items": [],
    }

    for item in matched:
        coverage = item.get("coverage", "gap")
        report["summary"][coverage] = report["summary"].get(coverage, 0) + 1

        entry = {
            "need_id": item["need_id"],
            "need_description": item["need_description"],
            "coverage": coverage,
            "confidence": item["best_confidence"],
            "matched_products": [],
            "mitigation": None,
            "risk_level": "low",
        }

        for m in item.get("matched_capabilities", []):
            cap = m["capability"]
            entry["matched_products"].append(
                cap.get("product_name", cap.get("pain_category", "—"))
            )

        if coverage == "gap":
            entry["mitigation"] = MITIGATION_STRATEGIES["gap"][:2]
            entry["risk_level"] = "high"
        elif coverage == "partial":
            entry["mitigation"] = MITIGATION_STRATEGIES["partial"][:2]
            entry["risk_level"] = "medium"

        report["items"].append(entry)

    return report


def format_report(report: dict, fmt: str = "markdown") -> str:
    """Format gap analysis report."""
    if fmt == "json":
        return json.dumps(report, ensure_ascii=False, indent=2)

    s = report["summary"]
    total = s["total"]

    lines = [
        "# 需求-能力差距分析报告\n",
        "## 覆盖度总览\n",
        f"| 状态 | 数量 | 占比 |",
        f"|------|:----:|:----:|",
        f"| ✅ 完全满足 | {s['full']} | {s['full']/max(total,1)*100:.0f}% |",
        f"| ⚠️ 部分满足 | {s['partial']} | {s['partial']/max(total,1)*100:.0f}% |",
        f"| ❌ 不满足 | {s['gap']} | {s['gap']/max(total,1)*100:.0f}% |",
        f"| **合计** | **{total}** | **100%** |",
        "",
    ]

    # Feasibility assessment
    full_rate = s["full"] / max(total, 1) * 100
    if full_rate >= 60:
        lines.append(f"**方案可行性评估：✅ 可行**（覆盖率{full_rate:.0f}% ≥ 60%）\n")
    elif full_rate >= 40:
        lines.append(f"**方案可行性评估：⚠️ 有风险**（覆盖率{full_rate:.0f}%，需重点关注差距项）\n")
    else:
        lines.append(f"**方案可行性评估：❌ 需重新评估**（覆盖率{full_rate:.0f}% < 40%）\n")

    # Detail table
    lines.extend([
        "## 逐项分析\n",
        "| # | 需求 | 覆盖 | 置信度 | 匹配产品 | 风险 | 缓解策略 |",
        "|---|------|:---:|:-----:|---------|:---:|---------|",
    ])

    risk_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}
    coverage_emoji = {"full": "✅", "partial": "⚠️", "gap": "❌"}

    for item in report["items"]:
        products = ", ".join(item["matched_products"][:3]) or "—"
        mitigation = "; ".join(item["mitigation"]) if item["mitigation"] else "—"
        lines.append(
            f"| {item['need_id']} | {item['need_description'][:30]} | "
            f"{coverage_emoji[item['coverage']]} | {item['confidence']:.2f} | "
            f"{products} | {risk_emoji[item['risk_level']]} | {mitigation[:50]} |"
        )

    # High-risk items detail
    high_risk = [i for i in report["items"] if i["risk_level"] == "high"]
    if high_risk:
        lines.extend(["\n## ⚠️ 高风险项详情\n"])
        for item in high_risk:
            lines.append(f"### {item['need_id']}: {item['need_description']}")
            lines.append(f"- **覆盖度**：❌ 不满足（置信度 {item['confidence']:.2f}）")
            lines.append(f"- **推荐缓解策略**：")
            if item["mitigation"]:
                for m in item["mitigation"]:
                    lines.append(f"  - {m}")
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="需求-能力差距分析")
    parser.add_argument("--matched", required=True, help="capability_match.py输出的JSON")
    parser.add_argument("--output", help="输出文件路径")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    matched = load_matched(args.matched)
    report = analyze_gaps(matched)
    output = format_report(report, args.format)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Output written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
