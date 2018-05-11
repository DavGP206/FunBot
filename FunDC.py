import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client ()
client = commands.Bot (command_prefix = "!")

@client.event
async def on_ready():
    print ("Egy bot készen áll. Az Online-ra kapcsolás sikeres volt. Bot ID: 000001")

@client.event
async def on_message(message):
    if message.content == "!teszt":
        await client.send_message(message.channel, "Gratulálok! A bot működik, vagyis életre keltettél ^^")
    if message.content == "!suti":
        await client.send_message(message.channel, ":cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie:")
    if message.content.upper().startswith('!MOND'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content == "bottt":
        await client.send_message(message.channel, "Hogy mertél megszólítani? Volt merszed? Szeretlek <3")
    if message.content == "!rex":
        await client.send_message(message.channel, "```Szeretem Rex-et :D Adok neki kutyakaját!``` :cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie:")
    
    


        
client.run ("NDQyMjY5MTcxODU4OTMxNzIz.Dc8Wzg.npmxmpv-eBcuRYKa-5cdqDh9Y8I")
