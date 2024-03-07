from http import server
import discord
import time
from discord.abc import GuildChannel
from discord.ext.commands.core import has_role
from discord.member import Member
from discord.guild import Role
from ruamel.yaml import YAML
from discord.utils import get
from discord.ext import commands
from datetime import timezone
from discord import app_commands
import os


yaml = YAML()
with open("bot/config.yml", "r", encoding='utf-8') as file: #config.yml
    config = yaml.load(file)

ver = ['0.2.0', '07/03/2024'] #versão atual do bot.
Prefix = config['Prefix']
client = commands.Bot(command_prefix=config['Prefix'], intents=discord.Intents.all()) #Definindo a variavel client, tendo como argumento o prefixo do comando.
ownerid = 337651715677618176 #DiscordID do desenvolvedor                                                                  #Intents são as permissoes do bot para capturar e armazenar a presença dos usuários.

