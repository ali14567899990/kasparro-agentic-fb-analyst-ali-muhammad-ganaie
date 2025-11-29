from src.utils import get_logger, save_state
import time
import random

class InsightAgent:
    def __init__(self, config):
        self.config = config
        self.logger = get_logger("InsightAgent")

    def generate_hypotheses(self, df, tasks, max_retries=3, min_confidence=0.75):
        """
        Generate diagnostic hypotheses with retry logic if confidence is too low.
        Adds:
        - Logging for each attempt
        - Backoff retry
        - Randomized confidence simulation (replace with LLM later)
        - Threshold-based acceptance
        - State saving to allow resuming / debugging
        """
        
        for attempt in range(1, max_retries + 1):
            self.logger.info(f"[Attempt {attempt}/{max_retries}] Generating hypotheses...")

            hypotheses = []

            # ROAS insights
            if "analyze_roas" in tasks:
                low_roas = df[df["ROAS"] < 1]
                for _, row in low_roas.iterrows():
                    confidence = random.uniform(0.5, 0.95)
                    hypotheses.append({
                        "title": f"Low ROAS in campaign {row['campaign_name']}",
                        "evidence_summary": f"ROAS={row['ROAS']:.2f}, Spend={row['spend']}",
                        "confidence": confidence
                    })

            # CTR insights
            if "analyze_ctr" in tasks:
                low_ctr = df[df["CTR"] < 0.02]
                for _, row in low_ctr.iterrows():
                    confidence = random.uniform(0.5, 0.95)
                    hypotheses.append({
                        "title": f"Low CTR in campaign {row['campaign_name']}",
                        "evidence_summary": f"CTR={row['CTR']:.3f}, Impressions={row['impressions']}",
                        "confidence": confidence
                    })

            # Compute average confidence
            avg_conf = sum(h['confidence'] for h in hypotheses) / max(len(hypotheses), 1)
            self.logger.info(f"Avg confidence generated = {avg_conf:.2f}")

            # Stop if confident enough
            if avg_conf >= min_confidence:
                self.logger.info("Confidence threshold met. Returning hypotheses.")
                
                # Save state
                save_state("insight_agent_state", hypotheses)
                self.logger.info(f"InsightAgent state saved with {len(hypotheses)} hypotheses.")
                
                return hypotheses

            # Retry needed
            self.logger.warning(
                f"Confidence {avg_conf:.2f} < threshold {min_confidence}. Retrying after backoff..."
            )
            time.sleep(attempt * 1.5)

        # Retries exhausted — return best effort
        self.logger.error("Max retries exhausted. Returning last generated hypotheses.")
        
        # Save final state
        save_state("insight_agent_state", hypotheses)
        self.logger.info(f"InsightAgent state saved after max retries ({len(hypotheses)} hypotheses).")
        
        return hypotheses
