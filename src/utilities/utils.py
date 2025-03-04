import traceback as _traceback


def get_traceback(exception: Exception) -> str:
    """Returns the traceback string from an exception

    Parameters
    ----------
    exception: :class:`Exception`
        The exception to get the traceback from

    Returns
    -------
    :class:`str`
        The traceback of the exception
    """
    return "".join(
        _traceback.format_exception(
            exception.__class__, exception, exception.__traceback__
        )
    )


def get_command(data: dict) -> str:
    """Returns the command string from a slash command data

    Parameters
    ----------
    data: :class:`dict`
        The data of the slash command, from :attr:`Interaction.data`

    Returns
    -------
    :class:`str`
        The command string
    """
    res = data.get("name", "")
    if "options" in data:
        for option in data["options"]:
            res += " " + get_command(option)
    if "value" in data:
        res += ":" + str(data["value"])
    return res
