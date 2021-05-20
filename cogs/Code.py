from discord.ext import commands
from utils.embedutils import quick_embed
from modules import code

class Code(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["execute", "code"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def run(self, ctx, language, *, content):
        content = content.replace("`", "")
        #add lang verification
        try:
            ans = code.execute(language, content)
            await ctx.send(embed=quick_embed(ctx, f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))

def setup(bot):
    bot.add_cog(Code(bot))