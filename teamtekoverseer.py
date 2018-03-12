from __future__ import print_function
import logging
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='T.', owner_id='269758783557730314')

@bot.event
async def on_ready():
    print("Connected!")
    print("Username: " + bot.user.name)
    print("-----------------")
    await bot.change_presence(game=discord.Game(type=3, name="Team TEK Servers"))
    print (discord.__version__)
    print ('Team TEK Overseer is ready')
    print ('Connected to '+str(len(bot.servers))+' servers')
    print ('Connected to '+str(len(set(bot.get_all_members())))+' users')
    print("-----------------")

@bot.command(pass_context=True)
@commands.has_role('Team TEK Member')
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description='Here is what I could find:', color=0x00ecff)
    embed.add_field(name='The Users Name is:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='The Users ID is:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='The Users Status is:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='The Users Highest Role is:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='The User Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role('Team TEK Member')
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find:", color=0x00ecff, inline=True)
    embed.set_author(name='Developers of Team TEK')
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Role Count", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Member Count", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_any_role('JackTEK05', 'Administrator', 'Admin')
async def ban(ctx, user: discord.Member):
    embed = discord.Embed(title='Ban Case:', description='{} Banned'.format(user.name), color=0xff0000)
    embed.add_field(name='The Users Name is:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='The Users ID is:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='415979321857933313'), embed=embed)
    await bot.ban(user)

@bot.command(pass_context=True)
@commands.has_any_role('JackTEK05', 'Administrator', 'Admin')
async def kick(ctx, user: discord.Member):
    embed = discord.Embed(title='Kick Case:', description='{} Kicked'.format(user.name), color=0xff7a00)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True) 
    embed.set_thumbnail(url=user.avatar_url)   
    await bot.kick(user)
    await bot.send_message(discord.Object(id='415979321857933313'), embed=embed)

@bot.command(pass_context=True)
@commands.has_role('Administrator')
async def mute(ctx, user: discord.Member):
    embed = discord.Embed(title='Mute Case:', description='{} Muted'.format(user.name), color=0xffee00)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='415979321857933313'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Muted')
    await bot.add_roles(user, role)

@bot.command(pass_context=True)
@commands.has_role('Administrator')
async def unmute(ctx, user: discord.Member):
    embed = discord.Embed(title='Unmute Case:', description='{} Unmuted'.format(user.name), color=0x4b7be8)
    embed.add_field(name='User', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='415979321857933313'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Muted')
    await bot.remove_roles(user, role)

#The following commands must be below all others (including new ones) 
@bot.command(pass_context=True)
@commands.has_role('JackTEK05')
async def kill(ctx):
    embed = discord.Embed(title='Kill Command Initiated, Terminating session!', color=0xff0000)
    embed.add_field(name='Have a nice day Team TEK', value=':wave::skin-tone-1:', inline=True)
    await bot.send_message(discord.Object(id='415979321857933313'), embed=embed)
    await bot.logout()

@bot.command(pass_context=True)
@commands.has_role('Team TEK Member')
async def commands(ctx):
    embed = discord.Embed(title='Command List', description='Here is what I could find:', color=0x00ecff,  inline=True)
    embed.set_author(name='Developers of Team TEK')
    embed.add_field(name='Commands', value='Displays this list', inline=True)
    embed.add_field(name='Info', value='Find user info', inline=True)
    embed.add_field(name='Kick', value='Kicks a user', inline=True)
    embed.add_field(name='Ban', value='Bans a user', inline=True)
    embed.add_field(name='Status', value='Shows a users status', inline=True)
    embed.add_field(name='ServerInfo', value='Shows server info', inline=True)
    embed.add_field(name='ServerIcon', value="Show's the server's icon", inline=True)
    embed.add_field(name='Kill', value="Log's the bot out (dev's only)", inline=True)
    embed.add_field(name='Mute', value="Mutes a user", inline=True)
    embed.add_field(name='Unmute', value="Unmutes a user", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def status(ctx, user: discord.Member):
    embed = discord.Embed(title='The users status is: {}'.format(user.status), color=0x00ecff)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def servericon(ctx):
    embed = discord.Embed(title='Here is what I could find:', color=0x00ecff)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

logging.basicConfig(level=logging.INFO)

bot.run('NDIyNTI5NDA0OTc2MTAzNDI2.DYdINw.t5SNcfnkODZaGRp28Un0y348tMA')