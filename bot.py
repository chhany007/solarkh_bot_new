# bot.py
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message when /start is issued"""
    user_id = update.effective_user.id
    welcome_message = get_text(user_id, 'welcome')
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message"""
    user_id = update.effective_user.id
    help_text = get_text(user_id, 'help')
    await update.message.reply_text(help_text, parse_mode='Markdown')

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
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle language selection callback"""
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    lang = query.data.split('_')[1]
    
    set_language(user_id, lang)
    
    await query.edit_message_text(
        text=get_text(user_id, 'language_changed'),
        parse_mode='Markdown'
    )

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /quote command"""
    user_id = update.effective_user.id
    
    try:
        if len(context.args) < 2:
            await update.message.reply_text(
                get_text(user_id, 'error_params'),
                parse_mode='Markdown'
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
        await update.message.reply_text(format_quote(q, user_id), parse_mode='Markdown')
        
        logger.info(f"Quote generated for user {user_id}: {monthly_kwh} kWh")
        
    except ValueError:
        await update.message.reply_text(
            get_text(user_id, 'error_invalid'),
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error in quote command: {e}")
        await update.message.reply_text(get_text(user_id, 'error_general'))

async def template(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /template command"""
    user_id = update.effective_user.id
    templates = DB.get("templates", {})
    
    # Get translated template names
    template_map_en = {
        "small": templates.get("small_home_kwh", 300),
        "medium": templates.get("medium_home_kwh", 600),
        "big": templates.get("big_home_kwh", 1200),
        "factory": templates.get("factory_kwh", 5000)
    }
    
    # Support Khmer template names
    template_map_kh = {
        "តូច": templates.get("small_home_kwh", 300),
        "មធ្យម": templates.get("medium_home_kwh", 600),
        "ធំ": templates.get("big_home_kwh", 1200),
        "រោងចក្រ": templates.get("factory_kwh", 5000)
    }
    
    template_map = {**template_map_en, **template_map_kh}
    
    try:
        if len(context.args) < 2:
            await update.message.reply_text(format_templates(user_id), parse_mode='Markdown')
            return
        
        template_type = context.args[0].lower()
        price_per_kwh = float(context.args[1])
        
        if template_type not in template_map:
            await update.message.reply_text(
                get_text(user_id, 'template_unknown').format(template_type) + format_templates(user_id),
                parse_mode='Markdown'
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
        await update.message.reply_text(format_quote(q, user_id), parse_mode='Markdown')
        
        logger.info(f"Template quote '{template_type}' for user {user_id}")
        
    except ValueError:
        await update.message.reply_text(
            get_text(user_id, 'template_error'),
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error in template command: {e}")
        await update.message.reply_text(get_text(user_id, 'error_general'))

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
    
    # Add callback query handler for language selection
    app.add_handler(CallbackQueryHandler(language_callback, pattern='^lang_'))
    
    # Add error handler
    app.add_error_handler(error_handler)
    
    # Start bot
    print("✅ SolarKH Bot started successfully!")
    print("Press Ctrl+C to stop the bot.")
    logger.info("Bot started")
    
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
