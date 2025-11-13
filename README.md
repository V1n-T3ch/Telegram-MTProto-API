# Telegram Auto Message Script

This script allows you to automatically send a pre-defined message to multiple Telegram groups, channels, or chats at specified intervals. The script uses the `Telethon` library to interact with the Telegram API and loads the configuration from a `.env` file for easy setup.

## Requirements

- Python 3.7 or higher
- Telegram Developer API credentials
- `Telethon` library
- `python-dotenv` library

---

## Steps to Set Up the Project

### Step 1: Sign up for Telegram Developer API

1. Visit [Telegram's Developer Portal](https://my.telegram.org/auth).
2. Log in using your Telegram account.
3. Once logged in, click on **API development tools**.
4. Under **Create new application**, fill out the form with your desired app name and short description.
5. After submitting, you will get your `API_ID` and `API_HASH`. These credentials will be used to authenticate your application.

### Step 2: Clone the Repository

If you have not yet cloned the repository, follow these steps:

```bash
git clone https://github.com/V1n-T3ch/Telegram-MTProto-API.git
cd Telegram-MTProto-API
```
### Step 3: Create and Activate your Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows Powershell run 

```bash
source venv\Scripts\Activate.ps1
```

### Step 4: Install the Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Setting up the Environment Variables

```bash
touch .env
```
Open the `.env` file and add your `API_ID`, `API_HASH`, `CHAT_IDS` and `INTERVAL_SECONDS` like this:

```bash
# Telegram API credentials
TELEGRAM_APP_ID=<your_api_id>
TELEGRAM_APP_HASH=<your_api_hash>
TELEGRAM_BOT_TOKEN=<your_bot_token>

# Comma-separated list of chat/group/channel IDs or usernames
CHAT_IDS=<chat_id_1>,<chat_id_2>,<chat_id_3>  # e.g., -1001234567890,-1234567890,@username

# Time interval in seconds between each message send
INTERVAL_SECONDS=60
```

Replace `<your_api_id>` and `<your_api_hash>` with the credentials you got from the Telegram Developer Portal and `<your_bot_token>` with the actual bot token from BotFather.

### Step 6: Getting Chat, Group and Channel IDs

To get IDs run this in your terminal

```bash
python ids.py
```

Remeber to Add the IDs or Usernames that will receive the message to `CHAT_IDS` in the `.env` file and seperate them with commas

### Step 7: Define Your Message

in `message.py` find the variable named `message` currently it will look like this

```bash
message="Hello from your friendly neighborhood python script!"
```

Replace it with your desired message

### Step 8: Run the Script
```bash
python message.py
```

This will send the message to the specified chat,group or channel IDs at the specified interval. 

When you run the script for the first time, `Telethon will prompt you for your phone number and a verification code (sent to your Telegram app)`. This only needs to be done once, as Telethon saves your session.

Make sure to keep the script running to send the message at the specified interval. You can use a scheduler like [APscheduler](https://apscheduler.readthedocs.io/en/latest/) to run the script

### License
This project is licensed under the MIT License.
