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
        facereplace.meme(path, facereplace.Memes.PEPE)
        await ctx.send(file=File(path))
        os.remove(path)

    @commands.command()
    @commands.cooldown(2, 15, commands.BucketType.channel)
    async def scream(self, ctx):
        path = await save_attachment(ctx)
        facereplace.meme(path, facereplace.Memes.SCREAM)
        await ctx.send(file=File(path))
        os.remove(path)

    @commands.command()
    @commands.cooldown(2, 15, commands.BucketType.channel)
    async def troll(self, ctx):
        path = await save_attachment(ctx)
        facereplace.meme(path, facereplace.Memes.TROLL)
        await ctx.send(file=File(path))
        os.remove(path)

    @commands.command()
    @commands.cooldown(2, 15, commands.BucketType.channel)
    async def keef(self, ctx):
        path = await save_attachment(ctx)
        facereplace.meme(path, facereplace.Memes.KEEF)
        await ctx.send(file=File(path))
        os.remove(path)

    @commands.command()
    @commands.cooldown(2, 15, commands.BucketType.channel)
    async def obama(self, ctx):
        path = await save_attachment(ctx)
        facereplace.meme(path, facereplace.Memes.OBAMA)
        await ctx.send(file=File(path))
        os.remove(path)



def setup(bot):
    pass
    #bot.add_cog(Memes(bot))