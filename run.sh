#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the agent with a default prompt
python src/run.py "Analyze ROAS drop in last 14 days"
