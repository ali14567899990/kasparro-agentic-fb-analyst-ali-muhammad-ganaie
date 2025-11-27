




class EvaluatorAgent:
    def __init__(self, config):
        self.config = config
        self.threshold = config.get("confidence_threshold", 0.6)

    def validate(self, df, hypotheses):
        validated = []
        for h in hypotheses:
            if h["confidence"] >= self.threshold:
                validated.append(h)
        return validated

