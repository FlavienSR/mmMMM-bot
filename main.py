import os
import discord
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

keep_alive()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est prêt.")
    try:
        guild = discord.Object(id=1098342509324800000)
        synced = await bot.tree.sync(guild=guild)
        print(f"{len(synced)} commandes slash sync pour le serveur {guild.id}")
    except Exception as e:
        print(f"Erreur de sync : {e}")

async def load_cogs():
    await bot.load_extension('cogs.prefix_commands')
    await bot.load_extension('cogs.slash_commands')
    await bot.load_extension('cogs.message_events')

async def main():
    await load_cogs()
    await bot.start(TOKEN)

asyncio.run(main())