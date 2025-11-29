from src.utils import get_logger, retry_with_backoff, save_state

class CreativeGenerator:
    def __init__(self, config):
        self.config = config
        self.low_ctr_threshold = config.get("low_ctr_threshold", 0.02)
        self.logger = get_logger("CreativeAgent")

    def _single_pass(self, df):
        """
        Generate creative suggestions for campaigns with low CTR.
        Returns:
            {
                "creatives": [...],
                "confidence": float
            }
        """
        low_ctr = df[df["CTR"] < self.low_ctr_threshold]
        creatives = []

        for _, row in low_ctr.iterrows():
            creatives.append({
                "suggestion": (
                    f"Improve creative for campaign {row['campaign_name']} — "
                    f"try a stronger hook, clearer CTA, and contrasting thumbnail."
                )
            })

        # Confidence example logic:
        # if we generate suggestions → high confidence
        # if none → low confidence → triggers retry
        confidence = 0.8 if len(creatives) > 0 else 0.3
        return {"creatives": creatives, "confidence": confidence}

    def generate_for_low_ctr(self, df):
        """
        Wrapper with retry logic and state saving.
        Calls _single_pass() multiple times until confidence improves.
        """
        self.logger.info("Generating creative suggestions with retry...")

        # Wrapper function to give retry_with_backoff
        def attempt():
            return self._single_pass(df)

        # retry_with_backoff is inside utils.py
        result = retry_with_backoff(attempt)

        # Save state after generation
        save_state("creative_agent_state", result)
        self.logger.info(
            f"Final creative confidence={result['confidence']:.2f}, state saved with {len(result['creatives'])} suggestions."
        )

        return result["creatives"]
