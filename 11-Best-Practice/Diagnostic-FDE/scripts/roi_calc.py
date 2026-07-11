#!/usr/bin/env python3
"""
roi_calc.py — ROI商业价值测算

计算效率提升/收入增长/投资回报期，含敏感性分析。

用法：
    python roi_calc.py --type efficiency --current-cost 500000 --time-saving 0.3
    python roi_calc.py --type revenue --conversion-lift 0.05 --avg-order-value 200 --monthly-traffic 100000
    python roi_calc.py --type payback --investment 1000000 --annual-benefit 2400000
    python roi_calc.py --type all --config roi_config.json --output roi.md
"""

import argparse
import json
import sys
from pathlib import Path


def calc_efficiency(current_cost: float, time_saving: float) -> dict:
    """Calculate efficiency savings."""
    annual_saving = current_cost * time_saving * 12
    return {
        "type": "efficiency",
        "label": "效率提升",
        "inputs": {
            "月人力成本（元）": current_cost,
            "预计节省比例": f"{time_saving*100:.0f}%",
        },
        "results": {
            "conservative": {"saving_pct": time_saving * 0.8, "annual": annual_saving * 0.8},
            "baseline": {"saving_pct": time_saving, "annual": annual_saving},
            "optimistic": {"saving_pct": time_saving * 1.2, "annual": annual_saving * 1.2},
        },
    }


def calc_revenue(conversion_lift: float, avg_order_value: float,
                  monthly_traffic: float) -> dict:
    """Calculate revenue increase."""
    annual_revenue = monthly_traffic * conversion_lift * avg_order_value * 12
    return {
        "type": "revenue",
        "label": "收入增长",
        "inputs": {
            "月流量": f"{monthly_traffic:,.0f}",
            "转化率提升": f"{conversion_lift*100:.1f}%",
            "客单价（元）": f"{avg_order_value:,.0f}",
        },
        "results": {
            "conservative": {"lift": conversion_lift * 0.8, "annual": annual_revenue * 0.8},
            "baseline": {"lift": conversion_lift, "annual": annual_revenue},
            "optimistic": {"lift": conversion_lift * 1.2, "annual": annual_revenue * 1.2},
        },
    }


def calc_payback(investment: float, annual_benefit: float) -> dict:
    """Calculate payback period."""
    monthly_benefit = annual_benefit / 12
    payback_months = investment / monthly_benefit if monthly_benefit > 0 else float("inf")
    roi_1y = (annual_benefit - investment) / investment * 100 if investment > 0 else 0
    roi_3y = (annual_benefit * 3 - investment) / investment * 100 if investment > 0 else 0
    return {
        "type": "payback",
        "label": "投资回报",
        "inputs": {
            "方案总投资（元）": f"{investment:,.0f}",
            "年收益（元）": f"{annual_benefit:,.0f}",
        },
        "results": {
            "payback_months": round(payback_months, 1),
            "roi_1year": f"{roi_1y:.0f}%",
            "roi_3year": f"{roi_3y:.0f}%",
            "npv_3year": round(annual_benefit * 2.486 - investment),  # 8% discount
        },
    }


def format_report(calculations: list[dict]) -> str:
    """Format ROI report as markdown."""
    lines = ["# ROI商业价值测算\n"]

    for calc in calculations:
        lines.append(f"## {calc['label']}\n")
        lines.append("### 输入假设")
        lines.append("| 参数 | 值 |")
        lines.append("|------|-----|")
        for k, v in calc["inputs"].items():
            lines.append(f"| {k} | {v} |")
        lines.append("")

        if calc["type"] in ("efficiency", "revenue"):
            results = calc["results"]
            lines.append("### 测算结果（三档）")
            lines.append("| 情景 | 年收益（元） |")
            lines.append("|------|:----------:|")
            lines.append(f"| 🔻 保守 (-20%) | {results['conservative']['annual']:,.0f} |")
            lines.append(f"| 📊 基准 | **{results['baseline']['annual']:,.0f}** |")
            lines.append(f"| 🔺 乐观 (+20%) | {results['optimistic']['annual']:,.0f} |")

        elif calc["type"] == "payback":
            results = calc["results"]
            lines.append("### 测算结果")
            lines.append("| 指标 | 值 |")
            lines.append("|------|-----|")
            lines.append(f"| 回收期 | **{results['payback_months']}个月** |")
            lines.append(f"| 1年ROI | {results['roi_1year']} |")
            lines.append(f"| 3年ROI | {results['roi_3year']} |")
            lines.append(f"| 3年NPV (8%折现) | ¥{results['npv_3year']:,} |")

        lines.append("")

    lines.append("---")
    lines.append("*注：所有数字基于输入假设计算，敏感性分析展示±20%波动范围。*")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="ROI商业价值测算")
    parser.add_argument("--type", choices=["efficiency", "revenue", "payback", "all"],
                        required=True)
    parser.add_argument("--current-cost", type=float, help="月人力成本(元)")
    parser.add_argument("--time-saving", type=float, help="节省比例(0-1)")
    parser.add_argument("--conversion-lift", type=float, help="转化率提升(0-1)")
    parser.add_argument("--avg-order-value", type=float, help="客单价(元)")
    parser.add_argument("--monthly-traffic", type=float, help="月流量")
    parser.add_argument("--investment", type=float, help="总投资(元)")
    parser.add_argument("--annual-benefit", type=float, help="年收益(元)")
    parser.add_argument("--config", help="配置JSON文件(--type all时使用)")
    parser.add_argument("--output", help="输出文件路径")
    args = parser.parse_args()

    calculations = []

    if args.type == "all" and args.config:
        with open(args.config) as f:
            config = json.load(f)
        if "efficiency" in config:
            calculations.append(calc_efficiency(**config["efficiency"]))
        if "revenue" in config:
            calculations.append(calc_revenue(**config["revenue"]))
        if "payback" in config:
            calculations.append(calc_payback(**config["payback"]))
    elif args.type == "efficiency":
        calculations.append(calc_efficiency(args.current_cost, args.time_saving))
    elif args.type == "revenue":
        calculations.append(calc_revenue(
            args.conversion_lift, args.avg_order_value, args.monthly_traffic))
    elif args.type == "payback":
        calculations.append(calc_payback(args.investment, args.annual_benefit))

    report = format_report(calculations)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Output written to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
