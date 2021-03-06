import random
from discord.ext import commands
from modules import general
from utils.embedutils import quick_embed

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["def", "d"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def define(self, ctx, *, word):
        if len(word.split()) > 1:
            await ctx.send(embed=quick_embed(ctx, "This feature only defines single word terms!", False))
        else:
            ans = await general.define(word)
            await ctx.send(embed=quick_embed(ctx, ans[0], ans[1]))

    # @commands.command(aliases=["syn", "synonyms"])
    # @commands.cooldown(1, 2, commands.BucketType.user)
    # async def synonym(self, ctx, *, word):
    #     if len(word.split()) > 1:
    #         await ctx.send(embed=quick_embed(ctx, "This feature only gets synonyms for single word terms!", False))
    #     else:
    #         ans = await general.synonyms(word)
    #         await ctx.send(embed=quick_embed(ctx, ans[0], ans[1]))

    @commands.command(aliases=["rand", "randomnumber"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def random(self, ctx, min=0, max=100):
        try:
            await ctx.send(embed=quick_embed(ctx, f"```python\n{random.randint(int(min), int(max))}```", title="Random Number:"))
        except Exception:
            await ctx.send("Something went wrong! The min and max must be integers!", False)

    @commands.command(aliases=["choice", "randomchoice"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def choose(self, ctx, *, items):
        try:
            await ctx.send(
                embed=quick_embed(ctx, f"```python\n{random.choice(items.split())}```", title="Randomly chose:"))
        except Exception:
            await ctx.send("Something went wrong! Check check the inputs!")

def setup(bot):
    bot.add_cog(General(bot))