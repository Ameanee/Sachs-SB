import aiohttp

import discord
from discord.ext import commands

class Fun (commands.Cog):
    def __init__(self, sachs):
        self.sachs = sachs

    @commands.command()
    async def ask_ai (self, ctx, *, question: str):
        async with aiohttp.ClientSession() as session:
            async with session.post("https://ai-api.replit.app/api/v1/chat", json={
                "message": question,
                "session_id": self.sachs.id
            }) as req:
                response = await req.json()
                await ctx.message.reply(f"`{response['message']}`")