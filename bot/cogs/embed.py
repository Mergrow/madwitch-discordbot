import discord
from ruamel.yaml import YAML

from discord.ext import commands



class _embed(commands.Cog):
    def __init__(self, witch):
        self.witch = witch

    @commands.command()
    async def embed(self, ctx):
        embed=discord.Embed(title="Teste", color=0xc034eb)
        embed.set_image(url="")
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(_embed(client))