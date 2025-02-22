from config import *
from utils import *
from bot import Bot
from nextcord.ext.commands import Cog
from nextcord.ext import commands

class OnMessageEdit(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener("on_message_edit")
    async def on_message_edit(self, before, after):
        if before.author.id == SUBJECT_ID:
            msg = f"**{before.author.id}** edited their message:\n{before.content} -> {after.content}"
            await before.channel.send(msg)

def setup(bot: Bot):
    bot.add_cog(OnMessageEdit(bot))
