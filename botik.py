from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я эхо-бот. Отправь мне сообщение, и я повторю его.")

# Эхо-обработка сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main():
    # Создание приложения с токеном бота
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # Обработчики команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запуск бота
    print("Бот запущен!")
    application.run_polling()

if name == "main":
    main()