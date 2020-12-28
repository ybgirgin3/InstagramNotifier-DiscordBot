# bot.py
import os

import discord
from discord.ext import commands

import asyncio


# import credentials
from inf import *

# post faker
from fake_poster import post


### how to make dc bot alive
# link : https://www.freecodecamp.org/news/create-a-discord-bot-with-python/


bot = commands.Bot(command_prefix='!')
client = discord.Client()

@client.event
async def on_ready():
    #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    await client.change_presence(activity=discord.Game('with it\'s life trying to reach top speed of 1000 HP M5'))
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
            f'{client.user} is connected to following guild:\n'
            f'{guild.name}(id: {guild.id})'
            )


    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    print(f'{client.user.name} has connected to Discord')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm.channel.send(
            f'{member.name}, Welcome to ANTISPEEDBUMP BMW CREW Discord Server'
            )


@client.event
async def on_message(message):
    await message.channel.send('hooppp')




"""
post = post()
@client.event
async def notifier(message, post):
    # for antispeedbump
    channel = client.get_channel('792385112062689320')
    msg_sent = False

    while True:
        if post:
            if not msg_sent:
                await message.channel.send()
                msg_sent = True
            else:
                msg_sent = False

    await asyncio.sleep(1)
"""

#client.loop.create_task(notifier(message,post))
client.run(TOKEN)
