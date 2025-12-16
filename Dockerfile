FROM python:3.11-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Статическая папка
RUN mkdir -p /app/static

# Порт приложения (документация)
EXPOSE 8001

# CMD оставлен для документации, реально используется command из compose
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "myproject.wsgi:application"]
