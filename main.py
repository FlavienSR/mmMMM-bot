import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
GUILD_ID = discord.Object(id=1098342509324800000)

@bot.event
async def on_ready():
    print(f'{bot.user} up')
    try:
        guild = discord.Object(id=1098342509324800000)
        synced = await bot.tree.sync(guild=guild)
        print(f'{len(synced)} commandes synchro sur le serv {guild.id}')
    except Exception as e:
        print(f'Erreur lors de la synchro : {e}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong !')

@bot.command(name="ping", description="Pour test le bot", guild=GUILD_ID)
async def slashPing(interaction: discord.Interaction):
    await interaction.response.send_message("Pong !")


bot.run(TOKEN)

1098342509324800000