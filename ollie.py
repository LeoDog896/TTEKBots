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
logging.basicConfig(level=logging.INFO)
startup_extensions = ["Music"]
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


@bot.command(pass_context=True,
             aliases=['Account', 'ACCOUNT'])
async def account(ctx):
    table.insert(dict(name=ctx.message.author.id, balance='100'))
    await bot.say('I have created you an account and added $100 to it, happy spending!')

@bot.command(pass_context=True,
             aliases=['Work', 'WORK'])
async def work(ctx):
    table.update(dict(name=ctx.message.author.id, balance=table + 500), ['name'])
    await bot.say('You were worked for 5 hours and earned $500!')

@bot.command(pass_context=True,
             aliases=['Balance', 'BALANCE'])
async def balance(ctx):
    balance = db['balance'].all()
    await bot.say('Your balance is:' + ' ' + '$' + balance)

@bot.command(pass_context=True,
             aliases=['About', 'ABOUT'])
async def about(ctx):
   embed = discord.Embed(description='Python v0.16.12', url='http://discordpy.readthedocs.io/en/latest/api.html', color=0x6e7be1)
   embed.add_field(name='Author:', value='JackTEK05#0851')
   embed.add_field(name='ID:', value='{}'.format(bot.user.id))
   embed.add_field(name='Prefix:', value='T. or @{}'.format(bot.user.name))
   embed.add_field(name='Certified:', value='No')
   embed.set_thumbnail(url=bot.user.avatar_url)
   await bot.say(embed=embed)

@bot.command(pass_context=True,
             aliases=['Info', 'INFO'])
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description='Here is what I could find:', color=0x6e7be1)
    embed.add_field(name='The Users Name is:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='The Users ID is:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='The Users Status is:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='The Users Highest Role is:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='The User Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.add_field(name='The User was created at:', value='{}'.format(user.created_at))
    embed.add_field(name='The Users Discriminator is:', value='{}'.format(user.discriminator), inline=True)
    embed.add_field(name='The User is playing:', value='{}'.format(user.game))
    embed.set_footer(text='{}'.format(user.name), icon_url='{}'.format(user.avatar_url))
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True,
             aliases=['ServerInfo', 'Serverinfo', 'SERVERINFO'])
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find:", color=0x6e7be1, inline=True)
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Role Count", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Member Count", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True,
             aiases=['nsfw', 'Nsfw'])
async def NSFW(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='NSFW')
    await bot.add_roles(ctx.message.author, role)

@bot.command(pass_context=True,
             aliases=['MUTE', 'Mute'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, user: discord.Member):
    embed = discord.Embed(title='Mute Case:', description='{} Muted'.format(user.name), color=0xffee00)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Muted')
    await bot.add_roles(user, role)

@bot.command(pass_context=True,
             aliases=['Certify', 'CERTIFY'])
@commands.has_permissions(administrator=True)
async def certify(ctx, user: discord.Member):
    embed = discord.Embed(title='Certify Case:', description='{} Certified'.format(user.name), color=0x4cff44)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Certified Members')
    await bot.add_roles(user, role)

@bot.command(pass_context=True,
             alliases=['Kick', 'KICK'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    embed = discord.Embed(title='Kick Case:', description='{} Kicked'.format(user.name), color=0xff7a00)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url) 
    await bot.kick(user)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)

@bot.command(pass_context=True,
             aiases=['UnMute', 'Unmute', 'UNMUTE'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, user: discord.Member):
    embed = discord.Embed(title='Unmute Case:', description='{} Unmuted'.format(user.name), color=0x4b7be8)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Muted')
    await bot.remove_roles(user, role)

@bot.command(pass_context=True,
             aiases=['Ban', 'BAN'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    embed = discord.Embed(title='Ban Case:', description='{} Banned'.format(user.name), color=0xff2d2d)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url)   
    await bot.ban(user)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)

@bot.command(pass_context=True,
             aliases=['PromoteAdmin', 'promoteadmin', 'PROMOTEADMIN'])
@commands.has_permissions(administrator=True)
async def promoteAdmin(ctx, user: discord.Member):
    embed = discord.Embed(title='Promote Admin Case:', color=0x6e7be1)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    role = discord.utils.get(ctx.message.server.roles, name='Administrators')
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    await bot.add_roles(user, role)

@bot.command(pass_context=True,
             aiases=['PromoteMod', 'promotemod', 'PROMOTEMOD'])
@commands.has_permissions(administrator=True)
async def promoteMod(ctx, user: discord.Member):
    embed = discord.Embed(title='Promote Mod Case:', color=0x6e7be1)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    role = discord.utils.get(ctx.message.server.roles, name='Moderators')
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    await bot.add_roles(user, role)

@bot.command(name='eval', pass_context=True, hidden=True)
async def debug(ctx, *, code : str):
    if ctx.message.author.id == '269758783557730314':
        """Evaluates code."""
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        try:
            result = eval(code)
        except Exception as e:
            await bot.say(python.format(type(e).__name__ + ': ' + str(e)))
            return

    if asyncio.iscoroutine(result):
        result = await result

    await bot.say(python.format(result))

@bot.command(pass_context=True,
             aliases=['AddChannel', 'ADDCHANNEL'])
@commands.has_permissions(manage_channels=True)
async def addchannel(ctx):
    await bot.create_channel(ctx.message.server, 'Text')
    await bot.say('I have created a text channel, you can change the settings at any time!')

@bot.command(pass_context=True,
             aliases=['AddTempChannel', 'ADDTEMPCHANNEL'])
@commands.has_permissions(manage_server=True)
async def addtempchannel(ctx):
    await bot.create_channel(ctx.message.server, 'Text Temp')
    await bot.say('I have created a text channel, it will be deleted in 3 minutes!')
    await asyncio.sleep(180)
    await bot.delete_channel('Text Temp')

@bot.command(pass_context=True,
             aliases=['AddTempVoiceChannel', 'ADDTEMPVOICECHANNEL'])
@commands.has_permissions(manage_server=True)
async def addtempvoicechannel(ctx):
    await bot.create_channel(ctx.message.server, 'Voice Temp', type=discord.ChannelType.voice)
    await bot.say('I have created a voice channel, it will be deleted in 3 minutes!')
    await asyncio.sleep(180)
    await bot.delete_channel('Voice Temp')

@bot.command(pass_context=True,
             aliases=['AddVoiceChannel', 'ADDVOICECHANNEL'])
@commands.has_permissions(manage_server=True)
async def addvoicechannel(ctx):
    await bot.create_channel(ctx.message.server, 'Voice', type=discord.ChannelType.voice)
    await bot.say('I have created a voice channel, you can change the settings at any time!')
@bot.command(pass_context=True,
             aliases=['Purge', 'PURGE'])

@commands.has_permissions(manage_messages=True)
async def purge(ctx):
    deleted = await bot.purge_from(ctx.message.channel, limit=10)
    await asyncio.sleep(2)
    await bot.send_message(ctx.message.channel, 'Deleted {} message(s)'.format(len(deleted)))
#The following commands must be below all others (including new ones) 



@bot.command(pass_context=True,
             aliases=['Kill', 'KILL'])
async def kill(ctx):
    if ctx.message.author.id == '269758783557730314':
        embed = discord.Embed(title='Kill Case:', color=0xff0000)    
        embed.add_field(name='Name:', value='{}'.format(ctx.message.author.name), inline=True)
        embed.add_field(name='ID:', value='{}'.format(ctx.message.author.id), inline=True)
        embed.add_field(name='Status:', value='{}'.format(ctx.message.author.status), inline=True)
        embed.add_field(name='Role:', value='{}'.format(ctx.message.author.top_role), inline=True)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
        await bot.logout()
    else:
        await bot.say('Hey! You are not authorized to do that!')

@bot.command(pass_context=True,
             aliases=['CommandsGeneral', 'COMMANDSGENERAL', "helpgeneral"])
async def commandsgeneral(ctx):
    await bot.say("I have sent you a DM, if you do not recieve a DM check your privacy settings!")
    embed = discord.Embed(title='General commands:', color=0x6e7be1)
    embed.add_field(name='Info \n', value='Find user info\n')
    embed.add_field(name='Status \n', value='Shows a users status \n')
    embed.add_field(name='ServerInfo\n', value='Shows server info\n')
    embed.add_field(name='ServerIcon\n', value="Shows servericon\n")
    embed.add_field(name='Useravatar\n', value="Shows the user's avatar\n")
    embed.add_field(name='About\n', value="Shows the bot's info\n")
    embed.add_field(name='Link\n', value='Gives all assigned links\n')
    embed.add_field(name='Invite\n', value='Gives the bot invite link\n')
    embed.set_footer(text='Authors: @JackTEK05#0851', icon_url='https://cdn.discordapp.com/emojis/424649813536145408.png?v=1')
    await bot.send_message(ctx.message.author, embed=embed)

@bot.command(pass_context=True,
             aliases=['CommandsMusic', 'COMMANDSMUSIC', "helpmusic"])
async def commandsmusic(ctx):
    await bot.say("I have sent you a DM, if you do not recieve a DM check your privacy settings!")
    embed = discord.Embed(title='Music commands:', color=0x6e7be1)    
    embed.add_field(name='Skip\n', value='Vote to skip a song\n')
    embed.add_field(name='Play\n', value='Plays a song\n')
    embed.add_field(name='Stop\n', value='Stops a song\n')
    embed.add_field(name='Summon\n', value='Joins the bot to voice\n')
    embed.add_field(name='Playing\n', value='Shows song playing\n')
    embed.set_footer(text='Authors: @JackTEK05#0851', icon_url='https://cdn.discordapp.com/emojis/424649813536145408.png?v=1')
    await bot.send_message(ctx.message.author, embed=embed)

@bot.command(pass_context=True,
             aliases=['CommandsFun', 'COMMANDSFUN', "helpfun"])
async def commandsfun(ctx):
    await bot.say("I have sent you a DM, if you do not recieve a DM check your privacy settings!")
    embed = discord.Embed(title='Fun commands:', color=0x6e7be1)
    embed.add_field(name='Legal\n', value='Trump makes something legal...\n')
    embed.add_field(name='Illegal\n', value='Trump makes something illegal...\n')
    embed.add_field(name='Flip\n', value='Flip a coin\n')
    embed.add_field(name='Hug\n', value='Give a warming hug\n')
    embed.add_field(name='8ball\n', value="Find your future\n")
    embed.add_field(name='R&MQuote\n', value="Rick & Morty Quote\n")  
    embed.set_footer(text='Authors: @JackTEK05#0851', icon_url='https://cdn.discordapp.com/emojis/424649813536145408.png?v=1') 
    await bot.send_message(ctx.message.author, embed=embed)

@bot.command(pass_context=True,
             aliases=['CommandsMod', 'COMMANDSMOD', "helpmod"])
async def commandsmod(ctx):
    await bot.say("I have sent you a DM, if you do not recieve a DM check your privacy settings!")
    embed = discord.Embed(title='Mod commands:', color=0x6e7be1) 
    embed.add_field(name='Kick\n', value='Kicks a user\n')
    embed.add_field(name='Ban\n', value='Bans a user\n')
    embed.add_field(name='Mute\n', value="Mutes a user\n")
    embed.add_field(name='Unmute\n', value="Unmutes a user\n")
    embed.add_field(name='PromoteAdmin\n', value='Promotes a user\n')
    embed.add_field(name='PromoteMod\n', value='Promotes a user\n')
    embed.add_field(name='Certify\n', value='Certifies a user\n')    
    embed.add_field(name='NSFW\n', value="Shows NSFW Channels\n")
    embed.add_field(name='Purge\n', value='Delete 10 messages\n')
    embed.add_field(name='AddChannel\n', value='Adds a text channel\n')
    embed.add_field(name='AddTempChannel\n', value='Adds a 3 minute text channel\n')
    embed.add_field(name='AddVoiceChannel\n', value='Adds a voice channel\n')
    embed.add_field(name='AddTempVoiceChannel\n', value='Adds a 3 minute voice channel\n')
    embed.set_footer(text='Authors: @JackTEK05#0851', icon_url='https://cdn.discordapp.com/emojis/424649813536145408.png?v=1')
    await bot.send_message(ctx.message.author, embed=embed)

@bot.command(pass_context=True)
async def allcommands(ctx):
    embed = discord.Embed(title='Cleverbot commands:', color=0x6e7be1)    
    embed.add_field(name='Square\n', value='Square a number\n')
    embed.add_field(name='Add\n', value='Adds 2 numbers\n')   
    embed.add_field(name='Ping\n', value="Find your ping\n")
    embed.add_field(name='Formula\n', value='Gives a random formula\n')
    embed.add_field(name='Color\n', value='Gives a random color\n')
    embed.add_field(name='Subtract', value='Subracts 2 numbers')
    await bot.send_message(ctx.message.author, embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(title='Mod commands:', color=0x6e7be1) 
    embed.add_field(name='Kick\n', value='Kicks a user\n')
    embed.add_field(name='Ban\n', value='Bans a user\n')
    embed.add_field(name='Mute\n', value="Mutes a user\n")
    embed.add_field(name='Unmute\n', value="Unmutes a user\n")
    embed.add_field(name='PromoteAdmin\n', value='Promotes a user\n')
    embed.add_field(name='PromoteMod\n', value='Promotes a user\n')
    embed.add_field(name='Certify\n', value='Certifies a user\n')    
    embed.add_field(name='NSFW\n', value="Shows NSFW Channels\n")
    embed.add_field(name='Purge\n', value='Delete 10 messages\n')
    embed.add_field(name='AddChannel\n', value='Adds a text channel\n')
    embed.add_field(name='AddTempChannel\n', value='Adds a 3 minute text channel\n')
    embed.add_field(name='AddVoiceChannel\n', value='Adds a voice channel\n')
    embed.add_field(name='AddTempVoiceChannel\n', value='Adds a 3 minute voice channel\n')
    await bot.send_message(ctx.message.author, embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(title='Fun commands:', color=0x6e7be1)
    embed.add_field(name='Legal\n', value='Trump makes something legal...\n')
    embed.add_field(name='Illegal\n', value='Trump makes something illegal...\n')
    embed.add_field(name='Flip\n', value='Flip a coin\n')
    embed.add_field(name='Hug\n', value='Give a warming hug\n')
    embed.add_field(name='8ball\n', value="Find your future\n")
    embed.add_field(name='R&MQuote\n', value="Rick & Morty Quote\n") 
    await bot.send_message(ctx.message.author, embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(title='Music commands:', color=0x6e7be1)    
    embed.add_field(name='Skip\n', value='Vote to skip a song\n')
    embed.add_field(name='Play\n', value='Plays a song\n')
    embed.add_field(name='Stop\n', value='Stops a song\n')
    embed.add_field(name='Summon\n', value='Joins the bot to voice\n')
    embed.add_field(name='Playing\n', value='Shows song playing\n') 
    await bot.send_message(ctx.message.author, embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(title='General commands:', color=0x6e7be1)
    embed.add_field(name='Info \n', value='Find user info\n')
    embed.add_field(name='Status \n', value='Shows a users status \n')
    embed.add_field(name='ServerInfo\n', value='Shows server info\n')
    embed.add_field(name='ServerIcon\n', value="Shows servericon\n")
    embed.add_field(name='Useravatar\n', value="Shows the user's avatar\n")
    embed.add_field(name='About\n', value="Shows the bot's info\n")
    embed.add_field(name='Link\n', value='Gives all assigned links\n')
    embed.add_field(name='Invite\n', value='Gives the bot invite link\n')
    await bot.send_message(ctx.message.author, embed=embed)
    await asyncio.sleep(1)

@bot.command(pass_context=True,
             aliases=['CommandsClever', 'COMMANDSCLEVER', "helpclever"])
async def commandsclever(ctx):
    await bot.say("I have sent you a DM, if you do not recieve a DM check your privacy settings!")
    embed = discord.Embed(title='Cleverbot commands:', color=0x6e7be1)    
    embed.add_field(name='Square\n', value='Square a number\n')
    embed.add_field(name='Add\n', value='Adds 2 numbers\n')   
    embed.add_field(name='Subtract', value='Subracts 2 numbers')
    embed.add_field(name='Ping\n', value="Find your ping\n")
    embed.add_field(name='Formula\n', value='Gives a random formula\n')
    embed.add_field(name='Color\n', value='Gives a random color\n')
    embed.set_footer(text='Authors: @JackTEK05#0851', icon_url='https://cdn.discordapp.com/emojis/424649813536145408.png?v=1')
    await bot.send_message(ctx.message.author, embed=embed)

@bot.command(pass_context=True,
             aliases=['Commands', 'COMMANDS', "help"])
async def commands(ctx):
    await bot.say("I have sent you a DM, if you do not recieve a DM check your privacy settings!")
    embed = discord.Embed(title='Command Categorys:', color=0x6e7be1)
    embed.add_field(name='General', value='(T.commandsgeneral)')
    embed.add_field(name='Music', value='(T.commandsmusic)')
    embed.add_field(name='Fun', value='(T.commandsfun)')
    embed.add_field(name='Mod', value='(T.commandsmod)')
    embed.add_field(name='Clever', value='(T.commandsclever)')
    embed.set_footer(text='Authors: @JackTEK05#0851', icon_url='https://cdn.discordapp.com/emojis/424649813536145408.png?v=1')
    await bot.send_message(ctx.message.author, embed=embed)

@bot.command(pass_context=True,
             aliases=['Invite', 'INVITE'])
async def invite(ctx):
    await bot.say('Here is the link: https://discordbots.org/bot/423889279630966787')
             
@bot.command(pass_context=True,
             aliases=['Links', 'Link', 'LINK', 'LINKS'])
async def link(ctx):
    embed = discord.Embed(title='Links:', color=0x6e7be1)
    embed.add_field(name='MC Forums:', value='https://www.ecraft.enjin.com')
    embed.add_field(name="Author's Facebook:", value='https://www.facebook.com/jack.gledhill.94')
    embed.add_field(name='Support Server:', value='https://discord.gg/mwwXtZ8')
    embed.add_field(name='Github Repository:', value='https://github.com/Team-TEK/TTEKBots')
    await bot.say(embed=embed)

@bot.command(pass_context=True,
             aliases=['Status', 'STATUS'])
async def status(ctx, user: discord.Member):
    embed = discord.Embed(title='The users status is: {}'.format(user.status), color=0x6e7be1)
    await bot.say(embed=embed)

@bot.command(pass_context=True,
             aliases=['UserAvatar', 'Useravatar', 'USERAVATAR'])
async def useravatar(ctx, user: discord.Member):
    embed = discord.Embed(color=0x6e7be1)
    embed.set_thumbnail(url=user.avatar_url) 
    await bot.say(embed=embed)

@bot.command(pass_context=True,
             aliases=['ServerIcon', 'Servericon', 'SERVERICON'])
async def servericon(ctx):
    embed = discord.Embed(color=0x6e7be1)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True,
             aliases=['Hug', 'HUG'])
async def hug(ctx, user: discord.Member):
    await bot.say('You hugged {}'.format(user.name))

@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'I dare say it is impossible',
        'Tis but a lie',
        'One cannot describe the truth within that',
        'If it were true, it would curse us all',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command(name='R&MQuote',
                pass_context=True,
                aliases=['r&mquote', 'R&MQUOTE'])
async def eight_ball(context):
    possible_responses = [
                'AIDS!',
                'Wubba lubba dub dub!',
                'Lick, lick, lick my balls!',
                'No jumping in the sewer.',
                'Uh ohhh summersoult jump.',
                'Graaasssss....Tastes bad.',
                'Hit the sack, Jack.',
                'And thats the wayyyyy the news goes.',
                'Rubber baby buggy bummpers!',
                "And that's why I always say, 'Shumshumschilpiddydah!'",
                'Peace among worlds, Rick! :middle_finger::skin-tone-1:',
                'Ricitikitavi Bitch!',
    ]
    await bot.say(random.choice(possible_responses)) 

@bot.command(name='Legal',
                pass_context=True,
                aliases=['legal', 'LEGAL'])
async def eight_ball(context):
    possible_responses = [
                'Eating you kids',
                'Underage pregnancy',
                'Murder',
                'Terrorism',
                'Underage tattooing',
                'Hacking',
                'Scamming',
                'Modifying guns',
    ]
    await bot.say('Trump made' + ' ' + random.choice(possible_responses) + ' ' + 'Legal!!!') 

@bot.command(name='IlLegal',
                pass_context=True,
                aliases=['illegal', 'ILLEGAL', 'Illegal'])
async def eight_ball(context):
    possible_responses = [
                'Education',
                'Firearms',
                'Programming',
                'Shopping',
                'Crop Farming',
                'Religion',
                'Chemical Research',
                'Discord',
    ]
    await bot.say('Trump made' + ' ' + random.choice(possible_responses) + ' ' + 'Illegal!!!') 

@bot.command(name='formula',
                pass_context=True,
                aliases=['Formula', 'FORMULA'])
async def eight_ball(context):
    possible_responses = [
                'Aerobic Respiration: glucose + oxygen --> carbon dioxide + water + energy / C6H12O6 + 6O2 --> 6Co2 + 6H2O + energy',
                'Anaerobic Respiration: glucose --> energy + lactic acid / C6H12O6 --> C3H6O3 + energy',
                'Photosynthesis: carbon dioxide + water --> glucose + oxygen / 6Co2 + 6H2O --> C6H12O6 + 6O2',
    ]
    await bot.say(random.choice(possible_responses))

@bot.command(name='color',
                pass_context=True,
                aliases=['Color', 'COLOR', 'Colour', 'colour', 'COLOUR'])
async def eight_ball(context):
    possible_responses = [
                '0xff0000',
                '0xfffb00',
                '0xff4b4b',
                '0x17ac86',
                '0x20ff00',
                '0x1400ff',
                '0x9100ff',
                '0xff00f0',
                '0xff7a00',
                '0x00fffc',
                '0x0070ff',
                '0x83ff00',
                '0x00ff70',
    ]
    await bot.say(random.choice(possible_responses))

@bot.command(name='flip',
                pass_context=True,
                aliases=['FLIP', 'Flip'])
async def eight_ball(context):
    possible_responses = [
                'Tails',
                'Heads',
    ]
    await bot.say(random.choice(possible_responses))                   

@bot.command(aliases=['Square', 'SQUARE'])
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " squared is " + str(squared_value))
    
@bot.command(aliases=['Add', 'ADD']) 
async def add(left : int, right : int): 
    """Adds two numbers together.""" 
    await bot.say(left + right) 

@bot.command(aliases=['Minus', 'MINUS', 'Subtract', 'subtract', 'SUBTRACT']) 
async def minus(left : int, right : int): 
    """Takes two numbers away.""" 
    await bot.say(left - right)



@bot.command(pass_context=True,
             aliases=['Ping', 'PING'])
async def ping(ctx):
    """Calculates the ping time."""
    # [p]ping

    t_1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t_2 = time.perf_counter()
    time_delta = round((t_2-t_1)*1000)                          # calculate the time needed to trigger typing
    await bot.say("Pong.\nTime: `{}ms`".format(time_delta))     # send a message telling the user the calculated ping time

@bot.command(pass_context=True)
async def PChangePlaying(ctx):
    if ctx.message.author.id == '269758783557730314':
        await bot.change_presence(game=discord.Game(type=1, name="{} Servers! | Upvote me on discordbots.org".format(len(bot.servers))))
        await bot.say('Changed Presence to: Playing')
    else:
        await bot.say('Hey! You are not authorized to do that!')

@bot.command(pass_context=True)
async def PChangeListening(ctx):
    if ctx.message.author.id == '269758783557730314':
        await bot.change_presence(game=discord.Game(type=2, name="{} Servers! | Upvote me on discordbots.org".format(len(bot.servers))))
        await bot.say('Changed Presence to: Listening')
    else:
        await bot.say('Hey! You are not authorized to do that!')

@bot.command(pass_context=True)
async def PChangeWatching(ctx):
    if ctx.message.author.id == '269758783557730314':
        await bot.change_presence(game=discord.Game(type=3, name="{} Servers! | Upvote me on discordbots.org".format(len(bot.servers))))
        await bot.say('Changed Presence to: Watching')  
    else:
        await bot.say('Hey! You are not authorized to do that!')     

@bot.command(pass_context=True)
async def PChangeStreaming(ctx):
    if ctx.message.author.id == '269758783557730314':
        await bot.change_presence(game=discord.Game(type=1, name="{} Servers! | Upvote me on discordbots.org".format(len(bot.servers)), url='https://twitch.tv/jacktek05'))
        await bot.say('Changed Presence to: Streaming')
    else:
        await bot.say('Hey! You are not authorized to do that!')





if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.token)