import discord
from discord.ext import commands
from data import token


client = commands.Bot(command_prefix='>')


@client.event
async def on_ready():
    print("Hello Thereee")


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send("pong!")


client.run(token)
