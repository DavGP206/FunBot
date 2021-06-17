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
 
@client.command()
async def unknown(ctx, a):
  channel = client.get_channel(854984443881979934)
  await ctx.delete()
  await ctx.send(channel=channel, content=f":exclamation: {a}")
 
    
client.run(os.environ.get('TOKEN'))
