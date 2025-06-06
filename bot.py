import telebot

BOT_TOKEN = '7512726154:AAHwPVIlwOVq7zHd5CGDHi8aVDU10TrY_zo'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello bhai! 🔥 Tera bot chal gaya!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Tune bola: {message.text}")

print("Bot is running...")

bot.infinity_polling()
