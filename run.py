import discord
from discord.ext import commands
from data import token

from ping import ping_run
from hello import say_hello
from kys import run_kys
from doit import do_it

client = commands.Bot(command_prefix='~')  # Jaruszewski tu był


@client.event
async def on_ready():
    print("Hello Thereee")


@client.command(pass_context=True)
async def ping(ctx):
    await ping_run(ctx)


@client.command(pass_context=True)
async def hello(ctx):
    await say_hello(ctx)


@client.command(pass_context=True)
async def kys(ctx):
    await run_kys(ctx)

client.run(token)
@client.command(pass_context=True)
async def doit(ctx):
    await do_it(ctx)

client.run(token)
