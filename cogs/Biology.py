from discord.ext import commands

class Biology(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["punnettsquare"])
    async def punnett(self, ctx, sequence):
        print("ok")

def setup(bot):
    bot.add_cog(Biology(bot))