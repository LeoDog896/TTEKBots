from __future__ import print_function
import logging
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import config


bot = commands.Bot(command_prefix=commands.when_mentioned_or('T.'), description='Here are all of my commands:', owner_id='269758783557730314', pm_help=True)
logging.basicConfig(level=logging.INFO)


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
    bot.remove_command('help')
    print("-----------------")

@bot.event
async def on_server_join(server):
    embed = discord.Embed(title='Join Case:', color=0x00ff00)
    embed.add_field(name='Server Name:', value=server.name, inline=True)
    embed.add_field(name='Server ID:', value=server.id, inline=True)
    embed.add_field(name='Role Count:', value=len(server.roles), inline=True)
    embed.add_field(name='Member Count:', value=len(server.members), inline=True)
    embed.set_thumbnail(url=server.icon_url)
    await bot.send_message(discord.utils.get(bot.get_all_channels(), id='422870347461820426'), embed=embed)

@bot.event
async def on_server_remove(server):
    embed = discord.Embed(title='Leave Case:', color=0x00ff00)
    embed.add_field(name='Server Name:', value=server.name, inline=True)
    embed.add_field(name='Server ID:', value=server.id, inline=True)
    embed.add_field(name='Role Count:', value=len(server.roles), inline=True)
    embed.add_field(name='Member Count:', value=len(server.members), inline=True)
    embed.set_thumbnail(url=server.icon_url)

@bot.command(pass_context=True)
async def botinfo(ctx):
    embed = discord.Embed(title='Bot Info:', color=0x6e7be1)
    embed.add_field(name='Name:', value='Team TEK Overseer', inline=True)
    embed.add_field(name='ID:', value='422529404976103426', inline=True)
    embed.add_field(name='Description:', value='A bot designed for the needs of Team TEK', inline=True)
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
@commands.has_role('Administrators')
async def mute(ctx, user: discord.Member):
    embed = discord.Embed(title='Mute Case:', description='{} Muted'.format(user.name), color=0xffee00)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='422870347461820426'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Muted')
    await bot.add_roles(user, role)

@bot.command(pass_context=True)
@commands.has_role('Administrators')
async def certify(ctx, user: discord.Member):
    embed = discord.Embed(title='Certify Case:', description='{} Certified'.format(user.name), color=0x21cfbd)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='422870347461820426'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Certified Members')
    await bot.add_roles(user, role)

@bot.command(pass_context=True)
@commands.has_any_role('JackTEK05', 'Administrators', 'Admin')
async def kick(ctx, user: discord.Member):
    embed = discord.Embed(title='Kick Case:', description='{} Kicked'.format(user.name), color=0xff7a00)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True) 
    embed.set_thumbnail(url=user.avatar_url)  
    await bot.kick(user)
    await bot.send_message(discord.Object(id='422870347461820426'), embed=embed)

@bot.command(pass_context=True)
@commands.has_role('Administrators')
async def unmute(ctx, user: discord.Member):
    embed = discord.Embed(title='Unmute Case:', description='{} Unmuted'.format(user.name), color=0x4b7be8)
    embed.add_field(name='User', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(discord.Object(id='422870347461820426'), embed=embed)
    role = discord.utils.get(ctx.message.server.roles, name='Muted')
    await bot.remove_roles(user, role)

@bot.command(pass_context=True)
@commands.has_role('Administrators')
async def ban(ctx, user: discord.Member):
    embed = discord.Embed(title='Ban Case:', description='{} Banned'.format(user.name), color=0xff2d2d)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True) 
    embed.set_thumbnail(url=user.avatar_url)   
    await bot.ban(user)
    await bot.send_message(discord.Object(id='422870347461820426'), embed=embed)

@bot.command(pass_context=True)
@commands.has_role('Administrators')
async def promoteAdmin(ctx, user: discord.Member):
    embed = discord.Embed(title='Promote Admin Case:', color=0x6e7be1)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Role', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    role = discord.utils.get(ctx.message.server.roles, name='Administrators')
    await bot.send_message(discord.Object(id='422870347461820426'), embed=embed)
    await bot.add_roles(user, role)

@bot.command(pass_context=True)
@commands.has_role('Administrators')
async def promoteMod(ctx, user: discord.Member):
    embed = discord.Embed(title='Promote Mod Case:', color=0x6e7be1)
    embed.add_field(name='Name:', value='{}'.format(user.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Role:', value='{}'.format(user.top_role), inline=True)
    embed.add_field(name='Joined at:', value='{}'.format(user.joined_at), inline=True)
    embed.add_field(name='Status:', value='{}'.format(user.status), inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    role = discord.utils.get(ctx.message.server.roles, name='Moderators')
    await bot.send_message(discord.Object(id='422870347461820426'), embed=embed)
    await bot.add_roles(user, role)

#The following commands must be below all others (including new ones) 

@bot.command(pass_context=True)
@commands.has_role('JackTEK05')
async def kill(ctx):
    embed = discord.Embed(title='Kill Case:', color=0xff0000)
    embed.add_field(name='Name:', value='{}'.format(ctx.message.author.name), inline=True)
    embed.add_field(name='ID:', value='{}'.format(ctx.message.author.id))
    embed.add_field(name='Role:', value='{}'.format(ctx.message.author.top_role))
    embed.add_field(name='Joined at:', value='{}'.format(ctx.message.author.joined_at))
    embed.add_field(name='Status:', value='{}'.format(ctx.message.author.status))
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.send_message(discord.Object(id='422870347461820426'), embed=embed)
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

bot.run(config.token)