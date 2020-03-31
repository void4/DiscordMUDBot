import asyncio
import discord
from discord.abc import PrivateChannel
from discord.ext.tasks import loop
from telnetlib import Telnet

connections = {}

NOPLAYER = b"Either that player does not exist, or has a different password."
CONNECTED = b"*** Connected ***\n"
CREATED = b"*** Created ***\n"

def makewiz():
    pass

"""

wiztn = Telnet("localhost", 7777)

wiztn.write()

@chparent #p to $wiz
@programmer #p
;#p.wizard=1
"""

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

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # only respond to private dms
        if not isinstance(message.channel, PrivateChannel):
            return
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.author.id not in connections:
            await message.channel.send("Reconnecting...")
            tn = Telnet("localhost", 7777)
            connections[message.author.id] = [tn, message.channel]
            #watch out for unicode!
            intro = tn.read_until(b"respectively.\r\n")
            print(intro)
            #TODO replace spaces in message.author!
            tn.write(f"connect {message.author} 12345\n".encode("utf8"))
            #result = tn.expect([NOPLAYER, CONNECTED])
            con = tn.read_until(CONNECTED, 3)
            print(con)
            if NOPLAYER in con:
                await message.channel.send("First login, creating player...")
                print(f"Creating player {message.author}")
                tn.write(f"create {message.author} 12345\n".encode("utf8"))
                crt = tn.read_until(CREATED, 3)
                await message.channel.send("Player created!")
            #tn.read_until()
            #print(tn.read_until(b"\n"))
            #print(tn.read_until(b"\n"))
            await message.channel.send(con.decode("utf8"))
        else:
            tn, _ = connections[message.author.id]

        tn.write(message.content.encode("ascii")+b"\n")

        #data = tn.read_until(b"\n", 1)#until(b"\n", 3)
        data = tn.read_very_eager()
        print(data)
        if data:
            await message.channel.send(escape(data))

        #telnet.close()

client = MyClient()
output_task.start()
#client.loop.create_task(output_task())
from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
client.run(config["DEFAULT"]["DISCORDTOKEN"])
