import os
import discord
from discord.ext import commands
import requests
from utils.embedutils import quick_embed

class STEMbot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=kwargs.get("command_prefix"),
            status=kwargs.get("status"),
            activity=kwargs.get("activity"),
            help_command=kwargs.get("help_command")
        )
        self.app_info = None
        self.runtimes = []

    async def on_ready(self):
        self.app_info = await self.application_info()
        self.runtimes = requests.get("https://emkc.org/api/v2/piston/runtimes").json()
        await self.user.edit(username="Stemby")
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
        command_prefix=commands.when_mentioned_or(",,"),
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.listening, name=',help'),
        help_command=None
    )

    def load_extensions():
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                try:
                    bot.load_extension(f"cogs.{file[:-3]}")
                    print(f"Loaded {file}!")
                except Exception as e:
                    print(e)
                    print(f"Unable to load {file}!")

    def initialize_caches():
        try:
            os.makedirs('./caches/punnett/')
            os.makedirs('./caches/graphs/')
            os.makedirs('./caches/facereplace/')
            print("Initialized caches!")
        except FileExistsError:
            print("Some cache directories already exist!")

    load_extensions()
    initialize_caches()

    try:
        bot.run(os.environ['TOKEN'])
    except KeyboardInterrupt:
        bot.logout()

if __name__ == "__main__":
    run()