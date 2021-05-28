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

        embed = quick_embed(f"Question for `{topic}`:")

def setup(bot):
    bot.add_cog(Quiz(bot))