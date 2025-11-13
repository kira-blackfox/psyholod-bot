from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# --- Главное меню ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🕊 Записаться на консультацию", callback_data="signup")],
        [InlineKeyboardButton("💭 Часто задаваемые вопросы", callback_data="faq_menu")],
        [InlineKeyboardButton("🌸 Подробнее о консультации", callback_data="info")],
        [InlineKeyboardButton("📞 Контакты / Соцсети", callback_data="contacts")],
        [InlineKeyboardButton("💬 Отзывы клиентов", callback_data="reviews")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет 🌿\nЯ — бот-помощник психолога Кати.\n"
        "Помогу записаться на консультацию, рассказать подробнее и ответить на частые вопросы 💬",
        reply_markup=reply_markup
    )


# --- Обработка кнопок ---
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "signup":
        await query.edit_message_text(
            "🕊 Чтобы записаться на консультацию, напишите Кате напрямую: @psyholod\n"
            "Или оставьте заявку по ссылке 👉 (сюда можно будет добавить позже)"
        )

    elif query.data == "info":
        await query.edit_message_text(
            "🌸 Консультация длится 60 минут.\n"
            "Формат — онлайн (Zoom/Telegram) или офлайн (Минск).\n"
            "Подходит для индивидуальных и семейных запросов.\n"
            "Стоимость и запись уточняются у Кати 💬"
        )

    elif query.data == "faq_menu":
        await show_faq_menu(query)

    elif query.data.startswith("faq_"):
        await show_faq_answer(query, query.data)

    elif query.data == "contacts":
        await query.edit_message_text(
            "📞 Контакты и соцсети Кати:\n\n"
            "Telegram: @psyholod\n"
            "Instagram: [@psyholod.by](https://www.instagram.com/psyholod.by)\n"
            "E-mail: psyholod.by@gmail.com\n\n"
            "🕊 Можно написать в любой из этих каналов 💫",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_menu")]
            ])
        )

    elif query.data == "reviews":
        await query.edit_message_text(
            "💬 Несколько отзывов клиентов:\n\n"
            "🌿 *«Очень тёплая и чуткая атмосфера, я почувствовала себя в безопасности.»*\n\n"
            "🌷 *«Кате удалось помочь мне понять свои чувства и разобраться в себе. Спасибо!»*\n\n"
            "🕊 *«После каждой встречи я чувствую лёгкость и ясность. Настоящая поддержка.»*\n\n"
            "✨ (Отзывы анонимные, приведены с согласия клиентов)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_menu")]
            ])
        )

    elif query.data == "back_to_menu":
        await start(update, context)


# --- Меню FAQ ---
async def show_faq_menu(query):
    keyboard = [
        [InlineKeyboardButton("🪷 Вы проводите консультации и лично и онлайн?", callback_data="faq_1")],
        [InlineKeyboardButton("🌼 Как проходит первая встреча?", callback_data="faq_2")],
        [InlineKeyboardButton("💰 Сколько стоит первая встреча?", callback_data="faq_3")],
        [InlineKeyboardButton("🕯 Как проходят последующие встречи и сколько стоят?", callback_data="faq_4")],
        [InlineKeyboardButton("🌸 Надо ли готовиться к первой встрече?", callback_data="faq_5")],
        [InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "💭 Часто задаваемые вопросы — выберите, чтобы узнать подробнее:",
        reply_markup=reply_markup
    )


# --- Ответы на вопросы ---
async def show_faq_answer(query, data):
    answers = {
        "faq_1": "🌿 Да, консультации проходят онлайн из любой точки мира 🌍\n"
                 "и лично по адресу: Минск, пр.Машерова 11-401.",

        "faq_2": "🕊 Первая встреча длится два часа. Она диагностическая.\n"
                 "Мы знакомимся, я задаю вопросы, чтобы составить карту вашей личности и семейной системы.\n"
                 "Вы делитесь своей ситуацией, а я даю обратную связь и план работы.\n"
                 "Главное — создать доверительное и безопасное пространство 🌷",

        "faq_3": "💰 Стоимость первой (диагностической) встречи — 250 белорусских рублей.",

        "faq_4": "🌸 После диагностики встречи длятся по часу, обычно раз в неделю.\n"
                 "Стоимость часовой встречи — 130 белорусских рублей.\n"
                 "Периодичность и формат можно обсудить индивидуально 🌿",

        "faq_5": "🕯 Нет, специально готовиться не нужно. Главное — просто прийти.\n"
                 "Не волнуйтесь, если перескакиваете с темы на тему — я помогу направить разговор.\n"
                 "Иногда между встречами даю домашние задания — их лучше выполнять 💫"
    }

    keyboard = [[InlineKeyboardButton("🔙 Назад к вопросам", callback_data="faq_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(answers[data], reply_markup=reply_markup)


# --- Команда /help ---
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌸 Напиши /start, чтобы начать общение со мной 🌿")


# --- Запуск приложения ---
def main():
    app = Application.builder().token("ВАШ_ТОКЕН_БОТА").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("🤖 Бот запущен и ждёт сообщений...")
    app.run_polling()


if __name__ == "__main__":
    main()


