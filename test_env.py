from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv("TELEGRAM_APP_ID")
api_hash = os.getenv("TELEGRAM_APP_HASH")
ids = os.getenv("CHAT_IDS").split(',')
interval_seconds = os.getenv("INTERVAL_SECONDS")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

print("App ID:", api_id)
print("App Hash:", api_hash)
print("Chat IDs:", ids)
print("Interval Seconds:", interval_seconds)
print("Bot Token:", bot_token)