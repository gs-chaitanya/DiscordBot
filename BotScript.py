# BotScript.py
import os

import discord

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    guild = client.guilds
    name1 = guild[0]
    print(name1)
    print(client.guilds)

client.run(TOKEN)
