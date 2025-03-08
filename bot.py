import discord
from discord.ext import commands
from discord import app_commands
import os

# 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True

# 봇 초기화
bot = commands.Bot(command_prefix="!", intents=intents)

# 봇이 준비되었을 때 실행
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Bot is running and connected to Discord!")
    try:
        GUILD_ID = 123456789012345678  # 서버 ID 입력
        guild = discord.Object(id=GUILD_ID)
        bot.tree.add_command(hello)  # 여기 추가
        synced = await bot.tree.sync(guild=guild)  
        print(f"Synced {len(synced)} command(s) in {GUILD_ID}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# 슬래시 명령어 추가: /hello
@app_commands.command(name="hello", description="Says hello to you!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! How can I assist you today?")

# 봇 시작
print("Starting bot...")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN이 설정되지 않았습니다.")
print("Token loaded successfully, running bot...")
bot.run(DISCORD_TOKEN)
print("This line should not appear unless bot.run() fails")
