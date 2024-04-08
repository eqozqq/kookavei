import discord
from discord.ext import commands
from typing import Union
import requests

class EmojiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

import discord
from discord.ext import commands
import requests

class EmojiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='emoji', description='Get the emoji')
    async def emoji_command(self, ctx, emoji: Union[discord.PartialEmoji, str] = None, *, emoji_name: str = None):
        try:
            if emoji:
                if isinstance(emoji, discord.PartialEmoji):
                    emoji_url = emoji.url
                else:
                    emoji_url = emoji
                    emoji = None

                if emoji:
                    emoji_info = await ctx.guild.fetch_emoji(emoji.id)
                    emoji_bytes = requests.get(emoji_url).content
                    emoji_size = len(emoji_bytes) / 1024

                    embed = discord.Embed(title=f"Emoji: {emoji.name}", color=0xFFFFFF)
                    embed.set_image(url=emoji_url)
                    embed.add_field(name="URL", value=emoji_url, inline=False)
                    embed.add_field(name="ID", value=emoji.id, inline=False)
                    embed.add_field(name="File Size", value=f"{emoji_size:.2f} KB", inline=False)
                    
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Please provide either a custom emoji or the name of a standard emoji.")
            elif emoji_name:
                emoji = discord.utils.get(self.bot.emojis, name=emoji_name)
                if emoji is None:
                    emoji = discord.utils.get(discord.emojis, name=emoji_name)

                if emoji:
                    emoji_url = emoji.url
                    emoji_bytes = requests.get(emoji_url).content
                    emoji_size = len(emoji_bytes) / 1024

                    embed = discord.Embed(title=f"Emoji: {emoji.name}", color=0xFFFFFF)
                    embed.set_image(url=emoji_url)
                    embed.add_field(name="URL", value=emoji_url, inline=False)
                    embed.add_field(name="ID", value=emoji.id, inline=False)
                    embed.add_field(name="File Size", value=f"{emoji_size:.2f} KB", inline=False)

                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Emoji with name {emoji_name} not found.")
            else:
                await ctx.send("Please provide either a custom emoji or the name of a standard emoji.")
        except commands.CommandError as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(EmojiCog(bot))