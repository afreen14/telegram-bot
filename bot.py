import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send app name to search 🔍")

@bot.message_handler(func=lambda message: True)
def search(message):
    text = message.text.lower()
    
    if "capcut" in text:
        bot.send_message(message.chat.id, "CapCut Found ✅")
        # Yahan channel message forward karna hoga
    else:
        bot.send_message(message.chat.id, "App not found ❌")

bot.polling()
