import configuration as _config
import os as _os

def file_to_module(root: str, filepath: str) -> str:
    """Converts a filepath to a module path
    
    Parameters
    ----------
    root: :class:`str`
        The root directory
    filepath: :class:`str`
        The filepath to convert
        
    Returns
    -------
    :class:`str`
        The module path
    """
    return _os.path.join(root, filepath).removesuffix(".py").replace("\\", ".").replace("/", ".")


def module_to_file(filepath: str) -> str:
    """Converts a module path to a filepath
    
    Parameters
    ----------
    filepath: :class:`str`
        The module path to convert
        
    Returns
    -------
    :class:`str`
        The filepath
    """
    return filepath.replace(".", _os.sep) + ".py"


def get_cogs():
    """Returns a set of all the cogs
    
    Returns
    -------
    :class:`set`
        The set of all the cogs
    """
    cogs = set()
    for cogDirectory in _config.COGS_DIRS:
        for root, dirs, files in _os.walk(cogDirectory):
            if not root.startswith("__"):
                for file in files:
                    if file.endswith(".py") and file not in _config.LOAD_EXCEPTIONS:
                        cogs.add(file_to_module(root, file))

    return cogs