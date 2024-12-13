from random import choice
from functools import partial

from apscheduler.schedulers.background import BackgroundScheduler
import telebot
from telebot import types, TeleBot
from telebot.types import BotCommandScopeDefault,MenuButtonDefault

from config.config import token
from extra.messages import funny_mess, jokes, smiles, answers

def gen_cron_str(interval: int):
    minute = [str(i) for i in range(0, 60, interval)]
    return ",".join(minute)


# создаем экземпляр бота
bot: TeleBot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет, я чат-бот, который будет тебе изредка😏 писать!\n😃 Пока каждые 15 минут.")
    # Очищаем список задач
    scheduler.remove_all_jobs()
    send_joke_with_chat_id = partial(send_joke, message.chat.id)
    # создаем расписание задач на каждые 15 минут по умолчанию в рабочее время
    scheduler.add_job(send_joke_with_chat_id, 'cron', minute=gen_cron_str(15), hour='8-17', id='task_working_hours')
    bot.send_message(message.chat.id, f"Выбран интервал 15 минут.")
    help_command(message)


@bot.message_handler(commands=['funny'])
def funny_message(message):
    funny = choice(funny_mess)
    bot.send_message(message.chat.id,"😏 Лови! 😏\n"+funny)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Вот список доступных команд:\n"+
                     "\n".join([f"/{command.command} - {command.description}"
                                for command in bot.get_my_commands()]
                               )
                     )
@bot.message_handler(commands=['joke'])
def funny_message(message):
    send_joke(message.chat.id)

def send_joke(chat_id):
    joke_mess = choice(jokes)
    bot.send_message(chat_id,joke_mess)

@bot.message_handler(commands=['menu'])
def show_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("5")
    button2 = types.KeyboardButton("10")
    button3 = types.KeyboardButton("15")
    button4 = types.KeyboardButton("30")
    button_remove = types.KeyboardButton("Убрать меню")
    keyboard.add(button1, button2, button3, button4, button_remove)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text in ["5", "10","15", "30"]:
        minutes = int(message.text)
        bot.send_message(message.chat.id, f"Вы выбрали интервал {minutes} минут.\nМеню скрыто.", reply_markup=types.ReplyKeyboardRemove())
        scheduler.remove_all_jobs()
        send_joke_with_chat_id = partial(send_joke, message.chat.id)
        scheduler.add_job(send_joke_with_chat_id, 'cron', minute=gen_cron_str(minutes), hour='8-17', id='task_working_hours')
        bot.send_message(message.chat.id, "Меню скрыто.", reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "Убрать меню":
        # Убираем клавиатуру
        bot.send_message(message.chat.id, "Меню скрыто.", reply_markup=types.ReplyKeyboardRemove())
    else:
        answer = [choice(smiles), choice(answers),choice(smiles),]

        bot.send_message(message.chat.id, f"{answer[0]} {answer[1]} {answer[2]}")


# Очищаем список команд у всех
bot.delete_my_commands(scope=BotCommandScopeDefault())

# Устанавливаем новый список команд
commands = [
    types.BotCommand("start", "Начать работу с ботом"),
    types.BotCommand("help", "Помощь по боту"),
    types.BotCommand("funny", "Забавное выражение"),
    types.BotCommand("joke", "Анекдот"),
    types.BotCommand("menu", "Открыть меню выбора времени выдачи анекдотов")
]
bot.set_my_commands(commands)

# Устанавливаем кнопку меню для всех чатов
menu_button = types.MenuButtonCommands()  # Кнопка для вызова команд
bot.set_chat_menu_button( menu_button=menu_button)  # Для всех чатов

# создаем экземпляр планировщика
scheduler = BackgroundScheduler()
# Запускаем планировщик
scheduler.start()

bot.polling(none_stop=True)
