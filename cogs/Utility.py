from discord.ext import commands
from utils.embedutils import quick_embed

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def help(self, ctx):
        print("help")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def ping(self, ctx):
        await ctx.send(embed=quick_embed(f"CroSenpai2's latency is **{round(self.bot.latency * 1000)}ms**!"))

    @commands.command(aliases=["alias"])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def aliases(self, ctx, command):
        try:
            aliases = commands.Bot.get_command(self.bot, command).aliases
            bs = "\n"
            await ctx.send(embed=quick_embed(f"The aliases for the `{command}` command are:\n\n {bs.join(aliases)}"))
        except Exception:
            await ctx.send(embed=quick_embed(f"`{command}` is not a command!", False))


def setup(bot):
    bot.add_cog(Utility(bot))