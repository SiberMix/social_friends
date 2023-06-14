# Используйте базовый образ PostgreSQL
FROM postgres:latest

# Определите переменные среды для настройки базы данных
ENV POSTGRES_DB friends_db
ENV POSTGRES_USER friends_admin
ENV POSTGRES_PASSWORD friends_admin

# Копирование скриптов инициализации базы данных в контейнер
COPY ./init.sql /docker-entrypoint-initdb.d/
