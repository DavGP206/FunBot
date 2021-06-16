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
client.remove_command('help')
vc_clients = {}
version = 7.9
 
players = {}
queues = {}
 
def check_queue(id):
    if queues[id] != []:
        players = queues[id].pop(0)
        players[id] = players
        players.start()
      
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Here to help!"))
    print("Bot online!")
       if message.content.upper().startswith("!!UNKNOWN"):
    if message.content.upper().startswith("=unknown"):
            args = message.content.split(" ")
            await client.delete_message(ctx.message)
            await client.send_message(message.channel, ":exclamation: %s" % (" ".join(args[1:])))
    
client.run(os.environ.get('TOKEN'))
