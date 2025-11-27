Kasparro Agentic Facebook Ads Performance Analyst — AI Agent System
Project Overview

This project implements a multi-agent AI system for marketing analytics, designed to autonomously analyze Facebook Ads performance, identify reasons for ROAS fluctuations, and recommend new creative strategies. The system demonstrates a modular, scalable architecture with specialized agents for planning, data processing, insight generation, evaluation, and creative improvement.

Objective

The system is capable of:

Diagnosing ROAS changes over time.

Identifying drivers behind performance fluctuations (e.g., audience fatigue, creative underperformance).

Proposing actionable creative ideas (headlines, messages, CTAs) for low-CTR campaigns, grounded in historical dataset insights.

Data Description

The project uses synthetic eCommerce and Facebook Ads datasets stored in the data/ folder. Key columns include:

campaign_name, adset_name, date, spend, impressions, clicks, ctr, purchases, revenue, roas, creative_type, creative_message, audience_type, platform, country.

Data includes both ad performance metrics and campaign metadata. Sample datasets are provided for reproducibility.


Agent System Architecture

The system follows a modular agent-based design:

Agent	Role
Planner Agent (planner.py)--->	Decomposes queries into actionable subtasks.
Data Agent (data_agent.py)	-->   Loads, cleans, and summarizes datasets.
Insight Agent (insight_agent.py)--->	Generates hypotheses explaining observed patterns.
Evaluator Agent (evaluator.py)--->	Quantitatively validates hypotheses and assigns confidence scores.
Creative Generator Agent (creative_generator.py)--->	Suggests new creative strategies for low-performing campaigns.

The run.py script orchestrates agent interactions, taking user queries as input and producing structured reports.

How to Run

Clone the repository:

git clone <repository-url>
cd kasparro-agentic-fb-analyst-<firstname-lastname>

Install dependencies:

pip install -r requirements.txt

Run the system with a query:

python src/run.py "Analyze ROAS drop in last 14 days"

Output: Generated reports are saved in the reports/ folder. This includes:

Step-by-step analysis plan

Key insights and trends

Recommendations to improve ROAS

Example visualizations (if applicable)


Example Output

Query: "Analyze ROAS drop in last 14 days"

Sample Insight:

Observed a 15% ROAS drop on social media campaigns.

High-performing ads target audiences aged 25–34.

Recommendation: Increase budget for high-performing ad sets and refine targeting for low-performing segments.

Folder Structure

kasparro-agentic-fb-analyst-ali-muhammad-ganaie/ – This is main project folder. Everything related to the project goes inside this.

data/ – This folder contains all  datasets, both raw and processed. Think of it as the project’s “data warehouse.”

logs/ – Any logs generated during execution, like errors or activity logs, are saved here. Useful for debugging.

prompts/ – Stores prompt templates for  AI agents. Basically, the “instructions” you give to your AI scripts.



reports/ – Any generated reports, insights, or results from  project will go here.

src/ – This is where all  source code lives. It’s divided into:

agents/ – Scripts for AI agents, like planner.py, data_agent.py, and insight_agent.py. These are the main components of AI workflow.

orchestrator/ – Scripts that manage and coordinate  agents. For example, main_orchestrator.py controls how everything runs together.

utils/ – Helper functions or utilities that  code uses repeatedly, like helpers.py.



tests/ – Unit tests to make sure  code works correctly.

config/ – Configuration files, like settings, parameters, or environment variables.

README.md – A project overview. Explains what  project does, how to run it, and any other important details.

requirements.txt – Lists all Python dependencies  project needs, so anyone can set up the environment quickly
