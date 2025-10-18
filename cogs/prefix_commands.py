from discord.ext import commands

class PrefixCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        latency_ms = round(ctx.bot.latency * 1000)
        await ctx.send(f"Pong ! {latency_ms} ms")

async def setup(bot):
    await bot.add_cog(PrefixCommands(bot))