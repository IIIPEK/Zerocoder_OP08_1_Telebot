import telebot
import datetime
import time
import threading

from config.config import token
from telebot import types
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])