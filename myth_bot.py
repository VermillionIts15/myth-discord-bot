import discord
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix='', intents=intents)  # Set the prefix to an empty string

# Define your bot token here
TOKEN = "BOT TOKEN HERE AND NOW"

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

# Ban Command
@client.command(
    name="ban",
    description="Ban a user"
)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, reason: str = None):
    await user.ban(reason=reason)
    await ctx.send(f'Banned user {user.display_name} for reason: {reason}')

# Kick Command
@client.command(
    name="kick",
    description="Kick a user"
)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, reason: str = None):
    await user.kick(reason=reason)
    await ctx.send(f'Kicked user {user.display_name} for reason: {reason}')

# Set Muted Role Command
@client.command(
    name="setmutedrole",
    description="Set the Muted role for the server"
)
@commands.has_permissions(manage_roles=True)
async def set_muted_role(ctx, role: discord.Role):
    await ctx.send(f'Successfully set the Muted role to {role.mention}.')

# Mute Command
@client.command(
    name="mute",
    description="Mute a user"
)
@commands.has_permissions(manage_roles=True)
async def mute(ctx, user: discord.User, reason: str = None, time: int = None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if muted_role:
        await user.add_roles(muted_role, reason=reason)
        if time:
            await asyncio.sleep(time * 60)
            await user.remove_roles(muted_role, reason="Mute time expired")
        await ctx.send(f'Muted user {user.display_name} for {time} minutes for reason: {reason}')
    else:
        await ctx.send('The Muted role is not set. Please use the /setmutedrole command to set it.')

# Prune (Bulk Delete) Command
@client.command(
    name="prune",
    description="Prune a specific number of messages"
)
@commands.has_permissions(manage_messages=True)
async def prune(ctx, number: int, reason: str = None):
    await ctx.message.delete()
    deleted = await ctx.channel.purge(limit=number + 1)
    await ctx.send(f'Successfully pruned {len(deleted) - 1} messages for reason: {reason}' if reason else f'Successfully pruned {len(deleted) - 1} messages.')

client.run(TOKEN)
