# JBot by JackTEK05
from __future__ import print_function

import os
import sys
import time
import logging
import tempfile
import traceback
import subprocess
import config
import subprocess
import os

from shutil import disk_usage, rmtree
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import logging

bot = commands.Bot(command_prefix='J.', owner_id='269758783557730314')

@bot.event
async def on_ready():
    print("Connected!")
    print("Username: " + bot.user.name)
    print("-----------------")
    await bot.change_presence(game=discord.Game(name="Use J.commands"))
    print (discord.__version__)
    print ('JBot is online and ready')
    print ('Connected to '+str(len(bot.servers))+' servers')
    print ('Connected to '+str(len(set(bot.get_all_members())))+' users')
    print("-----------------")

logging.basicConfig(level=logging.INFO)


@bot.command(pass_context=True)
@commands.has_any_role('Bot Developer', 'Team TEK Chief Executive Officer', 'JackTEK05', 'JBot Dev', 'Team TEK Developer')
async def kill(ctx):
    embed = discord.Embed(title='Kill Command Initiated, Terminating session!', color=0xff0000)
    embed.add_field(name='Have a nice day Team TEK', value=':wave::skin-tone-1:', inline=True)
    await bot.say(embed=embed)
    await bot.logout()

@bot.command(pass_context=True)
@commands.has_role('Admin')
async def kick(ctx, user: discord.Member):
    embed = discord.Embed(title='Kicked {}'.format(user.name), color=0x0000ff)    
    await bot.say(embed=embed)
    await bot.say(':boot: Cya, {}'.format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_role('JackTEK05')
async def ban(ctx, user: discord.Member):
    embed = discord.Embed(title='Banned {}'.format(user.name), color=0x0000ff)    
    await bot.say(embed=embed)
    await bot.say(':boot: Cya, {}'.format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
async def RMQuote(ctx):
    embed = discord.Embed(title='All those famous quotes...', description='Here is what I could find:', color=0xf0ff00)
    embed.set_author(name='Jack Gledhill of Team TEK')
    embed.add_field(name='Wabbalabadubdub!!!', value='S1 S2 S3', inline=True)
    embed.add_field(name='Ricitikitavi Bitch!', value='S2', inline=True)
    embed.add_field(name='Graassssss...Tastes baddd!', value='S2', inline=True)
    embed.add_field(name='Lick, Lick, Lick Ma Balls!', value='S2', inline=True)
    embed.add_field(name='And thats the Wayyyyy the News goes!', value='S2', inline=True)
    embed.add_field(name='Hit the sack, Jack!', value='S2', inline=True)
    embed.add_field(name='No jumping in the sewer.', value='S2', inline=True)
    embed.add_field(name="And that's why I always say, 'Shumshumschilpiddydah!'", value='S2', inline=True)
    embed.add_field(name='Uh ohhhh! Somersoult jump!', value='S2', inline=True)
    embed.add_field(name='Rubber baby buggy bumpers!', value='S2', inline=True)
    embed.add_field(name='Peace among worlds :middle_finger::skin-tone-1:', value='S2', inline=True)
    embed.add_field(name='AIDS!!', value='S2', inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def DTB(ctx):
    embed = discord.Embed(title='Fuck you!', color=0xff8900)
    embed.add_field(name=':middle_finger::skin-tone-1:', value='Happy now Bitch!?')
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def commands(ctx):
    embed = discord.Embed(title='Command List', description='Here is what I could find:', color=0x00ecff,  inline=True)
    embed.set_author(name='Jack Gledhill of Team TEK')
    embed.add_field(name='Commands', value='Displays this list', inline=True)
    embed.add_field(name='Ping', value='Pong!!', inline=True)
    embed.add_field(name='DTB', value='Drop The Bomb!', inline=True)
    embed.add_field(name='RMQuote', value='Rick & Morty Quotes!!', inline=True)
    embed.add_field(name='Info', value='Find user info', inline=True)
    embed.add_field(name='Kick', value='Kicks a user', inline=True)
    embed.add_field(name='Ban', value='Bans a user', inline=True)
    embed.add_field(name='Status', value='Shows a users status', inline=True)
    embed.add_field(name='ServerInfo', value='Shows server info', inline=True)
    embed.add_field(name='ServerIcon', value="Show's the server's icon", inline=True)
    embed.add_field(name='Kill', value="Log's the bot out (dev's only)", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def status(ctx, user: discord.Member):
    embed = discord.Embed(title='The users status is: {}'.format(user.status), color=0x00ecff)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find:", color=0x00ecff, inline=True)
    embed.set_author(name='Jack Gledhill of Team TEK')
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Role Count", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Member Count", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
        embed = discord.Embed(title=':ping_pong: Pong!!', color=0x00ff00)
        await bot.say(embed=embed)
        print ('A User has pinged!')

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description='Here is what I could find:', color=0x00ecff)
    embed.add_field(name='The Users Name is:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='The Users ID is:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='The Users Status is:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='The Users Highest Role is:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='The User Joined at:', value='{}'.format(user.joined_at), inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def servericon(ctx):
    embed = discord.Embed(title='Here is what I could find:', color=0x00ecff)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

bot.run(config.token)