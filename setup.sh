#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install the client library in editable mode
pip install -e .

# Launch Jupyter Lab
jupyter lab test_notebook.ipynb
