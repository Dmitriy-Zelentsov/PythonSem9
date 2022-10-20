import telebot

bot = telebot.TeleBot("5412173340:AAE0vAnlYEZjJQ30tggOSRK6sckDhjj-loI")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, new_echo(message.text))

def new_echo(message):
    a = 'абв'
    message = message.replace(a, '')
    return message

bot.infinity_polling()