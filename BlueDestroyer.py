# BlueDestroyer

# Declare Stuff
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import os
import random
import re
import sys
from pathlib import Path

# Create Response List
response = ['You will be contained!', 'Get your gayness outta here!', 'Sucken dick I see...', 'Stop linking gay shit', 'One day you will be no more.']
insult = random.SystemRandom()

# Create Coin
coin = ['Heads!', 'Tails!']
side = random.SystemRandom()
side = side.choice(coin)

# Create Bot Commands
bot = commands.Bot(command_prefix = '.')

# Prep Bot
@bot.event
async def on_ready():
    print ("Blue will be contained.")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)


@bot.event
async def on_message(message):
    for attachment in message.attachments:
        if attachment['filename'].find("cat3.jpg") > -1:
            await bot.delete_message(message)
            await bot.send_message(message.author, insult.choice(response))
            await bot.process_commands(message) 
            
    if message.content[-8:] == "cat3.jpg":
        await bot.delete_message(message)
        await bot.send_message(message.author, insult.choice(response))
        await bot.process_commands(message)
  
# Coin Flip Event
@bot.event
async def on_message(message):
    userID = message.author.name
    if message.content.upper().startswith('!COIN FLIP'):
        await bot.send_message(message.channel, '%s' %  userID + ' ' + side)
        await bot.process_commands(message)
    
bot.run(os.getenv('TOKEN'))
