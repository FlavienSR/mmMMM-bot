import discord
from discord.ext import commands
from discord import app_commands

GUILD_ID = 1098342509324800000

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Pour test le bot")
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def slash_ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong !")

    async def cog_load(self):
        self.bot.tree.add_command(self.slash_ping)
