#!/usr/bin/env python3
"""
architecture_gen.py — Mermaid架构图生成器

根据解决方案定义生成Mermaid架构图，支持系统架构/数据流/部署视图。

用法：
    python architecture_gen.py --solution solution.json --type system --output architecture.md
    python architecture_gen.py --solution solution.json --type dataflow
    python architecture_gen.py --solution solution.json --type deployment
"""

import argparse
import json
import re
import sys
from pathlib import Path


SYSTEM_TEMPLATE = """graph TB
    subgraph 展示层["展示层 (Presentation)"]
{presentation_nodes}
    end
    subgraph 业务层["业务逻辑层 (Business Logic)"]
{business_nodes}
    end
    subgraph 数据层["数据层 (Data)"]
{data_nodes}
    end
    subgraph 基础设施["基础设施层 (Infrastructure)"]
{infra_nodes}
    end
{connections}
"""

DATAFLOW_TEMPLATE = """graph LR
    subgraph 数据采集["数据采集 (Collection)"]
{source_nodes}
    end
    subgraph 数据处理["数据处理 (Processing)"]
{processing_nodes}
    end
    subgraph 数据存储["数据存储 (Storage)"]
{storage_nodes}
    end
    subgraph 数据应用["数据应用 (Application)"]
{app_nodes}
    end
{connections}
"""

DEPLOYMENT_TEMPLATE = """graph TB
    subgraph VPC["腾讯云 VPC"]
        subgraph 公共子网["公共子网 (Public Subnet)"]
{public_nodes}
        end
        subgraph 私有子网["私有子网 (Private Subnet)"]
{private_nodes}
        end
        subgraph 数据子网["数据子网 (Data Subnet)"]
{data_nodes}
        end
    end
    subgraph 外部["外部访问"]
{external_nodes}
    end
{connections}
"""


def load_solution(path: str) -> dict:
    """Load solution definition from JSON."""
    with open(path) as f:
        return json.load(f)


def generate_system_diagram(solution: dict) -> str:
    """Generate system architecture Mermaid diagram."""
    modules = solution.get("modules", [])

    layers = {
        "presentation": [],
        "business": [],
        "data": [],
        "infrastructure": [],
    }

    for i, mod in enumerate(modules):
        layer = mod.get("layer", "business")
        node_id = f"M{i}"
        product = mod.get("product", "")
        name = mod.get("name", f"Module {i}")
        label = f'{name}<br/><small>{product}</small>' if product else name
        layers.setdefault(layer, []).append(f'        {node_id}["{label}"]')

    connections = []
    for flow in solution.get("data_flows", []):
        src = f"M{flow['from']}"
        dst = f"M{flow['to']}"
        label = flow.get("label", "")
        if label:
            connections.append(f"    {src} -->|{label}| {dst}")
        else:
            connections.append(f"    {src} --> {dst}")

    return SYSTEM_TEMPLATE.format(
        presentation_nodes="\n".join(layers.get("presentation", ["        P0[用户界面]"])),
        business_nodes="\n".join(layers.get("business", ["        B0[业务服务]"])),
        data_nodes="\n".join(layers.get("data", ["        D0[数据库]"])),
        infra_nodes="\n".join(layers.get("infrastructure", ["        I0[云基础设施]"])),
        connections="\n".join(connections),
    )


def generate_dataflow_diagram(solution: dict) -> str:
    """Generate data flow Mermaid diagram."""
    stages = {
        "source": [],
        "processing": [],
        "storage": [],
        "application": [],
    }

    for i, mod in enumerate(solution.get("modules", [])):
        stage = mod.get("data_stage", "processing")
        node_id = f"D{i}"
        name = mod.get("name", f"Node {i}")
        product = mod.get("product", "")
        label = f'{name}<br/><small>{product}</small>' if product else name
        stages.setdefault(stage, []).append(f'        {node_id}["{label}"]')

    connections = []
    for flow in solution.get("data_flows", []):
        src = f"D{flow['from']}"
        dst = f"D{flow['to']}"
        label = flow.get("protocol", "")
        if label:
            connections.append(f"    {src} -->|{label}| {dst}")
        else:
            connections.append(f"    {src} --> {dst}")

    return DATAFLOW_TEMPLATE.format(
        source_nodes="\n".join(stages.get("source", ["        S0[数据源]"])),
        processing_nodes="\n".join(stages.get("processing", ["        P0[处理引擎]"])),
        storage_nodes="\n".join(stages.get("storage", ["        ST0[存储]"])),
        app_nodes="\n".join(stages.get("application", ["        A0[应用]"])),
        connections="\n".join(connections),
    )


def fix_mermaid_syntax(code: str) -> str:
    """Basic Mermaid syntax fixes."""
    # Fix unescaped special chars in labels
    code = re.sub(r'(\[")([^"]*?)(")', lambda m: m.group(1) + m.group(2).replace("#", "&#35;") + m.group(3), code)
    # Fix empty subgraphs (add placeholder)
    code = re.sub(r'(subgraph .+?\n)\s*(end)', r'\1        empty[" "]\n    \2', code)
    # Remove trailing whitespace
    code = "\n".join(line.rstrip() for line in code.split("\n"))
    return code


def main():
    parser = argparse.ArgumentParser(description="Mermaid架构图生成器")
    parser.add_argument("--solution", required=True, help="解决方案JSON文件")
    parser.add_argument("--type", choices=["system", "dataflow", "deployment"],
                        default="system", help="架构图类型")
    parser.add_argument("--output", help="输出文件路径")
    args = parser.parse_args()

    solution = load_solution(args.solution)

    generators = {
        "system": generate_system_diagram,
        "dataflow": generate_dataflow_diagram,
    }

    generator = generators.get(args.type)
    if not generator:
        print(f"Type '{args.type}' generator not yet implemented. Use system or dataflow.",
              file=sys.stderr)
        sys.exit(1)

    mermaid_code = generator(solution)
    mermaid_code = fix_mermaid_syntax(mermaid_code)

    output = f"# {args.type.title()} Architecture\n\n```mermaid\n{mermaid_code}\n```\n"

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Output written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
