# Создание веб приложения

## Настройка проекта

### Установка виртуального окружения

```bash
cd <название-папки-проекта>
```

```bash
python -m venv .venv
```

```bash
./.venv/Scripts/activate
```

### Установка зависимостей

```bash
pip install flask Flask-SQLAlchemy psycopg2-binary
```

## Начало разработки

### Настройка приложения

```python
from flask import Flask
from flask_sqlalchemy import

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

Импортируем нужные нам модули и создаем экземпляр приложения. В конфигурации указываем путь к базе данных и отключаем отслеживание изменений.

### Создание моделей

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
```

Для создания таблицы создаем класс, наследуемый от `db.Model`. В классе создаем поля таблицы, указывая тип данных и ограничения. Поле `id` является первичным ключом, `username` и `email` уникальными, а `password` не может быть пустым.

### Создание таблиц

Для того, чтобы база данных появилась, необходимо выполнить следующие команды:

```bash
flask shell
```

```
db.create_all()
```

### Создание эндпоинтов

```python
@app.route('/')
def index():
    return 'index.html'
```

Для создания эндпоинтов используем декоратор `@app.route()`. В качестве аргумента указываем путь, по которому будет доступен эндпоинт. В качестве возвращаемого значения указываем шаблон, который будет отображаться по этому пути.

### Запуск приложения

```bash
flask run
```