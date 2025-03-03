from nextcord import Interaction, Embed, Color
from prisma import Prisma

async def reportTalkMistake(
    prismaClient: Prisma,
    discordUserId: int,
    trigger: str,
    where: int
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

    user = await prismaClient.user.find_first(where={
        'discordId': str(discordUserId)
    })
    
    await prismaClient.talkmistakes.create(
        data={
            'userId': user.id,
            'trigger': trigger,
            'where': str(where),
        }
    )
    
    print('Saved data.')