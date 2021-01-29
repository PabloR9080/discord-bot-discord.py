from discord import Intents
from asyncio import sleep
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from glob import glob


PREFIX= "!"
OWNER_IDS = [270292360334802954]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]


class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self,cog):
        setattr(self, cog, True)
        print(f"{cog} cog ready")
    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
        def __init__(self):
            self.PREFIX = PREFIX

            self.ready = False
            self.cogs_ready = Ready()
            self.guild = None
            #No pressence intents:
            # intents = Intents.default()
            # intents.members = True
            super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents= Intents.all())

        def setup(self):
            for cog in COGS:
                self.load_extension(f"lib.cogs.{cog}")
                print(f" {cog} cog loaded")

            print("setup complete")


        def run(self, version):
            self.VERSION = version

            print("running setup...")
            self.setup()

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
                await args[0].send("Amlgom samlió maml.")

            await self.stdout.send("Ha omcumrrimdo umn emrror")
            raise

        async def on_command_error(self, ctx, exc):
            if isinstance(exc, CommandNotFound):
                await ctx.send("Comamndo no emnkomntrado")
            elif hasattr(exc, "original"):
                raise exc.original
            else:
                raise exc

        async def on_ready(self):
            if not self.ready:

                self.stdout = self.get_channel(776343201102430238)
                #self.guild = self.get_guild(642214035550502919)
                print("bot ready")
                channel = self.get_channel(776343201102430238)

                while not self.cogs_ready.all_ready():
                    await sleep(0.5)

                self.ready = True
                #await self.stdout.send("XD ola")

            else:
                print("bot reconnected")


        async def on_message(self, message):
            if not message.author.bot:
                await self.process_commands(message)

bot = Bot()
