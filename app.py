from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8210903805:AAEhDqmSda2n5MVTCELVlmnRNkhDoKbvSzo"
CHAT_ID = "1638555472"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'No message received')

    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(telegram_url, json=payload)
    return "OK", 200
