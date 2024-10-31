import telebot
import random
import os
API_TOKEN = '7329516426:AAHw4mbeA22v09cYxSyrXxZgqDTFj2tyOm4'

bot = telebot.TeleBot(API_TOKEN)

waste_objects = {
    "стекло":"Стекло можно сдавать на переработку",
    "пластик":"Пластик можно сдавать на переработку",
    "еда":"Еду выбрасываем в обычную урну",
    "лампочка":"Лампочку лучше сдать на специальную утилизацию",
    "металл": "Металлы можно сдавать на переработку.",
    "текстиль": "Текстиль лучше сдавать на переработку.",
    "медицинские отходы": "Медицинские отходы требуют специальной утилизации.",
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который поможет тебе сортировать отходы. Напиши название предмета, и я подскажу, как с ним поступить")



@bot.message_handler(func=lambda message: True)
def sort_waste(message):
    item = message.text.lower()
    response = waste_objects.get(item, "Извините, я пока не знаю как сортировать этот предмет.(")
    bot.send_message(message.chat.id, response)

if __name__ == '__main__':
    bot.polling(none_stop=True)

def help_command():
    commands = {
        "/start": "Запускает бота и показывает приветственное сообщение.",
        "/help": "Показывает список доступных команд.",
        "/go": "То же самое что и команда START"
    }
    
    help_message = "Доступные команды:n"
    for command, description in commands.items():
        help_message += f"{command} - {description}n"
    
    return help_message



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
