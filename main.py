import src.config as config
from src.api.discord import bot


def main():
    bot_settings = config.BotSettings()
    bot.start_discord_client(bot_settings)


if __name__ == "__main__":
    main()
