import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingRequiredArgument, has_permissions
from nextcord.member import Member
from nextcord.utils import get
import random
import time


class commands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client=client

    @commands.command(name="ping")
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("PONG!!")
        ping = round((time.monotonic() - before) * 1000)
        await message.edit(content=f"PONG!!\n\n\nLatency: *{ping} ms*")

    @commands.command(name="8-ball")
    async def ball(self, ctx, *, question:str):
        responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
                "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
                "Yes.", "Yes – definitely.", "You may rely on it."]

        await ctx.send("My response to `{}` is:\n{}".format(question, random.choice(responses)))

    @ball.error
    async def _8ballerror(self, ctx, error:commands.CommandError):
        if isinstance(error, MissingRequiredArgument):
            message="Hey hey hey what are you going to ask? Send a question after sending .8-ball command!"
            await ctx.send(message)

    @commands.command(name="hack")
    async def hack(self,ctx,target:nextcord.Member = None):
        if target == None:
            target = ctx.author
        virus = "NGGYU"
        initial_message = await ctx.send(f"``[▓                    ] / {virus}-virus.exe Packing files.``")
        list = (
            f"``[▓▓▓▓                   ] - {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓                  ] - {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓                 ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓                ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓               ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓              ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓             ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓            ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓          ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] | {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            "``Injecting virus... \``",
            f"``Successfully Injected {virus}-virus.exe into {target.name}``",
            )
        for i in list:
            time.sleep(0.15)
            await initial_message.edit(content=i)
        embed = nextcord.Embed()
        embed.set_image(url="https://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif")
        await target.send(embed=embed)

    @commands.command(name="dadjoke")
    async def dadjoke(self,ctx):
        with open('./cogs/dadjokes.txt', 'r', encoding='utf-8') as dj:
            joke=random.choice(dj.readlines())
            await ctx.send(joke)

    @commands.command(name="td", description="Your standard Truth or Dare Game!")
    async def TruthOrDare(self, ctx, *, choice:str = None):
        choices = ['truth', 'dare']
        if choice == None:
            choice = random.choice(choices)
            await ctx.send(choice)
        
        if choice not in choices:
            await ctx.send("Invalid Choice! Send `truth` or `dare` after sending .td command")
        else:
            if choice == "truth":
                with open('./cogs/t.txt', 'r', encoding='utf-8') as t:
                    truth = random.choice(t.readlines())
                    await ctx.send(truth)

            else:
                with open('./cogs/d.txt', 'r', encoding='utf-8') as d:
                    dare = random.choice(d.readlines())
                    await ctx.send(dare)

    @commands.command(name='flip')
    async def flip(self,ctx):
        coinstate = ["Heads", "Tails"]
        cflip = await ctx.send("Flipping...   -")
        i = (
            "Flipping...   \ ",
            "Flipping...   |",
            "Flipping...   /",
            "Flipping...   -",
            "Flipping...   \ ",
            "Flipping...   | ",
            "Flipping...   /",
            "Flipping...   -",
        )
        for L in i:
            time.sleep(0.25)
            await cflip.edit(content=L)
        await cflip.edit(content = "Flipped!\n\n\n{}".format(random.choice(coinstate), delete_after = 10))
 
    @commands.command(name='kill')
    async def kill(self,ctx,target:nextcord.Member):
        
        killMess = ["`BOOM!!` {} shot {}", "{} used his knife to slit {}'s throat",
        "`drip...` {} poisoned {}'s drink!!", "`BRRRRRRT` {} rains bullets on {}, killing them!",
        "{} stabs {} in the body 100 times!", "{} pushes {} on to their death.", "`Bullet Whiff` {} sniped {}, getting a headshot!",
        "{} gives the kiss of death to {}", "{} cut {}'s body into 2 with their machete!", "{} pushes {} into a grinder and gets shredded!!",
        "{} slaps {} to death!", "`Tick.... Tick.... BOOOOM!!!!` {} placed a grenade inside of {}'s pants!"]

        await ctx.send((random.choice(killMess).format(ctx.message.author.name, target.name)))
    @kill.error
    async def killerror(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("You didn't give me target boss!")

    @commands.command(name='addrole')
    @has_permissions(manage_roles = True)
    async def addrole(self,ctx, *, role:str):
        guild = ctx.guild
        await guild.create_role(name=role)
        await ctx.send("Role: {} has been sucessfully created!".format(role))

    @commands.command(name='setrole')
    @has_permissions(manage_roles = True)
    async def setrole(self,ctx, member:Member, *, roleName:str):
        role = get(member.guild.roles, name=roleName)
        await member.add_roles(role)
        await ctx.send("Role has been sucessfully added to {}!".format(member.mention), delete_after=10)

    @commands.command(name='setnickname')
    async def setnickname(self, ctx, member:Member=None, *, nickname):
        if member == None:
            member = ctx.author
        
        await member.edit(nick=nickname)
        await ctx.send("Nickname Changed for {}".format(member.mention))
def setup(client):
    client.add_cog(commands(client))
