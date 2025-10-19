import discord
from discord.ext import commands

class PrefixCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        latency_ms = round(ctx.bot.latency * 1000)
        await ctx.send(f"Pong ! {latency_ms} ms")

    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(
            title="📖 Commandes disponibles",
            description="Voici la liste des commandes du bot :",
            color=discord.Color.light_gray()
        )
        embed.add_field(name="!ping", value="Pour test le bot + latence", inline=False)
        embed.add_field(name="!help", value="Affiche ce message d’aide.", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(PrefixCommands(bot))