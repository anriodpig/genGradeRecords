import random

fp=open("random.txt","w+")

def genA():
    return str(random.randint(0, 99999999))
def genB():
    return (random.choice('abcdefghijklmnopqrstuvwxyz'))
def genC():
    return str(random.randint(0,10000)/100)
def genR():
    return genA()+' '+genB()+genB()+genB()+genB()+genB()+' '+genC()+' '+genC()+' '+genC()+' '+genC()+' '+genC()+' '+genC()+'\n'

i=30
while i>0:
    fp.write(genR())
    i-=1
