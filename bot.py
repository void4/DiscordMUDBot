import asyncio
import discord
from discord.abc import PrivateChannel
from discord.ext.tasks import loop
from telnetlib import Telnet
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")[0]
config = config["DEFAULT"]

connections = {}

NOPLAYER = b"Either that player does not exist, or has a different password."
CONNECTED = b"*** Connected ***\n"
CREATED = b"*** Created ***\n"

def conv(s):
    return s.encode("ascii")

wiztn = Telnet("localhost", int(config["PORT"]))
wiztn.write(conv("connect wizard\n"))
print(wiztn.read_very_eager())

def makewiz(id):
    magicwords = f"""@chparent #{id} to $wiz
@programmer #{id}
;#{id}.wizard=1
""".encode("ascii")

    wiztn.write(magicwords)

def escape(b):
    return b.decode("utf8").replace("`", "\`")

@loop(seconds=1)
async def output_task():
    for uid, meta in connections.items():
        tn, channel = meta
        data = tn.read_very_eager()
        if data:
            await channel.send(escape(data))

    print(".", end="")

class Bot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Only respond to private DMs
        if not isinstance(message.channel, PrivateChannel):
            return

        # Don't respond to ourselves
        if message.author == self.user:
            return

        if message.author.id not in connections:
            await message.channel.send("Reconnecting...")
            tn = Telnet("localhost", int(config["PORT"]))
            connections[message.author.id] = [tn, message.channel]
            #watch out for unicode!
            intro = tn.read_until(b"respectively.\r\n")
            print(intro)
            tn.write(f"connect {str(message.author).replace(' ', '-')} 12345\n".encode("utf8"))
            #result = tn.expect([NOPLAYER, CONNECTED])
            con = tn.read_until(CONNECTED, 3)
            print(con)

            if NOPLAYER in con:
                await message.channel.send("First login, creating player...")
                print(f"Creating player {message.author}")
                tn.write(f"create {str(message.author).replace(' ', '-')} 12345\n".encode("utf8"))
                crt = tn.read_until(CREATED, 3)
                await message.channel.send("Player created!")
            #print(tn.read_until(b"\n"))
            await message.channel.send(con.decode("utf8"))
        else:
            tn, _ = connections[message.author.id]

        if message.content.startswith("/makewiz ") and str(message.author) in config["WIZARDS"].split(","):
            id = message.content.split(" ")[1]
            makewiz(id)
            await message.channel.send(f"Made {id} a wizard :)")
            return

        tn.write(message.content.encode("ascii")+b"\n")

        #data = tn.read_until(b"\n", 1)#until(b"\n", 3)
        data = tn.read_very_eager()
        print(data)
        if data:
            await message.channel.send(escape(data))

        #telnet.close()

bot = Bot()
output_task.start()
bot.run(config["DISCORDTOKEN"])
