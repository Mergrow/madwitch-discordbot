import pyttsx3
import discord
from discord.ext import commands

engine = pyttsx3.init()

class _tts(commands.Cog):
    def __init__(self, witch):
        self.witch = witch

    @commands.command()
    async def say(self, ctx, *, text):
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            voice_client = ctx.voice_client
            if voice_client:
                if voice_client.is_connected():
                    await voice_client.move_to(voice_channel)
                else:
                    voice_client = await voice_channel.connect()
            else:
                voice_client = await voice_channel.connect()

            # Usa a biblioteca pyttsx3 para converter o texto em fala
            engine.save_to_file(text, 'temp_audio.mp3')
            engine.runAndWait()

            # Reproduz o áudio gerado
            source = discord.FFmpegPCMAudio('temp_audio.mp3')
            voice_client.play(source)


        else:
            await ctx.send('Você precisa estar em um canal de voz para usar esse comando!')


    @commands.command()
    async def chu(self, ctx):
        text = "Estava eu indo ao meu trabalho, como todo dia faço, quando de repente eu vejo uma fila. Não era uma fila normal. Havia muitas pessoas naquela fila, que chegava a sair daquele ginásio. Mas não havia nenhum jogo aquele dia. Sequer tinham anunciado o que haveria ali. A turma da fila entoava um canto estranho que eu não entendia de princípio. Fiquei curioso. Mas continuei pro trabalho. Na volta, tive uma enorme surpresa. A fila estava maior! Meu Deus, o que seria aquilo? Eu, então, resolvi entrar na fila e conferir o que se passava ali. Logo, me envolvi naquele canto estranho: Queremos Ver o CHU, o CHU é bom! o CHU é legal! CHUCHURURUCHUCHU! Fiquei mais curioso ainda: Quem era chu? Por que ele é bom? Por que ele é legal? Continuei na fila e o povo cantando: Queremos Ver o CHU, o CHU é bom! o CHU é legal! CHUCHURURUCHUCHU! Depois de muita espera, finalmente chegou minha vez de entrar lá! Porém, para o meu azar, o segurança do lugar pediu pra que eu me retirasse e voltasse com roupas brancas, pois o chu só pode ser realizado com o povo todo de branco. Mas o povo da fila não estava de branco! Se não, eu saberia disso. O segurança mostrou que eles já tinham visto o chu e que haviam deixado suas roupas no lugar. Droga. No outro dia, eu voltei lá, todo de branco, até com a cueca branca. Mas... a fila novamente. Aquela fila não parava de crescer! Já chegava a dar a volta no estádio! E todos cantando: Queremos Ver o CHU, o CHU é bom! o CHU é legal! CHUCHURURUCHUCHU! Eu estava eufórico e ansioso. Finalmente iria ver o chu. Eu já cantava com o povo: Queremos Ver o CHU, o CHU é bom! o CHU é legal! CHUCHURURUCHUCHU! Foi quando faltando 5 pessoas para chegar em mim, o segurança informou que não cabia mais ninguém no ginásio. Ahhh, eu fiquei louco, acampei ali na frente, para esperar por uma vaga, e todo cantando: Queremos Ver o CHU, o CHU é bom! o CHU é legal! CHUCHURURUCHUCHU! Foi quando algumas pessoas saíram e finalmente eu pude entrar! Quando eu entrei lá, todos estavam na arquibancada gritando: É isso aí, Chuuuu! Você é massa! Você é da hora!!! Vai lá, Chuuuu!!!! No meio do ginásio tinha uma piscina e uma tocha. Eu procurei um lugar pra mim enquanto o povo cantava. De repente, todos se calaram. Um negão enorme entrou no meio do ginásio, foi até o meio da piscina, pegou a tocha e... CHUUUUUU... HAHAHAHHAHAAHHAHAHAAHHAHAA gostou da piada?"
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            voice_client = ctx.voice_client
            if voice_client:
                if voice_client.is_connected():
                    await voice_client.move_to(voice_channel)
                else:
                    voice_client = await voice_channel.connect()
            else:
                voice_client = await voice_channel.connect()

            # Usa a biblioteca pyttsx3 para converter o texto em fala
            engine.save_to_file(text, 'temp_audio.mp3')
            engine.runAndWait()

            # Reproduz o áudio gerado
            source = discord.FFmpegPCMAudio('temp_audio.mp3')
            await ctx.send('Contando a piada do chu!')
            voice_client.play(source)


        else:
            await ctx.send('Você precisa estar em um canal de voz para usar esse comando!')


    @commands.command()
    async def stop(self, ctx):
        voice_client = ctx.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.stop()
            await ctx.send('Reprodução de áudio parada!')
        else:
            await ctx.send('Nenhum áudio está sendo reproduzido.')

         
async def setup(client):
    await client.add_cog(_tts(client))
