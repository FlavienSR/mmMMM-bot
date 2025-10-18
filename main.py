import os
import discord
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

from cogs.prefix_commands import PrefixCommands
from cogs.slash_commands import SlashCommands
from cogs.message_events import MessageEvents

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est prêt.")
    try:
        guild = discord.Object(id=1098342509324800000)
        synced = await bot.tree.sync(guild=discord.Object(id=guild))
        print(f"{len(synced)} commandes slash sync pour le serveur {guild}")
    except Exception as e:
        print(f"Erreur de sync : {e}")

async def load_cogs():
    await bot.add_cog(PrefixCommands(bot))
    await bot.add_cog(SlashCommands(bot))
    await bot.add_cog(MessageEvents(bot))

async def main():
    await load_cogs()
    keep_alive()
    await bot.start(TOKEN)

asyncio.run(main())