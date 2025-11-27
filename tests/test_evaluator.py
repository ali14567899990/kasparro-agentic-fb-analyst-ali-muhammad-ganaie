import pandas as pd
from agents.evaluator import EvaluatorAgent

def test_evaluator_validates_hypotheses():
    df = pd.DataFrame({
        "CTR": [0.01, 0.10],
        "ROAS": [0.5, 3.0],
        "spend": [200, 300]
    })

    hypotheses = [
        {"title": "Low ROAS", "evidence_summary": "ROAS=0.5", "confidence": 0.8}
    ]

    evaluator = EvaluatorAgent({})
    validated = evaluator.validate(df, hypotheses)

    assert len(validated) > 0
    assert "title" in validated[0]
