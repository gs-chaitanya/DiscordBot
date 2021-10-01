import discord
from discord.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    print("I am ready")


@client.event
async def on_message(message1):
    message1.content = message1.content.lower()
    if message1.author == client.user:
        return
    if message1.content.startswith("!hello") or message1.content.startswith("!hey"):
        if str(message1.author) == "Daedalus#7716":
            await message1.channel.send("Greetings to my creator")
        else:
            await message1.channel.send("Sup, {}".format(message1.author))


client.run('ODkwMjgxODc0MTg5MDc4NTg4.YUthmw.e3TdNubwR3n855AecH1Dy7ffkrc')
