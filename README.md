# Discord Bot

A simple Discord bot with stock price lookup.

## Setup

### 1. Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** and give it a name
3. Go to the **Bot** tab
4. Click **Add Bot**
5. Under **Privileged Gateway Intents**, enable:
   - **Message Content Intent**
   - **Server Members Intent**
6. Click **Reset Token** and copy your token

### 2. Invite Bot to Your Server

1. Go to **OAuth2** > **URL Generator**
2. Under **Scopes**, select `bot`
3. Under **Bot Permissions**, select:
   - Send Messages
   - Read Message History
   - Embed Links
4. Copy the generated URL and open it in your browser
5. Select your server and authorize

### 3. Run the Bot

```bash
git clone https://github.com/elcruzo/discord-bot-tengo.git
cd discord-bot-tengo
pip install -r requirements.txt
export DISCORD_BOT_TOKEN="your_token_here"
python bot.py
```

## Commands

| Command | Description |
|---------|-------------|
| `$ping` | Check bot latency |
| `$hello` | Get a greeting |
| `$stock AAPL` | Get stock price |
| `$info` | Bot information |

## Example

```
$stock TSLA

📈 Tesla, Inc. (TSLA)
Price: $248.50 (+2.14%)
```

## Requirements

- Python 3.8+
- discord.py
- yfinance

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DISCORD_BOT_TOKEN` | Your bot token from Discord Developer Portal |

## License

MIT License - see [LICENSE](LICENSE) for details.
