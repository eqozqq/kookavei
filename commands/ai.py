import discord
from discord.ext import commands
import requests

class AICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ai', description="Generate text using AI")
    async def ai_command(self, ctx, *, msg):
        URL = "https://www.llama2.ai/api"

        async with ctx.typing():
            response_msg = await ctx.reply("**Generating a response...**\nGeneration time depends on the length of the response.")

            resp = requests.post(URL, json={
                "prompt": f"<s> [INST] {msg} [/INST]",
                "model": "meta/llama-2-70b-chat",
                "systemPrompt": "You are a helpful assistant.",
                "temperature": 0.75,
                "topP": 0.9,
                "maxTokens": 800,
                "image": None,
                "audio": None
            })

        response_text = resp.text[:1996] + "..." if len(resp.text) > 2000 else resp.text

        await response_msg.edit(content=f"Response from AI:\n```{response_text}```\n **Answers may be incorrect and contain errors.**")

async def setup(bot):
    await bot.add_cog(AICog(bot))
