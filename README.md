## DiscordMUDBot

### Installation

#### Install Git (to get updated versions of the bot later)

- Linux: `sudo apt install git`
- Windows: https://gitforwindows.org/

#### Install Python

https://www.python.org/ -> Downloads -> Python 3.8.2

When installing on Windows, check "Add to PATH"

On Linux I'd recommend using [pyenv](https://github.com/pyenv/pyenv)

#### Download this repository

`git clone https://github.com/void4/DiscordMUDBot.git`

#### Discord Bot creation

https://discordapp.com/developers/applications

Add an application

Bot -> Add a Bot

Go to OAuth2

In the first set of fields, check *bot*

In the second set of fields, check *Sending Messages*

Copy the URL from the middle, open it in a new browser tab and add the bot to your server.

#### Python Bot installation and configuration

Go into the repository folder with cd ('change directory')

`cd DiscordMUDBot`

Install the required Python libraries

`pip install -r requirements.txt`

Copy example-config.ini to config.ini

On the Discord Bot page:

Reveal token

Paste it into config.ini's DISCORDTOKEN field

Set your own Discord username in the WIZARDS field (this allows you to make players wizards using the bot, but doesn't make yourself one yet)

#### Install and run a MUD server

Download a MOO server:

- Linux: [LambdaMOO](http://www.moo-cows.com/downloads.html)
- Windows: [WinMOO](https://www.chrisunkel.com/WinMOO/)

Download a MOO Core [Database](http://www.moo-cows.com/downloads.html)

Recommended: LambdaCore

Extract the files (you may need [7zip](https://www.7-zip.org/)) and start the server with a database:

`./moo databasename.db snapshotname.db`

The server will load all objects from the database file specificed by the first argument and then periodically, and when it shuts down, save snapshots of the world to the file specified by the second argument. When you start the server again, use snapshotname.db as the first argument.

If you want to connect to the server the old school way, read this: [MANUAL.md](MANUAL.md)

### Usage

Now that the server is running, start the bot

`python bot.py`

Your bot should now be online on your server

#### Making yourself or others a wizard

Only wizards can create, change or destroy objects.

DM your bot:

Every object in the MUD has an id, which looks like this: `#96`

Find out the players id with

`@who`

Then type

`/makewiz <number>` (for example `/makewiz 96`)

### Notes

For more information see here:

https://www.reddit.com/r/MUD/comments/fsf59a/discord_lambdamoo_experiment/
