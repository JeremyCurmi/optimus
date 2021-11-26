import discord


def new_discord_client():
    return discord.Client()


def start_discord_client(token: str):
    client = new_discord_client()

    @client.event
    async def on_ready():
        print("I'm in as ", client.user)

    @client.event
    async def on_message(message):
        if message.author != client.user:
            await message.channel.send("Jeris ghandu ragun!")

    client.run(token)
