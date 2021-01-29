from discord import Intents
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

PREFIX= "!"
OWNER_IDS = [270292360334802954]

class Bot(BotBase):
        def __init__(self):
            self.PREFIX = PREFIX
            self.guild = None
            self.ready = False

            #No pressence intents:
            # intents = Intents.default()
            # intents.members = True
            super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents= Intents.all())

        def run(self, version):
            self.VERSION = version
            with open("lib/bot/token.0","r",encoding="utf-8") as tf:
                self.TOKEN = tf.read()
                print("running bot...")
                super().run(self.TOKEN, reconnect=True)


        async def on_connect(self):
            print("bot connected")


        async def on_disconnect(self):
            print("bot disconnected")

        async def on_error(self, err, *args, **kwargs):
            if err == "on_command_error":
                await args[0].send("Algo salió mal.")
            raise

        async def on_command_error(self, ctx, exc):
            if isinstance(exc, CommandNotFound):
                await ctx.send("Cmamo el prro")
            elif hasattr(exc, "original"):
                raise exc.original
            else:
                raise exc

        async def on_ready(self):
            if not self.ready:
                self.ready = True
                #self.guild = self.get_guild(642214035550502919)
                print("bot ready")
                channel = self.get_channel(776343201102430238)
                await channel.send("XD ola")

            else:
                print("bot reconnected")


        async def on_message(self, message):
            pass

bot = Bot()
