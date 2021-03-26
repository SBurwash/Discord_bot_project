import discord
from discord.ext import commands

class BotInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Status not working
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
        print("Bot Info is online.")



def setup(bot):
    bot.add_cog(BotInfo(bot))