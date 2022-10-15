#!/usr/bin/env python3

import os
import discord
from discord.ext import commands
import yfinance as yf

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)


def get_stock_price(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    if data.empty:
        return None, None, None
    
    price = data["Close"].iloc[-1]
    prev = ticker.info.get("previousClose", price)
    change = ((price - prev) / prev) * 100
    return price, change, ticker.info.get("longName", symbol)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Connected to {len(bot.guilds)} server(s)")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome to the server, {member.name}!")


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(f"Pong! Latency: {round(bot.latency * 1000)}ms")


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")


@bot.command(name="stock")
async def stock(ctx, symbol: str = None):
    if not symbol:
        await ctx.send("Usage: `$stock AAPL`")
        return
    
    symbol = symbol.upper()
    price, change, name = get_stock_price(symbol)
    
    if price is None:
        await ctx.send(f"Could not find data for {symbol}")
        return
    
    emoji = "📈" if change >= 0 else "📉"
    sign = "+" if change >= 0 else ""
    
    await ctx.send(f"{emoji} **{name}** ({symbol})\nPrice: ${price:.2f} ({sign}{change:.2f}%)")


@bot.command(name="info")
async def info(ctx):
    embed = discord.Embed(title="Bot Info", color=0x00ff00)
    embed.add_field(name="Servers", value=len(bot.guilds))
    embed.add_field(name="Prefix", value="$")
    embed.add_field(name="Commands", value="ping, hello, stock, info")
    await ctx.send(embed=embed)


def main():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    
    if not token:
        print("Error: DISCORD_BOT_TOKEN not set")
        print("\nTo get a token:")
        print("1. Go to https://discord.com/developers/applications")
        print("2. Click 'New Application' and give it a name")
        print("3. Go to 'Bot' tab and click 'Add Bot'")
        print("4. Click 'Reset Token' and copy it")
        print("5. Set the environment variable:")
        print("   export DISCORD_BOT_TOKEN='your_token_here'")
        print("\nTo invite the bot to your server:")
        print("1. Go to 'OAuth2' > 'URL Generator'")
        print("2. Select 'bot' scope")
        print("3. Select permissions: Send Messages, Read Message History")
        print("4. Copy the URL and open it in your browser")
        return
    
    bot.run(token)


if __name__ == "__main__":
    main()
