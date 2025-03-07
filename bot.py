import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Bot is running and connected to Discord!")

print("Starting bot...")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN이 설정되지 않았습니다.")
print("Token loaded successfully, running bot...")
bot.run(DISCORD_TOKEN)
print("This line should not appear unless bot.run() fails")
