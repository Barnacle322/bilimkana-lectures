import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = "TOKEN"


async def quadratic(update: Update, context: ContextTypes) -> None:
    # Проверить сообщение ли это
    if not update.message:
        return
    # Это нужно пототму что в update.message.text лежит команда и аргументы типа
    # {text: "/quadratic 1 2 3"}
    text = update.message.text.replace("/quadratic", "").split()
    a, b, c = text
    d = int(b) ** 2 - 4 * int(a) * int(c)

    if d < 0:
        await update.message.reply_text("Дискриминант меньше нуля, корней нет")
    elif d == 0:
        x = -int(b) / (2 * int(a))
        await update.message.reply_text(
            f"Дискриминант равен нулю, корень один\n\nD = {d}\nx = {x}"
        )
    else:
        x1 = (-int(b) + d**0.5) / (2 * int(a))
        x2 = (-int(b) - d**0.5) / (2 * int(a))
        await update.message.reply_text(
            f"Дискриминант больше нуля, корней два\n\nD = {d}\nx1 = {x1}\nx2 = {x2}"
        )


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("quadratic", quadratic))
    application.run_polling()


if __name__ == "__main__":
    main()
