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
 
@Bot.command()
async def say(ctx, *, message):
    try:
        await ctx.send(message)
    except:
        await ctx.send("Please Give Some Message!")
    
client.run(os.environ.get('TOKEN'))
