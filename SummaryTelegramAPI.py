# TelegramBotAPI Summary File
# Creator: kiordev@gmail.com
# Date: 16 APRIL

# TelegramBot API for Python "https://pypi.org/project/pyTelegramBotAPI/#methods"

# === Bot Globals ===
# bot.polling(none_stop=True)  - для постоянной работы бота, писать в конец кода

# === Message Methods ===
# bot.send_message(message.chat.id, *сообщение*, parse_mode='html') - метод для вывода сообщения после команды
# bot.send_message(message.chat.id, message, parse_mode='html') - вывод всех параметров для обращения

# ...Фотография...
# photo = open('Блокнот.png', 'rb') - открытие файла в проекте перед работой (rb - формат)
# bot.send_photo(message.chat.id, photo) - отправка этого файла

# ...Декораторы...
# @bot.message_handler(commands=['*команда*']) - декоратор перед методом, который работает с командой
# @bot.message_handler (ничего) - просто декоратор для обработки текста пользователя

# === Button work ===
# ...Кнопки внутри диалога...
# markup = types.InlineKeyboardMarkup() | *название_переменной* = Инициализация кнопки (диалогой)
# markup.add(types.InlineKeyboardButton("Сайт", url="https://pypi.org/project/pyTelegramBotAPI/#methods"))
# ^создание кнопки как таковой(*Что на ней написано*, *че она делает*)
# ...Кнопки за диалогом

# === Work With User ===
# message.from_user.first_name - обращение к имени
# message.from_user.first_name - обращение к фамилии
# список параметров можно найти через bot.send_message(message.chat.id, message, parse_mode='html')
# @bot.message_handler(content_types=["photo"]) - декоратор для работы с файлами приёма пользователем

