from cogs.variables import *

class _wakeup(commands.Cog):
    def __init__(self, witch):
        self.witch = witch
    #Wakeup move o usuário entre dois canais.
    @commands.command(aliases=['saco'])
    @commands.has_role('woken')
    async def wakeup(self, ctx, member: discord.Member, channel1, channel2 ):
        if member.voice is None:
            return await ctx.send('O usuário precisa estar um canal de voz!')
        if member._user.id == ownerid:
            return await ctx.send('Meu mestre não pode ser acordado! ')


        channel1 = client.get_channel(int(channel1)) #converte o valor string para inteiro e define o id dos canais do wakup (channel1)
        channel2 = client.get_channel(int(channel2)) #converte o valor string para inteiro e define o id dos canais do wakup (channel2)
        if channel1 is None:                         #Checa se o argumento channel1 existe e retorna um erro se não existir
            await ctx.send('Canal.ID1 inválido!')   
        elif channel2 is None:                      #Checa se o argumento channel2 existe e retorna um erro se não existir
            await ctx.send('Canal.ID2 inválido!')
        else:

            channel_return = client.get_channel(member.voice.channel.id) #obtem o canal origem do usuário alvo, então converte para dado tipo ID.
            await ctx.send(f'{member} ACORDA!!!!')
            await member.move_to(channel1)                               #move o usuário entre os carais channel1 e channel2
            time.sleep(0.1)
            await member.move_to(channel2)
            time.sleep(0.1)
            await member.move_to(channel1)
            time.sleep(0.1)
            await member.move_to(channel2)
            time.sleep(0.1)
            await member.move_to(channel1)
            time.sleep(0.1)
            await member.move_to(channel2)
            time.sleep(0.1)
            await member.move_to(channel1)
            time.sleep(0.1)
            await member.move_to(channel2)
            time.sleep(0.1)
            await member.move_to(channel_return) #volta para o canal origem.
    @wakeup.error #checa se não estão faltando argumentos no comando wakeup
    async def wakeup_error(self, ctx, error):
            if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
                await ctx.send(f'** Argumento inválido! utilize {Prefix}wakeup @usuário Canal.ID1 Canal.ID2**')

    @wakeup.error #checa se o usuário possui a role woken necessária para utilizar o comando wakeup!
    async def woken_missing_role(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRole):
            await ctx.send('❌ É necessário ter a role **woken** para utilizar o wakeup!❌')