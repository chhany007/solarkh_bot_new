# ☀️ SolarKH Telegram Bot

A Telegram bot for calculating solar panel installation quotes in Cambodia.

## Features

- 📊 Custom solar quotes based on monthly consumption
- 🏠 Pre-configured templates (small/medium/big homes, factories)
- 💰 Detailed cost breakdown (panels, inverters, labor, materials)
- 📈 ROI calculation with payback period
- 🌐 Multi-tier pricing (low-cost/high-cost components)

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- A Telegram account
- A bot token from [@BotFather](https://t.me/BotFather)

### 2. Get Your Bot Token

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` and follow the instructions
3. Copy the bot token you receive

### 3. Installation

#### Option A: Using PowerShell Setup Script (Windows)

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup_solarbot_all_fixed.ps1
```

#### Option B: Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Or create a virtual environment first
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
```

### 4. Configure Bot Token

Edit `config.py` and replace the placeholder with your actual token:

```python
BOT_TOKEN = "your_actual_token_here"
```

### 5. Run the Bot

```bash
python bot.py
```

## Usage

### Commands

#### `/start`
Welcome message with bot overview

#### `/help`
Display help information and usage examples

#### `/quote <monthly_kwh> <price_per_kwh>`
Get a custom solar installation quote

**Example:**
```
/quote 450 0.20
```
- `450` = monthly electricity consumption in kWh
- `0.20` = current electricity price per kWh in USD

#### `/template <type> <price_per_kwh>`
Get a quote using pre-configured templates

**Template types:**
- `small` - Small home (300 kWh/month)
- `medium` - Medium home (600 kWh/month)
- `big` - Big home (1200 kWh/month)
- `factory` - Factory (5000 kWh/month)

**Example:**
```
/template medium 0.15
```

## Configuration

### Customizing System Parameters

Edit `config.py` to adjust:

- `SUN_HOURS` - Average daily sun hours (default: 5.0)
- `SYSTEM_EFFICIENCY` - Solar system efficiency (default: 0.80)
- `LABOR_DAILY` - Daily labor rate (default: $100)
- `CURRENCY` - Currency symbol (default: "$")

### Adding Components

Edit `data/components.json` to add or modify:

- Solar panels (low_cost/high_cost)
- Inverters
- Batteries
- Labor and material rates
- Template consumption values

## Project Structure

```
SolarKH_TelegramBot/
├── bot.py                      # Main bot application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── data/
│   └── components.json         # Solar components database
└── utils/
    ├── calculator.py           # Quote calculation logic
    └── formatter.py            # Output formatting
```

## Quote Calculation

The bot calculates:

1. **System Size** - Required kW based on consumption and sun hours
2. **Components** - Optimal panels and inverter selection
3. **Installation Costs** - Labor and materials
4. **Total Investment** - Complete system cost
5. **ROI** - Monthly savings and payback period

### Formula

```
Required kW = Daily kWh / (Sun Hours × System Efficiency)
```

## Troubleshooting

### Bot doesn't respond
- Verify your bot token is correct in `config.py`
- Check your internet connection
- Ensure the bot is not stopped by another instance

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're running Python 3.8+

### Calculation errors
- Check `data/components.json` is valid JSON
- Ensure all numeric values in config are positive

## Support

For issues or questions:
1. Check this README
2. Review the `/help` command in the bot
3. Contact SolarKH support team

## License

Copyright © 2024 SolarKH. All rights reserved.

---

Made with ☀️ by SolarKH Team
