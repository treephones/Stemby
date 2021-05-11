from discord.ext import commands

class Math_calculus(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Math_calculus(bot))