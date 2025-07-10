import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("BOT_TOKEN")

# متن اطلاعات توسعه‌دهنده
ABOUT_TEXT = """
🧑‍💻 *طراح و برنامه‌نویس*: شیرازی
📞 *تماس*: 09031701895
🌐 *سورس ربات*: 
[GitHub Repository](https://github.com/Shirazi-workplace/Botsh1/tree/main)

_ طراحی و مدرن سازی انواع سایت و اپلیکیشن _
"""

async def start(update: Update, context):
    """دستور شروع"""
    user = update.effective_user
    await update.message.reply_markdown(
        f"✨ سلام {user.first_name}!\n"
        "به ربات خوش آمدید.\n\n"
        "برای اطلاعات بیشتر دستور /about را وارد کنید"
    )

async def about(update: Update, context):
    """نمایش اطلاعات توسعه‌دهنده"""
    user = update.effective_user
    await update.message.reply_markdown(
        f"{ABOUT_TEXT}\n\n"
        f"🆔 *آی‌دی شما*: `{user.id}`"
    )

async def echo(update: Update, context):
    """پاسخ به پیام‌های متنی"""
    user = update.effective_user
    await update.message.reply_text(
        f"پیام شما دریافت شد: {update.message.text}\n"
        f"🆔 آی‌دی شما: {user.id}\n"
        "برای اطلاعات بیشتر /about را امتحان کنید"
    )

def main():
    if not TOKEN:
        logger.error("❌ توکن ربات تنظیم نشده است!")
        return

    app = Application.builder().token(TOKEN).build()
    
    # ثبت دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    
    # ثبت هندلر پیام
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    logger.info("✅ ربات در حال اجرا است...")
    app.run_polling()

if __name__ == '__main__':
    main()
