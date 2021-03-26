import discord
from discord.ext import commands

import random

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Greetings is online.")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(name='99', help='Responds with a random quote from Brooklyn 99')
    async def nine_nine(self, ctx):

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]


        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)





def setup(bot):
    bot.add_cog(Greetings(bot))