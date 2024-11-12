import settings

import os
from colorama import Fore

import discord
from discord.ext import commands

Sachs = commands.Bot(
    command_prefix=settings.PREFIX,
    help_command=None
)

@Sachs.event
async def on_ready():
    for file in os.listdir("./backend"):
        if file.endswith(".py"):
            await Sachs.load_extension(f"backend.{file[:-3]}")

    os.system("clear")

    print(f"""
     ______     ______     ______     __  __     ______    
    /\  ___\   /\  __ \   /\  ___\   /\ \_\ \   /\  ___\   
    \ \___  \  \ \  __ \  \ \ \____  \ \  __ \  \ \___  \  
     \/\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
      \/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/ 
    Logged in as {Sachs.user}""")

Sachs.run(settings.TOKEN)