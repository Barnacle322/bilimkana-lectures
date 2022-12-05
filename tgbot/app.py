import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "5949614522:AAFK9loD14yuHn7SFBGdXqaIIJ_BjaWobNc"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет, вы запустили бота 10IT класса")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parsed = update.message.text.removeprefix("/help")
    print(context.user_data)
    if parsed:
        await update.message.reply_text(parsed)
    else:
        await update.message.reply_text("Вы не ввели ничего")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    get_context = context.user_data.get("something", "empty")
    context.user_data["something"] = update.message.text
    await update.message.reply_text(get_context)


async def me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update)


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("me", me))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()


if __name__ == "__main__":
    main()
