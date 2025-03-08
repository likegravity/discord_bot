# -*- coding: utf-8 -*-

# import
import importlib
import os
import discord
import discord.ext
from discord import app_commands

# discord
intent = discord.Intents.default()
intent.emojis = True
intent.message_content = True
intent.messages = True
client = discord.Client(intents=intent)
tree = app_commands.CommandTree(client)

# slash command
@app_commands.command(name="ㄹㅇㅋㅋ", description="ㄹㅇㅋㅋ를 출력")
async def mother(interaction: discord.Interaction):
    await interaction.response.send_message("ㄹㅇㅋㅋ")

@client.event
async def on_message(message):
    global llmUserCooltime, llmIsRunning
    if message.guild == None:
        # reject DM
        return
    if message.content == None:
        # reject no message
        return
    if message.channel == None:
        # reject DM
        return
    if message.author == client.user:
        # reject echo
        return
    if message.author.bot == True:
        # reject bot
        return
    
    # 여기다가 채팅 들어온거 처리하셈
    async with message.channel.trigger_typing():
        await message.channel.send(f"message.content:{message.content}\nmessage.channel.name:{message.channel.name}\nmessage.author.name:{message.author.name}")


@client.event
async def on_ready():
    tree.add_command(mother)
    await tree.sync()
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="엄"))
    
client.run(os.getenv("DISCORD_TOKEN"))
