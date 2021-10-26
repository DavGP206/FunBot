import discord
import asyncio
import random

client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel("801727780655988767")
        messages = ["Hello!", "How are you doing?", "Howdy!"]
        await client.send_message(channel, random.choice(messages))
        await asyncio.sleep(120)

client.loop.create_task(background_loop())
client.run(os.environ.get('TOKEN'))
