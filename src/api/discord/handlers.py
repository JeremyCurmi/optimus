from typing import Any


def get_message_author(message: Any) -> str:
    """
    param: discord message
    return: stringified message error, with id removed
    """
    return str(message.author).split('#')[0]
