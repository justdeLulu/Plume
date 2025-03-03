from bot import Bot
from nextcord import Activity, ActivityType, Embed
from nextcord.ext.commands import Cog
from nextcord.ext import commands

import os
import nextcord

from utilities.reports import reportTalkMistake

class MuzzleModule(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        
        self.muzzledRoleId = 1345605806904574023

    @commands.Cog.listener("on_message")
    async def on_message(self, message: nextcord.Message):
        # Safe Zone guard
        if (message.channel.id in self.bot.safe_channels):
            return
        
        # Is Muzzled
        if (nextcord.utils.get(message.guild.roles, id=self.muzzledRoleId) in message.author.roles):
            count = await self.bot.prisma.talkmistakes.count(where={
                'trigger': 'MUZZLED',
                'user': {
                    'discordId': str(message.author.id),
                }
            })
            
            await reportTalkMistake(prismaClient=self.bot.prisma, discordUserId=message.author.id, trigger="MUZZLED", where=message.channel.id)
            
            embed = Embed(color=nextcord.Colour.dark_red())
            embed.title = "Shuuush!"
            embed.description = "You're actually gag darling, shush act like it, you can't use words like that dear"
        
            embed.add_field(
                name="Nombre d'erreurs commise:",
                value=f":warning: ||**{count}**||"
            )
            
            embed.add_field(
                name="Temps restant:",
                value=f":sparkling_heart: ||Owner decide.||"
            )
            
            embed.add_field(
                name="Message:",
                value=f":envelope: ||{message.content}||",
                inline=False
            )
            
            await message.delete()
            await message.channel.send(embed=embed)

def setup(bot: Bot):
    bot.add_cog(MuzzleModule(bot))
