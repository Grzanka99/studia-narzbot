from random import randrange

async def do_it(ctx):
    los = randrange(5)
    t = []
    t.append("11")
    t.append("https://media.tenor.com/images/cf87814ec30fae132dcf1a38ee33c5f1/tenor.gif")
    t.append("xd")
    t.append("lol")
    t.append("xdd")
    wiadomosc = t[los]
    await ctx.send(wiadomosc)