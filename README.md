# Telegram Joke Bot 🤖😂

## Описание проекта
Это забавный Telegram-бот, который отправляет случайные анекдоты в выбранном вами интервале времени. Бот предоставляет несколько развлекательных функций и гибкую настройку периодичности отправки шуток.

## Возможности
- 📨 Отправка случайных анекдотов с заданным интервалом
- 🕒 Настройка интервала отправки шуток (5, 10, 15 или 30 минут)
- 📅 Отправка шуток только в рабочее время (с 8:00 до 17:00)
- 🎲 Команды для получения случайных забавных сообщений
- 📋 Интерактивное меню для выбора интервала

## Команды бота
- `/start` - Начать работу с ботом
- `/help` - Получить справку о доступных командах
- `/funny` - Получить забавное выражение
- `/joke` - Получить случайный анекдот
- `/menu` - Открыть меню выбора времени отправки анекдотов

## Требования
- Python 3.7+
- Библиотеки:
  - telebot
  - APScheduler
  - functools

## Установка
1. Клонируйте репозиторий
```bash
git clone https://your-repo-url.git
cd telegram-joke-bot
```

2. Установите зависимости
```bash
pip install pyTelegramBotAPI APScheduler
```

3. Настройте конфигурацию
- Создайте файл `config/config.py`
- Добавьте в него токен вашего Telegram-бота:
```python
token = 'ВАШ_ТОКЕН_TELEGRAM_БОТА'
```

## Запуск
```bash
python main.py
```

## Особенности работы
- Бот отправляет анекдоты с выбранным интервалом
- Работает только в рабочее время (8:00-17:00)
- Можно легко изменить интервал через встроенное меню

## Лицензия
MIT License

## Вклад в проект
Приветствуются pull requests и suggestions для улучшения бота!
