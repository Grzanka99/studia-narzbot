async def run_overwatch(ctx):
    from random import randrange
los = randrange(5)
if los==0:
  tresc = 1
elif los==2:
  tresc = 2
elif los==3:
  tresc = 3
elif los==4:
  tresc = 4
    await ctx.send(tresc)