import random
import re
import os

import discord
from discord.ext import commands

class MessageEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.video_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "media", "kram"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content == "tg":
            for _ in range(random.randint(1, 7)):
                await message.channel.send("tg")

        pattern_quoi = re.compile(r"quoi[\s\?\!\.]*$", re.IGNORECASE)
        if pattern_quoi.search(message.content):
            await message.channel.send("FEUR")

        if len(message.content) > 200:
            try:
                video_file = random.choice(os.listdir(self.video_dir))
                video_path = os.path.join(self.video_dir, video_file)
                file = discord.File(video_path)
                await message.reply(file=file)
            except Exception as e:
                print(f"Error sending file: {e}")

        pattern_mmmm = re.compile(r"^[mM]+[?]?$", re.IGNORECASE)
        if pattern_mmmm.search(message.content):
            await message.channel.send("^^?")

async def setup(bot):
    await bot.add_cog(MessageEvents(bot))
