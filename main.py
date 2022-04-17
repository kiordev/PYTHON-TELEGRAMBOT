# SashaKiorBot Python File
# Creator: kiordev@gmail.com
# Date: 16 APRIL

import telebot
import configure
from telebot import types

# Telegram Bot Token
bot = telebot.TeleBot(configure.config['token'])


@bot.message_handler(commands=['get_info', 'info'])
def get_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, "Информация", reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('МОЙ ID')
        item_username = types.KeyboardButton('МОЙ НИК')
        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, "Нажми одну из кнопок", reply_markup=markup_reply)
    elif call.data == 'no':
        pass


@bot.message_handler(content_types=['text'])
def get_start(message):
    if message.text == "МОЙ ID":
        bot.send_message(message.chat.id, f"Твой ИД: {message.from_user.id}")
    elif message.text == "МОЙ НИК":
        bot.send_message(message.chat.id, f"Имя: {message.from_user.first_name} {message.from_user.last_name}")


bot.polling(none_stop=True, interval=0)
