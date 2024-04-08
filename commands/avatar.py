import discord
from discord.ext import commands
from typing import Union

class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='avatar', description='Get the avatar for a user')
    async def avatar_command(self, ctx, user: Union[discord.User, str] = None):
        try:
            if user is None:
                user = ctx.author
            elif isinstance(user, str):
                member = discord.utils.find(lambda m: m.display_name.startswith(user), ctx.guild.members)
                if member:
                    user = member
                else:
                    user = discord.utils.find(lambda u: u.name.startswith(user), self.bot.users)
                    if not user:
                        raise commands.CommandError(f"User with display name or username {user} not found.")

            avatar_url = user.avatar.url if user.avatar else user.default_avatar.url

            embed = discord.Embed(title=f"{user.display_name}'s Avatar", color=0xFFFFFF)
            embed.set_image(url=avatar_url)

            await ctx.send(embed=embed)
        except commands.CommandError as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(AvatarCog(bot))