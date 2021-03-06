import discord
from discord.ext import commands
from data import token

from ping import ping_run
from hello import say_hello
from kys import run_kys
from doit import do_it
from overwatch import run_overwatch
from timeFn import run_time

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


@client.command(pass_context=True)
async def doit(ctx):
    await do_it(ctx)


@client.command(pass_context=True)
async def overwatch(ctx):
    await run_overwatch(ctx)


@client.command(pass_context=True)
async def time(ctx):
    await run_time(ctx)

client.run(token)
