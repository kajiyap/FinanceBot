import telebot
import ia

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

telegramKey = os.getenv("TELEGRAM_API_KEY")

bot = telebot.TeleBot(telegramKey, parse_mode='markdown')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, ia.question(message.text))

bot.infinity_polling()