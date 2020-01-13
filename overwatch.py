from random import randrange

async def run_overwatch(ctx):
    los = randrange(32)
    if los==0:
        tresc = "Never stop fighting for what you believe in."
    elif los==2:
        tresc = "My business, my rules."
    elif los==3:
        tresc = "No dying on my watch."
    elif los==4:
        tresc = "Bwee, hoo hoo, bwoo."
    elif los==5:
        tresc = "I will prove myself!"
    elif los==6:
        tresc = "I play to win!"
    elif los==7:
        tresc = "Only through conflict do we evolve."
    elif los==8:
        tresc = "身を捨てても、名利は捨てず。"
    elif los==9:
        tresc = "With every death, comes honor. With honor, redemption."
    elif los==10:
        tresc = "It's a perfect day for some mayhem."
    elif los==11:
        tresc = "Come on, let's bring it together!"
    elif los==12:
        tresc = "Justice ain't gonna dispense itself."
    elif los==13:
        tresc = "Our world is worth fighting for."
    elif los==14:
        tresc = "I'll be watching over you."
    elif los==15:
        tresc = "Science will reveal the truth."
    elif los==16:
        tresc = "Your safety is my primary concern."
    elif los==17:
        tresc = "I will protect the innocent."
    elif los==18:
        tresc = "Death walks among you."
    elif los==19:
        tresc = "Justice will be done."
    elif los==20:
        tresc = "I'm a one-man apocalypse."
    elif los==21:
        tresc = "There is no obligation for the universe to make sense to you."
    elif los==22:
        tresc = "We're all soldiers now."
    elif los==23:
        tresc = "Everything can be hacked... and everyone."
    elif los==24:
        tresc = "The true enemy of humanity is disorder."
    elif los==25:
        tresc = "Build 'em up, break 'em down."
    elif los==26:
        tresc = "Cheers, love! The cavalry's here!"
    elif los==27:
        tresc = "One shot, one kill."
    elif los==28:
        tresc = "Imagination is the essence of discovery."
    elif los==29:
        tresc = "Control link established."
    elif los==30:
        tresc = "Together we are strong."
    elif los==31:
        tresc = "True self is without form."
    await ctx.send(tresc)