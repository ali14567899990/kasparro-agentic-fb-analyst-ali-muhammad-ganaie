class InsightAgent:
    def __init__(self, config):
        self.config = config

    def generate_hypotheses(self, df, tasks):
        hypotheses = []

        # ROAS insights
        if "analyze_roas" in tasks:
            low_roas = df[df["ROAS"] < 1]
            for _, row in low_roas.iterrows():
                hypotheses.append({
                    "title": f"Low ROAS in campaign {row['campaign_name']}",
                    "evidence_summary": f"ROAS={row['ROAS']:.2f}, Spend={row['spend']}",
                    "confidence": 0.8
                })

        # CTR insights
        if "analyze_ctr" in tasks:
            low_ctr = df[df["CTR"] < 0.02]
            for _, row in low_ctr.iterrows():
                hypotheses.append({
                    "title": f"Low CTR in campaign {row['campaign_name']}",
                    "evidence_summary": f"CTR={row['CTR']:.3f}, Impressions={row['impressions']}",
                    "confidence": 0.7
                })

        return hypotheses


