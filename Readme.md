Запуск и использование API
===========================

Установка зависимостей
----------------------

Перед запуском сервиса убедитесь, что у вас установлены следующие зависимости:

- Python 3.9 или выше
- PostgreSQL

Установка переменных окружения
------------------------------

1. Создайте файл с именем `.env` в корневой директории проекта.
2. Укажите необходимые значения переменных окружения в файле `.env`. Например:

```plaintext
DB_NAME=friends_db
DB_USER=friends_admin
DB_PASSWORD=friends_admin
DB_HOST=db
DB_PORT=5432
```
Установка зависимостей Python
Выполните следующую команду для установки зависимостей Python:

```
pip install -r requirements.txt
```
Выполнение миграций и сборка статических файлов
Выполните следующие команды для выполнения миграций базы данных:

```
python manage.py migrate
```

Запуск сервера Django
Выполните следующую команду для запуска сервера Django:

```
python manage.py runserver
```
API будет доступно по адресу http://localhost:8000/.

Создание контейнеров
Для создания контейнеров используйте два Docker-файла, описанных ниже.

Dockerfile для Django-сервиса

```
Copy code
# Используем базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Выполняем миграции и собираем статические файлы
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Открываем порт, на котором будет работать сервер Django
EXPOSE 8000

# Запускаем сервер Django внутри контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
Dockerfile для PostgreSQL
Dockerfile
Copy code
```
# Используйте базовый образ PostgreSQL
```
FROM postgres:latest

# Определите переменные среды для настройки базы данных
ENV POSTGRES_DB friends_db
ENV POSTGRES_USER friends_admin
ENV POSTGRES_PASSWORD friends_admin

# Копирование скриптов инициализации базы данных в контейнер
COPY ./init.sql /docker-entrypoint-initdb.d/
```
