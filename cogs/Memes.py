import os
from discord import File
from discord.ext import commands
from modules import facereplace
from utils.cache import save_attachment

class Memes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(2, 15, commands.BucketType.channel)
    async def pepe(self, ctx):
        path = await save_attachment(ctx)
        facereplace.pepe(path)
        await ctx.send(file=File(path))
        os.remove(path)

def setup(bot):
    bot.add_cog(Memes(bot))