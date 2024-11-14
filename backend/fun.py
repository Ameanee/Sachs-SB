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

    @commands.command()
    async def cat (self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as req:
                response = await req.json()
                await ctx.message.reply(response[0]["url"])

    @commands.command()
    async def dog (self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as req:
                response = await req.json()
                await ctx.message.reply(response["message"])

async def setup (sachs):
    await sachs.add_cog(Fun(sachs))