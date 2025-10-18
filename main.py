import os
import discord
import random

from discord.ext import commands
from discord import app_commands

from dotenv import load_dotenv

from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()

class Bot(commands.Bot):
    async def on_ready(self):
        print(f'{bot.user} up')
        try:
            guild = discord.Object(id=1098342509324800000)
            synced = await bot.tree.sync(guild=guild)
            print(f'{len(synced)} commandes synchro sur le serv {guild.id}')
        except Exception as e:
            print(f'Erreur lors de la synchro : {e}')

intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix="!", intents=intents)
GUILD_ID = discord.Object(id=1098342509324800000)


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong !')

@bot.tree.command(name="ping", description="Pour test le bot", guild=GUILD_ID)
async def slashPing(interaction: discord.Interaction):
    await interaction.response.send_message("Pong !")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == "tg":
        for i in range(random.randint(1,7)):
            await message.channel.send("tg")

    await bot.process_commands(message)

bot.run(TOKEN)