import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# تنظیمات لاگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# تغییر مهم: TOKEN به BOT_TOKEN
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context):
    await update.message.reply_text('👋 سلام! من از GitHub اجرا میشم!')

async def echo(update: Update, context):
    await update.message.reply_text(f'شما گفتید: {update.message.text}')

def main():
    if not TOKEN:
        logger.error("❌ توکن ربات تنظیم نشده است!")
        return
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == '__main__':
    main()
