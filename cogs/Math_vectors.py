from discord.ext import commands

class Math_vectors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
def setup(bot):
    bot.add_cog(Math_vectors(bot))