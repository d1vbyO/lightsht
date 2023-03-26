import telebot
from telebot import types
import random

API_TOKEN = 'TOKEN HERE'  # - бот тестовый
bot = telebot.TeleBot(API_TOKEN)

symbols = '1234567890abcdefghijklnopqrstuvwxyz'
id_length = 6

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    nextbnt = types.KeyboardButton('===>ON<===')
    markup.add(nextbnt)
    bot.send_message(message.chat.id,'Бот для просмотра картнок с lightshot', reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(content_types=['text'])
def send_pic(message):
    if message.text == '===>ON<===':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        nextbnt = types.KeyboardButton('===>ON<===')
        markup.add(nextbnt)
        image_id = ''
        for item in range(id_length):
            image_id += random.choice(symbols)
        bot.send_message(message.chat.id, 'prnt.sc/' + image_id, reply_markup=markup, parse_mode="Markdown")

bot.polling(True)
