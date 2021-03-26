import discord
from discord.ext import commands, tasks



class Sounds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Sounds is online.")

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    # @commands.command(help="Ask bot to join a specific channel")
    # async def join_specific_channel(self, *, channel_name):
    #     channel = channel_name
    #     await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
    # @commands.command(aliases=[], help='This comand plays a song')
    # async def play(self, ctx):
def setup(bot):
    bot.add_cog(Sounds(bot))