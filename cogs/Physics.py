from discord.ext import commands

class Physics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kin(self, arg1, arg2, arg3, find):
        args = [tuple(arg.split("=")) for arg in [arg1, arg2, arg3]]

def setup(bot):
    bot.add_cog(Physics(bot))