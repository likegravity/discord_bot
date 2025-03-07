import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("안녕! 나는 Railway에서 호스팅된 봇이야!")

bot.run(os.getenv("DISCORD_TOKEN"))
