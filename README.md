# DJ-Z
A simple bot for Discord that plays music from YouTube via URL.
It uses Discord's Application Commands API so users can interact directly through Discord's UI instead of through messages.

You can follow my tutorial [here](https://medium.com/@ameermushani/how-to-create-a-music-bot-using-discord-py-and-slash-commands-e3c0a0f92e53) if you'd like to make it from scratch.

## Setup
In order to use this bot you need a discord developer account and a bot token.
Create a .env file in the root directory of the project and add the following lines:
```
BOT_TOKEN=<your bot token>
GUILD_ID=<your discord server/guild id>
```
You can get your guild id by enabling developer mode in discord and right clicking on your server icon.

Invite the bot to your server by using the link generated in your discord developer portal.
## Usage
Simply run the bot with `python3 djz.py` and use the slash commands in discord.
