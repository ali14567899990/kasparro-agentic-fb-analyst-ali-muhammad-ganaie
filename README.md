Kasparro Agentic Facebook Ads Performance Analyst — AI Agent System
The Multi-Agent Marketing Analytics System is an advanced AI-driven solution engineered to autonomously diagnose and optimize Facebook Ads performance. This project integrates multiple specialized agents that collaborate to deliver a comprehensive end-to-end analytics workflow. Its primary purpose is to monitor campaign trends, interpret fluctuations in Return on Ad Spend (ROAS), and uncover the underlying factors influencing these changes—whether related to audience behavior, creative fatigue, targeting inconsistencies, or shifts in market dynamics.



Kasparro Agentic Facebook Ads Performance Analyst
The Multi-Agent Marketing Analytics System is an advanced AI-driven solution engineered to autonomously diagnose and optimize Facebook Ads performance. This project integrates multiple specialized agents that collaborate to deliver a comprehensive end-to-end analytics workflow. Its primary purpose is to monitor campaign trends, interpret fluctuations in Return on Ad Spend (ROAS), and uncover the underlying factors influencing these changes—whether related to audience behavior, creative fatigue, targeting inconsistencies, or shifts in market dynamics.
Built with a modular and scalable architecture, the system ensures clean separation of responsibilities across different agents, enabling efficient planning, structured data processing, insightful performance interpretation, robust evaluation, and intelligent creative recommendation generation. Each agent functions independently yet coordinates seamlessly through a centralized orchestrator, reflecting industry-grade agentic AI design principles.
In addition to diagnosing performance decline or growth, the system intelligently generates tailored creative recommendations—such as improved headlines, messaging angles, and call-to-action variations—grounded in historical dataset insights. This makes the system not only analytical but also prescriptive, delivering actionable strategies for improving ad engagement and boosting overall marketing ROI. By automating complex ad-diagnosis tasks, the project showcases how agentic AI can significantly enhance digital marketing decision-making and support scalable, data-backed creative optimization Objective The objective of this system is to provide a comprehensive analysis and optimization framework for Facebook ad performance. It is designed to diagnose changes in Return on Ad Spend (ROAS) over time and detect patterns or anomalies in campaign behavior. By identifying key drivers behind performance fluctuations—such as audience fatigue, declining engagement, or underperforming creatives—the system helps advertisers understand the root causes of inefficiencies. Additionally, it generates actionable creative recommendations tailored to campaigns with low click-through rates (CTR), offering improved headlines, messaging angles, and call-to-action variations. These suggestions are grounded in insights extracted from historical campaign data, ensuring that the advice is data-backed, relevant, and directly aligned with improving overall ad effectiveness.



Data Description

(1)The project uses synthetic eCommerce and Facebook Ads datasets stored in the data/ folder. Key columns include:

(2)campaign_name, adset_name, date, spend, impressions, clicks, ctr, purchases, revenue, roas, creative_type, creative_message, audience_type, platform, country.

(3)Data includes both ad performance metrics and campaign metadata. Sample datasets are provided for reproducibility.


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
