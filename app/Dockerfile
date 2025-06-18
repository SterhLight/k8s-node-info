# Используем базовый образ с Python
FROM python:3.9-slim

# Добавляем лицензию в образ
COPY LICENSE /LICENSE

# Добавляем метку с лицензией
LABEL license="GPL-3.0-or-later" \
      maintainer="krasava al.popytaev@yandex.ru"

# Устанавливаем зависимости
RUN pip install flask

# Копируем код приложения
COPY app.py /app.py

# Указываем переменную окружения, которая будет использоваться в приложении
ENV NODE_NAME=''

# Указываем рабочую директорию
WORKDIR /

# Запускаем приложение
CMD ["python", "app.py"]