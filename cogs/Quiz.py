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
        topic = quiz.clean_topic(topic)
        link = await quiz.get_quiz(await quiz.get_topic_link(topic))
        question, answer = choice(await quiz.get_questions(link))

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '👀'

        txt = f"\n\n"\
              f"{question}\n\n**Answer**: \nReact with the 👀 emote to show the answer!"\
              f"\n\nFlashcard fetched from: \n[{link}]({link})"
        ans_txt = f"\n\n" \
              f"{question}\n\n**Answer**: \n```\n{answer}\n```" \
              f"\n\nFlashcard fetched from: \n[{link}]({link})"

        msg = await ctx.send(embed=quick_embed(ctx, txt, title=f"**Flashcard for `{topic}`**:"))
        await msg.add_reaction('👀')
        try:
            await self.bot.wait_for("reaction_add", timeout=60.0, check=check)
            await msg.edit(embed=quick_embed(ctx, ans_txt, title=f"**Flashcard for `{topic}`**:"))
        except asyncio.TimeoutError:
            await ctx.send(embed=quick_embed(ctx, f"Did not answer flashcard in time! Answer is: \n```\n{answer}\n```", False))
            return

def setup(bot):
    bot.add_cog(Quiz(bot))