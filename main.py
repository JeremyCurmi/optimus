import src.config as config
from src.api import discord


def main():
    bot_settings = config.BotSettings()
    discord.start_discord_client(bot_settings)


if __name__ == "__main__":
    main()
