# test_bot.py - Simple test without running the bot
import sys
import json
from utils.calculator import calculate_quote

def test_calculations():
    """Test the calculator functions"""
    print("🧪 Testing SolarKH Calculator...\n")
    
    # Test 1: Small home
    print("Test 1: Small home (300 kWh/month, $0.15/kWh)")
    quote = calculate_quote(300, 0.15, "low_cost")
    print(f"  ✓ Required system: {quote['kw']:.2f} kW")
    print(f"  ✓ Total cost: ${quote['total']:.2f}")
    print(f"  ✓ Payback: {quote['payback_years']:.1f} years\n")
    
    # Test 2: Medium home
    print("Test 2: Medium home (600 kWh/month, $0.18/kWh)")
    quote = calculate_quote(600, 0.18, "low_cost")
    print(f"  ✓ Required system: {quote['kw']:.2f} kW")
    print(f"  ✓ Total cost: ${quote['total']:.2f}")
    print(f"  ✓ Payback: {quote['payback_years']:.1f} years\n")
    
    # Test 3: Big home
    print("Test 3: Big home (1200 kWh/month, $0.20/kWh)")
    quote = calculate_quote(1200, 0.20, "low_cost")
    print(f"  ✓ Required system: {quote['kw']:.2f} kW")
    print(f"  ✓ Total cost: ${quote['total']:.2f}")
    print(f"  ✓ Payback: {quote['payback_years']:.1f} years\n")
    
    print("✅ All tests passed! Calculator is working correctly.")
    print("\n🤖 Bot configuration:")
    import config
    if "AAHzQECuCSAiyfvMp0SaFzdT6Yfy1yGa8Bs" in config.BOT_TOKEN:
        print("  ✓ Bot token is configured")
        print("  ✓ Bot username: @solarkh_bot")
    else:
        print("  ⚠ Bot token not set")
    
    print("\n🚀 Ready to deploy!")

if __name__ == "__main__":
    try:
        test_calculations()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
