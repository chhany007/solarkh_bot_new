# Test quote calculation
from utils.calculator import calculate_quote
from utils.formatter import format_quote

try:
    print("Testing quote calculation...")
    q = calculate_quote(800, 0.18)
    print("\n✅ Calculation successful!")
    print(f"System size: {q['kw']:.2f} kW")
    print(f"Total cost: ${q['total']:.2f}")
    print(f"Monthly savings: ${q['monthly_savings']:.2f}")
    
    print("\n\nTesting formatter...")
    formatted = format_quote(q, 123456)  # Test user ID
    print(formatted)
    print("\n✅ Formatting successful!")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
