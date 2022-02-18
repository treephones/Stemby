import json
import discord
from discord.ext import commands
import aiohttp


class Code(commands.Cog):
    """Test your big brain code"""

    PISTON_API = "https://emkc.org/api/v2/piston/execute"

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.language_info = json.load(open(f"./statics/language_info.json"))

        self.timeout = aiohttp.ClientTimeout(total=10)
        self.session = aiohttp.ClientSession(timeout=self.timeout)

    def addcodecommands(self):
        for lang in self.language_info:

            @commands.command(
                name=lang,
                help=f"Executes your {self.language_info[lang]['name']} code.",
                aliases=self.language_info[lang]["aliases"],
            )
            @commands.cooldown(5, 2.5, commands.BucketType.channel)
            @commands.max_concurrency(3, commands.BucketType.default, wait=True)
            @commands.bot_has_permissions(embed_links=True)
            async def cmd(self, ctx, *, code: commands.clean_content):
                await self.run_code(ctx, ctx.command.name, code)

            cmd.cog = self
            self.__cog_commands__ = self.__cog_commands__ + (cmd,)
            self.bot.add_command(cmd)

    async def run_code(self, ctx: commands.Context, language: str, code: str):
        data = {
            "language": language,
            "version": "*",
            "files": [
                {"content": code.replace("```", "").replace(f"```{language}", "")}
            ],
        }

        r = None
        async with self.session.post(self.PISTON_API, data=json.dumps(data)) as resp:
            r = await resp.json()

        if r is None or "message" in r:
            return await ctx.send("`Sorry, I couldn't run code at that moment`")

        output = (
            r["run"]["output"]
            if len(r["run"]["output"]) <= 1900
            else r["run"]["output"][:1900] + " Exceded Character Limit!"
        )

        if output.replace(" ", "") == "":
            output = "No Output!"

        embed = (
            discord.Embed(
                description=f"Output:```\n{output}```",
                color=discord.Color.red()
                if len(r["run"]["stderr"]) > 0
                else discord.Color.green(),
            )
            .set_author(
                name=f"{ctx.author}'s Code",
                icon_url=ctx.author.avatar.url,
            )
            .set_footer(
                text=f"{self.language_info[r['language']]['name']} - {r['version']}",
                icon_url=self.language_info[r["language"]]["logo"],
            )
        )
        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    cog = Code(bot)
    bot.add_cog(cog)
    cog.addcodecommands()
