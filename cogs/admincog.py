import nextcord
from nextcord import guild, utils
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from nextcord.ext.commands import MissingAnyRole
import datetime
import humanfriendly

class admincog(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(description="kicks member")
    @has_permissions(kick_members=True)
    async def kick(self,ctx, member:nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send("I have successfully kicked {}".format(member))

    @commands.command(description="bams member")
    @has_permissions(ban_members=True)
    async def ban(self,ctx, member:nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send("I have successfully banned {}".format(member))

    @commands.command(description="unbans")
    @has_permissions(ban_members=True)
    async def unban(self,ctx, *, member):
        bannedusers = await ctx.guild.bans()
        name, discriminator = member.split('#')
        for ban in bannedusers:
            user = ban.user
            if(user.name, user.discriminator) == (name, discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} has been unbanned from {ctx.guild.name}")
                return

    @commands.command()
    @has_permissions(administrator=True, manage_messages=True)
    async def clear(self,ctx, amount:int=5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"***{amount} messages have been cleared***", delete_after=5)

    @commands.command(name='help')
    async def help(self,ctx):
        hembed = nextcord.Embed(
            title="**Pan de Coco Bot Commands!**",
            colour=nextcord.Colour.dark_gold()
        )
        hembed.set_footer(text="Please use the commands in servers where Pan de Coco is in. Thank you!!\nI hope you found this helpful!")
        hembed.set_image(url="https://bulbandkey.com/blog/wp-content/uploads/2020/10/05_pastry_bakery-shops.1920x0.jpg")
        hembed.add_field(name="Basic Information: ", value="Hi! I'm Pan De Coco! A bot made by <@741364782581416007>. My prefix is `.` and `;` \nI hope you find my functions enjoyable!", inline=True)
        hembed.add_field(name=".ping or ;ping", value="Sends Pong and Bot latency", inline=False)
        hembed.add_field(name=".8-ball or ;8-ball", value="(is used by sending the command and a yes/no question)\nShows your fortune!", inline=False)
        hembed.add_field(name=".clear or ;clear", value="Clears the 5 recent messages\nYou can set the amount of messages to be deleted by adding a number after the command", inline=False)
        hembed.add_field(name=".help or ;help", value="Sends you this message!", inline=False)
        hembed.add_field(name=".td or ;td",value="Truth or Dare! Send the command along with `truth` or `dare` to get chilling Truths or spicy Dares!", inline=False)
        hembed.add_field(name='.sinfo or ;sinfo', value="Sends the Server's Info!",inline=False)
        hembed.add_field(name=".flip or ;flip", value="Coin Flip!!", inline=False)
        hembed.add_field(name=".dadjoke or ;dadjoke", value="Sends you the best type of comedy!", inline=False)        
        hembed.add_field(name=".kill or ;kill", value="Kills a target you mention!", inline=False)
        await ctx.send(embed=hembed)

    @commands.command(name='sinfo')
    async def sinfo(self,ctx):
        role_count = len(ctx.guild.roles)
        pic = ctx.guild.icon.url

        hembed = nextcord.Embed(
            title="**SERVER INFO**",
            timestamp=ctx.guild.created_at,
            colour=nextcord.Colour.dark_gold())
        hembed.set_thumbnail(url=pic)
        hembed.set_footer(text="Date of Creation: ")
        hembed.add_field(name="Name of Server: ", value=f"{ctx.guild.name}", inline=False)
        hembed.add_field(name="Number of Members: ", value=f"{ctx.guild.member_count}", inline=False)
        hembed.add_field(name="Number of Member Roles:", value=str(role_count), inline=False)
        hembed.add_field(name="Highest Role:", value=str(ctx.guild.roles[-2]), inline=False)
        await ctx.send(embed=hembed,delete_after=60)
        
    @commands.command(name='mute')
    async def mute(self, ctx, member:nextcord.Member, time):
        time = humanfriendly.parse_timespan(time)
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        await ctx.send("{} has been muted by {} due to: {}".format(member, ctx.author.mention))

def setup(client):
    client.add_cog(admincog(client))