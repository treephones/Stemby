# import os
# from discord import File
from discord.ext import commands

# from modules import facereplace
# from utils.cache import save_attachment

import requests
import discord
from discord.ext import commands
from urllib.parse import quote


class MultiString(commands.Converter):
    def __init__(
        self,
        n=2,
        require=False,
        fill_missing=False,
    ):
        self.n = n
        self.require = require
        self.fill_missing = fill_missing

    async def convert(self, ctx: commands.Context, argument: str) -> list:
        args = argument.replace(", ", ",").replace(" ,", ",").split(",")
        if not isinstance(args, list):
            args = [args]

        args = args[: self.n]
        if not self.fill_missing:
            if self.require and len(args) != self.n:
                raise commands.UserInputError()
        else:
            diff = self.n - len(args)
            args += ["" for _ in range(diff)]

        parsed = []
        for arg in args:
            parsed.append(
                await commands.clean_content(
                    use_nicknames=True, fix_channel_mentions=True
                ).convert(ctx, arg)
            )

        return parsed[: self.n]


class Memes(commands.Cog):
    """Custom Memes"""

    BASE_URL = "https://cdn.nathanferns.xyz/memes"
    DOCS_URL = "https://mime.rcp.r9n.co/multidocs"

    def __init__(self, bot):
        self.bot = bot

        self.memes = "all"
        self.memes_data = None

    @staticmethod
    def to_query_string(fields: dict) -> str:
        return "&".join(f"{k}={quote(v)}" for k, v in fields.items())

    def add_meme_commands(self):
        resp = requests.post(self.DOCS_URL, json=self.memes)
        self.memes_data = {
            k: v for k, v in resp.json().items() if "image" not in v.values()
        }

        for meme_id, meme_fields in self.memes_data.items():

            @commands.command(
                name=meme_id,
                help=f'{", ".join(f"<{k}>" for k in meme_fields.keys())} | Sends your custom meme',
            )
            @commands.bot_has_permissions(embed_links=True)
            async def cmd(
                self,
                ctx: commands.Context,
                *,
                content: MultiString(n=5, fill_missing=True),
            ):
                fields = self.to_query_string(
                    {
                        k: v
                        for k, v in zip(
                            self.memes_data[ctx.command.name].keys(),
                            content[: len(self.memes_data[ctx.command.name])],
                        )
                    }
                )

                embed = (
                    discord.Embed(color=discord.Color.random())
                    .set_image(url=f"{self.BASE_URL}/{ctx.command.name}?{fields}")
                    .set_footer(text=f"{ctx.author}'s meme")
                )
                await ctx.reply(embed=embed, mention_author=False)

            cmd.cog = self
            self.__cog_commands__ = self.__cog_commands__ + (cmd,)
            self.bot.add_command(cmd)

    # @commands.command()
    # @commands.cooldown(2, 15, commands.BucketType.channel)
    # async def pepe(self, ctx):
    #     path = await save_attachment(ctx)
    #     facereplace.meme(path, facereplace.Memes.PEPE)
    #     await ctx.send(file=File(path))
    #     os.remove(path)

    # @commands.command()
    # @commands.cooldown(2, 15, commands.BucketType.channel)
    # async def scream(self, ctx):
    #     path = await save_attachment(ctx)
    #     facereplace.meme(path, facereplace.Memes.SCREAM)
    #     await ctx.send(file=File(path))
    #     os.remove(path)

    # @commands.command()
    # @commands.cooldown(2, 15, commands.BucketType.channel)
    # async def troll(self, ctx):
    #     path = await save_attachment(ctx)
    #     facereplace.meme(path, facereplace.Memes.TROLL)
    #     await ctx.send(file=File(path))
    #     os.remove(path)

    # @commands.command()
    # @commands.cooldown(2, 15, commands.BucketType.channel)
    # async def keef(self, ctx):
    #     path = await save_attachment(ctx)
    #     facereplace.meme(path, facereplace.Memes.KEEF)
    #     await ctx.send(file=File(path))
    #     os.remove(path)

    # @commands.command()
    # @commands.cooldown(2, 15, commands.BucketType.channel)
    # async def obama(self, ctx):
    #     path = await save_attachment(ctx)
    #     facereplace.meme(path, facereplace.Memes.OBAMA)
    #     await ctx.send(file=File(path))
    #     os.remove(path)


def setup(bot):
    cog = Memes(bot)
    bot.add_cog(cog)
    cog.add_meme_commands()
