import base64

import discord
from discord.ext import commands

class Utils (commands.Cog):
    def __init__(self, sachs):
        self.sachs = sachs

    @commands.command()
    async def user (self, ctx, user: discord.User):
        await ctx.message.edit(f"""```{user.name} ({user.display_name})
        
ID: {user.id}
BOT: {user.bot}
CREATED AT: {user.created_at}
BANNER/ACCENT COLOR: {user.color}/{user.accent_color}
TOKEN: {base64.b64encode(str(user.id).encode("utf-8")).decode("utf-8")[:-2]}
```
{user.avatar.url}""")

    @commands.command(aliases=["guild"])
    async def server (self, ctx):
        guild = ctx.guild
        await ctx.message.edit(f"""```{guild.name}
        
ID: {guild.id}
OWNER: {guild.owner_id}
CREATED AT: {guild.created_at}
MEMBERS: {guild.member_count}
ROLES: {len(guild.roles)}
CHANNELS: {len(guild.channels)}
EMOJIS: {len(guild.emojis)}
```
{guild.icon.url}""")

    @commands.command()
    async def block (self, ctx, user: discord.User):
        await self.sachs.block_user(user)
        await ctx.message.edit(f"`Blocked {user.id}`")

    @commands.command()
    async def unblock (self, ctx, user: discord.User):
        await self.sachs.unblock_user(user)
        await ctx.message.edit(f"`Unblocked {user.id}`")

    @commands.command(aliases=["gc"])
    async def groupchat (self, ctx, *, users: discord.User):
        await self.sachs.create_groupchat(users)

async def setup (sachs):
    await sachs.add_cog(Utils(sachs))