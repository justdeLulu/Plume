from nextcord import Interaction, Embed, Color

async def buildTalkMistakeEmbed(trigger: str, userId: str):
    """|coro|
    
    Send a success message to an interaction

    Parameters
    ----------
    interaction: :class:Interaction
        The interaction to respond to
    message: :class:`str`
        The message to send
    ephemeral: :class:`bool`
        If the response is only visible to the user, by default True
    """
    embed = Embed(description=f"**Success**: {message}", color=Color.green())
    
    embed.set_author("LANA")
    
    embed.add_field("Déclenchement:", "**Talk Error**")
    embed.add_field("Déclenchement:", "**Talk Error**")
    
    embed.set_footer("**L**earning **A**ssistive **N**euronnal **A**pplication")
    return embed