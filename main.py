# -*- coding: utf-8 -*-
'''
import telebot

TOKEN = '1701470033:AAE39aOdBGS1bWggWE_Vq3amSobyhZtN0DQ'
from telebot import types
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "напишите команду меню")
    if message.text == "меню":
        bot.send_message(message.from_user.id, "Выбери однин из видов материалов")
        keyboard = types.InlineKeyboardMarkup()
        key_laminat = types.InlineKeyboardButton(text='Ламинат', callback_data='laminat')
        keyboard.add(key_laminat)
        key_linoleum = types.InlineKeyboardButton(text='Линолеум', callback_data='laminat')
        keyboard.add(key_linoleum)
        key_kvarts = types.InlineKeyboardButton(text='Кварц Винил', callback_data='laminat')
        keyboard.add(key_kvarts)
        key_doska = types.InlineKeyboardButton(text='Паркетная доска', callback_data='laminat')
        keyboard.add(key_doska)
        key_plintus = types.InlineKeyboardButton(text='Плинтус', callback_data='laminat')
        keyboard.add(key_plintus)
        key_acsesuar = types.InlineKeyboardButton(text='Аксессуары', callback_data='laminat')
        keyboard.add(key_acsesuar)

    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши меню")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")


@bot.message_handler(func=lambda call: True, content_types=['text'])
def get_text_messages(message1, call):
    bot.send_message1(message1.from_user.id, "напишите команду меню")
    if call.data == "laminat":
        bot.send_message(message1.from_user.id, "Выбери одну из коллекций ламината ")
        keyboard = types.InlineKeyboardMarkup()
        key_Floorwood = types.InlineKeyboardButton(text='Floorwood', callback_data='Floorwood')
        keyboard.add(key_Floorwood)
        key_Kromostar = types.InlineKeyboardButton(text='Kromostar', callback_data='Kromostar')
        keyboard.add(key_Kromostar)
        key_Family = types.InlineKeyboardButton(text='Family', callback_data='Family')
        keyboard.add(key_Family)
        key_Balterio = types.InlineKeyboardButton(text='Balterio', callback_data='Balterio')
        keyboard.add(key_Balterio)
        key_Kronopol = types.InlineKeyboardButton(text='Kronopol', callback_data='Kronopol')
        keyboard.add(key_Kronopol)
        key_Kronoflooring = types.InlineKeyboardButton(text='Kronoflooring', callback_data='Kronoflooring')
        keyboard.add(key_Kronoflooring)
        key_Faus = types.InlineKeyboardButton(text='Faus', callback_data='Faus')
        keyboard.add(key_Faus)
        key_Varioslis = types.InlineKeyboardButton(text='Varioslis', callback_data='Varioslis')
        keyboard.add(key_Varioslis)

    elif message1.text == "/start":
        bot.send_message(message1.from_user.id, "Напиши ")
    else:
        bot.send_message(message1.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "laminat":
        msg = "Олегу привет"
        bot.send_message(call.message.chat.id, msg)
bot.polling(none_stop=True, interval=0)
'''
# Подключаем модуль случайных чисел
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('1701470033:AAE39aOdBGS1bWggWE_Vq3amSobyhZtN0DQ')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "start":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_laminat = types.InlineKeyboardButton(text='Ламинат', callback_data='laminat')
        # И добавляем кнопку на экран
        keyboard.add(key_laminat)
        key_linolium = types.InlineKeyboardButton(text='Линолеум', callback_data='linolium')
        keyboard.add(key_linolium)
        key_kvarts = types.InlineKeyboardButton(text='Кварц Винил', callback_data='kvarts')
        keyboard.add(key_kvarts)
        key_doska = types.InlineKeyboardButton(text='Паркетная доска', callback_data='doska')
        keyboard.add(key_doska)
        key_plintus = types.InlineKeyboardButton(text='Плинтус', callback_data='plintus')
        keyboard.add(key_plintus)
        key_acsesuar = types.InlineKeyboardButton(text='Аксессуары', callback_data='acsesuar')
        keyboard.add(key_acsesuar)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "laminat":
        msg = 1
        bot.send_message(call.message.chat.id, msg)
    if call.data == "linolium":
        msg = 2
        bot.send_message(call.message.chat.id, msg)
    if call.data == "kvarts":
        msg = 3
        bot.send_message(call.message.chat.id, msg)
    if call.data == "doska":
        msg = 4
        bot.send_message(call.message.chat.id, msg)
    if call.data == "plintus":
        msg = 5
        bot.send_message(call.message.chat.id, msg)
    if call.data == "acsesuar":
        msg = 6
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)