# BlueDestroyer

#Declare Stuff
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

# Create Bot Commands
bot = commands.Bot(command_prefix='#')

# Prep Bot
@bot.event
async def on_ready():
    print ("Blue will be contained.")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)


@bot.event
async def on_message(message):
    if message.content[-8:] == "cat3.jpg":
        await bot.delete_message(message)
        await bot.send_message(message.author, 'You will be contained!!!!!!!!!!')
        await bot.process_commands(message)


bot.run("Token")
