from discord import Embed, Color

def quick_embed(description, success=True):
    return Embed(description=description, color=Color.default() if success else Color.dark_red())

def mention(id):
    return f"<@{id}>"