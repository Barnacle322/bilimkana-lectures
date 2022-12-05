# Телеграм бот с помощью питона

## Документация

[Главная страница](https://python-telegram-bot.org/)

[Доки](https://docs.python-telegram-bot.org/en/v20.0a6/)

[Примеры](https://docs.python-telegram-bot.org/en/v20.0a6/examples.html)

[Вики](https://github.com/python-telegram-bot/python-telegram-bot/wiki)

## Установка

```bash
pip install python-telegram-bot --pre
```

Если не работает установка откройте Windows Powershell от имени администратора
```powershell
set-executionpolicy remotesigned
```

Если предыдущее не сработало
```powershell
Set-ExecutionPolicy Unrestricted -Force
```

## Получение токена

[Получить токен можно тут](https://t.me/BotFather)

1. Отправляете команду `/newbot`
1. Даете название боту
1. Даете юзернейм боту с окончанием `bot` (например `@my_bot` или `@myBot`)
1. Получаете токен

## Код

После того как вы установили библиотеку и получили токен, создайте файл `main.py` и вставьте в него следующий код:

```python
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "TOKEN"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет, вы запустили бота 10IT класса")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_rext(update.message.text)


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()


if __name__ == "__main__":
    main()
```

Код для вывода информации в консолоь
```python
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
```

Импортируем нужные классы и определяем токен

```python
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "TOKEN"
```

Основная часть
```python
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()


if __name__ == "__main__":
    main()
```

Логика обработки сообщений
```python
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет, вы запустили бота 10IT класса")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_rext(update.message.text)
```
