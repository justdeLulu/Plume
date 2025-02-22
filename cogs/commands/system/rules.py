from config import *
from views import *
from bot import Bot
from nextcord import Interaction, Embed, slash_command
from nextcord.ext.commands import Cog
from views.page_buttons import PageButtons

import prisma

def buildRuleEmbed(rule: prisma.models.Rule):
    return Embed(
        title=rule.name,
        description=rule.description
    )
        
class RulesCommand(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @slash_command(description="Rules", guild_ids=GUILD_IDS)
    async def rules(self, interaction: Interaction):
        rules = await self.bot.prisma.rule.find_many(
            where={
              'active': True,  
            },
            order={
                'power': 'asc'
            }
        )
        print(rules)
        
        
        # Create a list of embeds
        embeds = list(map(buildRuleEmbed, rules))
        
        # Initialize the view
        view = PageButtons(self.bot, embeds)
        
        # Send a message with the first embed and attach the view
        await interaction.send(embed=embeds[0], view=view, ephemeral=False)


def setup(bot: Bot):
    bot.add_cog(RulesCommand(bot))