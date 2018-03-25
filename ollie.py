from __future__ import print_function
import time
import logging
import discord
import random
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import config
import dbl
import aiohttp
import pickle
import os
from discord.voice_client import VoiceClient
import json
import requests
from discord.ext import commands
import dataset

bot = commands.Bot(command_prefix=commands.when_mentioned_or('T.', 't.'), description='Here are all of my commands:', owner_id = '269758783557730314', pm_help=True)
bot.remove_command('help')
#logging.basicConfig(level=logging.INFO)
startup_extensions = ["Music", "rolecommands", "devcommands", "generalcommands", "helpcommands", "funcommands", "modcommands"]
db = dataset.connect()

table = db['balances']

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

dbltoken = config.dbltoken
url = "https://discordbots.org/api/bots/" + '423889279630966787' + "/stats"
headers = {"Authorization" : dbltoken, "Content-Type" : "application/json"}

@bot.event
async def on_ready():
    print("-----------------")
    print("Connected!")
    print("Username: " + bot.user.name)
    await bot.change_presence(game=discord.Game(type=1, name="{} Servers! | Upvote me on discordbots.org".format(len(bot.servers)), url='https://twitch.tv/jacktek05'))
    print (discord.__version__)
    print ('Connected to '+str(len(bot.servers))+' servers')
    print ('Connected to '+str(len(set(bot.get_all_members())))+' users')
    payload = {"server_count"  : len(bot.servers)}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)
    print(r.text)
    print("-----------------")

@bot.event
async def on_server_join(server):
    embed = discord.Embed(title='Join Case:', color=0x00ff00)
    embed.add_field(name='Server Name:', value=server.name, inline=True)
    embed.add_field(name='Server ID:', value=server.id, inline=True)
    embed.add_field(name='Role Count:', value=len(server.roles), inline=True)
    embed.add_field(name='Member Count:', value=len(server.members), inline=True)
    await bot.change_presence(game=discord.Game(type=1, name="{} Servers! | Upvote me on discordbots.org".format(len(bot.servers)), url='https://twitch.tv/jacktek05'))
    embed.set_thumbnail(url=server.icon_url)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    payload = {"server_count"  : len(bot.servers)}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)
    print(r.text)
    
@bot.event
async def on_server_remove(server):
    embed = discord.Embed(title='Leave Case:', color=0x00ff00)
    embed.add_field(name='Server Name:', value=server.name, inline=True)
    embed.add_field(name='Server ID:', value=server.id, inline=True)
    embed.add_field(name='Role Count:', value=len(server.roles), inline=True)
    embed.add_field(name='Member Count:', value=len(server.members), inline=True)
    embed.set_thumbnail(url=server.icon_url)
    await bot.change_presence(game=discord.Game(type=1, name="{} Servers! | Upvote me on discordbots.org".format(len(bot.servers)), url='https://twitch.tv/jacktek05'))
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    payload = {"server_count"  : len(bot.servers)}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)
    print(r.text)

@bot.command(pass_context=True)
async def load(ctx, extension_name : str):
    if ctx.message.author.id == '269758783557730314':
        """Loads an extension."""
        try:
            bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await bot.say("{} loaded.".format(extension_name))
    else:
        await bot.say('Hey! You are unauthorized to do that!')

@bot.command(pass_context=True)
async def unload(ctx, extension_name : str):
    if ctx.message.author.id == '269758783557730314':
        """Unloads an extension."""
        bot.unload_extension(extension_name)
        await bot.say("{} unloaded.".format(extension_name))
    else:
        await bot.say('Hey! You are unauthoriized to do that!')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.token)