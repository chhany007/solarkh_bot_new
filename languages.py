# languages.py - Bilingual support (English/Khmer)

LANGUAGES = {
    "en": {
        "welcome": """
🌞 Welcome to SolarKH Bot!

Your trusted solar energy partner in Cambodia 🇰🇭

What can I help you with today?

💰 Get Quote - Calculate solar system cost
📋 Templates - Quick quotes for common sizes
🛒 Products - Browse panels, inverters & batteries
📚 Learn - Solar energy education center
🌐 Language - Switch to ភាសាខ្មែរ

📞 Contact us for professional installation!
📢 Follow updates: @solar_kh

Let's power your future with clean energy! ☀️
""",
        "help": """
📖 **How to Use SolarKH Bot**

🔹 Get a Quote:
/quote <monthly_kwh> <price_per_kwh>
Example: /quote 300 0.15

🔹 Use Templates:
/template - Quick quotes for common sizes

🔹 View Products:
/products - Browse solar panels, inverters & batteries

🔹 Learn About Solar:
/learn - Educational guides & system recommendations

🔹 Change Language:
/language - Switch between English/Khmer

💡 Tip: Check your electricity bill for monthly kWh usage

📢 Follow our channel: @solar_kh
""",
        "language_select": "🌐 **Select Language / ជ្រើសរើសភាសា**\n\nChoose your preferred language:",
        "language_changed": "✅ Language changed to English",
        "calculating": "⏳ Calculating your solar quote...",
        "calculating_template": "⏳ Calculating {} home quote ({} kWh/month)...",
        "error_params": "❌ Please provide both parameters:\n`/quote <monthly_kwh> <price_per_kwh>`\n\nExample: `/quote 300 0.15`",
        "error_positive": "❌ Values must be positive numbers!",
        "error_invalid": "❌ Invalid input. Please use numbers only.\nExample: `/quote 300 0.15`",
        "error_general": "❌ An error occurred. Please try again or contact support.",
        "template_list": """
📋 **Quick Templates:**
Use /template <type> <price_per_kwh>

Available types:
• `small` - Small home (300 kWh/month)
• `medium` - Medium home (600 kWh/month)
• `big` - Big home (1200 kWh/month)
• `factory` - Factory (5000 kWh/month)

Example: `/template medium 0.15`
""",
        "template_unknown": "❌ Unknown template: {}\n\n",
        "template_error": "❌ Invalid price. Please use a number.\nExample: `/template medium 0.15`",
        "quote_title": "☀️ **SolarKH Quote**",
        "system_req": "📊 **System Requirements:**",
        "required_size": "• Required System Size: {:.2f} kW",
        "daily_consumption": "• Daily Consumption: {:.2f} kWh",
        "solar_panels": "🔆 **Solar Panels:**",
        "panel_info": "• {} ({}W)",
        "quantity": "• Quantity: {} panels",
        "inverter": "🔌 **Inverter:**",
        "inverter_info": "• {} ({}kW)",
        "installation": "💼 **Installation:**",
        "labor": "• Labor: {}",
        "materials": "• Materials: {}",
        "total_investment": "💰 **Total Investment:** {}",
        "savings": "📈 **Savings:**",
        "monthly_savings": "• Monthly Savings: {}",
        "payback": "• Payback Period: {:.1f} years ({:.0f} months)",
        "contact": "✅ Contact us to proceed with installation!\n\n📢 Follow updates: @solar_kh",
        "cost": "• Cost: {}",
        "small": "small",
        "medium": "medium",
        "big": "big",
        "factory": "factory",
        "products_menu": "🛒 **Product Catalog**\n\nWhat would you like to view?",
        "learn_menu": "📚 **Solar Education Center**\n\nChoose a topic to learn more:",
        "product_details": "📦 **Product Details**",
        "specs": "📋 **Specifications:**",
        "back_to_menu": "⬅️ Back to Menu"
    },
    "kh": {
        "welcome": """
🌞 សូមស្វាគមន៍មកកាន់ SolarKH Bot!

ដៃគូថាមពលសូឡាដែលអ្នកទុកចិត្តនៅកម្ពុជា 🇰🇭

តើខ្ញុំអាចជួយអ្វីបានសម្រាប់អ្នកថ្ងៃនេះ?

💰 សម្រង់តម្លៃ - គណនាតម្លៃប្រព័ន្ធសូឡា
📋 គំរូ - សម្រង់រហ័សសម្រាប់ទំហំទូទៅ
🛒 ផលិតផល - រកមើលបន្ទះសូឡា inverter និងថ្ម
📚 រៀនសូត្រ - មជ្ឈមណ្ឌលអប់រំថាមពលសូឡា
🌐 ភាសា - ប្តូរទៅ English

📞 ទាក់ទងមកយើងសម្រាប់ការដំឡើងប្រកបដោយវិជ្ជាជីវៈ!
📢 តាមដានព័ត៌មាន: @solar_kh

សូមបំពេញអនាគតរបស់អ្នកដោយថាមពលស្អាត! ☀️
""",
        "help": """
📖 **របៀបប្រើ SolarKH Bot**

🔹 ទទួលសម្រង់តម្លៃ:
/quote <kwh_ប្រចាំខែ> <តម្លៃ_kwh>
ឧទាហរណ៍: /quote 300 0.15

🔹 ប្រើគំរូ:
/template - សម្រង់រហ័សសម្រាប់ទំហំទូទៅ

🔹 មើលផលិតផល:
/products - រកមើលបន្ទះសូឡា inverter និងថ្ម

🔹 រៀនអំពីសូឡា:
/learn - មគ្គុទ្ទេសក និងការណែនាំប្រព័ន្ធ

🔹 ប្តូរភាសា:
/language - ប្តូរភាសា អង់គ្លេស/ខ្មែរ

💡 ជំនួយ: ពិនិត្យវិក្កយបត្រអគ្គិសនីសម្រាប់ការប្រើប្រាស់ kWh ប្រចាំខែ

📢 តាមដានឆានែល: @solar_kh
""",
        "old_help": """
 **របៀបប្រើ SolarKH Bot:**

**ទទួលបានសម្រង់តម្លៃផ្ទាល់ខ្លួន:**
`/quote <kwh_ប្រចាំខែ> <តម្លៃ_ក្នុងមួយ_kwh>`

ឧទាហរណ៍: `/quote 450 0.20`
- kwh_ប្រចាំខែ: ការប្រើប្រាស់អគ្គិសនីជាមធ្យមប្រចាំខែរបស់អ្នក
- តម្លៃ_ក្នុងមួយ_kwh: អត្រាអគ្គិសនីបច្ចុប្បន្នរបស់អ្នក

**ប្រើគំរូរហ័ស:**
`/template <ប្រភេទ> <តម្លៃ_ក្នុងមួយ_kwh>`

គំរូដែលមាន:
• `តូច` - ផ្ទះតូច (300 kWh/ខែ)
• `មធ្យម` - ផ្ទះមធ្យម (600 kWh/ខែ)
• `ធំ` - ផ្ទះធំ (1200 kWh/ខែ)
• `រោងចក្រ` - រោងចក្រ (5000 kWh/ខែ)

ឧទាហរណ៍: `/template ធំ 0.18`

**ប្តូរភាសា:**
• `/language` - ប្តូររវាងភាសាអង់គ្លេស/ខ្មែរ

**ទទួលបានព័ត៌មានថ្មីៗ:**
📢 តាមដានឆានែលរបស់យើង: @solar_kh

ត្រូវការជំនួយ? ទាក់ទងមកយើង! 📞
""",
        "language_select": "🌐 **Select Language / ជ្រើសរើសភាសា**\n\nជ្រើសរើសភាសាដែលអ្នកចង់បាន:",
        "language_changed": "✅ បានប្តូរភាសាទៅជាភាសាខ្មែរ",
        "calculating": "⏳ កំពុងគណនាសម្រង់តម្លៃព្រះអាទិត្យរបស់អ្នក...",
        "calculating_template": "⏳ កំពុងគណនាសម្រង់តម្លៃផ្ទះ{} ({} kWh/ខែ)...",
        "error_params": "❌ សូមផ្តល់ប៉ារ៉ាម៉ែត្រទាំងពីរ:\n`/quote <kwh_ប្រចាំខែ> <តម្លៃ_ក្នុងមួយ_kwh>`\n\nឧទាហរណ៍: `/quote 300 0.15`",
        "error_positive": "❌ តម្លៃត្រូវតែជាលេខវិជ្ជមាន!",
        "error_invalid": "❌ ការបញ្ចូលមិនត្រឹមត្រូវ។ សូមប្រើតែលេខប៉ុណ្ណោះ។\nឧទាហរណ៍: `/quote 300 0.15`",
        "error_general": "❌ មានកំហុសកើតឡើង។ សូមព្យាយាមម្តងទៀត ឬទាក់ទងមកយើង។",
        "template_list": """
📋 **គំរូរហ័ស:**
ប្រើ /template <ប្រភេទ> <តម្លៃ_ក្នុងមួយ_kwh>

ប្រភេទដែលមាន:
• `តូច` - ផ្ទះតូច (300 kWh/ខែ)
• `មធ្យម` - ផ្ទះមធ្យម (600 kWh/ខែ)
• `ធំ` - ផ្ទះធំ (1200 kWh/ខែ)
• `រោងចក្រ` - រោងចក្រ (5000 kWh/ខែ)

ឧទាហរណ៍: `/template មធ្យម 0.15`
""",
        "template_unknown": "❌ មិនស្គាល់គំរូ: {}\n\n",
        "template_error": "❌ តម្លៃមិនត្រឹមត្រូវ។ សូមប្រើលេខ។\nឧទាហរណ៍: `/template មធ្យម 0.15`",
        "quote_title": "☀️ **សម្រង់តម្លៃ SolarKH**",
        "system_req": "📊 **តម្រូវការប្រព័ន្ធ:**",
        "required_size": "• ទំហំប្រព័ន្ធត្រូវការ: {:.2f} kW",
        "daily_consumption": "• ការប្រើប្រាស់ប្រចាំថ្ងៃ: {:.2f} kWh",
        "solar_panels": "🔆 **បន្ទះពន្លឺព្រះអាទិត្យ:**",
        "panel_info": "• {} ({}W)",
        "quantity": "• បរិមាណ: {} បន្ទះ",
        "inverter": "🔌 **ឧបករណ៍បំប្លែង:**",
        "inverter_info": "• {} ({}kW)",
        "installation": "💼 **ការដំឡើង:**",
        "labor": "• ថ្លៃដំណើរការ: {}",
        "materials": "• សម្ភារៈ: {}",
        "total_investment": "💰 **ការវិនិយោគសរុប:** {}",
        "savings": "📈 **ការសន្សំ:**",
        "monthly_savings": "• ការសន្សំប្រចាំខែ: {}",
        "payback": "• រយៈពេលសងត្រលប់: {:.1f} ឆ្នាំ ({:.0f} ខែ)",
        "contact": "✅ ទាក់ទងមកយើងដើម្បីបន្តការដំឡើង!\n\n📢 តាមដានព័ត៌មាន: @solar_kh",
        "cost": "• តម្លៃ: {}",
        "small": "តូច",
        "medium": "មធ្យម",
        "big": "ធំ",
        "factory": "រោងចក្រ",
        "products_menu": "🛒 **កាតាឡុកផលិតផល**\n\nអ្នកចង់មើលអ្វី?",
        "learn_menu": "📚 **មជ្ឈមណ្ឌលអប់រំសូឡា**\n\nជ្រើសរើសប្រធានបទដើម្បីរៀនបន្ថែម:",
        "product_details": "📦 **ព័ត៌មានលម្អិតផលិតផល**",
        "specs": "📋 **លក្ខណៈបច្ចេកទេស:**",
        "back_to_menu": "⬅️ ត្រឡប់ទៅម៉ឺនុយ"
    }
}

# User language preferences (stored in memory)
user_languages = {}

def get_text(user_id, key):
    """Get translated text for a user"""
    lang = user_languages.get(user_id, "en")
    return LANGUAGES[lang].get(key, LANGUAGES["en"][key])

def set_language(user_id, lang):
    """Set user's preferred language"""
    if lang in LANGUAGES:
        user_languages[user_id] = lang
        return True
    return False

def get_language(user_id):
    """Get user's current language"""
    return user_languages.get(user_id, "en")

def format_currency(amount):
    """Format currency with $ symbol"""
    from config import CURRENCY
    return f"{CURRENCY}{amount:.2f}"
