from discord.ext import commands
from modules import general
from utils.embedutils import quick_embed

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["def", "d"])
    async def define(self, ctx, *, word):
        if len(word.split(" ")) > 1:
            await ctx.send(embed=quick_embed("This feature only defines single word terms!"))
        else:
            await ctx.send(embed=quick_embed(general.define(word)))

def setup(bot):
    bot.add_cog(General(bot))