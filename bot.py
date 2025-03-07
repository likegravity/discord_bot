import discord
from discord import app_commands
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

# 랜덤 메시지 목록
messages = [
    "Hey there!",
    "What’s up?",
    "Random message incoming!",
    "Beep boop, I’m a bot!",
    "Gravity is cool, right?"
]

@app_commands.command(name="sayrandom", description="Sends a random message!")
async def say_random(interaction: discord.Interaction):
    random_message = random.choice(messages)  # 랜덤으로 메시지 선택
    await interaction.response.send_message(random_message)

bot.run('YOUR_BOT_TOKEN_HERE')
