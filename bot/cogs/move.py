from cogs.variables import *


class _move(commands.Cog): 
    def __init__(self, witch):
        self.witch = witch
    @commands.command()
    async def move(self, ctx, member: discord.Member, *, channel_name):
        if member.voice is None:
            # Se nao estiver conectado ao canal de voz envia essa mensagem.
            return await ctx.send('O usuários precisa estar em um canal de voz!')

        channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name) #Define o channel com base na busca dos nomes de canais
        if channel is None:
            return await ctx.send('Canal inválido!') #retorna a mensagem de canal inválido caso o canal não seja encontrado.
        
        # move o usuario
        await member.move_to(channel)



async def setup(client):
    await client.add_cog(_move(client))