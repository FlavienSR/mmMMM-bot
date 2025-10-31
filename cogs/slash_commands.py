import re
import asyncio
import random
from datetime import datetime, timedelta

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
        embed.add_field(name="/rmd", value="Pour ajouter un rappel", inline=False)
        embed.add_field(name="/help", value="Affiche ce message d’aide.", inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="rmd", description="Pour avoir un reminder")
    @app_commands.guilds(discord.Object(id=PERSO),discord.Object(id=ROOTFARM))
    async def slash_rmd(self, interaction: discord.Interaction, temps: str, raison: str):
        pattern_date = re.compile(r"\b(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[0-2])[\/\-](\d{2}|\d{4})\s+(?:[01]?\d|2[0-3]):[0-5]\d(?:\:[0-5]\d)?\b", re.IGNORECASE)
        pattern_temps = re.compile(r"^(?:(\d+)j)?(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$", re.IGNORECASE)
        if pattern_date.search(temps):
            target = datetime.strptime(temps, "%d/%m/%Y %H:%M")
            now = datetime.now()
            delay = (target - now).total_seconds()
            if delay <= 0:
                await interaction.response.send_message(f"Il faut mettre une date dans le futur!")
            else:
                await interaction.response.send_message(f"Rappel ajouté ({temps}). Raison : {raison}")
                await asyncio.sleep(delay)
                await interaction.user.send(f"RAPPEL : {raison}")
        elif pattern_temps.search(temps):
            match = pattern_temps.match(temps)
            jours, heures, minutes, secondes = match.groups(default="0")
            total = (int(jours) * 86400 + int(heures) * 3600 + int(minutes) * 60 + int(secondes))
            if total <= 0:
                await interaction.response.send_message(f"Il faut mettre un temps supérieur à 0!")
            else:
                await interaction.response.send_message(f"Rappel ajouté (dans {temps}). Raison : {raison}")
                await asyncio.sleep(total)
                await interaction.user.send(f"RAPPEL : {raison}")
        else:
            await interaction.response.send_message(f"Mauvais formattage. (Rappel: jj/mm/aaaa hh:mm OU XXj/h/m/s")

    @app_commands.command(name="gay", description="T'es gay à combien de %")
    @app_commands.guilds(discord.Object(id=PERSO),discord.Object(id=ROOTFARM))
    async def simprate(self, interaction: discord.Interaction, user: discord.User = None):
        user = user or interaction.user
        await interaction.response.send_message(f"💞 {user.mention} est gay à **{random.randint(0, 100)}%**")

async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
