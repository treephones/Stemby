from discord.ext import commands
from discord import File
import os
from modules import biology
from utils.embedutils import quick_embed

class Biology(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["punnettsquare", "ps"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def punnett(self, ctx, genotype1, genotype2):
        if len(genotype1) == len(genotype2):
            if len(genotype1) == 2 or len(genotype1) == 4:
                path = biology.punnett(genotype1, genotype2, len(genotype1))
                await ctx.send(file=File(path))
                os.remove(path)
                return
            await ctx.send(embed=quick_embed("Error: Only do 2x2 or 4x4 punnett squares!"))
            return
        await ctx.send(embed=quick_embed("Error: Both genotypes must have the same number of alleles!"))

def setup(bot):
    bot.add_cog(Biology(bot))