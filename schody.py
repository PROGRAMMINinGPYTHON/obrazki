from turtle import *
global a
a = 40

def romb(kol): 
    fillcolor(kol)
    begin_fill()
    fd(a)
    lt(60)
    fd(a)
    lt(120)
    fd(a)
    lt(60)
    fd(a)
    end_fill()

    
def schodek():
    setheading(30)
    romb("black")
    rt(120)
    fd(a)
    rt(60)
    fd(a)
    rt(180)
    romb("grey")
    rt(180)
    romb("white")
    lt(60)


def jeden_poz(ile):
    for i in range(ile):
        schodek()
        setheading(-30)
        pu()
        fd(a)
        rt(60)
        fd(a)
        lt(60)
        fd(a)
        lt(60)
        pd()
def SCHODY(ile):
    for i in range(ile):
        pass


speed(0)    
SCHODY(2)
