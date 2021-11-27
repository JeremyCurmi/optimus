import discord
from .handlers import get_message_author


def new_discord_client():
    return discord.Client()


def start_discord_client(token: str):
    client = new_discord_client()

    @client.event
    async def on_ready():
        print("I'm in as", client.user)

    @client.event
    async def on_message(message):
        channel = message.channel
        author = get_message_author(message)

        if message.author != client.user:
            if message.content.startswith('Hi'):
                await channel.send(f"Hi {author}")

            await channel.send(f"I should say something here ...")

    client.run(token)
