import settings

import os
import aiohttp
from colorama import Fore

from discord.ext import commands

sachs = commands.Bot(
    command_prefix=settings.PREFIX,
    help_command=None,
    self_bot=True
)


@sachs.event
async def on_ready():
    for file in os.listdir("./backend"):
        if file.endswith(".py"):
            await sachs.load_extension(f"backend.{file[:-3]}")

    async with aiohttp.ClientSession() as session:
        await session.delete("https://ai-api.replit.app/api/v1/session", json={"session_id": sachs.user.id})
        await session.post("https://ai-api.replit.app/api/v1/session", json={"session_id": sachs.user.id, "context": "You are my personal assitant"})

sachs.run(settings.TOKEN)