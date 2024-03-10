import discord
from cogs.variables import *
from discord.ext import commands



#comandos de RPC

class _rpc(commands.Cog):
    def __init__(self, witch):
        self.witch = witch

    @commands.command()
    async def rpc(self, ctx, type, rpc):
        if ctx.author.id == ownerid:
            if type == "streaming":
                await ctx.send(f"Status RPC atualizado para **{type}** {rpc}", delete_after=1)
                print("Status RPC atualizado para Transmitindo.")
                await client.change_presence(activity=discord.Streaming(name=f'{rpc}', url='https://www.twitch.tv/mergrow_', status=discord.Status.idle))
            elif type == "playing":
                await client.change_presence(activity=discord.Game(name=f'{rpc}', status=discord.Status.idle))
                await ctx.send(f"Status RPC atualizado para **{type}** {rpc}", delete_after=1)
                print("Status RPC atualizado para Jogando.")
            elif type != "playing" and type != "streaming":
                await ctx.send("Tipo não reconhecido. Use `live` ou `playing`.")    
        else: return await ctx.send("Você não tem permissão para executar este comando!")
                
    @commands.command()
    async def rpc1(self, ctx):
        if ctx.author.id == ownerid:
            await ctx.send('Status RPC atualizado para **Transmitindo** com sucesso!',  delete_after=1)
            print("Status RPC atualizado para Transmitindo.")
            await client.change_presence(activity=discord.Streaming(name='Primeiro Discordbot do Mergrow!', url='https://www.twitch.tv/mergrow_', status=discord.Status.idle))
            time.sleep(3)
            await ctx.message.delete()
        else: return await ctx.send('Você não tem permissão para executar este comando!')
    @commands.command()
    async def rpc2(self, ctx):
        if ctx.author.id == ownerid:
            await ctx.send('Status RPC atualizado para **Jogando** com sucesso!', delete_after=1)
            print("Status RPC atualizado para Jogando.")
            await client.change_presence(activity=discord.Game(name='Primeiro Discordbot do Mergrow!', status=discord.Status.idle))
            time.sleep(3)
            await ctx.message.delete()
        else: return await ctx.send('Você não tem permissão para executar este comando!')


        
async def setup(client):
    await client.add_cog(_rpc(client))