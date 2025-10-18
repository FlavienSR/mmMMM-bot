from discord.ext import commands
import random

class MessageEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content == "tg":
            for i in range(random.randint(1, 7)):
                await message.channel.send("tg")

        await self.bot.process_commands(message)
