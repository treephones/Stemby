from discord.ext import commands
from modules import math_general
from utils.embedutils import quick_embed

class Math_general(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["conv"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def convert(self, ctx, *, args):
        args = args.split()
        if len(args) == 2:
            await ctx.send(embed=quick_embed(await math_general.convert(args[0], args[1])))
        elif len(args) == 3:
            await ctx.send(embed=quick_embed(await math_general.convert(f"{args[0]}{args[1]}", args[2])))
        else:
            await ctx.send(embed=quick_embed("Something went wrong! The command format is \n\n,convert `[value]` `[from]` `[to]`"))

    @commands.command(aliases=["eval"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def evaluate(self, ctx, *, expr):
        await ctx.send(embed=quick_embed(await math_general.evaluate(expr)))

def setup(bot):
    bot.add_cog(Math_general(bot))