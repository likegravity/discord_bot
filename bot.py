import discord
from discord.ext import commands
import os

# 🔹 필수 intents 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 읽기 활성화

# 🔹 intents 적용해서 봇 생성
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN이 설정되지 않았습니다.")

bot.run(DISCORD_TOKEN)
