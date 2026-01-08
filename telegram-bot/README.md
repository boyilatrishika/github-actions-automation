# Telegram Copy-Paste Bot

🤖 A Telegram bot that allows you to manually copy messages from WhatsApp and forward them to your Telegram chat.

## Features

✅ **Manual Copy-Paste** - Copy WhatsApp messages and forward to Telegram
✅ **Message Formatting** - Includes sender name, timestamp, and message content
✅ **Simple Commands** - Easy-to-use `/copy` command
✅ **Error Handling** - Robust error handling with helpful messages

## Setup

### 1. Environment Variables

Add these secrets to your GitHub Actions:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### 2. Installation

```bash
pip install -r requirements.txt
```

### 3. Running the Bot

```bash
python telegram_copy_bot.py
```

## Usage

### Available Commands

- `/start` - Show welcome message
- `/help` - Show help information  
- `/copy [message]` - Forward a message to your Telegram chat

### Example

```
User: /copy Great news from the team about the project!
Bot: ✅ Message forwarded to your Telegram chat!
```

The forwarded message will include:
- 📱 Sender information
- 👤 Who shared the message
- ⏰ Timestamp
- Message content

## How It Works

1. Copy a message from your WhatsApp Business group
2. Send `/copy [message]` to the bot
3. The bot forwards it to your personal Telegram chat
4. You receive a formatted message with all details

## Requirements

- Python 3.9+
- python-telegram-bot 20.3
- python-dotenv 1.0.0

## File Structure

```
telegram-bot/
├── telegram_copy_bot.py       # Main bot script
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Troubleshooting

**Bot not responding?**
- Check if bot token is correct
- Verify chat ID is properly set
- Check internet connection

**Message not forwarding?**
- Ensure message text is provided with `/copy`
- Check if bot has permission to send messages
- Review error message for details

## Future Enhancements

- AI processing with Groq/Gemini API
- Message summarization
- Media forwarding (images, documents)
- WhatsApp Business API integration

---

**Created for manual WhatsApp to Telegram message forwarding** 📲
