import discord
from discord.ext import commands
import pyfiglet

class AsciiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ascii', description='Convert text to ASCII')
    async def ascii_command(self, ctx, *, text):
        ascii_art = pyfiglet.figlet_format(text)
        await ctx.send(f'```{ascii_art}```')

async def setup(bot):
    await bot.add_cog(AsciiCog(bot))