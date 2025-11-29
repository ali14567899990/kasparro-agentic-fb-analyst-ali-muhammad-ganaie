#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the agent with a default prompt
!python -m src.run "Analyze ROAS drop in last 14 days"
