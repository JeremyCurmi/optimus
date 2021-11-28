from typing import Tuple
from src.api import models


def return_command_type_if_given_command(msg: str) -> Tuple[bool, str]:
    is_voice_command = True
    for cmd in models.command_terms:
        if cmd in msg:
            return not is_voice_command, cmd

    for voice_cmd, cmd in models.voice_command_terms.items():
        if voice_cmd in msg:
            return is_voice_command, cmd
