from discord.ext import commands

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ext):
        self.load_extension(f"cogs.{ext}")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ext):
        self.unload_extension(f"cogs.{ext}")

def setup(bot):
    bot.add_cog(Owner(bot))