#!/bin/bash
# keepalive.sh - Keep bot running with auto-restart

cd "$(dirname "$0")"

while true; do
    echo "$(date): Starting SolarKH Bot..."
    python3.10 bot.py
    
    echo "$(date): Bot stopped. Restarting in 5 seconds..."
    sleep 5
done
