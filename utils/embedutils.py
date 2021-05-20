from discord import Embed, Color
from datetime import datetime

def quick_embed(description, success=True):
    embed = Embed(description=description, color=Embed.Empty if success else Color.dark_red())
    embed.set_footer(text=datetime.today().strftime('%Y-%m-%d %H:%M:%S') if success else Embed.Empty)
    return embed

def mention(id):
    return f"<@{id}>"