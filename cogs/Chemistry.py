import os
import discord
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
                await ctx.send(embed=quick_embed(ctx, self.chem.format_all_properties(self.chem.get_all_properties(element))))
            except KeyError:
                await ctx.send(embed=quick_embed(ctx, "That element does not exist! Enter the name or symbol of a valid element.", False))
        else:
            try:
                elem_properties = self.chem.get_all_properties(element)
                try:
                    await ctx.send(embed=quick_embed(ctx, self.chem.format_property(elem_properties, property)))
                except KeyError:
                    await ctx.send(embed=quick_embed(ctx, "That property does not exist. Might be spelling?", False))
            except KeyError:
                await ctx.send(embed=quick_embed(ctx, "That element does not exist! Enter the name or symbol of a valid element.", False))

    @commands.command(aliases=["molmass"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def mass(self, ctx, compound):
        ans = self.chem.mass(compound)
        await ctx.send(embed=quick_embed(ctx, ans[0], success=ans[1]))

    @commands.command(aliases=[])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def balance(self, ctx, *, reaction):
        reaction = reaction.replace(" ", "")
        sides = reaction.split("->") if "->" in reaction else reaction.split("=")
        if len(sides) != 2:
            await ctx.send(embed=quick_embed(ctx, "The equation was formatted incorrectly! Seperate sides with \'->\' or \'=\'!", False))
            return
        compounds = {}
        compounds["reacs"] = sides[0].split("+")
        compounds["prods"] = sides[1].split("+")
        ans = self.chem.balance(compounds)
        await ctx.send(embed=quick_embed(ctx, ans[0], ans[1]))

    @commands.command(aliases=["pt", "periodictable"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def periodic(self, ctx):
        pt_path = f"{os.path.abspath(os.getcwd())}\statics\periodic_table_pic.jpg"
        embed, file = quick_embed(ctx, "Periodic Table:"), discord.File(pt_path)
        embed.set_image(url=f"attachment://periodic_table_pic.jpg")
        await ctx.send(embed=embed, file=file)

def setup(bot):
    bot.add_cog(Chemistry(bot))