import discord
from discord.ext import commands
import asyncio

# 키워드 리스트
KEYWORDS = ["ㄴㄱㅁ", "sra", "SRA", "ㄴㅇㅁ", "니애미", "애미"]

# 봇 설정
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # 유저 타임아웃하려면 필요함

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} 준비 완료!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if any(keyword in message.content.lower() for keyword in KEYWORDS):
        try:
            # 60초 타임아웃 (단위는 초)
            duration = 60
            await message.author.timeout(discord.utils.utcnow() + discord.timedelta(seconds=duration), reason="금지 키워드 사용")

            await message.channel.send(f"{message.author.mention}새끼가 금지어를 사용해 {duration}초 타임아웃 처리됨.")
        except Exception as e:
            print(f"타임아웃 실패: {e}")

    await bot.process_commands(message)
    
bot.run(os.getenv("DISCORD_TOKEN"))
