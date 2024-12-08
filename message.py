from telethon import TelegramClient
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

api_id = int(os.getenv("TELEGRAM_APP_ID"))
api_hash = os.getenv("TELEGRAM_APP_HASH")
chat_identifiers = os.getenv("CHAT_IDS").split(',')
interval_seconds = int(os.getenv("INTERVAL_SECONDS", 60))

chat_ids = [int(chat.strip()) for chat in chat_identifiers]

client = TelegramClient('session_name', api_id, api_hash)

async def send_message_to_multiple_chats(message):
    while True:
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

    message="Hello from your friendly neighborhood bot!"

    await send_message_to_multiple_chats(message)

with client:
    client.loop.run_until_complete(main())
