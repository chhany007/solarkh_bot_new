# utils/formatter.py
from config import CURRENCY

def format_quote(q):
    """Format quote data into readable message"""
    message = f"""
☀️ **SolarKH Quote**

📊 **System Requirements:**
• Required System Size: {q['kw']:.2f} kW
• Daily Consumption: {q['daily_kwh']:.2f} kWh

🔆 **Solar Panels:**
• {q['panel']['name']} ({q['panel']['watt']}W)
• Quantity: {q['panel_qty']} panels
• Cost: {CURRENCY}{q['panel_cost']:.2f}

🔌 **Inverter:**
• {q['inverter']['name']} ({q['inverter']['kw']}kW)
• Cost: {CURRENCY}{q['inverter_cost']:.2f}

💼 **Installation:**
• Labor: {CURRENCY}{q['labor']:.2f}
• Materials: {CURRENCY}{q['materials']:.2f}

💰 **Total Investment:** {CURRENCY}{q['total']:.2f}

📈 **Savings:**
• Monthly Savings: {CURRENCY}{q['monthly_savings']:.2f}
• Payback Period: {q['payback_years']:.1f} years ({q['payback_months']:.0f} months)

✅ Contact us to proceed with installation!
"""
    return message.strip()

def format_templates():
    """Format template options"""
    return """
📋 **Quick Templates:**
Use /template <type> <price_per_kwh>

Available types:
• `small` - Small home (300 kWh/month)
• `medium` - Medium home (600 kWh/month)
• `big` - Big home (1200 kWh/month)
• `factory` - Factory (5000 kWh/month)

Example: `/template medium 0.15`
"""
