# AI Agent System for Marketing Analytics Insights

## Project Introduction
This project implements an AI-powered agent system designed to analyze marketing and sales data and provide actionable insights. The system can handle queries such as identifying ROAS drops, analyzing trends, and generating creative recommendations. By leveraging multiple agents specialized for different tasks, the project demonstrates a modular and scalable architecture suitable for marketing analytics applications.

## Data Description
The project uses historical marketing and sales datasets stored in the `data/` folder. The datasets include:

- **Ad performance data:** Metrics such as impressions, clicks, conversions, cost, and revenue.
- **Campaign metadata:** Information about ad campaigns, platforms, and targeting parameters.
- **Date range:** Data includes a time series of daily metrics for analysis.

All datasets are expected to be in CSV format. The system can be extended to handle multiple campaigns and additional marketing channels.

## Agent-System Architecture
The system follows a modular agent-based design. Each agent has a specialized role:

- **Planner Agent (`planner.py`):** Generates a step-by-step plan for analyzing a given query.
- **Data Agent (`data_agent.py`):** Handles data retrieval, cleaning, and preprocessing.
- **Insight Agent (`insight_agent.py`):** Analyzes trends and patterns from the processed data.
- **Evaluator Agent (`evaluator.py`):** Evaluates the quality and relevance of insights generated.
- **Creative Generator Agent (`creative_generator.py`):** Produces recommendations and creative suggestions based on insights.

The `run.py` script orchestrates the workflow, taking user queries as input and coordinating the agents to produce a structured report.

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>




Install dependencies:

pip install -r requirements.txt


Run the system with a query:

python src/run.py "Analyze ROAS drop in last 14 days"


The output report will be generated in the Reports/ folder.

Example Output

For the query "Analyze ROAS drop in last 14 days", the system produces a report containing:

Step-by-step analysis plan

Key data insights

Identified trends and anomalies

Recommendations to improve ROAS

Visualizations (if applicable)

Example snippet:

ROAS Analysis (Last 14 Days):
- Observed a 15% drop in ROAS on social media campaigns.
- High-performing ads are those targeting audiences aged 25-34.
- Recommendation: Increase budget for high-performing ad sets and adjust targeting.

Folder Structure
project-root/
│
├─ data/                   # Raw and processed datasets
├─ logs/                   # Logs generated during execution
├─ prompts/                # Prompt templates for AI agents
├─ Reports/                # Generated reports
├─ src/
│   ├─ agents/
│   │   ├─ planner.py
│   │   ├─ data_agent.py
│   │   ├─ insight_agent.py
│   │   ├─ evaluator.py
│   │   └─ creative_generator.py
│   ├─ run.py               # Main script to execute the project
│   └─ utils.py             # Utility functions
├─ requirements.txt         # Python dependencies
└─ README.md                # Project documentation