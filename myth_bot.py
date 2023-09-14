import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

TOKEN = "TOKEN-HERE-BABY" # Don't share or print your token with me or anyone else. Put your BOT token.

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

# User Info Command
@client.command(
    name="userinfo",
    description="Get detailed information about a user"
)
async def userinfo(ctx, user: discord.User = None):
    if user is None:
        user = ctx.author

    embed = discord.Embed(
        title=f"User Information - {user.name}",
        color=discord.Color.blue()
    )
    embed.add_field(name="Username", value=user.name, inline=True)
    embed.add_field(name="Display Name", value=user.display_name, inline=True)
    embed.add_field(name="Account ID", value=user.id, inline=True)
    embed.add_field(name="Account Creation Date", value=user.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=True)
    embed.add_field(name="Joined Server Date", value=user.joined_at.strftime('%Y-%m-%d %H:%M:%S') if isinstance(user, discord.Member) else "N/A", inline=True)
    embed.add_field(name="Status", value=str(user.status).capitalize(), inline=True)

    if isinstance(user, discord.Member):
        embed.add_field(name="Activities", value=user.activities[0].name if user.activities else "None", inline=True)
        embed.add_field(name="Voice Channel", value=user.voice.channel.name if user.voice else "N/A", inline=True)
        roles = [role.name for role in user.roles if role.name != "@everyone"]
        roles_str = ', '.join(roles) if roles else "None."
        embed.add_field(name="Server Roles", value=roles_str, inline=False)
        embed.add_field(name="Permissions", value=', '.join([perm[0] for perm in user.guild_permissions if perm[1]]) if user.guild_permissions else "None.", inline=False)
        embed.add_field(name="Nickname", value=user.nick if user.nick else "None", inline=True)

    await ctx.send(embed=embed)

# Help Command
@client.command(
    name="commands",
    description="List all available commands and their descriptions"
)
async def myhelp_command(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description="Here is a list of available commands and their descriptions:",
        color=discord.Color.blue()
    )
    for command in client.commands:
        embed.add_field(
            name=command.name,
            value=command.description,
            inline=False
        )
    await ctx.send(embed=embed)

client.run(TOKEN)
