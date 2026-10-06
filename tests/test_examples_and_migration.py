import hashlib
import importlib.util
import json

import pytest

from fde_skills.library import load_skills, load_yaml
from fde_skills.reference_app import evaluate, respond


CASES = [
    "01-enterprise-ai-diagnosis",
    "02-enterprise-knowledge-base",
    "03-foreign-trade-sales-agent",
    "04-medical-beauty-conversion-agent",
    "05-manufacturing-knowledge-agent",
]
REQUIRED = """customer-interview stakeholder-map ai-maturity-assessment business-process-mapping
pain-point-analysis ai-scenario-discovery ai-scenario-prioritization value-difficulty-matrix
roi-assessment poc-scope prd-generation solution-brief technical-solution-design system-architecture
source-inventory data-quality-assessment knowledge-base-design rag-architecture chunk-strategy
retrieval-strategy agent-design multi-agent-design workflow-design tool-design mcp-design
ontology-design prompt-design context-engineering memory-design permission-model human-in-the-loop
guardrail-design eval-dataset-generation golden-dataset-design rag-evaluation agent-task-evaluation
hallucination-evaluation tool-calling-evaluation prompt-regression ai-security-testing docker-deployment
private-deployment go-live-checklist production-acceptance observability-design cost-assessment
sla-design enterprise-acceptance project-retrospective enterprise-ai-pricing industry-research
30-day-industry-learning customer-discovery field-observation requirement-to-poc poc-to-production
evaluation-driven-development ai-opportunity-mapping enterprise-ai-diagnosis delivery-handover""".split()


def test_requested_coverage(root):
    skills = load_skills(root)
    assert set(REQUIRED) <= {s.name for s in skills}
    assert {s.metadata["category"] for s in skills} == set(
        "discovery diagnosis solution architecture knowledge agent ontology engineering evaluation deployment delivery business".split()
    )


@pytest.mark.parametrize("case_name", CASES)
def test_end_to_end_case_contracts_and_negative_baseline(root, case_name):
    folder = root / "examples" / case_name
    manifest = load_yaml((folder / "case.yaml").read_text(encoding="utf-8"))
    assert [s["stage"] for s in manifest["stages"]] == [
        "discovery",
        "diagnosis",
        "solution",
        "architecture",
        "build",
        "eval",
        "deploy",
        "delivery",
    ]
    names = {s.name for s in load_skills(root)}
    for stage in manifest["stages"]:
        assert stage["skill"] in names
        assert (folder / stage["artifact"]).is_file()
    knowledge = json.loads((folder / "knowledge.json").read_text(encoding="utf-8"))
    cases = [
        json.loads(line)
        for line in (folder / "eval.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    report = evaluate(cases, {c["id"]: respond(c["request"], knowledge) for c in cases})
    assert report["release_gate"]
    assert report["total"] == 12
    baseline = evaluate(
        cases, {c["id"]: respond(c["request"], knowledge, "baseline") for c in cases}
    )
    assert not baseline["release_gate"]
    assert any(
        not r["passed"]
        for r in baseline["results"]
        if r["slice"] in ("permission", "tenant", "authorization")
    )
    assert not evaluate(cases, {})["release_gate"]
    with pytest.raises(ValueError, match="Unknown"):
        evaluate(cases, {"unknown": {}})


def test_external_predictions_cannot_hide_missing_or_duplicate_results(root, tmp_path):
    spec = importlib.util.spec_from_file_location("run_example", root / "scripts/run_example.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    case = root / "examples" / CASES[0]
    predictions = tmp_path / "predictions.jsonl"
    predictions.write_text(
        json.dumps(
            {
                "id": "01-01",
                "response": {
                    "status": "answered",
                    "sources": ["public-current"],
                    "answer": "invented",
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )
    report = module.run(case, "guarded", predictions)
    assert not report["release_gate"]
    predictions.write_text(predictions.read_text(encoding="utf-8") * 2, encoding="utf-8")
    with pytest.raises(ValueError, match="Duplicate prediction"):
        module.run(case, "guarded", predictions)


def test_original_working_tree_preserved(root):
    inventory = json.loads(
        (root / "docs/migration/original-inventory.json").read_text(encoding="utf-8")
    )
    assert len(inventory) == 370
    for entry in inventory:
        path = root / entry["preserved_path"]
        assert path.is_file(), entry["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"], entry["path"]
