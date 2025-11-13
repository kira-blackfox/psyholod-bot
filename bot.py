from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# --- Приветственное сообщение ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔹 Записаться на консультацию", callback_data="signup")],
        [InlineKeyboardButton("ℹ️ Подробнее о консультации", callback_data="info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет 🌿\nЯ — бот-помощник психолога Кати.\n"
        "Помогу записаться на консультацию или рассказать чуть подробнее.",
        reply_markup=reply_markup
    )

# --- Обработка нажатий кнопок ---
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "signup":
        await query.edit_message_text(
            "🕊 Чтобы записаться на консультацию, напишите Кате напрямую: @psyholod\n"
            "Или оставьте заявку по ссылке 👉 (сюда вставим ссылку позже)"
        )
    elif query.data == "info":
        await query.edit_message_text(
            "💬 Консультация длится 60 минут.\n"
            "Формат — онлайн (Zoom/Telegram) или офлайн (Минск).\n"
            "Подходит для индивидуальных и семейных запросов.\n"
            "Стоимость и запись уточняются у Кати."
        )

# --- Команда /help ---
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Напиши /start, чтобы начать 😉")

# --- Запуск приложения ---
def main():
    app = Application.builder().token("8541064492:AAGNlTCpppWfymS6TpthQS7sWYMqK4QYCEI").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("🤖 Бот запущен и ждёт сообщений...")
    app.run_polling()

if __name__ == "__main__":
    main()
