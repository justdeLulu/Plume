from configuration import GUILD_IDS
from bot import Bot
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Cog

class PingCommand(Cog):
    
    def __init__(self, bot: Bot):
        self.bot = bot

    @slash_command(
        name="ping",
        description="Pong",
        guild_ids=GUILD_IDS, 
        force_global=True
    )
    async def ping(self, interaction: Interaction):
        await interaction.send(f"Pong! {self.bot.latency * 1000:.2f}ms")

def setup(bot: Bot):
    bot.add_cog(PingCommand(bot))