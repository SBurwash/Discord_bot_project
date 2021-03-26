#main.py

import os
import random

import ffmpeg
import youtube_dl

import discord
from discord.ext import commands
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.members = True
intents.presences = True


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!')