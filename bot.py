# bot.py
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from utils.calculator import calculate_quote, DB
from utils.formatter import format_quote, format_templates
from languages import get_text, set_language, get_language
import config

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_main_keyboard(user_id):
    """Get main reply keyboard based on user language"""
    lang = get_language(user_id)
    if lang == 'kh':
        keyboard = [
            [KeyboardButton("💰 សម្រង់តម្លៃ"), KeyboardButton("📋 គំរូ")],
            [KeyboardButton("🌐 ប្តូរភាសា"), KeyboardButton("❓ ជំនួយ")]
        ]
    else:
        keyboard = [
            [KeyboardButton("💰 Get Quote"), KeyboardButton("📋 Templates")],
            [KeyboardButton("🌐 Language"), KeyboardButton("❓ Help")]
        ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message when /start is issued"""
    user_id = update.effective_user.id
    welcome_message = get_text(user_id, 'welcome')
    keyboard = get_main_keyboard(user_id)
    await update.message.reply_text(welcome_message, reply_markup=keyboard)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message"""
    user_id = update.effective_user.id
    help_text = get_text(user_id, 'help')
    await update.message.reply_text(help_text)

async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /language command"""
    user_id = update.effective_user.id
    
    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
            InlineKeyboardButton("🇰🇭 ភាសាខ្មែរ", callback_data="lang_kh")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        get_text(user_id, 'language_select'),
        reply_markup=reply_markup
    )

async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle language selection callback"""
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    lang = query.data.split('_')[1]
    
    set_language(user_id, lang)
    
    # Edit the message to show language changed
    await query.edit_message_text(
        text=get_text(user_id, 'language_changed')
    )
    
    # Send new message with updated keyboard
    keyboard = get_main_keyboard(user_id)
    welcome_msg = get_text(user_id, 'welcome')
    await query.message.reply_text(welcome_msg, reply_markup=keyboard)

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /quote command"""
    user_id = update.effective_user.id
    
    try:
        if len(context.args) < 2:
            await update.message.reply_text(
                get_text(user_id, 'error_params')
            )
            return
        
        monthly_kwh = float(context.args[0])
        price_per_kwh = float(context.args[1])
        
        if monthly_kwh <= 0 or price_per_kwh <= 0:
            await update.message.reply_text(get_text(user_id, 'error_positive'))
            return
        
        # Calculate quote
        await update.message.reply_text(get_text(user_id, 'calculating'))
        q = calculate_quote(monthly_kwh, price_per_kwh)
        
        # Send formatted quote
        await update.message.reply_text(format_quote(q, user_id))
        
        logger.info(f"Quote generated for user {user_id}: {monthly_kwh} kWh")
        
    except ValueError:
        await update.message.reply_text(
            get_text(user_id, 'error_invalid')
        )
    except Exception as e:
        logger.error(f"Error in quote command: {e}")
        await update.message.reply_text(get_text(user_id, 'error_general'))

async def template(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /template command - show template buttons"""
    user_id = update.effective_user.id
    lang = get_language(user_id)
    
    # Show template selection with inline buttons
    if lang == 'kh':
        keyboard = [
            [InlineKeyboardButton("🏠 តូច (300 kWh)", callback_data="template_small")],
            [InlineKeyboardButton("🏡 មធ្យម (600 kWh)", callback_data="template_medium")],
            [InlineKeyboardButton("🏢 ធំ (1200 kWh)", callback_data="template_big")],
            [InlineKeyboardButton("🏭 រោងចក្រ (5000 kWh)", callback_data="template_factory")]
        ]
        message = "📋 សូមជ្រើសរើសគំរូ:\n\nតើអ្នកចង់បានសម្រង់តម្លៃសម្រាប់ប្រភេទណា?"
    else:
        keyboard = [
            [InlineKeyboardButton("🏠 Small Home (300 kWh)", callback_data="template_small")],
            [InlineKeyboardButton("🏡 Medium Home (600 kWh)", callback_data="template_medium")],
            [InlineKeyboardButton("🏢 Big Home (1200 kWh)", callback_data="template_big")],
            [InlineKeyboardButton("🏭 Factory (5000 kWh)", callback_data="template_factory")]
        ]
        message = "📋 Select a template:\n\nWhich type of quote would you like?"
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def template_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle template selection callback"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    lang = get_language(user_id)
    template_type = query.data.replace("template_", "")
    
    templates = DB.get("templates", {})
    template_map = {
        "small": templates.get("small_home_kwh", 300),
        "medium": templates.get("medium_home_kwh", 600),
        "big": templates.get("big_home_kwh", 1200),
        "factory": templates.get("factory_kwh", 5000)
    }
    
    # Ask for electricity price
    if lang == 'kh':
        type_names = {"small": "តូច", "medium": "មធ្យម", "big": "ធំ", "factory": "រោងចក្រ"}
        msg = f"✅ អ្នកបានជ្រើសរើស: {type_names[template_type]} ({template_map[template_type]} kWh)\n\n💡 សូមបញ្ចូលតម្លៃអគ្គិសនីរបស់អ្នក ($/kWh)\nឧទាហរណ៍: 0.15"
    else:
        msg = f"✅ You selected: {template_type.title()} ({template_map[template_type]} kWh)\n\n💡 Please enter your electricity price ($/kWh)\nExample: 0.15"
    
    await query.edit_message_text(msg)
    context.user_data['waiting_for_price'] = template_type
    
    try:
        template_type = context.args[0].lower() if context.args else None
        if not template_type:
            return
        
        price_per_kwh = float(context.args[1])
        
        if template_type not in template_map:
            await update.message.reply_text(
                get_text(user_id, 'template_unknown').format(template_type) + format_templates(user_id)
            )
            return
        
        if price_per_kwh <= 0:
            await update.message.reply_text(get_text(user_id, 'error_positive'))
            return
        
        monthly_kwh = template_map[template_type]
        
        # Get template name in user's language
        lang = get_language(user_id)
        if template_type in template_map_kh:
            display_type = template_type
        else:
            display_type = get_text(user_id, template_type)
        
        # Calculate quote
        await update.message.reply_text(
            get_text(user_id, 'calculating_template').format(display_type, monthly_kwh)
        )
        q = calculate_quote(monthly_kwh, price_per_kwh)
        
        # Send formatted quote
        await update.message.reply_text(format_quote(q, user_id))
        
        logger.info(f"Template quote '{template_type}' for user {user_id}")
        
    except ValueError:
        await update.message.reply_text(
            get_text(user_id, 'template_error')
        )
    except Exception as e:
        logger.error(f"Error in template command: {e}")
        await update.message.reply_text(get_text(user_id, 'error_general'))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses from reply keyboard"""
    user_id = update.effective_user.id
    text = update.message.text
    
    # Map button text to commands
    button_map = {
        "💰 Get Quote": "quote_prompt",
        "💰 សម្រង់តម្លៃ": "quote_prompt",
        "📋 Templates": "templates",
        "📋 គំរូ": "templates",
        "🌐 Language": "language",
        "🌐 ប្តូរភាសា": "language",
        "❓ Help": "help",
        "❓ ជំនួយ": "help"
    }
    
    action = button_map.get(text)
    
    if action == "quote_prompt":
        lang = get_language(user_id)
        if lang == 'kh':
            msg = "💡 សូមបញ្ចូលការប្រើប្រាស់អគ្គិសនីប្រចាំខែ និងតម្លៃ:\n\nឧទាហរណ៍: 300 0.15\n(300 kWh, $0.15/kWh)"
        else:
            msg = "💡 Please enter your monthly usage and price:\n\nExample: 300 0.15\n(300 kWh, $0.15/kWh)"
        await update.message.reply_text(msg)
        context.user_data['waiting_for_quote'] = True
        
    elif action == "templates":
        await template(update, context)
        
    elif action == "language":
        await language_command(update, context)
        
    elif action == "help":
        await help_command(update, context)

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages (for quote input)"""
    user_id = update.effective_user.id
    text = update.message.text
    
    # Check if waiting for quote input
    if context.user_data.get('waiting_for_quote'):
        try:
            parts = text.split()
            if len(parts) == 2:
                monthly_kwh = float(parts[0])
                price_per_kwh = float(parts[1])
                
                if monthly_kwh <= 0 or price_per_kwh <= 0:
                    await update.message.reply_text(get_text(user_id, 'error_positive'))
                    return
                
                # Calculate quote
                await update.message.reply_text(get_text(user_id, 'calculating'))
                q = calculate_quote(monthly_kwh, price_per_kwh)
                await update.message.reply_text(format_quote(q, user_id))
                
                context.user_data['waiting_for_quote'] = False
                logger.info(f"Quote generated for user {user_id}: {monthly_kwh} kWh")
            else:
                await update.message.reply_text(get_text(user_id, 'error_params'))
        except ValueError:
            await update.message.reply_text(get_text(user_id, 'error_invalid'))
    
    # Check if waiting for price after template selection
    elif context.user_data.get('waiting_for_price'):
        try:
            price_per_kwh = float(text)
            if price_per_kwh <= 0:
                await update.message.reply_text(get_text(user_id, 'error_positive'))
                return
            
            template_type = context.user_data['waiting_for_price']
            templates = DB.get("templates", {})
            template_map = {
                "small": templates.get("small_home_kwh", 300),
                "medium": templates.get("medium_home_kwh", 600),
                "big": templates.get("big_home_kwh", 1200),
                "factory": templates.get("factory_kwh", 5000)
            }
            
            monthly_kwh = template_map[template_type]
            
            # Calculate quote
            await update.message.reply_text(get_text(user_id, 'calculating'))
            q = calculate_quote(monthly_kwh, price_per_kwh)
            await update.message.reply_text(format_quote(q, user_id))
            
            context.user_data['waiting_for_price'] = None
            logger.info(f"Template quote '{template_type}' for user {user_id}")
        except ValueError:
            await update.message.reply_text(get_text(user_id, 'error_invalid'))

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors caused by updates"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot"""
    if config.BOT_TOKEN == "<PUT_YOUR_TELEGRAM_BOT_TOKEN_HERE>":
        print("❌ ERROR: Please set your BOT_TOKEN in config.py")
        print("Get a token from @BotFather on Telegram")
        return
    
    # Create application
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("language", language_command))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("template", template))
    
    # Add callback query handlers
    app.add_handler(CallbackQueryHandler(language_callback, pattern='^lang_'))
    app.add_handler(CallbackQueryHandler(template_callback, pattern='^template_'))
    
    # Add message handlers for buttons and text input
    app.add_handler(MessageHandler(filters.Regex('^(💰|📋|🌐|❓)'), button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    
    # Add error handler
    app.add_error_handler(error_handler)
    
    # Start bot
    print("✅ SolarKH Bot started successfully!")
    print("Press Ctrl+C to stop the bot.")
    logger.info("Bot started")
    
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
