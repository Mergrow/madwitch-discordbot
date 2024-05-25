import discord
from discord.ext import commands
import yt_dlp
from cogs.variables import *
import os


download_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../audio'))

os.makedirs(download_directory, exist_ok=True)

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_directory, '%(extractor)s-%(id)s-%(title)s.%(ext)s'),
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class _music(commands.Cog): 
    def __init__(self, witch):
        self.witch = witch

    async def get_info(self, query):
        with ytdl as ydl:
            try:
                info = ydl.extract_info(query, download=False)
                return info
            except Exception as e:
                print(e)
                return None

# Tá quebrado essa porra n sei arrumar

    @commands.command()
    async def play(self, ctx, *, query):
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_channel:
            try:

                if not voice_client:
                    voice_client = await voice_channel.connect() 
                info = await self.get_info(query)
                if info:
                    url = info['formats'][0]['url']
                    voice_client.play(discord.FFmpegPCMAudio(os.path.join(download_directory, 'song.mp3')))
            except Exception as e:
                print(e)
                await ctx.send("Ocorreu um erro ao reproduzir a música.")
        else:
            await ctx.send("Você precisa estar em um canal de voz para usar este comando.")


    @commands.command()
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client and voice_client.is_playing():
            await voice_client.disconnect()
        else:
            await ctx.send("Eu não estou conectado a um canal de voz.")


    @commands.command()
    async def song(self, ctx):
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client
        if voice_channel:
            voice_client = ctx.voice_client
            if voice_client:
                if voice_client.is_connected():
                    await voice_client.move_to(voice_channel)
                else:
                    voice_client = await voice_channel.connect()
            else:
                voice_client = await voice_channel.connect()

            song_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../audio/song.mp3'))    

            source = discord.FFmpegPCMAudio(song_path)
            voice_client.play(source)

        else:
            await ctx.send('Você precisa estar em um canal de voz para usar esse comando!')


async def setup(client):
    await client.add_cog(_music(client))
