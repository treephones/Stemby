from discord.ext import commands

class Quiz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["quizme"])
    @commands.cooldown(1, 2, commands.BucketType.channel)
    async def quiz(self, ctx, *, subject):
       pass

def setup(bot):
    bot.add_cog(Quiz(bot))