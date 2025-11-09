# setup_solarbot_all.ps1
# One-click setup for SolarKH Telegram Bot
# Usage: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\setup_solarbot_all.ps1

Write-Host "✅ Starting SolarKH Telegram Bot setup..." -ForegroundColor Cyan

# Use the current folder as project root
$root = $PSScriptRoot
if (-not $root) { $root = Get-Location }
$projectDir = Join-Path $root "SolarKH_TelegramBot"
$dataDir = Join-Path $projectDir "data"
$utilsDir = Join-Path $projectDir "utils"

Write-Host "Creating folders..."
New-Item -ItemType Directory -Force -Path $projectDir, $dataDir, $utilsDir | Out-Null

# 1️⃣ requirements.txt
@'
python-telegram-bot==20.4
'@ | Out-File -FilePath (Join-Path $projectDir "requirements.txt") -Encoding utf8 -Force

# 2️⃣ config.py
@'
# config.py
BOT_TOKEN = "<PUT_YOUR_TELEGRAM_BOT_TOKEN_HERE>"

SUN_HOURS = 5.0
SYSTEM_EFFICIENCY = 0.80
LABOR_DAILY = 100.0
LABOR_FLAT_UNDER_5KW = 350.0
MATERIALS_FLAT_UNDER_5KW = 400.0
KW_PER_DAY_PER_PERSON = 5.0
CURRENCY = "$"
'@ | Out-File -FilePath (Join-Path $projectDir "config.py") -Encoding utf8 -Force

# 3️⃣ components.json
@'
{
  "panels": {
    "low_cost": [
      {"name": "LV 340W", "watt": 340, "price": 44},
      {"name": "LV 550W", "watt": 550, "price": 66},
      {"name": "LV 620W", "watt": 620, "price": 82}
    ],
    "high_cost": [
      {"name": "LongGi 360W", "watt": 360, "price": 49},
      {"name": "LongGi 585W", "watt": 585, "price": 99}
    ]
  },
  "inverters": {
    "low_cost_preferred": [
      {"name": "LUX 6kW", "kw": 6, "price": 516},
      {"name": "LV 5kW", "kw": 5, "price": 488}
    ],
    "high_cost_preferred": [
      {"name": "DeYe EU1p 5kW", "kw": 5, "price": 888},
      {"name": "DeYe 8kW", "kw": 8, "price": 1320},
      {"name": "DeYe 10kW", "kw": 10, "price": 1800},
      {"name": "LV 10kW", "kw": 10, "price": 1116}
    ]
  },
  "batteries": [
    {"name": "DeYe 5.12kWh", "kwh": 5.12, "price": 1380},
    {"name": "LV 5.12kWh", "kwh": 5.12, "price": 678},
    {"name": "LV 10.24kWh", "kwh": 10.24, "price": 1208},
    {"name": "LV 15.36kWh", "kwh": 15.36, "price": 1440}
  ],
  "labor": {"flat_under_5kw": 350, "daily_rate": 100},
  "materials": {"flat_under_5kw": 400},
  "templates": {
    "small_home_kwh": 300,
    "medium_home_kwh": 600,
    "big_home_kwh": 1200,
    "factory_kwh": 5000
  }
}
'@ | Out-File -FilePath (Join-Path $dataDir "components.json") -Encoding utf8 -Force

# 4️⃣ utils/calculator.py
@'
# utils/calculator.py
import math, json
from config import *

with open("data/components.json", "r", encoding="utf-8") as f:
    DB = json.load(f)

def daily_kwh_from_monthly(monthly_kwh):
    return monthly_kwh / 30.0

def estimate_required_kw(daily_kwh):
    return daily_kwh / (SUN_HOURS * SYSTEM_EFFICIENCY)

def select_panels_and_qty(required_kw, tier="low_cost"):
    panels = DB["panels"].get(tier, DB["panels"]["low_cost"])
    best = max(panels, key=lambda p: p["watt"])
    qty = math.ceil(required_kw * 1000 / best["watt"])
    return {"panel": best, "qty": qty}

def select_inverter(required_kw, tier="low_cost"):
    invs = DB["inverters"]["low_cost_preferred"] + DB["inverters"]["high_cost_preferred"]
    needed = required_kw * 1.25
    for i in sorted(invs, key=lambda x: x["kw"]):
        if i["kw"] >= needed: return i
    return invs[-1]

def compute_labor_and_materials(system_kw):
    if system_kw <= 5: return LABOR_FLAT_UNDER_5KW, MATERIALS_FLAT_UNDER_5KW
    days = math.ceil(system_kw / KW_PER_DAY_PER_PERSON)
    return days * LABOR_DAILY, MATERIALS_FLAT_UNDER_5KW + (50 * (system_kw - 5))

def calculate_quote(monthly_kwh, price_per_kwh, tier="low_cost"):
    daily = daily_kwh_from_monthly(monthly_kwh)
    kw = estimate_required_kw(daily)
    p = select_panels_and_qty(kw, tier)
    inv = select_inverter(kw, tier)
    lab, mat = compute_labor_and_materials(kw)
    total = p["qty"] * p["panel"]["price"] + inv["price"] + lab + mat
    return {"kw": kw, "total": total}
'@ | Out-File -FilePath (Join-Path $utilsDir "calculator.py") -Encoding utf8 -Force

# 5️⃣ utils/formatter.py
@'
# utils/formatter.py
from config import CURRENCY

def format_quote(q):
    return f"✅ Required system: {q['kw']:.2f} kW\n➡️ Estimated total: {CURRENCY}{q['total']:.2f}"
'@ | Out-File -FilePath (Join-Path $utilsDir "formatter.py") -Encoding utf8 -Force

# 6️⃣ bot.py
@'
# bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils.calculator import calculate_quote
from utils.formatter import format_quote
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("☀️ Welcome to SolarKH! Send /quote <monthly_kwh> <price_per_kwh>")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        monthly_kwh = float(context.args[0])
        price = float(context.args[1])
        q = calculate_quote(monthly_kwh, price)
        await update.message.reply_text(format_quote(q))
    except Exception:
        await update.message.reply_text("Usage: /quote 300 0.15")

def main():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))
    print("✅ Bot started. Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
'@ | Out-File -FilePath (Join-Path $projectDir "bot.py") -Encoding utf8 -Force

Write-Host "All project files created." -ForegroundColor Yellow

# 7️⃣ Create venv and install
$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    Write-Host "Python found. Creating venv..." -ForegroundColor Cyan
    & python -m venv (Join-Path $projectDir "venv")
    Write-Host "Installing dependencies..."
    & (Join-Path $projectDir "venv\Scripts\python.exe") -m pip install --upgrade pip
    & (Join-Path $projectDir "venv\Scripts\python.exe") -m pip install -r (Join-Path $projectDir "requirements.txt")
    Write-Host "✅ Virtual environment ready!" -ForegroundColor Green
    Write-Host "Next steps:"
    Write-Host "  cd '$projectDir'"
    Write-Host "  .\\venv\\Scripts\\Activate"
    Write-Host "  python bot.py"
} else {
    Write-Host "⚠️ Python not found. Please install Python and re-run." -ForegroundColor Red
}

Write-Host "✅ Done. Edit config.py to add your BOT_TOKEN." -ForegroundColor Green
