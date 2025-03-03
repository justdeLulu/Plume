from config import *
from utils import *
from bot import Bot
from nextcord import Activity, ActivityType
from nextcord.ext.commands import Cog
from nextcord.ext import commands

import os
import nextcord

restrictedChannels = [1345388718495764550, 1345388949899837501, 1344828391160807476, 1344828493342441565]
adminRoleId: int = 1345532797082664960
reportChannel: int = 1344820579626258464

class PowerRoles(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        
        self.retries = 0

    @commands.Cog.listener("on_message")
    async def on_message(self, message: nextcord.Message):
        if (message.author.id == SUBJECT_ID and self.retries > 3):
            await message.delete()
            await message.channel.send(embed=nextcord.Embed(
                    color=15794176,
                    title="Ferme la, t'as plus le droit Chienne!",
                    description="T'as trop parler quand t'avais pas le droit t'as perdu le droit jusqu'a nouvel ordre.",
                ))
            return 
        
        if (message.channel.id in restrictedChannels and message.author.id == SUBJECT_ID):
            if (nextcord.utils.get(message.guild.roles, id=adminRoleId) not in message.author.roles):
                self.retries += 1
                await self.bot.get_channel(1345531191029137480).send(f"Elle n'est pas a sa place...\n Message: ```{message.content}```")
                await message.delete()
                await message.channel.send(embed=nextcord.Embed(
                    color=15794176,
                    title="Ferme la, t'as plus le droit Chienne!",
                    description="C'est finis l'amusement, coucouche panier. A la niche. Et vite.",
                ))

def setup(bot: Bot):
    bot.add_cog(PowerRoles(bot))
