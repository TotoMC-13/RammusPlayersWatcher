# DISCORD IMPORTS
import discord
from discord.ext import commands

# AIOHTTP IMPORTS
import aiohttp

# OS AND PATHLIB IMPORTS
import os
from dotenv import load_dotenv
from pathlib import Path


class client(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        super().__init__(
            command_prefix=".",
            intents=intents,
            application_id=os.getenv("BOT_ID"),
        )
        self.synced = False

    async def setup_hook(self) -> None:

        self.session = aiohttp.ClientSession()

        target_dir = Path.cwd() / "cogs"

        for cog in target_dir.rglob("*.py"):
            await self.load_extension(f"cogs.{cog.stem}")

        await cltree.sync()
        self.synced = True
        print("All commands are now synced.")

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID:{self.user.id})")
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"Jugadores de Rammus (Subhumanos)",
            ),
        )


aclient = client()
cltree = aclient.tree

load_dotenv()
aclient.run(os.getenv("TOKEN"))
