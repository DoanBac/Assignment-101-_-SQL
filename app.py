from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Đọc biến môi trường từ Render
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# Route mặc định để tránh lỗi 404
@app.route('/')
def home():
    return "Webhook server is running."

# Route nhận webhook từ TradingView
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)  # Log dữ liệu nhận được

    # Lấy thông tin từ JSON
    signal = data.get('signal', 'unknown')
    symbol = data.get('symbol', 'unknown')
    price = data.get('price', 'unknown')
    sl = data.get('sl', 'unknown')
    tp = data.get('tp', 'unknown')

    # Tạo nội dung tin nhắn
    message = f"""
📡 {signal.upper()} SIGNAL
📈 Symbol: {symbol}
💰 Entry: {price}
🛑 SL: {sl}
🎯 TP: {tp}
"""

    # Gửi tin nhắn đến Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(telegram_url, json=payload)
    print("Telegram response:", response.text)  # Log phản hồi từ Telegram

    return "OK", 200

# Khởi chạy Flask app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
