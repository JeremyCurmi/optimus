from discord.channel import DMChannel


def startswith(statement: str) -> str:
    return statement.split(' ')[0]


class Message:
    def __init__(self, message):
        self.msg = message
        self.channel = message.channel
        self.content = message.content
        self.author = message.author.name
        self.is_dm = isinstance(message.channel, DMChannel)
        self.responded = False

    # def respond(func):
    #     if not self.responded:
    #         return func()

    async def greet(self):
        greet_terms = ['Hi', 'Hey']

        def check(msg: str) -> bool:
            if startswith(msg) in greet_terms:
                return True
            return False

        if check(self.content):
            if self.is_dm:
                await self.channel.send(f"Hi, how can I help you?")
            else:
                await self.channel.send(f"Hi {self.author}, how can I help you?")

    async def on_message_logic(self):

        def check(msg):
            return msg.content == 'Jeris is awesome'

        if check(self.msg):
            await self.channel.send(f"yes Jeris is awesome")
        else:
            await self.channel.send(f"I should say something here ...")
