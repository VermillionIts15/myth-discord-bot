# Myth Bot

Myth Bot is a simple Discord moderation tool bot designed to assist with common moderation tasks in Discord servers. It provides features like banning, kicking, muting, and message pruning (bulk message deletion) using slash commands.

## Features

- **Ban Command**: Ban a user from the server.
- **Kick Command**: Kick a user from the server.
- **Mute Command**: Mute a user with an optional time limit.
- **Prune Command**: Bulk delete a specific number of messages from a channel.
- **Set Muted Role Command**: Set a designated "Muted" role for muting users.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/YourUsername/Myth-Bot.git
```

2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

3. Replace `"YOUR_BOT_TOKEN_HERE"` in `myth_bot.py` with your bot's actual token.

4. Run the bot:

```
python myth_bot.py
```

## Usage

To use Myth Bot in your Discord server, invite the bot to your server and ensure it has the necessary permissions (e.g., ban, kick, manage roles, manage messages).

Once the bot is in your server, you can use the following slash commands:

- `/ban @user [reason]`: Ban a user from the server with an optional reason.
- `/kick @user [reason]`: Kick a user from the server with an optional reason.
- `/mute @user [reason] [time]`: Mute a user with an optional reason and time limit (in minutes).
- `/prune [number] [reason]`: Bulk delete a specific number of messages from the current channel with an optional reason.
- `/setmutedrole @role`: Set the Muted role for the server.

```
Make sure to replace placeholders like `"YOUR_BOT_TOKEN_HERE"` and GitHub repository URLs with your actual information. You can also add more sections or details specific to your bot project if needed.
```

## Contributing 

Contributions to Myth Bot are welcome! If you have suggestions, bug reports, or would like to contribute code, please follow these steps:

- Please, If your going to show your code, DON'T SHOW YOUR BOT TOKEN. I shouldn't even have to say it, but don't do it.

1. Fork the repository

2. Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature` or `git checkout -b bug/fix-bug`.

3. Make your changes and commit them: `git commit -m "Description of your changes"`.

4. Push your changes to your fork: `git push origin feature/new-feature` or `git push origin bug/fix-bug`.

5. Create a pull request on the main repository.



## License 

This project is licensed under the MIT License - see the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) file for details.
