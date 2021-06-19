import aiohttp
import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Bot
import datetime, time
import os
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
 
@client.command
async def say(ctx, *, text=''):
    if text == '':
        ctx.send("You need to say something")
    else:
        ctx.send(text)
        ctx.message.delete()
    
client.run(os.environ.get('TOKEN'))
