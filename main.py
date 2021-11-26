import src.config as config
from src.api import discord


def main():
    discord.start_discord_client(config.token)


if __name__ == "__main__":
    main()
