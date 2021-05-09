import os
import discord
from discord.ext import commands

class STEMbot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=kwargs.get("command_prefix"),
        )
        self.app_info = None

    async def on_ready(self):
        self.app_info = await self.application_info()
        print('-' * 11)
        print(f'Logged in as: {self.user.name}\n'
              f'discord.py version: {discord.__version__}\n'
              f'Owner: {self.app_info.owner}')
        print('-' * 11)
        print("STEMbot is now online.")

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

def run():
    bot = STEMbot(
        command_prefix=",",
        help_command=None
    )

    def load_extensions():
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                try:
                    bot.load_extension(f"cogs.{file[:-3]}")
                    print(f"Loaded {file}!")
                except Exception:
                    print(f"Unable to load {file}!")

    load_extensions()
    try:
        bot.run("ODQwNzAwODk1MjUxMDA1NDgx.YJcBuA.XLbtcZdjeCEMmJgXWk9Oe9Tga_4")
    except KeyboardInterrupt:
        bot.logout()

if __name__ == "__main__":
    run()