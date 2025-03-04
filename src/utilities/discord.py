from nextcord import Interaction, Embed, Color


async def sendSuccessMessage(
    interaction: Interaction, message: str, ephemeral: bool = True
):
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
    await interaction.send(embed=embed, ephemeral=ephemeral)
