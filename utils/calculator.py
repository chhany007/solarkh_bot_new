# utils/calculator.py
import math
import json
import os
from config import *

# Load components database
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "components.json")
with open(data_path, "r", encoding="utf-8") as f:
    DB = json.load(f)

def daily_kwh_from_monthly(monthly_kwh):
    """Convert monthly kWh to daily average"""
    return monthly_kwh / 30.0

def estimate_required_kw(daily_kwh):
    """Estimate required system size in kW"""
    return daily_kwh / (SUN_HOURS * SYSTEM_EFFICIENCY)

def select_panels_and_qty(required_kw, tier="low_cost"):
    """Select best panel and calculate quantity needed"""
    panels = DB["panels"].get(tier, DB["panels"]["low_cost"])
    best = max(panels, key=lambda p: p["watt"])
    qty = math.ceil(required_kw * 1000 / best["watt"])
    return {"panel": best, "qty": qty}

def select_inverter(required_kw, tier="low_cost"):
    """Select appropriate inverter for system"""
    invs = DB["inverters"]["low_cost_preferred"] + DB["inverters"]["high_cost_preferred"]
    needed = required_kw * 1.25
    for i in sorted(invs, key=lambda x: x["kw"]):
        if i["kw"] >= needed:
            return i
    return invs[-1]

def compute_labor_and_materials(system_kw):
    """Calculate labor and materials costs"""
    if system_kw <= 5:
        return LABOR_FLAT_UNDER_5KW, MATERIALS_FLAT_UNDER_5KW
    days = math.ceil(system_kw / KW_PER_DAY_PER_PERSON)
    labor = days * LABOR_DAILY
    materials = MATERIALS_FLAT_UNDER_5KW + (50 * (system_kw - 5))
    return labor, materials

def calculate_quote(monthly_kwh, price_per_kwh, tier="low_cost"):
    """Calculate complete solar system quote"""
    daily = daily_kwh_from_monthly(monthly_kwh)
    kw = estimate_required_kw(daily)
    p = select_panels_and_qty(kw, tier)
    inv = select_inverter(kw, tier)
    lab, mat = compute_labor_and_materials(kw)
    
    panel_cost = p["qty"] * p["panel"]["price"]
    inverter_cost = inv["price"]
    total = panel_cost + inverter_cost + lab + mat
    
    # Calculate payback period
    monthly_savings = monthly_kwh * price_per_kwh
    payback_months = total / monthly_savings if monthly_savings > 0 else 0
    
    return {
        "kw": kw,
        "daily_kwh": daily,
        "panel": p["panel"],
        "panel_qty": p["qty"],
        "panel_cost": panel_cost,
        "inverter": inv,
        "inverter_cost": inverter_cost,
        "labor": lab,
        "materials": mat,
        "total": total,
        "monthly_savings": monthly_savings,
        "payback_months": payback_months,
        "payback_years": payback_months / 12
    }
