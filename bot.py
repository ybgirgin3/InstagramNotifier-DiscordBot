# bot.py
import os

import discord
from inf import *

import sys

client = discord.Client()



@client.event
async def on_ready():
    #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
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
    await member.dm.channnel.send(
            f'Hey!! {member.name} DC sunucuma hoşgeldin'
            )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Mahmut':
        response = 'onun ben amk'
        await message.channel.send(response)


    if message.content == 'Bilo':
        response = 'Azgın Teke bilo'
        await message.channel.send(response)


    if message.content == 'Berkay':
        response = 'Abi yarrrrrağını yerim'
        await message.channel.send(response)


    if message.content == 'Kero':
        response = 'Sinoplu Bela'
        await message.channel.send(response)


    if message.content == 'Alper':
        response = 'Eskişehirin sikicisi'
        await message.channel.send(response)


client.run(TOKEN)
