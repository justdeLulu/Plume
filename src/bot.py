import logging

from nextcord import Embed, ApplicationInvokeError, Forbidden, Interaction, DiscordServerError, Color
from nextcord.ext.commands import Bot as NextcordBot
from datetime import datetime
from prisma import Prisma

from utilities.logger import Logger

class Bot(NextcordBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.initialised = False
        self.logger = Logger("bot", "logs/bot.log", print_level=logging.DEBUG)
        self.loaded_cogs: dict[str, int] = {} # {cog path: last modified time}

        self.subject_id = 939288874281222225
        self.log_channel = 1344820579626258464
        self.safe_channels = [1344815506917560330]
        self.prisma = Prisma()
        
    # Prevents errors from being printed twice
    async def on_application_command_error(self, interaction: Interaction, error: ApplicationInvokeError):
        pass

    async def handle_interaction_error(self, interaction: Interaction, exception: Exception):
        if isinstance(exception, Forbidden):
            embed = Embed(title="**Erreur de permissions**", description="I don't have the necessary permissions to perform this action", color=Color.red())
            await interaction.send(embed=embed, ephemeral=True)
            
        else:
            self.logger.error("An unexpected error occured")
            self.logger.error(interaction.user, f"({interaction.user.id})")
            self.logger.exception(exception)
            
            embed = Embed(title="An unexpected error occured", color=Color.red(), timestamp=datetime.now())
            await interaction.send(embed=embed, ephemeral=True)
            
    async def handle_task_error(self, exception: Exception, task: str):
        if not isinstance(exception, DiscordServerError):
            self.logger.error(f"An unexpected error occured in task `{task}`")
            self.logger.exception(exception)

    
    
    
    