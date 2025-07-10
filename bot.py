import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("BOT_TOKEN")

# طراحی زیبا با استایل شیشه‌ای (Glassmorphism)
ABOUT_TEXT = """
<b>✨ طراحی حرفه‌ای با استایل شیشه‌ای ✨</b>

<code>┌──────────────────────────────┐
│   🧑‍💻 طراح و برنامه‌نویس:     │
│      شیرازی                   │
├──────────────────────────────┤
│   📞 تماس:                    │
│      09031701895             │
├──────────────────────────────┤
│   🌐 سورس ربات:               │
│      <a href="https://github.com/Shirazi-workplace/Botsh1/tree/main">GitHub Repository</a>  │
└──────────────────────────────┘</code>

<i>این اولین ربات تلگرام من است ☺️</i>
"""

async def start(update: Update, context):
    """دستور شروع با طراحی زیبا"""
    user = update.effective_user
    welcome_msg = f"<b>✨ سلام {user.first_name}!\nبه ربات خوش آمدید.</b>"
    
    # ارسال پیام با طراحی حرفه‌ای
    await update.message.reply_html(
        f"{welcome_msg}\n\nبرای اطلاعات بیشتر دستور /about را وارد کنید",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("درباره من ℹ️", callback_data="about")]
        ])
    )

async def about(update: Update, context):
    """نمایش اطلاعات تماس با طراحی شیشه‌ای"""
    await update.message.reply_html(
        ABOUT_TEXT,
        disable_web_page_preview=True
    )

async def button_handler(update: Update, context):
    """مدیریت کلیک روی دکمه‌ها"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "about":
        await query.edit_message_text(
            ABOUT_TEXT,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

async def echo(update: Update, context):
    """پاسخ به پیام‌های متنی"""
    await update.message.reply_text(
        f"پیام شما دریافت شد: {update.message.text}\n"
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
    
    # ثبت هندلرهای پیام
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    logger.info("✅ ربات در حال اجرا است...")
    app.run_polling()

if __name__ == '__main__':
    main()
