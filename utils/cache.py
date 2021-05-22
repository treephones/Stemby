from random import randint as rand

def gen_cache_name():
    return "".join([str(rand(1,9)) for _ in range(8)])

async def save_attachment(ctx):
    path = f'./caches/facereplace/{gen_cache_name()}.png'
    await ctx.message.attachments[0].save(path)  # no attachments error
    return path