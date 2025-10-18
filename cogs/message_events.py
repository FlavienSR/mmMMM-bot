from discord.ext import commands
import random
import re

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
        
        pattern = re.compile(r"quoi[\s\?\!\.]*$", re.IGNORECASE)
        if pattern.search(message.content):
            await message.channel.send("FEUR")


async def setup(bot):
    await bot.add_cog(MessageEvents(bot))