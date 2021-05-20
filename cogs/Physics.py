from discord.ext import commands
from utils.embedutils import quick_embed
from modules import physics

class Physics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["kinematics", "big5"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kin(self, ctx, arg1, arg2, arg3, find):
        find = find.lower()
        try:
            args = [tuple([arg.split("=")[0].lower(), float(arg.split("=")[1])]) for arg in [arg1, arg2, arg3]]
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input formatting!", False))
            return
        vars = [arg[0] for arg in args]
        vars.append(find)
        vars = sorted(vars)
        if vars != sorted(list(set(vars))):
            await ctx.send(embed=quick_embed(ctx, "You can only enter a variable once!", False))
            return
        given = " ".join(vars)
        vars.remove(find)
        pairs = []
        for var in vars:
            for arg in args:
                if arg[0] == var:
                    pairs.append(arg[1])
                    break
        ans = physics.kinematics(given, find, pairs)
        await ctx.send(embed=quick_embed(ctx, ans[0], ans[1]))

def setup(bot):
    bot.add_cog(Physics(bot))