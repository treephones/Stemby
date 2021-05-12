from discord.ext import commands
from utils.embedutils import quick_embed
from modules import math_vect

class VectorInputFormatException(Exception):
    def __init__(self, issue):
        if issue == ",":
            self.message = "You must seperate both vectors values by a comma! \n Example `,orthogonal x y z , x y z`"
        elif issue == "len-all":
            self.message = "This command only takes 2 vectors!"
        elif issue == "len-vect":
            self.message = "Both vectors must have the same number of dimensions!"
        elif issue == "not-valid":
            self.message = "Those are not valid vectors!"
        else:
            self.message = "Something went wrong."

def clean_input(input):
    if "," not in input:
        raise VectorInputFormatException(",")
    if len(input.strip().split(",")) != 2:
        raise VectorInputFormatException("len-all")
    try:
        vecs = [list(map(float, vec.strip().split())) for vec in input.strip().split(",")]
    except Exception:
        raise VectorInputFormatException("not-valid")
    if len(vecs[0]) != len(vecs[1]):
        raise VectorInputFormatException("len-vect")
    else:
        return vecs

class Math_vectors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["dot_product", "dot-product"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def dot(self, ctx, *, vecs):
        try:
            vecs = clean_input(vecs)
            await ctx.send(embed=quick_embed(
                f"The dot product of the vectors\n `{vecs[0]}` and `{vecs[1]}` is:\n\n"
                f"**{math_vect.dot_product(vecs[0], vecs[1])}**"
            ))
        except VectorInputFormatException as e:
            await ctx.send(embed=quick_embed(e.message))

    @commands.command(aliases=["vproduct", "vectorproduct", "vmultiply"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def product(self, ctx, *, vecs):
        try:
            vecs = clean_input(vecs)
            await ctx.send(embed=quick_embed(
                f"The product of the vectors\n `{vecs[0]}` and `{vecs[1]}` is:\n\n"
                f"**{math_vect.multiply(vecs[0], vecs[1])}**"
            ))
        except VectorInputFormatException as e:
            await ctx.send(embed=quick_embed(e.message))

    @commands.command(aliases=["vadd", "vsum", "sum"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def add(self, ctx, *, vecs):
        try:
            vecs = clean_input(vecs)
            await ctx.send(embed=quick_embed(
                f"The sum of the vectors\n `{vecs[0]}` and `{vecs[1]}` is:\n\n"
                f"**{math_vect.addition(vecs[0], vecs[1])}**"
            ))
        except VectorInputFormatException as e:
            await ctx.send(embed=quick_embed(e.message))

    @commands.command(aliases=["vsubtract", "vsub", "difference", "vdifference", "vdiff", "diff"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def subtract(self, ctx, *, vecs):
        try:
            vecs = clean_input(vecs)
            await ctx.send(embed=quick_embed(
                f"The difference of the vectors\n `{vecs[0]}` and `{vecs[1]}` is:\n\n"
                f"**{math_vect.subtraction(vecs[0], vecs[1])}**"
            ))
        except VectorInputFormatException as e:
            await ctx.send(embed=quick_embed(e.message))

    @commands.command(aliases=["vsubtract", "vsub", "difference", "vdifference", "vdiff", "diff"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def subtract(self, ctx, *, vecs):
        try:
            vecs = clean_input(vecs)
            await ctx.send(embed=quick_embed(
                f"The difference of the vectors\n `{vecs[0]}` and `{vecs[1]}` is:\n\n"
                f"**{math_vect.subtraction(vecs[0], vecs[1])}**"
            ))
        except VectorInputFormatException as e:
            await ctx.send(embed=quick_embed(e.message))

    @commands.command(aliases=["ortho"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def orthogonal(self, ctx, *, vecs):
        try:
            vecs = clean_input(vecs)
            await ctx.send(embed=quick_embed(
                f"The vectors `{vecs[0]}` and `{vecs[1]}` "
                f"**{'ARE' if math_vect.is_orthogonal(vecs[0], vecs[1]) else 'ARE NOT'}** orthogonal."
            ))
        except VectorInputFormatException as e:
            await ctx.send(embed=quick_embed(e.message))

def setup(bot):
    bot.add_cog(Math_vectors(bot))