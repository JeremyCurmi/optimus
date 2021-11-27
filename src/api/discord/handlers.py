from typing import Any


def extract_username_from_name(username: str) -> str:
    """
    param: discord username with id
    return: stringified message error, with id removed
    """
    return username.split('#')[0]


def get_message_author(message: Any) -> str:
    """
    param: discord message
    return: stringified message error, with id removed
    """
    return extract_username_from_name(str(message.author))
