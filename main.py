import re
import requests
from telebot import TeleBot, types
bot = TeleBot('1002398401:AAGBu-ZrLis1wjTKG6RMfoEMqcpAI53cvhI')



markup = types.ReplyKeyboardMarkup(row_width=2)

@bot.message_handler(commands=['all'])
def get_definition(message):
    req = requests.get(
        'http://api.urbandictionary.com/v0/define?term={}")'.format(message.text))

    text = ""

    for _ in req.json().get('list'):
        text += _.get('definition')

    result = re.finditer(r'\[\w+\]', text)

    bot.send_message(message.chat.id, text)

    definitions = []

    for _ in result:
        definitions.append(_.group()[1:-1])

    for word in definitions[:10]:
        word = types.KeyboardButton(word)
        markup.add(word)

    bot.send_message(message.chat.id, "Choose a word:",
                     reply_markup=markup)

    req = requests.get(
        'http://api.urbandictionary.com/v0/define?term={}")'.format(message.text))

    text = ""

    for _ in req.json().get('list'):
        text += _.get('definition')

    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.polling()






