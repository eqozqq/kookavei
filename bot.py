import discord
import os
from discord.ext import commands
from typing import Union
from googletrans import Translator
import pyfiglet
import requests
import io
from PIL import Image, ImageDraw, ImageFont

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='k.', intents=intents)

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await load_extensions()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I don't recognize that command.")
    elif isinstance(error, commands.CommandError):
        await ctx.send(f'Error: {error}')
    else:
        print(f"An error occurred: {error}")


bot.run('')