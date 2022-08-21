import requests
import telebot
from telebot import types

bot = telebot.TeleBot('5707469669:AAHyYeODg_9M3DJJQJWLZgHhPOBoTSXa3DA')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("💻 ПЛАН РАБОТЫ")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! В данном боте мы рассмотрим пошаговый план работы с БИЗНЕС-АККАУНТОМ в INSTAGRAM".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привет. Я рад что тебе интересна данная тема 😉!")
    elif (message.text == "💻 ПЛАН РАБОТЫ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton("I шаг")
        btn2 = types.KeyboardButton("II шаг")
        btn3 = types.KeyboardButton("III шаг")
        btn4 = types.KeyboardButton("IV шаг")
        btn5 = types.KeyboardButton("Воронка продаж")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выбери какой этап работы вам предстоит просмотреть", reply_markup=markup)

    elif message.text == 'I шаг':
        photo1 = open('11.JPG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, f"1 шаг. \n <b>Внешняя упаковка.</b> \n 🔗 Люди не хотят писать, делать лишние действия."
                                               "\n 🔗 Дайте им заранее ответы на вопросы, которые могут у них возникнуть.", parse_mode="html")

    elif message.text == "II шаг":
        photo1 = open('22.JPG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, f"2 шаг. \n <b>Внутреннее наполнение.</b> \n ✔️Смысловое наполнение в постах. \n ✔️Взаимодействе через истории (сторителлинг). \n ✔️Взаимодествие в комментариях.", parse_mode="html")

    elif (message.text == "III шаг"):
        photo2 = open('3.JPG', 'rb')
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, f"3 шаг. \n <b>ПРОДВИЖЕНИЕ</b>. \n Что можно делать? \n ♦️ Покупать рекламу у лидеров мнений. \n ♦️ Настраивать таргетированную рекламу.", parse_mode="html")


    elif (message.text == "IV шаг"):
        photo3 = open('4.jpg', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, f"4 шаг.  <b>МОНЕТИЗАЦИЯ</b>. \n  🎈 Успешная монетизация профиля будет доступна только тогда, когда все прошлые 3 этапа были соблюдены. \n  Каждая продажа проходит через доверие аудитории к вам. Следовательно,необходимо на каждом этапе затрагивать боль. \n 🎈 Например, в студии лазерной эпиляции  безопасное оборудование. Так мы закрываем боль о том, что это не больно", parse_mode="html")

    elif (message.text == "Воронка продаж"):
        photo4 = open('5.png', 'rb')
        bot.send_photo(message.chat.id, photo4)
        bot.send_message(message.chat.id, f" <b>Воронка продаж</b> \n 📎 Воронка продаж в бизнесе-аккаунте может строится через сторис,посты,встречи,консультации,чеклисты,гайды. \n 📎 Изучите ваши предлагаемые услуги или товары. подумайте, кому они могли бы бытьинтересны. \n 📎 После определения кому это интересно, изучите дизайн и подачу: позиционирование должно отражать интересы вашей целевой аудитории.", parse_mode="html")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("💻 ПЛАН РАБОТЫ")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Я не понимаю вашу комманду...")

bot.polling(none_stop=True)