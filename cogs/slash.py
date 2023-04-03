import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ext.commands import MissingRequiredArgument, has_permissions
from nextcord.member import Member
from nextcord.utils import get
import random
import time

class slash(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @nextcord.slash_command(name='ping', description='Pong🏓! Oh and I send my latency! :>')
    async def ping(self, interaction: Interaction):
        before = time.monotonic()
        message = await interaction.response.send_message("Pong🏓!")
        ping = round((time.monotonic() - before) * 1000)
        await interaction.edit_original_message(content=f"PONG!!\n\n\nLatency: *{ping} ms*")


def setup(client):
    client.add_cog(slash(client))