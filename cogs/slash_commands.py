import discord
from discord.ext import commands
from discord import app_commands

PERSO = 1098342509324800000
ROOTFARM = 1288930612048166962

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Pour test le bot + latence")
    @app_commands.guilds(discord.Object(id=PERSO),discord.Object(id=ROOTFARM))
    async def slash_ping(self, interaction: discord.Interaction):
        latency_ms = round(interaction.client.latency * 1000)
        await interaction.response.send_message(f"Pong ! {latency_ms} ms")

    @app_commands.command(name="help", description="Affiche la liste des commandes disponibles.")
    @app_commands.guilds(discord.Object(id=PERSO), discord.Object(id=ROOTFARM))
    async def slash_help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📖 Commandes disponibles",
            description="Voici la liste des commandes du bot :",
            color=discord.Color.light_gray()
        )
        embed.add_field(name="/ping", value="Pour test le bot + latence", inline=False)
        embed.add_field(name="/help", value="Affiche ce message d’aide.", inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
