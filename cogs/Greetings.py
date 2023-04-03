import nextcord
from nextcord import guild, Member
from nextcord.ext import commands
from nextcord.utils import get


class Greetings(commands.Cog):
    def __init__(self,client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is ready")

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("OOPS! I don't have a command like that!", delete_after=10)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Aha {ctx.author.mention}! Thou hasn't p...... why am i making this hard for myself\nYou have no permission to use that.", delete_after=10)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing Requirement! Use .help to see what you need to invoke a command!", delete_after=10)
        elif isinstance(error, commands.UserInputError):
            await ctx.send(f"uhm {ctx.author.mention}! Check .help or fix your inputs oke?", delete_after=10)
        else:
            await ctx.send("This is awkward.. there's an error in the command I'm sorry", delete_after=10)

    @commands.Cog.listener()
    async def on_member_join(self,member:Member):
        channel = member.guild.system_channel
        if member.avatar:
            pic = member.avatar.url
        else:
            pic = member.default_avatar.url

        greet = nextcord.Embed(
        title="**HEYOOOO**",
        colour=nextcord.Colour.dark_gold())
        greet.set_thumbnail(url=pic)
        greet.add_field(name="**WELCOME**", value=f"**Hello {member.mention}!!** Welcome to {member.guild.name}!", inline=False)
        greet.add_field(name= "***RULES***", value=None, inline=False)
        greet.add_field(name= "**1. Be respectful**", value="Respect all users! Treat them the way you want to be treated.", inline=False)
        greet.add_field(name= "**2. NO ADS**", value="No personal advertising will happen on this server! I (or my mods) will personally remove those.", inline=False)
        greet.add_field(name= "**2. NO NSFW CONTENT**", value="Keep it clean in General Chat or you will be banned!! There is a separate NSFW Channel", inline=False)
        greet.add_field(name= "**3. DON'T PING EVERYONE**", value="Don't ping everyone. Don't mention someone too much.", inline=False)
        greet.set_footer(text="Hope you enjoy your stay!")
        await channel.send(embed=greet)

        crumbs = 939914340671311882
        role = get(member.guild.roles, id=crumbs)
        await member.add_roles(role)

def setup(client):
    client.add_cog(Greetings(client))