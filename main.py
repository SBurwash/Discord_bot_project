#main.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.presences = True


load_dotenv()
print(f'OMG ITS A TOKKEEEEENNNNNNN {os.getenv("DISCORD_TOKEN")}')
TOKEN = os.getenv('DISCORD_TOKEN')


# bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found.')

    else:
        await ctx.send(f"Unhandled error: {error}")

bot.run(TOKEN)