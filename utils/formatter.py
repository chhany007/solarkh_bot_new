# utils/formatter.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from languages import get_text, format_currency

def format_quote(q, user_id):
    """Format quote data into readable message"""
    message = f"""
{get_text(user_id, 'quote_title')}

{get_text(user_id, 'system_req')}
{get_text(user_id, 'required_size').format(q['kw'])}
{get_text(user_id, 'daily_consumption').format(q['daily_kwh'])}

{get_text(user_id, 'solar_panels')}
{get_text(user_id, 'panel_info').format(q['panel']['name'], q['panel']['watt'])}
{get_text(user_id, 'quantity').format(q['panel_qty'])}
{get_text(user_id, 'cost').format(format_currency(q['panel_cost']))}

{get_text(user_id, 'inverter')}
{get_text(user_id, 'inverter_info').format(q['inverter']['name'], q['inverter']['kw'])}
{get_text(user_id, 'cost').format(format_currency(q['inverter_cost']))}

{get_text(user_id, 'installation')}
{get_text(user_id, 'labor').format(format_currency(q['labor']))}
{get_text(user_id, 'materials').format(format_currency(q['materials']))}

{get_text(user_id, 'total_investment').format(format_currency(q['total']))}

{get_text(user_id, 'savings')}
{get_text(user_id, 'monthly_savings').format(format_currency(q['monthly_savings']))}
{get_text(user_id, 'payback').format(q['payback_years'], q['payback_months'])}

{get_text(user_id, 'contact')}
"""
    return message.strip()

def format_templates(user_id):
    """Format template options"""
    return get_text(user_id, 'template_list')
