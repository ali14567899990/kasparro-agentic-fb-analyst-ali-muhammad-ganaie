#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import argparse
import os
import json
from datetime import datetime
import yaml

from agents.planner import PlannerAgent
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.evaluator import EvaluatorAgent
from agents.creative_generator import CreativeGenerator
from utils import ensure_dirs, save_json, timestamped_log







CONFIG_PATH = "config/config.yaml"
with open(CONFIG_PATH, "r") as f:
    CONFIG = yaml.safe_load(f)

REPORTS_DIR = CONFIG.get("reports_dir", "reports")
LOGS_DIR = CONFIG.get("logs_dir", "logs")
DATA_CSV = CONFIG.get("data_csv")

ensure_dirs([REPORTS_DIR, LOGS_DIR])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Analysis query")
    args = parser.parse_args()

    run_id = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    log_path = os.path.join(LOGS_DIR, f"run_{run_id}.json")
    log = {"run_id": run_id, "query": args.query, "steps": []}

    planner = PlannerAgent()
    tasks = planner.plan(args.query)
    log["steps"].append({"planner": tasks})

    data_agent = DataAgent(DATA_CSV, CONFIG)
    df = data_agent.load_data()
    summary = data_agent.summarize()
    log["steps"].append({"data_summary": summary})

    insight_agent = InsightAgent(CONFIG)
    hypotheses = insight_agent.generate_hypotheses(df, tasks)
    log["steps"].append({"hypotheses_unvalidated": hypotheses})

    evaluator = EvaluatorAgent(CONFIG)
    validated = evaluator.validate(df, hypotheses)
    log["steps"].append({"validated_hypotheses": validated})

    creative_gen = CreativeGenerator(CONFIG)
    creatives = creative_gen.generate_for_low_ctr(df)
    log["steps"].append({"creatives": creatives[:3]})

    insights_path = os.path.join(REPORTS_DIR, "insights.json")
    creatives_path = os.path.join(REPORTS_DIR, "creatives.json")
    report_path = os.path.join(REPORTS_DIR, "report.md")

    save_json(validated, insights_path)
    save_json(creatives, creatives_path)

    with open(report_path, "w") as f:
        f.write("# Kasparro Agentic FB Analyst Report\n\n")
        f.write(f"Query: {args.query}\n\n")
        f.write("## Top Hypotheses\n\n")
        for h in validated:
            f.write(f"- {h['title']} (confidence: {h['confidence']:.2f})\n")
            f.write(f"  - {h['evidence_summary']}\n\n")

        f.write("## Creatives\n\n")
        for c in creatives[:8]:
            f.write(f"- {c['suggestion']}\n")

    timestamped_log(log_path, log)
    print("DONE!")
    print(f"Report saved to: {report_path}")

if __name__ == "__main__":
    main()
