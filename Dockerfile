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
