## DiscordMUDBot

### Installation

Created/tested with Python 3.8.2

`pip install -r requirements.txt`

https://discordapp.com/developers/applications

Add a Bot

Reveal token

Paste it into config.ini

Go to OAuth2

In the first set of fields, check *bot*

In the second set of fields, check *Sending Messages*

Copy the URL from the middle, open it in a new browser tab and add the bot to your server.

Download a MOO server:

- Linux: [LambdaMOO](http://www.moo-cows.com/downloads.html)
- Windows: [WinMOO](https://www.chrisunkel.com/WinMOO/)

Download a MOO Core [Database](http://www.moo-cows.com/downloads.html)

Extract the files and start the server with a database:

`./moo databasename.db snapshotname.db`

The server will load all objects from the database file specificed by the first argument and then periodically, and when it shuts down, save snapshots of the world to the file specified by the second argument. When you start the server again, use snapshotname.db as the first argument.

On Windows, activate the telnet client.

On Linux, install it with `sudo apt install telnet`

`telnet localhost 7777`

`connect wizard`

Making players wizards

(to allow them to create new objects and rooms)

replace p with the players object id, which you can find out with `@who`
```
@chparent #p to $wiz
@programmer #p
;#p.wizard=1
```

## Usage

Add your Bots' Discord access token to config.ini. Then:

`python bot.py`

For more information see here:

https://www.reddit.com/r/MUD/comments/fsf59a/discord_lambdamoo_experiment/
