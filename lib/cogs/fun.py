from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.utils import get
import discord
from random import choice
from asyncio import sleep
from discord import File

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
        message = await ctx.send(f"{choice(('👻','El niño'))}")
        await message.add_reaction('👻')


    @command(name="cake", aliases=["keki","caking","caker","quake"])
    async def cake(self,ctx):
        message = await ctx.send(f"yui cake 🙄")
        await message.add_reaction('💩')
        await message.add_reaction('🇨')
        await message.add_reaction('🅰️')
        await message.add_reaction('🇰')
        await message.add_reaction('🇪')

    @command(name="ana", aliases=["ano"])
    async def ana(self,ctx):
        message = await ctx.send(f"{choice(('https://tenor.com/view/ana-beaver-tp-gif-18732481','https://tenor.com/view/tp-teleperformance-ana-sheldon-bigbang-theory-gif-18986132'))}")

    @command(name="ctm", aliases=["chingatumadre"])
    async def ctm(self,ctx):
        message = await ctx.send(f"Chinga tu madre {choice(('celia','apokinto','babi','pablo','tosino','sislia','el infante'))}")
        await message.add_reaction('🇨')
        await message.add_reaction('🇹')
        await message.add_reaction('〽️')

    @command(name="babo", aliases=["babañin"])
    async def babo(self,ctx):
        channel = ctx.channel
        await channel.send(file=File("lib/img/babo.jpeg"))
        pass


    @command(name="pantoja", aliases=["pantoj","pantojita","panj","breadj","panjoto","panjot","panjota","🍞J","🍞j"])
    async def roll(self,ctx):
        message = await ctx.send(f"https://tenor.com/view/mairena-pantoja-polla-carmen-gif-11612945")





    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

        #await self.bot.stdout.send("Funcion cog lista.")
        #print("fun cog ready")


def setup(bot):
    bot.add_cog(Fun(bot))
