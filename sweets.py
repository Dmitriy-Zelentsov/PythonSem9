import telebot
from random import randint
bot = telebot.TeleBot("5628348400:AAE3ufSUyQEYiRJIv3DCMJBU2rrEyXkqTTk", parse_mode=None)
sweets = 2021

def bot_motion(message):
    global sweets
    a = randint(1,28)
    if a < sweets:
        sweets -= a
        bot.send_message(message.chat.id, f'Бот взял {a} конфет. Остаток: {sweets} конфет')
    else:
        bot.send_message(message.chat.id, f'Конец игры. Бот одержал победу!')
        sweets = 2021
        bot.send_message(message.chat.id, 'Для начала новой игры нажмите /start')

@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, """Добро пожаловать на игру! Условие игры: 
На столе лежит 2021 конфета.Играют игрок и бот делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.""")
        queue = randint(0,1)
        if queue == 0:
            bot.send_message(message.chat.id, f'Вы делаете ход первым.Остаток: {sweets} конфет')
        else:
            bot.send_message(message.chat.id, f'Первый ход делает Бот. Остаток: {sweets} конфет ')
            bot_motion(message)

@bot.message_handler(func=lambda message: True)
def player_motion(message):
    global sweets
    a = int(message.text)
    if a > 28:
       bot.send_message(message.chat.id, 'Число конфет должно быть меньше 29')
    else:
        if a < sweets:
            sweets -= a
            bot.send_message(message.chat.id, f'Остаток: {sweets} конфет')
            bot_motion(message)
        else:
            sweets = 0
            bot.send_message(message.chat.id, 'Поздравляем, Вы победили!!!')
            sweets = 2021
            bot.send_message(message.chat.id, 'Для начала новой игры нажмите /start')
bot.infinity_polling()