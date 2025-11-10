# utils/product_viewer.py
import json
import os
from languages import get_text, get_language

# Load components database
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "components.json")
with open(data_path, "r", encoding="utf-8") as f:
    DB = json.load(f)

def format_product_specs(product, product_type, user_id):
    """Format product specifications for display"""
    lang = get_language(user_id)
    
    message = f"📦 **{product['name']}**\n\n"
    message += f"💰 Price: ${product['price']}\n\n"
    message += f"📋 **Specifications:**\n"
    
    if product_type == "panel":
        message += f"• Power: {product['watt']}W\n"
        if 'specs' in product:
            specs = product['specs']
            message += f"• Efficiency: {specs.get('efficiency', 'N/A')}\n"
            message += f"• Voltage: {specs.get('voltage', 'N/A')}\n"
            message += f"• Type: {specs.get('type', 'N/A')}\n"
            message += f"• Dimensions: {specs.get('dimensions', 'N/A')}\n"
            message += f"• Warranty: {specs.get('warranty', 'N/A')}\n"
    
    elif product_type == "inverter":
        message += f"• Power: {product['kw']}kW\n"
        if 'specs' in product:
            specs = product['specs']
            message += f"• Type: {specs.get('type', 'N/A')}\n"
            message += f"• Phases: {specs.get('phases', 'N/A')}\n"
            message += f"• Efficiency: {specs.get('efficiency', 'N/A')}\n"
            message += f"• Battery Compatible: {'Yes' if specs.get('battery_compatible') else 'No'}\n"
            message += f"• Warranty: {specs.get('warranty', 'N/A')}\n"
    
    elif product_type == "battery":
        message += f"• Capacity: {product['kwh']}kWh\n"
        if 'specs' in product:
            specs = product['specs']
            message += f"• Type: {specs.get('type', 'N/A')}\n"
            message += f"• Voltage: {specs.get('voltage', 'N/A')}\n"
            message += f"• Cycles: {specs.get('cycles', 'N/A')}\n"
            message += f"• Expandable: {'Yes' if specs.get('expandable') else 'No'}\n"
            message += f"• Warranty: {specs.get('warranty', 'N/A')}\n"
    
    return message

def get_all_panels(user_id):
    """Get all solar panels"""
    panels = []
    for tier in ['low_cost', 'high_cost']:
        panels.extend(DB['panels'][tier])
    return panels

def get_all_inverters(user_id):
    """Get all inverters"""
    inverters = []
    for tier in ['low_cost_preferred', 'high_cost_preferred']:
        inverters.extend(DB['inverters'][tier])
    return inverters

def get_all_batteries(user_id):
    """Get all batteries"""
    return DB['batteries']
