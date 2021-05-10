from discord.ext import commands
from utils.embedutils import quick_embed

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def ping(self, ctx):
        await ctx.send(embed=quick_embed(f"CroSenpai2's latency is **{round(self.bot.latency * 1000)}ms**!"))

def setup(bot):
    bot.add_cog(Utility(bot))