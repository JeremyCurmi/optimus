from discord.channel import DMChannel
from .. import models
from . import commands


def startswith(statement: str) -> str:
    first_word = statement.split(' ')[0]
    if first_word.lower() in models.multiple_word_greeting_terms_first_word:
        return ' '.join(statement.split(' ')[:2])
    return first_word


class Message:
    def __init__(self, message):
        self.msg = message
        self.channel = message.channel
        self.content = message.content
        self.author = message.author.name
        self.is_dm = isinstance(message.channel, DMChannel)
        self.responded = False

    def respond(func):
        """
        link: https://stackoverflow.com/questions/1263451/python-decorators-in-classes
        this is a decorator with the purpose of blocking bot responding functions from running after the bot has responded once
        """
        async def self_wrapper(*args):
            self = args[0]
            if not self.responded:
                self.responded = True
                await func(*args)
        return self_wrapper

    @respond
    async def greet(self) -> bool:

        def check(msg: str) -> bool:
            if startswith(msg).lower() in models.greeting_terms:
                return True
            return False

        if check(self.content):
            if self.is_dm:
                await self.channel.send(f"Hi, how can I help you?")
            else:
                await self.channel.send(f"Hi {self.author}, how can I help you?")
        else:
            self.responded = False

    @respond
    async def message_ai(self):

        if commands.check_is_command(self.content):
            commands.process_command(self.content)
        else:
            await self.channel.send(f"I should say something here ...")
