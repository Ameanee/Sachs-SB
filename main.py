import settings

import os
import aiohttp
from colorama import Fore

import discord
from discord.ext import commands

sachs = commands.Bot(
    command_prefix=settings.PREFIX,
    help_command=None
)

@sachs.event
async def on_ready():
    for file in os.listdir("./backend"):
        if file.endswith(".py"):
            await sachs.load_extension(f"backend.{file[:-3]}")

    async with aiohttp.ClientSession() as session:
        await session.delete("https://ai-api.replit.app/api/v1/session", json={"session_id": sachs.user.id})
        await session.post("https://ai-api.replit.app/api/v1/session", json={"session_id": sachs.user.id})

    os.system("clear")

    print(f"""
     ______     ______     ______     __  __     ______    
    /\  ___\   /\  __ \   /\  ___\   /\ \_\ \   /\  ___\   
    \ \___  \  \ \  __ \  \ \ \____  \ \  __ \  \ \___  \  
     \/\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
      \/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/ 
    Logged in as {sachs.user}""")

sachs.run(settings.TOKEN)