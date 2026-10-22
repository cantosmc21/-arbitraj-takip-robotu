
import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def main():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": "🤖 Arbitraj takip robotu çalışıyor!\n"
                    "Ağ: Arbitrum\n"
                    "Mod: İzleme — gerçek işlem yapmıyor."
        },
        timeout=20,
    )
    response.raise_for_status()
    print("Telegram test mesajı gönderildi.")

if __name__ == "__main__":
    main()
