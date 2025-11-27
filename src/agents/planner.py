class PlannerAgent:
    def __init__(self):
        pass

    def plan(self, query: str):
        query = query.lower()
        tasks = []

        if "roas" in query:
            tasks.append("analyze_roas")
        if "ctr" in query:
            tasks.append("analyze_ctr")
        if "creative" in query:
            tasks.append("analyze_creatives")

        print(f"Planning for query: {query}")
        return tasks
