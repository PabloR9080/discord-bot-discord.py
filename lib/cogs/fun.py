from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.utils import get
import discord
from random import choice
from asyncio import sleep

class Fun(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="XD", aliases=["xd","Xd","xD"])
    async def XD(self,ctx):
        await ctx.send(f"XD cmamo {choice(('elpapu','lamamu','elprro'))} {ctx.author.mention} :v")

    @command(name="aduana")
    async def aduana(self,ctx):

        await sleep(0.5)
        client = discord.Client()
        channel = discord.utils.get(ctx.guild.channels, id = 712517531000242196)
        VC = discord.utils.get(ctx.guild.channels, id = 768682980033953813)

        print(VC.members)
        for user in VC.members:
            client = discord.Client()
            print(user.name)

            if ctx.author.id == user.id:
                await ctx.send(f"Revimsamdo pmapemles dem {ctx.author.mention}")
                await sleep(2)
                await user.move_to(channel)
                print(f"{user.name} ha sido movido")
            elif user.Name is None:
                await ctx.send(f"No hay naiden en aduan")
            else:
                await ctx.send(f"Nosepuede :'v ")

    @command(name="babi", aliases=["baby"])
    async def babi(self,ctx):
        await ctx.send(f"Baby, ya estoy cansado de tu bipolaridad, yah-yah-yeh\n"+
                        "Deja ya de estar peleando sin una necesidad\n"+
                        "Valórame, bebé, yo\n"+
                        "Con ese humor nadie te aguantará\n"+
                        "¿Quién te entiende? Si conmigo no te falta na'\n"+
                        "Cógela suave, ma', porque esta bomba explotará\n"+
                        "Si te saco el genio no vuelvo a frotar tu lámpara\n"+
                        "Y listo, te dejé en visto\n"+
                        "Pero fue porque estaba grabando mi disco\n"+
                        "Y tú pensando que yo estaba en la disco\n"+
                        "Deja de pelear, que la pasamos más rico")

    @command(name="noelle", aliases=["keqing","qiqi"])
    async def noelle(self,ctx):
        await ctx.send(f"{choice(('noelle','keqing','qiqi'))} le {choice(('gana','wins','pierde'))} Bv")

    @command(name="lenin", aliases=["Lenin"])
    async def lenin(self,ctx):
        message = await ctx.send(f"👻")
        await message.add_reaction('👻')
    @command(name="cake", aliases=["keki","caking","caker","quake"])
    async def lenin(self,ctx):
        message = await ctx.send(f"yui cake 🙄")
        await message.add_reaction('💩')
        await message.add_reaction('🇨')
        await message.add_reaction('🅰️')
        await message.add_reaction('🇰')
        await message.add_reaction('🇪')


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

        #await self.bot.stdout.send("Funcion cog lista.")
        #print("fun cog ready")


def setup(bot):
    bot.add_cog(Fun(bot))
