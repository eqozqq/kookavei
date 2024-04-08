import discord
from discord.ext import commands
from googletrans import Translator

class TranslateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='translate', aliases=['tr'], description="Translate text to a different language")
    async def translate_command(self, ctx, *, args):
        args_list = args.split('-to')
        
        text_to_translate = args_list[0].strip()
        target_language = args_list[1].strip() if len(args_list) > 1 else 'en'
        
        translator = Translator()
        translation = translator.translate(text_to_translate, dest=target_language)
        
        await ctx.send(f'Translation from {translation.src} to {translation.dest}:\n```{translation.text}```')

async def setup(bot):
    await bot.add_cog(TranslateCog(bot))