from discord.ext import commands
from modules import math_general
from utils.embedutils import quick_embed

class Math_general(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["conv"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def convert(self, ctx, *, value, to_unit):
        await ctx.send(embed=quick_embed(await math_general.convert(value, to_unit)))

def setup(bot):
    bot.add_cog(Math_general(bot))