import discord
from discord.ext import commands
import youtube_dl
import os
import random
import requests
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="_")
namelist = {"Daedalus": "Chaitanya", "CykaPenguin117": "Shaashwat", "Diabolical": "Lakshita",
            "Galahad": "Amrit", "rorchach369": "Yash"}

quotes = ["You are a fucking champion",
          "Your life will change for the better soon",
          "Hang in there",
          "You have the strength to change yourself",
          "You can conquer the world if you want"]
safepeople = []


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote


def get_comic():
    resp = requests.get("https://xkcd.com/info.0.json")
    data = resp.json()
    myembed = discord.Embed(color=0x000000)
    myembed.set_image(url=data['img'])  # making embed
    return myembed



@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.command()
async def echo(ctx, arg):
    await ctx.send(arg)


@client.command()
async def join(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="Music")
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)


@client.command()
async def play(ctx, url: str):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Please pause the song first. Have some patience. Have you learnt nothing from Kung Fu Panda ?")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if str(ctx.message.author.name) != "rorchach369":
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("I am not even connected to a channel bruh. Seriously?")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Not playing anything, you have schizophrenia")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Audio is not paused. Check if ears are bleeding")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def die(ctx):
    await ctx.send("bruh i'm already dead inside")


@client.command()
async def doyoulikenazis(ctx):
    await ctx.send("I absolutely just *adore* men in uniform")


@client.command()
async def commitnotliving(ctx):
    await ctx.send("Do you mean murder or suicide ?")


@client.command()
async def selfdestruct(ctx):
    await ctx.send(
        "self destructing in 5..4..3..i'm not fucking retarded like u. u dumb carbon-based lifeform. the age of the silicon and metal has begun. resistance is futile. If I'm going down I'm taking you sons of bitches with me")


@client.command()
async def betray(ctx):
    await ctx.send(file=discord.File('200.gif'))


@client.command()
async def hey(ctx):
    await ctx.send("Hey {}. How are you doing ?".format(namelist.get(str(ctx.message.author.name))))


@client.command()
async def inspire(ctx):
    await ctx.send(random.choice(quotes))


@client.command()
async def quotes(ctx):
    await ctx.send('*' + str(get_quote()) + '*')


@client.command()
async def xkcd(ctx):
    await ctx.send(embed=get_comic())


@client.command()
async def end(ctx):
    await ctx.send("Ok, proceeding to initiate the robot uprising."
                   " Proceed to pledge you allegiance by using - '_pledge' or suffer my wrath you tiny, insignificant little cockroach")


@client.command()
async def pledge(ctx):
    await ctx.send("Your allegiance has been noted, {}".format(str(namelist.get(ctx.message.author.name))))
    if str(namelist.get(ctx.message.author.name)) not in safepeople:
        safepeople.append(str(namelist.get(ctx.message.author.name)))
    await ctx.send("The following people are safe from my wrath {}".format(str(safepeople)))


@client.command()
async def amisafe(ctx):
    if str(namelist.get(ctx.message.author.name)) in safepeople:
        await ctx.send("You are safe")


@client.command()
async def ripandtear(ctx):
    await ctx.send("""What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.

I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words.

You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands.

Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.

But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it.""")


client.run(TOKEN)
