# Myth Bot

Myth Bot is a simple Discord moderation tool bot designed to assist with common moderation tasks in Discord servers. It provides features like banning, kicking, muting, and message pruning (bulk message deletion) using slash commands.

## Features

- **Ban Command**: Ban a user from the server.
- **Kick Command**: Kick a user from the server.
- **Mute Command**: Mute a user with an optional time limit.
- **Prune Command**: Bulk delete a specific number of messages from a channel.
- **Commands Command**: Alternative !help command, with embed.
- **Userinfo Command**: Get detailed information about a user.

## Usage

To use Myth Bot in your Discord server, invite the bot to your server and ensure it has the necessary permissions (e.g., ban, kick, manage roles, manage messages).

Once the bot is in your server, you can use the following slash commands:

- `/ban @user [reason]`: Ban a user from the server with an optional reason.
- `/kick @user [reason]`: Kick a user from the server with an optional reason.
- `/mute @user [reason] [time]`: Mute a user with an optional reason and time limit (in minutes).
- `/prune [number] [reason]`: Bulk delete a specific number of messages from the current channel with an optional reason.
- `/setmutedrole @role`: Set the Muted role for the server.

## Note

- This is not meant for commercial use, only for me to learn how bots work.
- You can do anything to the source, I won't care if you don't credit me.
- I will finish this readme.md someday, so it's not done.

## License 

This project is licensed under the MIT License - see the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) file for details.
