from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.getenv("TELEGRAM_APP_ID"))
api_hash = os.getenv("TELEGRAM_APP_HASH")

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()

    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        print(f"Chat name: {dialog.name}, Chat ID: {dialog.id}")

with client:
    client.loop.run_until_complete(main())
