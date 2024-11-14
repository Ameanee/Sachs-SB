import aiohttp

import discord
from discord.ext import commands

class Fun (commands.Cog):
    def __init__(self, sachs):
        self.sachs = sachs

    @commands.command()
    async def ask_ai (self, ctx, *, question: str): # broken for now
        async with aiohttp.ClientSession() as session:
            async with session.post("https://ai-api.replit.app/api/v1/chat", json={
                "message": question,
                "session_id": self.sachs.user.id
            }) as req:
                response = await req.json()
                await ctx.message.reply(f"`{response['message']}`")

async def setup (sachs):
    await sachs.add_cog(Fun(sachs))