import os
from dotenv import load_dotenv

load_dotenv()


class BotSettings:
    def __init__(self):
        self.token = os.getenv("DISCORD_BOT_SECRET")

        # channel IDs
        self.general_id = 913537728682004543

        # bot settings
        self.command_prefix = ''
