# SashaKiorBot Python File
# Creator: kiordev@gmail.com
# Date: 16 APRIL

import telebot
from telebot import types # Для работы с кнопками

# Telegram Bot Token
bot = telebot.TeleBot('5209918140:AAFLAgz1TIcV5R8EpYN5c-gm-dtYg1X9Q7M')


# Telegram Start Message
@bot.message_handler(commands=['start'])  # Декоратор, для отслеживания вводимых команд
def start(message):
    meet_message = f"Привет, <b>{message.from_user.first_name} </b> <u>{message.from_user.last_name}</u>"


# Telegram Default Speech Message
# @bot.message_handler()
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Твой ИД: {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('Блокнот.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "Ты ввел какую-то хуйню", parse_mode='html')


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Крутое фото, лошара")

# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Сайт", url="https://pypi.org/project/pyTelegramBotAPI/#methods"))
#     bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("Сайт")
    start = types.KeyboardButton("Start")

    markup.add(website, start)
    bot.send_message(message.chat.id, "Какие-то кнопки", reply_markup=markup)



# For Regular Bot Work
bot.polling(none_stop=True)
