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
bot_prefix= "="
client = commands.Bot(command_prefix=bot_prefix)
Client = discord.Client()
client.remove_command('help')
version = 7.9

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Here to help!"))
    print("Bot online!")
 
@client.event
async def on_message(message):
    if message.content.upper().startswith("=UNKNOWN"):
            channel = client.get_channel(854984443881979934)
            args = message.content.split(" ")
            await client.delete_message(message)
            await client.send_message(Channem(channel), ":exclamation: %s" % (" ".join(args[1:])))
            await client.send_message(Channem(channel), "%s" % (" ".join(args[1:])))
 
    
client.run(os.environ.get('TOKEN'))
