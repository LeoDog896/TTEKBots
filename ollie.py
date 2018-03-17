
from __future__ import print_function
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

bot = commands.Bot(command_prefix=commands.when_mentioned_or('T.'), description='Here are all of my commands:', owner_id = '269758783557730314', pm_help=True)
logging.basicConfig(level=logging.INFO)
startup_extensions = ["Music"]

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

dbltoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQyMzg4OTI3OTYzMDk2Njc4NyIsImJvdCI6dHJ1ZSwiaWF0IjoxNTIxMzA2NjMyfQ.pyUzUsH9X0xYcK8LiN2Eqfcc_bohrju4QFh4vWGvlzk"
url = "https://discordbots.org/api/bots/" + '423889279630966787' + "/stats"
headers = {"Authorization" : dbltoken, "Content-Type" : "application/json"}

@bot.event
async def on_ready():
    print("Connected!")
    print("Username: " + bot.user.name)
    print("-----------------")
    await bot.change_presence(game=discord.Game(type=3, name="{} Servers! | T.commands".format(len(bot.servers))))
    print (discord.__version__)
    print ('Connected to '+str(len(bot.servers))+' servers')
    print ('Connected to '+str(len(set(bot.get_all_members())))+' users')
    bot.remove_command('help')
    print("-----------------")
    payload = {"server_count"  : len(bot.servers)}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)
    print(r.text)


@bot.event
async def on_server_join(server):
    embed = discord.Embed(title='Join Case:', color=0x00ff00)
    embed.add_field(name='Server Name:', value=server.name, inline=True)
    embed.add_field(name='Server ID:', value=server.id, inline=True)
    embed.add_field(name='Role Count:', value=len(server.roles), inline=True)
    embed.add_field(name='Member Count:', value=len(server.members), inline=True)
    await bot.change_presence(game=discord.Game(type=3, name="{} Servers! | T.commands".format(len(bot.servers))))
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
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    payload = {"server_count"  : len(bot.servers)}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)
    print(r.text)

@bot.command(pass_context=True)
async def botinfo(ctx):
    embed = discord.Embed(title='Bot Info:', color=0x6e7be1)
    embed.add_field(name='Name:', value='Ollie', inline=True)
    embed.add_field(name='ID:', value='423889279630966787', inline=True)
    embed.add_field(name='Language:', value='Discord.py', inline=True)
    embed.add_field(name='Version:', value='0.16.12', inline=True)
    embed.add_field(name='Owner:', value='JackTEK05/MrSheldon', inline=True)
    embed.add_field(name='Prefix:', value='T. or @Ollie#8088', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/423889279630966787/ff42483864b61a16b4ef7ccd69cd0dd1.webp?size=128')
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description='Here is what I could find:', color=0x6e7be1)
    embed.add_field(name='The Users Name is:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='The Users ID is:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='The Users Status is:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='The Users Highest Role is:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='The User Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find:", color=0x6e7be1, inline=True)
    embed.set_author(name='Developers of Team TEK')
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Role Count", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Member Count", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def NSFW(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='NSFW')
    await bot.add_roles(ctx.message.author, role)

@bot.command(pass_context=True)
@commands.has_any_role('Administrators', 'Admin', 'Administrator', 'Moderator', 'Moderators', 'Mod')
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

@bot.command(pass_context=True)
@commands.has_any_role('Administrators', 'Admin', 'Administrator', 'Moderator', 'Moderators', 'Mod')
async def certify(ctx, user: discord.Member):
    embed = discord.Embed(title='Mute Case:', description='{} Muted'.format(user.name), color=0xffee00)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Certified Members')
    await bot.add_roles(user, role)

@bot.command(pass_context=True)
@commands.has_any_role('Administrators', 'Admin', 'Administrator', 'Moderator', 'Moderators', 'Mod')
async def kick(ctx, user: discord.Member):
    embed = discord.Embed(title='Kick Case:', description='{} Kicked'.format(user.name), color=0xff7a00)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url) 
    await bot.kick(user)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)

@bot.command(pass_context=True)
@commands.has_any_role('Administrators', 'Admin', 'Administrator', 'Moderator', 'Moderators', 'Mod')
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

@bot.command(pass_context=True)
@commands.has_any_role('Administrators', 'Admin', 'Administrator', 'Moderator', 'Moderators', 'Mod')
async def ban(ctx, user: discord.Member):
    embed = discord.Embed(title='Ban Case:', description='{} Banned'.format(user.name), color=0xff2d2d)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.set_thumbnail(url=user.avatar_url)   
    await bot.ban(user)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)

@bot.command(pass_context=True)
@commands.has_any_role('Administrators', 'Admin', 'Administrator')
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

@bot.command(pass_context=True)
@commands.has_any_role('Administrators', 'Admin', 'Administrator', 'Moderator', 'Moderators', 'Mod')
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

#The following commands must be below all others (including new ones) 

@bot.command(pass_context=True)
@commands.has_role('JackTEK05')
async def kill(ctx):
    embed = discord.Embed(title='Kill Case:', color=0xff0000)    
    embed.add_field(name='Name:', value='{}'.format(ctx.message.author.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(ctx.message.author.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(ctx.message.author.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(ctx.message.author.top_role), inline=True)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.send_message(discord.Object(id='423890604645285888'), embed=embed)
    await bot.logout()

@bot.command(pass_context=True)
async def commands(ctx):
    embed = discord.Embed(title='Command List:', color=0x6e7be1)
    embed.add_field(name='Info', value='Find user info')
    embed.add_field(name='Status', value='Shows a users status')
    embed.add_field(name='ServerInfo', value='Shows server info')
    embed.add_field(name='ServerIcon', value="Shows servericon")
    embed.add_field(name='Useravatar', value="Shows the user's avatar")
    embed.add_field(name='Botinfo', value="Shows the bot's info")
    embed.add_field(name='NSFW', value="Shows NSFW Channels")    
    embed.add_field(name='Kick', value='Kicks a user')
    embed.add_field(name='Ban', value='Bans a user')
    embed.add_field(name='Mute', value="Mutes a user")
    embed.add_field(name='Unmute', value="Unmutes a user")
    embed.add_field(name='PromoteAdmin', value='Promotes a user')
    embed.add_field(name='PromoteMod', value='Promotes a user')
    embed.add_field(name='Certify', value='Certifies a user')
    embed.add_field(name='Kill', value="Devs only")
    embed.add_field(name='Ping', value="Pong!!")
    embed.add_field(name='8ball', value="Find your future")
    embed.add_field(name='R&MQuote', value="Rick & Morty Quote")
    embed.add_field(name='Square', value='Square a number')
    embed.add_field(name='Add', value='Adds to numbers')
    embed.add_field(name='Flip', value='Flip a coin')
    embed.add_field(name='Play', value='Plays a song')
    embed.add_field(name='Stop', value='Stops a song')
    embed.add_field(name='Summon', value='Joins the bot to voice')
    await bot.send_message(ctx.message.author, embed=embed)
    await bot.say("I have sent you a DM")

@bot.command(pass_context=True)
async def status(ctx, user: discord.Member):
    embed = discord.Embed(title='The users status is: {}'.format(user.status), color=0x6e7be1)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def useravatar(ctx, user: discord.Member):
    embed = discord.Embed(title='Here is what I could find:', color=0x6e7be1)
    embed.set_thumbnail(url=user.avatar_url) 
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def servericon(ctx):
    embed = discord.Embed(title='Here is what I could find:', color=0x6e7be1)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

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
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command(name='R&MQuote',
                pass_context=True)
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

@bot.command(name='flip',
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
                'Tails',
                'Heads',
    ]
    await bot.say(random.choice(possible_responses))                   

@bot.command()
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " squared is " + str(squared_value))
    

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(':ping_pong: Pong!!')

@bot.command() 
async def add(left : int, right : int): 
    """Adds two numbers together.""" 
    await bot.say(left + right) 

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.token)