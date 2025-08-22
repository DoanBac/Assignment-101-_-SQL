from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)  # Thêm dòng này để debug

    signal = data.get('signal', 'unknown')
    symbol = data.get('symbol', 'unknown')
    price = data.get('price', 'unknown')
    sl = data.get('sl', 'unknown')
    tp = data.get('tp', 'unknown')

    message = f"{signal.upper()} SIGNAL\nSymbol: {symbol}\nPrice: {price}\nSL: {sl}\nTP: {tp}"

    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(telegram_url, json=payload)
    print("Telegram response:", response.text)  # Thêm dòng này để kiểm tra phản hồi

    return "OK", 200


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
