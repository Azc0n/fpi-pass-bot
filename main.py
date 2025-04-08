from flask import Flask, request
import telegram

TOKEN = '7842549053:AAG9lc6OMYgSplgy40xq1fWh7zX2_G8HA-0'
WEBAPP_URL = 'https://Azc0n.io/fpi-pass/'

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.effective_chat.id
    text = update.message.text

    if text == "/start":
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
    return "ok"

@app.route("/")
def index():
    return "FPI bot is running!"