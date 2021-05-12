from discord.ext import commands
import json
from modules.chemistry import ChemistryFunctions
from utils.embedutils import quick_embed

class Chemistry(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("./statics/periodic-table-lookup.json", encoding='utf-8') as file:
            self.chem = ChemistryFunctions(json.load(file))

    @commands.command(aliases=["property", "prop"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def properties(self, ctx, element, *, property="all"):
        element, property = element.lower(), property.lower().strip().replace(" ", "_")
        if 0 < len(element) <= 2:
            element = await self.chem.get_element_name_by_symbol(element)

        if property == "all":
            try:
                await ctx.send(embed=quick_embed(self.chem.format_all_properties(self.chem.get_all_properties(element))))
            except KeyError:
                await ctx.send(embed=quick_embed("That element does not exist! Enter the name or symbol of a valid element."))
        else:
            try:
                elem_properties = self.chem.get_all_properties(element)
                try:
                    await ctx.send(embed=quick_embed(self.chem.format_property(elem_properties, property)))
                except KeyError:
                    await ctx.send(embed=quick_embed("That property does not exist. Might be spelling?"))
            except KeyError:
                await ctx.send(embed=quick_embed("That element does not exist! Enter the name or symbol of a valid element."))

def setup(bot):
    bot.add_cog(Chemistry(bot))