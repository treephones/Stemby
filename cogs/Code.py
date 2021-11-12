from discord.ext import commands
from utils.embedutils import quick_embed
from modules import code

class Code(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["python3"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def python(self, ctx, *, content):
        content = content.replace("```python", "").replace("```py", "").replace("`", "")
        #add lang verification
        try:
            ans = code.execute(content, "python", self.bot.runtimes)
            await ctx.send(embed=quick_embed(ctx, f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def java(self, ctx, *, content):
        content = content.replace("```java", "").replace("`", "")
        # add lang verification
        try:
            ans = code.execute( content, "java", self.bot.runtimes)
            await ctx.send(embed=quick_embed(ctx, f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def c(self, ctx, *, content):
        content = content.replace("```c", "").replace("`", "")
        # add lang verification
        try:
            ans = code.execute(content, "c", self.bot.runtimes)
            await ctx.send(embed=quick_embed(ctx, f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))

    @commands.command(aliases=["js"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def javascript(self, ctx, *, content):
        content = content.replace("```js", "").replace("```javascript", "").replace("`", "")
        # add lang verification
        try:
            ans = code.execute(content, "javascript", self.bot.runtimes)
            await ctx.send(embed=quick_embed(ctx, f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def swift(self, ctx, *, content):
        content = content.replace("```swift", "").replace("`", "")
        # add lang verification
        try:
            ans = code.execute(content, "swift", self.bot.runtimes)
            await ctx.send(embed=quick_embed(ctx,f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cpp(self, ctx, *, content):
        content = content.replace("```cpp", "").replace("```c++", "").replace("`", "")
        # add lang verification
        try:
            ans = code.execute(content, "c++", self.bot.runtimes)
            await ctx.send(embed=quick_embed(ctx,f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def csharp(self, ctx, *, content):
        content = content.replace("```c#", "").replace("```csharp", "").replace("`", "")
        # add lang verification
        try:
            ans = code.execute(content, "csharp", self.bot.runtimes)
            await ctx.send(embed=quick_embed(ctx,f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ruby(self, ctx, *, content):
        content = content.replace("```ruby", "").replace("`", "")
        # add lang verification
        try:
            ans = code.execute(content, "ruby", self.bot.runtimes)
            await ctx.send(embed=quick_embed(ctx,f"Language: **{ans['language'].upper()}**\nVersion: **{ans['version']}**\n\nOutput:\n```{ans['run']['output']}```"))
        except Exception:
            await ctx.send(embed=quick_embed(ctx, "Something went wrong! Check the input format of the code.", False))
def setup(bot):
    bot.add_cog(Code(bot))