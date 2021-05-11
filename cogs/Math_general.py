from discord.ext import commands

class Math_general(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def convert(self, ctx, value, unit1, unit2):
        print("ok")

def setup(bot):
    bot.add_cog(Math_general(bot))