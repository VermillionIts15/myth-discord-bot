import discord
from discord.ext import commands
from discord_slash import SlashCommand

# I shouldn't have to say this but this is needed.
# Put your bot token here, otherwise your bot won't work.
bot_token = "TOKEN HERE"

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

# Bot event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Ban Command
@slash.slash(
   name='ban',
   description='Ban a user',
   options=[
       {
           'name': 'user',
           'description': 'User to ban',
           'type': 6,  # User type
           'required': True
       },
       {
           'name': 'reason',
           'description': 'Reason for banning',
           'type': 3,  # String type
           'required': False
       }
   ]
)
async def ban(ctx, user, reason=None):
   if ctx.author.guild_permissions.ban_members:
       await user.ban(reason=reason)
       await ctx.send(f'Banned user {user.display_name} for reason: {reason}')
   else:
       await ctx.send('You do not have permission to ban users.')

# Kick Command
@slash.slash(
   name='kick',
   description='Kick a user',
   options=[
       {
           'name': 'user',
           'description': 'User to kick',
           'type': 6,  # User type
           'required': True
       },
       {
           'name': 'reason',
           'description': 'Reason for kicking',
           'type': 3,  # String type
           'required': False
       }
   ]
)
async def kick(ctx, user, reason=None):
   if ctx.author.guild_permissions.kick_members:
       await user.kick(reason=reason)
       await ctx.send(f'Kicked user {user.display_name} for reason: {reason}')
   else:
       await ctx.send('You do not have permission to kick users.')

# Set Muted Role Command
@slash.slash(
    name='setmutedrole',
    description='Set the Muted role for the server',
    options=[
        {
            'name': 'role',
            'description': 'Muted role to set',
            'type': 8,  # Role type
            'required': True
        }
    ]
)

async def set_muted_role(ctx, role):
    if ctx.author.guild_permissions.manage_roles:
        muted_role = discord.utils.get(ctx.guild.roles, id=role.id)

        if muted_role:
            await ctx.send(f'Successfully set the Muted role to {muted_role.mention}.')
        else:
            await ctx.send('The specified role does not exist. Please create the Muted role first.')

    else:
        await ctx.send('You do not have permission to set the Muted role.')

# Mute Command
@slash.slash(
    name='mute',
    description='Mute a user',
    options=[
        {
            'name': 'user',
            'description': 'User to mute',
            'type': 6,  # User type
            'required': True
        },
        {
            'name': 'reason',
            'description': 'Reason for muting',
            'type': 3,  # String type
            'required': False
        },
        {
            'name': 'time',
            'description': 'Duration of mute in minutes',
            'type': 4,  # Integer type
            'required': False
        }
    ]
)
async def mute(ctx, user, reason=None, time=None):
    if ctx.author.guild_permissions.manage_roles:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role:
            await user.add_roles(muted_role, reason=reason)
            if time:
                await asyncio.sleep(int(time) * 60)
                await user.remove_roles(muted_role, reason="Mute time expired")
            await ctx.send(f'Muted user {user.display_name} for {time} minutes for reason: {reason}')
        else:
            await ctx.send('The Muted role is not set. Please use the /setmutedrole command to set it.')
    else:
        await ctx.send('You do not have permission to mute users.')

bot.run(bot_token)
