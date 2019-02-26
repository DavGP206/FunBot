import aiohttp
import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Bot
import datetime, time
import os
import youtube_dl
from discord.voice_client import VoiceClient
global playing
playing = "Jelenleg nem megy semmilyen zene!"
players = {}
global chat_filter
global bypass_list
bot_prefix= "!!"
client = commands.Bot(command_prefix=bot_prefix)
Client = discord.Client()
vc_clients = {}
version = 2.3

players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        players = queues[id].pop(0)
        players[id] = players
        players.start()

@client.event
async def on_ready():
    print("Bot online!")

@client.event
async def on_message(message):
    if message.content.upper().startswith("!!KEX"):
        await client.send_message(message.channel, ":cookie:")

    if message.content.upper().startswith("!!PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.upper().startswith("!!FIGYELMEZTETES"):
        if message.author.server_permissions.administrator == True:
            args = message.content.split(" ")
            await client.send_message(message.channel, ":warning: Figyelem :warning:")
            await client.send_message(message.channel, "⠀")
            await client.send_message(message.channel, ":exclamation: %s" % (" ".join(args[1:])))
            await client.send_message(message.channel, "⠀")
            await client.send_message(message.channel, "[ @here ]")
        else:
            emb3 = (discord.Embed(Title="Cim", colour=0xff0000))
            emb3.add_field(name="Ehhez nincs jogod! :(", value="LaserBot")
            await client.send_message(message.channel, embed=emb3)

    if message.content.upper().startswith("!!DOBOKOCKA"):
        await client.send_message(message.channel, random.choice([":game_die: Ennyit dobtál: 1",
                                                                 ":game_die: Ennyit dobtál: 2",
                                                                 ":game_die: Ennyit dobtál: 3",
                                                                 ":game_die: Ennyit dobtál: 4",
                                                                 ":game_die: Ennyit dobtál: 5",
                                                                 ":game_die: Ennyit dobtál: 6"]))

    if message.content.upper().startswith("!!HELP"):
        emb = (discord.Embed(Title="Cim", colour=0x3DF270))
        emb.add_field(name="Parancsok listája", value="⠀")
        emb.add_field(name="!!help", value="Kiírja a parancsok listáját", inline=False)
        emb.add_field(name="!!kex", value="Ad egy kexet", inline=False)
        emb.add_field(name="!!dobokocka", value="Mond egy számot 1-6 között", inline=False)
        emb.add_field(name="!!ping", value="Pong!", inline=False)
        emb.set_footer(text="LaserBot")
        await client.send_message(message.channel, embed=emb)

    if message.content.upper().startswith("!!HELP"):
        emb2 = (discord.Embed(Title="Cim", colour=0xff0000))
        emb2.add_field(name="Admin parancsok", value="⠀")
        emb2.add_field(name="!!figyelmeztetes [Szöveg]", value="Kiírja a pmegadott szöveget Figyelmeztetés ként", inline=False)
        emb2.set_footer(text="LaserBot")
        await client.send_message(message.channel, embed=emb2)
        
@client.command(pass_context=True)
async def purge(ctx, amount=0):
    if not ctx.message.server == None:
        if ctx.message.author.server_permissions.manage_messages or ctx.message.author.id == "388697370725974016":
            channel = ctx.message.channel
            messages = []
            async for message in client.logs_from(channel, limit=int(amount)):
                messages.append(message)
            await client.delete_messages(messages)
            await client.say("✅ Sikeresen töröltél **{}** üzenetet!.".format(int(amount)))
        else:
            await client.say("❌ Ehhez nincs jogod!")
    else:
        await client.say("❌ Privátban nem használható ez a parancs!")
@purge.error
async def clear_error(error, ctx):
    if ctx.message.author.server_permissions.manage_messages or ctx.message.author.id == "338748699129937930":
        embed = discord.Embed(title='Hiba!', description='Használat: !!purge (szám)', colour=discord.Colour.gold())
        embed.set_footer(text='LaserBot
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title='Hiba!', description='Ehhez nincs jogod!', colour=discord.Colour.gold())
        embed.set_footer(text='LaserBot')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)
        await client.say("Beléptem a hangcsatornába, indíthatjátok a zenéket!")

@client.command(pass_context=True)
async def left(ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()
        await client.say("Elhagytam a hangcsatornát, remélem tetszettek a zenék!")   

@client.command(pass_context=True)
async def pause(ctx):
        id = ctx.message.server.id
        players[id].pause()
        await client.say("A zenét megállítottam!")


@client.command(pass_context=True)
async def stop(ctx):
    try:
        id = ctx.message.server.id
        players[id].stop()
        await client.say("A zenét leállítottam!")
    except:
        await client.say("Jelenleg nem szól egy zene sem!")
    return False


@client.command(pass_context=True)
async def folytat(ctx):
    try:
        id = ctx.message.server.id
        players[id].resume()
        await client.say("A zene folytatódik!")
    except:
        await client.say("Jelenleg nem szól egy zene sem!")
    return False


@client.command(pass_context=True)
async def skip(ctx):
    try:
        id = ctx.message.server.id
        players[id].stop()
    except:
        await client.say("A zenét átugrottam!")
    return False                        

client.run(os.environ.get('TOKEN'))
