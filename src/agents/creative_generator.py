class CreativeGenerator:
    def __init__(self, config):
        self.config = config
        self.low_ctr_threshold = config.get("low_ctr_threshold", 0.02)

    def generate_for_low_ctr(self, df):
        low_ctr = df[df["CTR"] < self.low_ctr_threshold]
        creatives = []

        for _, row in low_ctr.iterrows():
            creatives.append({
                "suggestion": f"Improve creative for campaign {row['campaign_name']} — try a stronger hook, clearer CTA, and contrasting thumbnail."
            })

        return creatives
