__version__ = 'v0.0.1'

import os
import json

import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_key = os.getenv("CONTENT_CHAT_BOT")

bot = telebot.TeleBot(bot_key)


# def choise_model():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("gpt-3.5-turbo",
#                                     callback_data="{\"command\":\"model\",\"param\":\"gpt-3.5-turbo\"}"),
#                InlineKeyboardButton("gpt-3.5-turbo-16k",
#                                     callback_data="{\"command\":\"model\",\"param\":\"gpt-3.5-turbo-16k\"}"),
#                InlineKeyboardButton("gpt-4",
#                                     callback_data="{\"command\":\"model\",\"param\":\"gpt-4\"}"),
#                InlineKeyboardButton("gpt-4-0613",
#                                     callback_data="{\"command\":\"model\",\"param\":\"gpt-4-0613\"}"),
#                )
#     return markup


# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):

#     message = json.loads(call.data)
#     from_user = call.from_user.id
#     bot.answer_callback_query(call.id, show_alert=False)
#     if Session.sessions_list.get(from_user, False):
#         session = Session.sessions_list[from_user]
#     else:
#         session = Session(from_user)

#     if message['command'] == 'model':
#         session.model = message['param']
#         bot.send_message(chat_id=from_user,
#                          text='Moдель установлена')


# @bot.message_handler(commands=['model'])
# def model(mess):
#     bot.send_message(mess.chat.id, "Выберите модель из списка",
#                      reply_markup=choise_model())


# @bot.message_handler(commands=['info'])
# def info(mess):
#     from_user = mess.from_user.id

#     session_info = Session.sessions_list[from_user].__repr__(
#     ) if Session.sessions_list.get(from_user, False) else 'Сессия не создана'

#     bot.send_message(chat_id=from_user,
#                      text=f"Версия {__version__}\n\nДоступные команды:\n"
#                      "/clear - очистить сессию (остается только системный промт)\n"
#                      "/model - выбрать модель для сессии\n"
#                      "/context - выбрать режим работы с контекстом\n"
#                      "/system [текст] - поменять системный промт на [текст] (сессия будет очищена)\n"
#                      "/session - вывести информацию о сессии\n"
#                      f"/t, /т, /tokens - вывести количество токенов в сессии\n\n{session_info}")


# @bot.message_handler(commands=['sessions'])
# def sessions(mess):
#     from_user = mess.from_user.id
#     text = '\n'.join([ses.__repr__()
#                      for ses in Session.sessions_list.values()])
#     bot.send_message(chat_id=from_user,
#                      text=text if len(text) > 0 else 'Нет активных сессий')


# @bot.message_handler(commands=['session'])
# def sessions(mess):
#     from_user = mess.from_user.id
#     text = ""
#     if Session.sessions_list.get(from_user, False):
#         text = Session.sessions_list[from_user].__repr__()

#     bot.send_message(chat_id=from_user,
#                      text=text if len(text) > 0 else 'Нет активных сессий')

@bot.message_handler(func=lambda mess: True)
def message_handler(mess):

    message = mess.text
    from_user = mess.from_user.id

# Может получать и картинки/файлы тоже. Должен их преобразовать в заметки
# Может формировать сложную заметку. Тогда высылается команда на начало формирования заметки, потом все что идет добавляется в заметку. Когда приходит команда на завершение, все сохраняется в файл
# На медиа контент добавляются ссылки в формате obsidian

# По команде выводит статус репо контента
# По команде выводит настройки периодичности автоматического обновления (1 мин, 15 мин, 1 час, 6 час, 12 часов, 1 день)
# По команде инициирует ручной пуш в репо контента


bot.infinity_polling()
