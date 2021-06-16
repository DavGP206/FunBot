import aiohttp
import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Bot
global chat_filter
global bypass_list
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
            args = message.content.split(" ")
            await client.delete_message(ctx.message)
            await client.send_message(message.channel, ":warning: Figyelem :warning:")
            await client.send_message(message.channel, "⠀")
            await client.send_message(message.channel, ":exclamation: %s" % (" ".join(args[1:])))
            await client.send_message(message.channel, "⠀")
            await client.send_message(message.channel, "[ @here ]")
 
  
client.run(os.environ.get('TOKEN'))
