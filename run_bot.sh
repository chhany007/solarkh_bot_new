#!/bin/bash
# run_bot.sh - Script to run SolarKH bot on PythonAnywhere

# Change to bot directory
cd "$(dirname "$0")"

# Run the bot
python3.10 bot.py
