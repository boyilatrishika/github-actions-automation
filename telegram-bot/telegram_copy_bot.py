#!/usr/bin/env python3

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get environment variables
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID environment variables")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '🤖 Telegram Copy-Paste Bot\n\n'
        'Available commands:\n'
        '/copy [message] - Forward WhatsApp message\n'
        '/help - Show help\n\n'
        'Example: /copy Check this out!'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '📋 How to use:\n\n'
        '1. Copy message from WhatsApp group\n'
        '2. Send /copy followed by message\n\n'
        'Examples:\n'
        '/copy Great news!\n'
        '/copy Meeting at 3 PM\n'
    )

async def copy_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text(
            'Please provide a message.\n'
            'Usage: /copy [message]'
        )
        return
    
    message_text = ' '.join(context.args)
    sender_name = update.message.from_user.first_name or "Unknown"
    
    try:
        formatted_message = (
            f"📱 From WhatsApp Group\n"
            f"👤 Shared by: {sender_name}\n"
            f"⏰ Time: {update.message.date.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"{message_text}"
        )
        
        await context.bot.send_message(
            chat_id=CHAT_ID,
            text=formatted_message
        )
        
        await update.message.reply_text(
            'Message forwarded to Telegram!'
        )
        
        logger.info(f"Message forwarded: {message_text[:100]}")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text(
            f'Error: {str(e)}'
        )

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('copy', copy_message))
    
    logger.info("Starting Telegram Copy-Paste Bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
