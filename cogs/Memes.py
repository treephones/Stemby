from discord import Attachment
from discord.ext import commands
from utils.cache import save_attachment

class Memes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(2, 15, commands.BucketType.channel)
    async def pepe(self, ctx):
        path = save_attachment(ctx)

def setup(bot):
    bot.add_cog(Memes(bot))