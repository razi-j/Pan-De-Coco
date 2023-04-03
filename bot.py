import nextcord
from nextcord import guild
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord.member import Member
import os
from key import SECRETKEY

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=[".", ";"], intents=intents)
client.remove_command('help')


InitCogs = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        InitCogs.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for cog in InitCogs:
        client.load_extension(cog)
        print("cogs loaded")

client.run(SECRETKEY)
