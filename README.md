Kasparro Agentic Facebook Ads Performance Analyst — AI Agent System

The Kasparro Agentic Facebook Ads Performance Analyst is a multi-agent AI system designed to autonomously diagnose and optimize Facebook Ads performance. It integrates a set of specialized agents that work together to monitor campaign-level metrics, interpret fluctuations in Return on Ad Spend (ROAS), and identify underlying performance drivers such as creative fatigue, audience saturation, targeting inconsistencies, or shifts in market dynamics. The system follows a modular and scalable architecture where each agent is responsible for a single well-defined task, ensuring clean separation of concerns and enabling easy extensibility. A central orchestrator coordinates these agents to execute end-to-end analytical workflows that are both diagnostic and prescriptive.

In addition to diagnosing ROAS trends, the system generates actionable creative recommendations—such as improved messaging angles, headline variations, and call-to-action enhancements—based on patterns found in the historical dataset. This ensures not only analytical depth but also practical decision-making support that directly impacts marketing ROI. By automating complex analysis steps, the project demonstrates how agentic AI systems can augment performance marketing teams with structured, data-driven intelligence.

Objective

The primary objective of this system is to deliver a comprehensive, automated framework for analyzing Facebook Ads performance. It aims to detect ROAS fluctuations, uncover anomalies, identify the most influential performance drivers, and provide targeted recommendations for optimizing campaigns. The system focuses on understanding audience behavior, creative effectiveness, and campaign-level patterns while also suggesting improved creative strategies for campaigns exhibiting low engagement or weak CTR. Collectively, this enables advertisers to make informed, data-backed decisions that result in more effective and profitable ad strategies.

Design Reasoning

The system is intentionally designed using a modular multi-agent architecture, where each agent performs a single specialized function. This simplifies debugging, enhances reproducibility, and makes the system highly scalable for enterprise environments.

The Planner Agent breaks down natural-language queries into executable analytical subtasks.

The Data Agent ensures consistent access to structured datasets while performing cleaning, filtering, and summarization.

The Insight Agent identifies hypotheses that explain observed performance patterns.

The Evaluator Agent measures quantitative validity and assigns confidence levels to insights.

The Creative Generator Agent transforms insights into prescriptive recommendations.

A central orchestrator ensures that execution remains orderly, traceable, and extensible.

This design allows new agents, additional data sources, or advanced models to be integrated smoothly over time without disrupting existing workflows.

Assumptions

The system assumes that datasets provided in the data/ folder are either already cleaned or can be processed automatically by the Data Agent. It also assumes that standard Facebook Ads metrics—such as impressions, CTR, purchases, revenue, and ROAS—are consistently recorded and follow typical naming conventions. The system is optimized for text-based creative analysis and assumes campaigns follow the common Facebook structure of Campaign → Ad Set → Ad. Multimedia content such as images or videos is not analyzed in the current version.

Limitations and Future Improvements

This version does not integrate directly with the Facebook Ads API and instead operates on static or synthetic datasets. Creative recommendations rely on historical trends and may not capture real-time market dynamics. Additionally, the system does not fully address multi-platform or cross-country campaign discrepancies, which may impact accuracy in diverse advertising environments.

Future improvements include adding real-time data integration through the Facebook Ads API, supporting multi-modal creative evaluation (images and videos), implementing robust state-saving and checkpointing for long-running workflows, expanding retry and confidence scoring mechanisms across agents, and integrating schema drift detection to automatically validate new datasets.

Data Description

The system uses synthetic or sample eCommerce and Facebook Ads datasets stored in the data/ directory. These datasets include key performance and targeting columns such as campaign_name, adset_name, date, spend, impressions, clicks, ctr, purchases, revenue, roas, creative_type, creative_message, audience_type, platform, and country. The data includes both performance metrics and metadata, ensuring all agents have the contextual information needed for accurate analysis.

Agent System Architecture

The multi-agent architecture includes the following roles:

Planner Agent: Decomposes user queries into structured analytical steps.

Data Agent: Loads, transforms, filters, and summarizes datasets.

Insight Agent: Identifies key patterns, anomalies, and causes behind ROAS changes.

Evaluator Agent: Validates insights with quantitative evidence and provides confidence scoring.

Creative Generator Agent: Recommends optimized creatives for low-performing campaigns.

The run.py orchestrator coordinates these agents sequentially to produce a comprehensive performance report.

How to Run

To run the system locally, clone the repository and navigate into the project directory:

git clone https://github.com/ali14567899990/kasparro-agentic-fb-analyst-ali-muhammad-ganaie.git
cd kasparro-agentic-fb-analyst-ali-muhammad-ganaie
Install all required dependencies:

pip install -r requirements.txt


Execute an analysis query:

python -m src.run "Analyze ROAS drop in last 14 days"


All generated insights, evaluation results, and creative recommendations will be saved automatically in the reports/ folder. These include detailed analysis plans, trend explanations, quantified insights, confidence scores, and actionable recommendations.

Example Output

Query: "Analyze ROAS drop in last 14 days"

Sample Insight:
Low CTR in campaign Women-Studio Sports (confidence: 0.72)
  - CTR=0.011, Impressions=266100

- Low CTR in campaign Women | Studio Sports (confidence: 0.93)
  - CTR=0.006, Impressions=159662

- Low CTR in campaign Women_|_Studio_Sports (confidence: 0.86)
  - CTR=0.008, Impressions=378419

  
## Creatives

- Improve creative for campaign Men ComfortMax Launch � try a stronger hook, clearer CTA, and contrasting thumbnail.
- Improve creative for campaign Men ComfortMax Launch � try a stronger hook, clearer CTA, and contrasting thumbnail.
- Improve creative for campaign Men_ComfortMax_Launch � try a stronger hook, clearer CTA, and contrasting thumbnail.


Project Folder Structure

kasparro-agentic-fb-analyst-ali-muhammad-ganaie/        # Main project folder

│
├── data/                                               # Datasets (raw + processed)

│
├── logs/                                               # Execution logs for debugging & observability

│
├── prompts/                                            # Prompt templates for AI agents


│
├── reports/                                            # Auto-generated analytical reports & insights


│
├── src/                                                # Source code

│   ├── agents/                                         # All autonomous agents
│   │   ├── planner.py

│   │   ├── data_agent.py

│   │   ├── insight_agent.py

│   │   ├── evaluator.py

│   │   └── creative_generator.py
│   │
│   ├── orchestrator/                                   # Central controller coordinating all agents
│   │   └── main_orchestrator.py
│   │
│   └── utils/                                          # Utility functions (logging, helpers, retry logic)

│       └── helpers.py


│
├── config/                                             # Configuration files (settings, parameters)

│
├── README.md                                           # Project documentation
│
└── requirements.txt                                     # Python dependencies list
