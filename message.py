from telethon import TelegramClient
from dotenv import load_dotenv
import os
import asyncio
import requests

load_dotenv()

api_id = int(os.getenv("TELEGRAM_APP_ID"))
api_hash = os.getenv("TELEGRAM_APP_HASH")
chat_identifiers = os.getenv("CHAT_IDS").split(',')
interval_seconds = int(os.getenv("INTERVAL_SECONDS", 60))
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

chat_ids = [int(chat.strip()) for chat in chat_identifiers]

client = TelegramClient('session_name', api_id, api_hash)

def fetch_latest_message():
    """
    Fetch the latest message sent to the bot using Telegram Bot API.
    """
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["ok"] and data["result"]:
            # Get the latest update
            latest_update = data["result"][-1]
            # Check if it contains a message
            if "message" in latest_update:
                return latest_update["message"]["text"]
        return None
    except Exception as e:
        print(f"Error fetching message: {e}")
        return None

async def send_message_to_multiple_chats():
    while True:
        # Fetch the latest message from the bot
        message = fetch_latest_message()
        if not message:
            print("No new message to send.")
        else:
            for chat in chat_ids:
                try:
                    entity = await client.get_entity(chat)
                    chat_id = entity.id
                    print(f"Sending message to: {entity.title if hasattr(entity, 'title') else entity.username}")

                    await client.send_message(chat_id, message)
                    print(f"Message sent to {chat_id}")
                except Exception as e:
                    print(f"Failed to send message to {chat}: {e}")

        await asyncio.sleep(interval_seconds)

async def main():
    await client.start()
    await send_message_to_multiple_chats()

with client:
    client.loop.run_until_complete(main())
