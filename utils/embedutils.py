from discord import Embed

def quick_embed(description):
    return Embed(description=description)

def mention(id):
    return f"<@{id}>"