import aiohttp
import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Bot
import datetime, time
import os
import youtube_dl
import hashlib
import os
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
    await client.change_presence(game=discord.Game(name='Parancsok: !!help'))
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
                                                               
    if message.content.upper().startswith("!!PENZ"):
        await client.send_message(message.channel, random.choice([":dollar: Fej",
                                                                 ":dollar: Írás"]))
                                                                 
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
 
    await client.process_commands(message)

@client.command(pass_context=True)
async def kick(ctx, member: discord.Member=None):
    if not member:
        await client.say("Kérlek említs meg felhasználót!")
        return
    await client.kick(member)
    await client.say("{} ki lett kickelve!".format(member.mention))
 
@client.command(pass_context=True)
async def ban(ctx, member: discord.Member=None):
    if not member:
        await client.say("Kérlek említs meg felhasználót!")
        return
    await client.ban(member)
    await client.say("{} ki lett bannolva!".format(member.mention))
 
@client.command(pass_context=True)
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(member.server.roles, name="Muted")
    if not member:
        await client.say("Kérlek említs meg felhasználót!")
        return
    await client.add_roles(member, role)
    await client.say("Felhasználó némítva!")
 
@client.command(pass_context=True)
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(member.server.roles, name="Muted")
    if not member:
        await client.say("Kérlek említs meg felhasználót!")
        return
    await client.add_roles(member, role)
    await client.say("A felhasználó már nincs némítva!")

@client.command(pass_context=True)
async def belep(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    await client.say("Beléptem a Voice channelbe!")

@client.command(pass_context=True)
async def kilep(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    await client.say("Kiléptem a Voice channelből!")

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

client.run(os.environ.get('TOKEN'))
