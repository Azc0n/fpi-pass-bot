from flask import Flask, request
import telegram
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем .env

TOKEN = os.environ['TOKEN']
WEBAPP_URL = os.environ['WEBAPP_URL']

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.effective_chat.id
    message = update.message

    if message and message.text == '/start':
        bot.send_message(
            chat_id=chat_id,
            text="🎟 Нажми на кнопку ниже, чтобы получить FPI-пропуск:",
            reply_markup=telegram.InlineKeyboardMarkup([
                [telegram.InlineKeyboardButton(
                    text="Получить пропуск 🪪",
                    web_app=telegram.WebAppInfo(url=WEBAPP_URL)
                )]
            ])
        )
    return 'ok'

@app.route('/')
def index():
    return 'FPI bot is running'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)