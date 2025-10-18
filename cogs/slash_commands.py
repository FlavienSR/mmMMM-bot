import discord
from discord.ext import commands
from discord import app_commands

perso = 1098342509324800000
rootfarm = 1288930612048166962

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Pour test le bot + latence")
    @app_commands.guilds(discord.Object(id=perso),discord.Object(id=rootfarm))
    async def slash_ping(self, interaction: discord.Interaction):
        latency_ms = round(interaction.client.latency * 1000)
        await interaction.response.send_message(f"Pong ! {latency_ms} ms")

async def setup(bot):
    await bot.add_cog(SlashCommands(bot))