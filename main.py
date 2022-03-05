import telebot
import random
from telebot import types

# Загружаем список неправильных глаголов
f = open('data/irregular_verb.txt', 'r', encoding='UTF-8')
irregVerb = f.read().split('\n')
f.close()

# Загружаем список правильных глаголов
f = open('data/regular_verb.txt', 'r', encoding='UTF-8')
regVerb = f.read().split('\n')
f.close()

bot = telebot.TeleBot('5205297356:AAEanCnLca5Z0_B28vHZg3eegifXpM4vZ8c')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Правильный глагол")
    item2 = types.KeyboardButton("Неправильный глагол")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми и выучи следующий рандомный глагол',  reply_markup=markup)

# Получение сообщений от пользователя
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если пользователь прислал 1, выдаем правильный глагол
    if message.text.strip() == 'Правильный глагол':
        answer = random.choice(irregVerb)
    # Если пользователь прислал 2, выдаем неправильный глагол
    elif message.text.strip() == 'Неправильный глагол':
        answer = random.choice(regVerb)
    else:
        answer = 'Выбери глагол !'
    # Отсылаем пользователю сообщение в чат
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)