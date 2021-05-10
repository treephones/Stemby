from discord.ext import commands
import json

class Chemistry(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("./statics/periodic-table-lookup.json") as file:
            self.pt = json.load(file)

    @commands.command(aliases=["property"])
    async def properties(self, ctx, property):
        print("ok")

def setup(bot):
    bot.add_cog(Chemistry(bot))