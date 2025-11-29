

from src.utils import get_logger

class PlannerAgent:
    def __init__(self):
        self.logger = get_logger("PlannerAgent")

    def plan(self, query: str):
        query = query.lower()
        self.logger.info(f"Planning tasks for query: {query}")

        tasks = []

        if "roas" in query:
            tasks.append("analyze_roas")
        if "ctr" in query:
            tasks.append("analyze_ctr")
        if "creative" in query:
            tasks.append("analyze_creatives")

        self.logger.info(f"Planned tasks: {tasks}")
        return tasks
