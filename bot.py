# bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils.calculator import calculate_quote, DB
from utils.formatter import format_quote, format_templates
import config

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message when /start is issued"""
    welcome_message = """
☀️ **Welcome to SolarKH Bot!**

I can help you get quotes for solar panel installations.

**Commands:**
• `/quote <monthly_kwh> <price_per_kwh>` - Get a custom quote
  Example: `/quote 300 0.15`

• `/template <type> <price_per_kwh>` - Get quote from template
  Types: small, medium, big, factory
  Example: `/template medium 0.15`

• `/help` - Show this help message

Let's power your future with solar! 🌞
"""
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message"""
    help_text = """
🔆 **How to use SolarKH Bot:**

**Get a Custom Quote:**
`/quote <monthly_kwh> <price_per_kwh>`

Example: `/quote 450 0.20`
- monthly_kwh: Your average monthly electricity consumption
- price_per_kwh: Your current electricity rate

**Use Quick Templates:**
`/template <type> <price_per_kwh>`

Available templates:
• `small` - Small home (300 kWh/month)
• `medium` - Medium home (600 kWh/month)
• `big` - Big home (1200 kWh/month)
• `factory` - Factory (5000 kWh/month)

Example: `/template big 0.18`

Need assistance? Contact us! 📞
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /quote command"""
    try:
        if len(context.args) < 2:
            await update.message.reply_text(
                "❌ Please provide both parameters:\n"
                "`/quote <monthly_kwh> <price_per_kwh>`\n\n"
                "Example: `/quote 300 0.15`",
                parse_mode='Markdown'
            )
            return
        
        monthly_kwh = float(context.args[0])
        price_per_kwh = float(context.args[1])
        
        if monthly_kwh <= 0 or price_per_kwh <= 0:
            await update.message.reply_text("❌ Values must be positive numbers!")
            return
        
        # Calculate quote
        await update.message.reply_text("⏳ Calculating your solar quote...")
        q = calculate_quote(monthly_kwh, price_per_kwh)
        
        # Send formatted quote
        await update.message.reply_text(format_quote(q), parse_mode='Markdown')
        
        logger.info(f"Quote generated for user {update.effective_user.id}: {monthly_kwh} kWh")
        
    except ValueError:
        await update.message.reply_text(
            "❌ Invalid input. Please use numbers only.\n"
            "Example: `/quote 300 0.15`",
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error in quote command: {e}")
        await update.message.reply_text(
            "❌ An error occurred. Please try again or contact support."
        )

async def template(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /template command"""
    templates = DB.get("templates", {})
    template_map = {
        "small": templates.get("small_home_kwh", 300),
        "medium": templates.get("medium_home_kwh", 600),
        "big": templates.get("big_home_kwh", 1200),
        "factory": templates.get("factory_kwh", 5000)
    }
    
    try:
        if len(context.args) < 2:
            await update.message.reply_text(format_templates(), parse_mode='Markdown')
            return
        
        template_type = context.args[0].lower()
        price_per_kwh = float(context.args[1])
        
        if template_type not in template_map:
            await update.message.reply_text(
                f"❌ Unknown template: {template_type}\n\n" + format_templates(),
                parse_mode='Markdown'
            )
            return
        
        if price_per_kwh <= 0:
            await update.message.reply_text("❌ Price must be a positive number!")
            return
        
        monthly_kwh = template_map[template_type]
        
        # Calculate quote
        await update.message.reply_text(
            f"⏳ Calculating {template_type} home quote ({monthly_kwh} kWh/month)..."
        )
        q = calculate_quote(monthly_kwh, price_per_kwh)
        
        # Send formatted quote
        await update.message.reply_text(format_quote(q), parse_mode='Markdown')
        
        logger.info(f"Template quote '{template_type}' for user {update.effective_user.id}")
        
    except ValueError:
        await update.message.reply_text(
            "❌ Invalid price. Please use a number.\n"
            "Example: `/template medium 0.15`",
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"Error in template command: {e}")
        await update.message.reply_text(
            "❌ An error occurred. Please try again or contact support."
        )

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
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("template", template))
    
    # Add error handler
    app.add_error_handler(error_handler)
    
    # Start bot
    print("✅ SolarKH Bot started successfully!")
    print("Press Ctrl+C to stop the bot.")
    logger.info("Bot started")
    
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
