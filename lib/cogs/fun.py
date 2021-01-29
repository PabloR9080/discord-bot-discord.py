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
        await ctx.send(f"Revimsamdo pmapemles dem {ctx.author.mention}")
        await sleep(0.5)
        client = discord.Client()
        channel = discord.utils.get(ctx.guild.channels, id = 712517531000242196)
        VC = discord.utils.get(ctx.guild.channels, id = 768682980033953813)

        print(VC.members)
        for user in VC.members:
            client = discord.Client()
            print(user.name)
            #member = client.get_member(user.id)
            await user.move_to(channel)
            print(f"{user.name} ha sido movido")



    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")

        #await self.bot.stdout.send("Funcion cog lista.")
        #print("fun cog ready")


def setup(bot):
    bot.add_cog(Fun(bot))
