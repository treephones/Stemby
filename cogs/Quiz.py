import asyncio
from discord.ext import commands
from random import choice
from modules import quiz
from utils.embedutils import quick_embed

class Quiz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["quizme"])
    @commands.cooldown(2, 10, commands.BucketType.channel)
    async def quiz(self, ctx, *, topic):
        try:
            question, answer, link = await quiz.get_flashcard(topic)
        except quiz.TopicNotFoundException as e:
            await ctx.send(embed=quick_embed(ctx, f"The topic `{e.entered}` could not be found. Could you have meant `{e.suggested}`?", False))
            return
        except Exception as e:
            print(e)
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Could not fetch flashcard. Maybe try a different topic?", False))
            return

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '👀'

        txt = f"\n\n"\
              f"{question}\n\n**Answer**: \nReact with the 👀 emote to show the answer!"\
              f"\n\nFlashcard fetched from: \n[{link}]({link})"
        ans_txt = f"\n\n" \
              f"{question}\n\n**Answer**: \n```\n{answer}\n```" \
              f"\nFlashcard fetched from: \n[{link}]({link})"
        title = f"**Flashcard for `{topic}`**:"
        msg = await ctx.send(embed=quick_embed(ctx, txt, title=title))
        await msg.add_reaction('👀')
        try:
            await self.bot.wait_for("reaction_add", timeout=60, check=check)
            await msg.edit(embed=quick_embed(ctx, ans_txt, title=title))
        except asyncio.TimeoutError:
            await msg.reply(embed=quick_embed(ctx, f"Did not answer flashcard in time! Answer is: \n```\n{answer}\n```", False))
            return

def setup(bot):
    bot.add_cog(Quiz(bot))