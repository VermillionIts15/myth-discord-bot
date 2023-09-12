import discord
from discord.ext import commands
from discord_slash import SlashCommand
import asyncio

bot_token = "YOUR_BOT_TOKEN_HERE"

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

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
@commands.has_permissions(ban_members=True)
async def ban(ctx, user, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f'Banned user {user.display_name} for reason: {reason}')

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
@commands.has_permissions(kick_members=True)
async def kick(ctx, user, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f'Kicked user {user.display_name} for reason: {reason}')

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
@commands.has_permissions(manage_roles=True)
async def set_muted_role(ctx, role):
    await ctx.send(f'Successfully set the Muted role to {role.mention}.')

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

@commands.cooldown(1, 60, commands.BucketType.user)
@commands.has_permissions(timeout_members=True)
async def mute(ctx, user, reason=None, time=None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if muted_role:
        await user.add_roles(muted_role, reason=reason)
        if time:
            await asyncio.sleep(int(time) * 60)
            await user.remove_roles(muted_role, reason="Mute time expired")
        await ctx.send(f'Muted user {user.display_name} for {time} minutes for reason: {reason}')
    else:
        await ctx.send('The Muted role is not set. Please use the /setmutedrole command to set it.')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Try again in {int(error.retry_after)} seconds.')

# Prune (Bulk Delete) Command
@slash.slash(
    name='prune',
    description='Prune a specific number of messages',
    options=[
        {
            'name': 'number',
            'description': 'Number of messages to prune',
            'type': 4,  # Integer type
            'required': True
        },
        {
            'name': 'reason',
            'description': 'Reason for pruning (optional)',
            'type': 3,  # String type
            'required': False
        }
    ]
)
@commands.has_permissions(manage_messages=True)
async def prune(ctx, number, reason=None):
    await ctx.message.delete()
    deleted = await ctx.channel.purge(limit=number + 1)
    if reason:
        await ctx.send(f'Successfully pruned {len(deleted) - 1} messages for reason: {reason}')
    else:
        await ctx.send(f'Successfully pruned {len(deleted) - 1} messages.')

bot.run(bot_token)
