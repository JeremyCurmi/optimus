import discord
from discord.channel import DMChannel
from discord.ext.commands import Bot
from .handlers import run_encouragement
from .message import Message


def new_discord_client():
    return discord.Client()


def new_discord_bot(command_prefix):
    return Bot(command_prefix=command_prefix)


def is_bot_the_author(bot: Bot, ctx) -> bool:
    return ctx.author == bot.user


def should_bot_activate(bot: Bot, ctx) -> bool:
    is_bot_mentioned = bot.user.mentioned_in(ctx)
    is_dm = isinstance(ctx.channel, DMChannel)

    if is_bot_the_author(bot, ctx):
        return False
    else:
        return is_bot_mentioned or is_dm


def start_discord_client(settings):
    bot = new_discord_bot(settings.command_prefix)

    @bot.event
    async def on_ready():
        print("I'm in as", bot.user.name)
        run_encouragement(bot, settings.general_id)

    @bot.event
    async def on_message(ctx):
        print(ctx.author, ctx.content, ctx.channel)
        if should_bot_activate(bot, ctx):
            msg = Message(ctx)

            await msg.greet()

            await msg.message_ai()
        elif not is_bot_the_author(bot, ctx):
            # print("I could log this information to improve myself ...",
            #       ctx.author, ctx.content, ctx.channel)
            pass

    bot.run(settings.token)
