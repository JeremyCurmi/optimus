from typing import Any
from discord.ext import tasks, commands
from src.api import jobs


def run_encouragement(bot: commands.Bot, channel_id: int):
    @tasks.loop(hours=2)
    async def run():
        await bot.wait_until_ready()
        channel = bot.get_channel(channel_id)
        await channel.send(jobs.get_encouraging_quote())
    run.start()
