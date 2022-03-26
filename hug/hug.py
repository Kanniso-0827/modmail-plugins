import logging
from enum import Enum
from random import randint, choice
import discord
from discord.ext import commands
from core import checks
import box
import json
import string
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)

logger = logging.getLogger("Modmail")


class Hug(Cog):
    """
    Commands
    """

    image = [
           "https://images-ext-1.discordapp.net/external/jwF714rmMQCNUy_uhW2dp_ot2TJ3SNdAmHdPRvKSH80/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/Veq4zvSQkdAAAAPo/hugmati.mp4",
    ]

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        # self.db = bot.plugin_db.get_partition(self)

    @commands.command(name="hug", aliases=["huh"])
    async def _gaytime(self, ctx):
        """
        Hug Gifs
        """
        embed = discord.Embed(color=15383739)
        embed.set_image(url=choice(self.image))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Hug(bot))
