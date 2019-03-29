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
    await client.change_presence(game=discord.Game(name="{} Szerveren".format(str(len(client.servers)))))
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
        emb.add_field(name="!!invite", value="Bot szervere, bot meghívó linkje", inline=False)
        emb.add_field(name="!!penz", value="Fej vagy Írás", inline=False)
        emb.add_field(name="!!userinfo", value="Kiírja egy megadott személy információit", inline=False)
        emb.add_field(name="!!keszito", value="Kiírja a készítőm nevét", inline=False)
        emb.set_footer(text="LaserBot")
        await client.send_message(message.channel, embed=emb)

    if message.content.upper().startswith("!!HELP"):
        emb3 = (discord.Embed(Title="Cim", colour=0xFFFF00))
        emb3.add_field(name="Zene parancsok", value="⠀")
        emb3.add_field(name="!!belep", value="Bot belép a csatornádba", inline=False)
        emb3.add_field(name="!!play [Link]", value="Lejátsza a megadott zenét! :warning: Csak akkor adj meg más zenét, ha a másik már lejárt, vagy a bot kifagy! :warning: Csak linkel küködik!", inline=False)
        emb3.add_field(name="!!kilep", value="Bot kilép a csatornából", inline=False)
        emb3.set_footer(text="LaserBot")
        await client.send_message(message.channel, embed=emb3)
 
    if message.content.upper().startswith("!!HELP"):
        emb2 = (discord.Embed(Title="Cim", colour=0xff0000))
        emb2.add_field(name="Admin parancsok", value="⠀")
        emb2.add_field(name="!!clear [Szám]", value="Törli a chatben az üzeneteket", inline=False)
        emb2.add_field(name="!!figyelmeztetes [Szöveg]", value="Kiírja a megadott szöveget Figyelmeztetés ként", inline=False)
        emb2.set_footer(text="LaserBot")
        await client.send_message(message.channel, embed=emb2)

    if message.content.upper().startswith("!!KESZITO"):
        emb4 = (discord.Embed(Title="Cim", colour=0x0000CD))
        emb4.add_field(name="Bot készítője", value="⠀")
        emb4.add_field(name="OnlyDAVE", value="⠀", inline=False)
        emb4.add_field(name="Szervere:", value="https://discord.gg/BnT2qA3", inline=False)
        emb4.add_field(name="Programozási nyelv:", value="Discord.py", inline=False)
        emb4.set_footer(text="LaserBot")
        await client.send_message(message.channel, embed=emb4)
        
    if message.content.upper().startswith("!!INVITE"):
        userID = message.author.id
        await client.send_message(message.channel, "Bot meghívása a szerveredre: https://discordapp.com/api/oauth2/authorize?client_id=442269171858931723&permissions=8&scope=bot")
        await client.send_message(message.channel, "Bot hivatalos szervere: https://discord.gg/uxkRKhw")
 
    await client.process_commands(message)


@client.command(pass_context=True)
async def belep(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    await client.say("Beléptem a Voice channelbe!")
    
@client.command(aliases=['server', 'sinfo', 'si', 'serverinfo'], pass_context=True)
async def szerverinfo(ctx):
    if not ctx.message.author.bot:
        online = 0
        for i in ctx.message.server.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
        role_count = len(ctx.message.server.roles)
        emoji_count = len(ctx.message.server.emojis)
        embed = discord.Embed(title="Információk a következő szerverről: {}".format(ctx.message.server.name), description="Ezeket találtam:", color=0x00ff00)
        embed.add_field(name="Név: ", value=ctx.message.server.name, inline=True)
        embed.add_field(name="ID: ", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Rangok: ", value=len(ctx.message.server.roles), inline=True)
        embed.add_field(name="Tagok: ", value=len(ctx.message.server.members))
        embed.add_field(name='Jelenleg elérhető', value=online)
        embed.add_field(name="Szerver létrehozási dátuma: ", value=ctx.message.server.created_at.__format__('%A, %Y. %m. %d. @ %H:%M:%S'), inline=True)
        embed.add_field(name="Jelenlegi szoba létrehozási dátuma: ",value=ctx.message.channel.created_at.__format__('%A, %Y. %m. %d. @ %H:%M:%S'), inline=True)
        embed.add_field(name="Jelenlegi szoba: ",value=ctx.message.channel, inline=True)
        embed.add_field(name="Szerver tulajdonosa: ",value=ctx.message.server.owner.mention, inline=True)
        embed.add_field(name="Szerver tulajdonosának az állapota: ",value=ctx.message.server.owner.status, inline=True)
        embed.add_field(name="Szerver régiója: ",value=ctx.message.server.region, inline=True)
        embed.add_field(name='Ellenőrzési szint', value=str(ctx.message.server.verification_level))
        embed.add_field(name='Emoteok száma', value=str(emoji_count))
        embed.add_field(name='Szerver legmagasabb rangja', value=ctx.message.server.role_hierarchy[0])
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
        embed.set_footer(text="LaserBot")
        await client.say(embed=embed)
    else:
        return False

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

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)+ 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Üzenetek törölve!')
    
@client.command(aliases=['user-info', 'ui'], pass_context=True, invoke_without_command=True)
async def info(ctx, user: discord.Member):
    '''Használat: !!info <Név>'''
    if not ctx.message.author.bot:
        try:
            embed = discord.Embed(title="Információk: {}-ról/ről".format(user.name), description="Ezeket találtam:", color=0x00ff00)
            embed.add_field(name="Neve", value=user.name, inline=True)
            embed.add_field(name='Beceneve', value=user.nick, inline=True)
            embed.add_field(name="ID-je", value=user.id, inline=True)
            embed.add_field(name="Állapota", value=user.status, inline=True)
            embed.add_field(name='Játékban', value=user.game, inline=True)
            embed.add_field(name="Legmagasabb rangja", value=user.top_role)
            #embed.add_field(name="Csatlakozott", value=user.joined_at)
            embed.add_field(name='Csatlakozott', value=user.joined_at.__format__('%A, %Y. %m. %d. @ %H:%M:%S'))
            embed.set_author(name=user, icon_url=user.avatar_url)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text="LaserBot")
            await client.say(embed=embed)
        except:
            await client.say("Hoppá! Valószínűleg nem említetted meg a felhasználót! :x:\nHelyes használat: !!info [említés]")
    else:
        return False
   
@client.command(pass_context=True)
async def osszead(ctx, a: float, b: float):
   if not ctx.message.author.bot:
        try:
             await client.say("Az eredmény: {}".format(a + b))
        except:
             await client.say("Csak számot adhatsz meg!..")
   else:
        pass
    
@client.command(pass_context=True)
async def kivon(ctx, a: float, b: float):
   if not ctx.message.author.bot:
        try:
             await client.say("Az eredmény: {}".format(a - b))
        except:
             await client.say("Csak számot adhatsz meg!..")
   else:
        pass

@client.command(pass_context=True)
async def plusz(ctx, a: float, b: float):
   if not ctx.message.author.bot:
        try:
             await client.say("Az eredmény: {}".format(a * b))
        except:
             await client.say("Csak számot adhatsz meg!..")
   else:
        pass
    
@client.command(pass_context=True)
async def plusz(ctx, a: float, b: float):
   if not ctx.message.author.bot:
        try:
             await client.say("Az eredmény: {}".format(a / b))
        except:
             await client.say("Csak számot adhatsz meg. Vigyázz!! A nulla nem értelmezett szám!")
   else:
        pass
    
client.run(os.environ.get('TOKEN'))
