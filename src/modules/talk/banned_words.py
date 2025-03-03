from configuration import *
from bot import Bot
from nextcord.ext.commands import Cog
from nextcord.ext import commands
from nextcord import Interaction, slash_command, SlashOption, Embed

from prisma.models import BannedWords

import asyncio
import nextcord

class BannedWords(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        
        self.bannedWords = []
        
        self.bot.loop.create_task(self.initializeWords())
      
    """
        Initialize Banned Words/Expressions
    """  
    async def initializeWords(self):
        self.bot.logger.info('Loading Words...')
        
        if (len(self.bannedWords) == 0):
            await asyncio.sleep(2)
        
        self.bannedWords = await self.bot.prisma.bannedwords.find_many(where={
            'active': True,
        })
        
        self.bot.logger.info(f"Loaded {len(self.bannedWords)} banned expressions successfully!")
        
    @slash_command(
        name="banword",
        description="[TalkModule] Commandes pour les Mots Bannis",
        guild_ids=GUILD_IDS
    )
    async def main(self, interaction: Interaction):
        pass

    @main.subcommand(
        name="list",
        description="List des Expressions Bannis."
    )
    async def list(self, interaction: Interaction):
        await interaction.send("HIHI. Decouvre les mots pour debloquer ce module.")
    
    @main.subcommand(
        name="add",
        description="Bannis un Mots/Expressions",
    )
    async def add(
        self, 
        interaction: Interaction,
        name: str = SlashOption(
          name="name",
          description="Nom de l'Expression.",
          required=True  
        ),
        trigger: str = SlashOption(
          name="trigger",
          description="Expression interdites",
          required=True  
        ),
        active: bool = SlashOption(
            name="active",
            description="Active?",
            default="Oui",
            choices=["Oui", "Non"],
            required=True
        ),
        description: str = SlashOption(
          name="description",
          description="Commentaires..",
          required=False
        ),
    ):
        await interaction.response.defer()

        await self.bot.prisma.bannedwords.create(
            data={
                'name': name,
                'trigger': trigger,
                'active': active,
                'description': "Default Description"
            }
        )
        
        self.bot.logger.info(f"Successfully banned the use of '{trigger}'.")
        
        embed = Embed(title="BannedWords!")

        embed.add_field(
            name="Nom",
            value=f":sparkling_heart: {name}"
        )
        
        embed.add_field(
            name="Trigger",
            value=f"||{trigger}||"
        )
        
        await interaction.followup.send(content=f"Trigger `{trigger}` ajouter! Reloading Banned Words...", embed=embed)
        
        await self.initializeWords()
        await interaction.followup.send(content=f"Banned Words reloaded!", delete_after=5)
        
        
        pass
        
    @main.subcommand(
        name="toggle",
        description="Active/Desactive une Expression bannis."
    )
    async def toggle(self, interaction: Interaction):
        pass
        
    @main.subcommand(
        name="secret",
        description="Oui. Oui. Oui."
    )
    async def secret(self, interaction: Interaction):
        await interaction.send("aie... pourquoi? la curiosité.. un vilain défaut..")
        
    @commands.Cog.listener("on_message")
    async def on_message(self, message: nextcord.Message):
        # Safe Zone guard
        if (message.channel.id in self.bot.safe_channels):
            return
        
        return
        
        # Subject?
        if message.author.id != self.bot.subject_id:
            words: list[str] = message.content.lower().split(' ');
            
            for item in self.bannedWords:
                if (item.trigger.lower() in words):
                    await self.bot.get_channel(self.bot.log_channel).send(f"Utilisateur {message.author.display_name} \nMessage utiliser: {message.content} \n Trigger: {item.trigger}")
                    await message.delete()
                    await message.channel.send(embed=nextcord.Embed(
                        color=15794176,
                        title="Expression Interdite!",
                        description="Cette expression est Interdite pour vous. Ne recommence pas sous peine de sanctions.",
                    ))
                    return 

def setup(bot: Bot):
    bot.add_cog(BannedWords(bot))
