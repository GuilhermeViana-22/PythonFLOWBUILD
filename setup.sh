#!/usr/bin/env bash
# Simple setup script to create a virtual environment and install dependencies
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
