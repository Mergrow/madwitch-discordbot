from cogs.variables import *
from cogs.embed import _embed
from cogs.rpc import _rpc
from cogs.move import _move
from cogs.wakeup import _wakeup
from cogs.manager import _invite, _servers, _witchery
from cogs.twitch import *



bot_token = os.environ.get('DISCORD_TOKEN') #Token do bot

#
async def load_extensions():
    await client.load_extension("cogs.wakeup")
    await client.load_extension("cogs.manager") 
    await client.load_extension("cogs.rpc")
    await client.load_extension("cogs.move") 
    await client.load_extension("cogs.embed") 


## Logging

log_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
current_time = time.strftime("%d-%m-%Y %H-%M-%S")

if not os.path.exists(log_directory):
    os.makedirs(log_directory)



logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=os.path.join(log_directory, f"{current_time}.log"),
                    filemode='w')


console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)

# Adiciona o handler ao root logger
logging.getLogger('').addHandler(console_handler)

# Substitui sys.stdout para redirecionar a saída padrão para o logger
class LoggerWriter:
    def __init__(self, level):
        self.level = level

    def write(self, message):
        if message != '\n':
            logging.log(self.level, message)

    def flush(self):
        pass

sys.stdout = LoggerWriter(logging.INFO)
sys.stderr = LoggerWriter(logging.ERROR)

###


@client.event               #evento no inicio do bot
async def on_ready():

    print("Bot esta funcionando! " .format(client)) #log no console, para saber se o bot foi iniciado corretamente!
    print('Logado como {0.user} '  .format(client)) 
    print(f'Hoje é: ' + time.strftime("%d/%m/%Y %H:%M:%S") .format(client)) 
    print(f'Versão atual: {ver}\n '  .format(client)) 
    await client.change_presence(activity=discord.Streaming(name='Primeiro Discordbot do Mergrow!', url='https://www.twitch.tv/mergrow_', status=discord.Status.idle)) # Atualiza o RPC do discordbot
    check_streamer_status.start()
    await client.tree.sync(guild=discord.Object(id=922349610771546112))
    await load_extensions()

        
#Slash commands

@client.tree.command(name="hi", description="Say hi", guild=discord.Object(id=922349610771546112))   
async def hi(ctx):
    await ctx.response.send_message("Hello!")


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
async def host(ctx):
    embed = discord.Embed(title="Self-hosted", color=0xc034eb)
    await ctx.send(embed=embed)



client.run(bot_token)