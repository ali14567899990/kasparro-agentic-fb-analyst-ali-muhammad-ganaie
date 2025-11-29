from src.utils import get_logger

class EvaluatorAgent:
    def __init__(self, config):
        self.config = config
        self.threshold = config.get("confidence_threshold", 0.6)
        self.logger = get_logger("EvaluatorAgent")

    def validate(self, df, hypotheses):
        self.logger.info("Validating hypotheses based on confidence thresholds...")
        validated = []

        for h in hypotheses:
            if h["confidence"] >= self.threshold:
                validated.append(h)

        self.logger.info(f"Validated {len(validated)} hypotheses.")
        return validated
