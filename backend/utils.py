import base64
import asyncio

import settings

import discord
from discord.ext import commands

class Utils (commands.Cog):
    def __init__(self, sachs):
        self.sachs = sachs

    @commands.command()
    async def help (ctx, category: str or int = None):
        pages = {
            "utils": 0,
            "fun": 1
        }
        page = 0
        
        if category is not None:
            page = pages[category]

        if settings.EMBED:
            await ctx.message.edit()
        else:
            await ctx.message.edit(content[page])

    @commands.command()
    async def user (self, ctx, user: discord.User):
        await ctx.message.edit(f"""# {user.display_name}
`{user.name}`
        
`ID: {user.id}`
`BOT: {user.bot}`
`CREATED AT: {user.created_at}`
`BANNER/ACCENT COLOR: {user.color}/{user.accent_color}`
`TOKEN: {base64.b64encode(str(user.id).encode("utf-8")).decode("utf-8")[:-2]}`

{user.avatar.url}""")

    @commands.command(aliases=["guild"])
    async def server (self, ctx):
        guild = ctx.guild
        await ctx.message.edit(f"""# {guild.name}
        
`ID: {guild.id}`
`OWNER: {guild.owner_id}`
`CREATED AT: {guild.created_at}`
`MEMBERS: {guild.member_count}`
`ROLES: {len(guild.roles)}`
`CHANNELS: {len(guild.channels)}`
`EMOJIS: {len(guild.emojis)}`

{guild.icon.url}""")

    @commands.command()
    async def block (self, ctx, user: discord.User):
        await self.sachs.block_user(user)
        await ctx.message.edit(f"`Blocked {user.id}`", delete_after=settings.DELETE_AFTER)

    @commands.command()
    async def unblock (self, ctx, user: discord.User):
        await self.sachs.unblock_user(user)
        await ctx.message.edit(f"`Unblocked {user.id}`", delete_after=settings.DELETE_AFTER)

    @commands.command(aliases=["gc"])
    async def groupchat (self, ctx, *, users: discord.User):
        await self.sachs.create_groupchat(users)
        await ctx.message.edit("`Done`", delete_after=settings.DELETE_AFTER)

    @commands.command()
    async def status (self, ctx, type: str, *, name: str):
        if type == "play":
            act = discord.Activity(type=discord.ActivityType.playing, name=name)
        elif type == "stream":
            act = discord.Activity(type=discord.ActivityType.streaming, name=name)
        elif type == "listen":
            act = discord.Activity(type=discord.ActivityType.listening, name=name)
        elif type == "watching":
            act = discord.Activity(type=discord.ActivityType.watching, name=name)

        await self.sachs.change_presence(activity=act)

    @commands.command()
    async def spam (self, ctx, count: int = None, *, text: str):
        await ctx.message.delete()

        if count is None:
            count = 10**10
        
        for i in range(count):
            await ctx.message.send(text)

    @commands.command()
    async def aspam (self, ctx, count: int = None, *, text: str):
        await ctx.message.delete()

        if count is None:
            count = 10**10
        
        for i in range(count // 5):
            tasks = [ctx.send(text) for j in range(5)]
            await asyncio.gather(*tasks)

        tasks = [ctx.send(text) for j in range(count % 5)]
        await asyncio.gather(*tasks)

    @commands.command(aliases=["ip"])
    async def iplookup (self, ctx, ip: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://ip-api.com/json/{ip}") as req:
                response = await req.json()
                await ctx.message.edit(f"""# {ip}
`COUNTRY: {response["country"]}`
`STATE: {response["regionName"]}`
`CITY`: {response["city"]}`
`ZIP: {response["zip"]}`
`CORDS: {response["lat"]}, {response["lon"]}`
`ISP: {response["isp"]}`
`PROXY: {response["proxy"]}`
`MOBILE: {response["mobile"]}`

https://www.google.com/maps/place/{response["lat"]},{response["lon"]}""")

    @commands.command(aliases=["token"])
    async def check_token (self, ctx, token: str):
        for i in ["", "Bot "]:
            headers = {
                "authorization": i + token
            }
            
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get("https://discord.com/api/v9/users/@me") as req:
                    if req.status == 200:
                        ...
                    else:
                        ...

        await ctx.message.edit(f"`{token}` is not a valid token", delete_after=settings.DELETE_AFTER)

async def setup (sachs):
    await sachs.add_cog(Utils(sachs))