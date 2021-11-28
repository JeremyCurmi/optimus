from typing import Tuple
from src.api import models


def check_is_command(msg: str) -> Tuple[bool, str]:
    for cmd in models.command_terms.keys():
        if cmd in msg:
            return True
    return False


def select_command_type(msg: str) -> Tuple[bool, str]:
    is_voice_command = True
    for term, cmd in models.command_terms.items():
        if term in msg:
            if '$' in term:
                return not is_voice_command, cmd
            else:
                return is_voice_command, cmd


def process_command(msg: str):
    print("command processing ...")
    is_voice_command, command_type = select_command_type(msg)
    print(is_voice_command, command_type)
