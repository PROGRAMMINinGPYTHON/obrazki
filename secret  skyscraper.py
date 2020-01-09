from turtle import *
import math
global a
a = 20
def NYC():
    tło()
    ulica()
    ludzie()
    duzo_wiezowcow()
    glowny_budynek()
def okna_do_wiezowca(poz,odleglosc_okien,swiatlo):
    setpos(poz+a,2.5*a)
    for i in range(2):
        for j in range(8):
            fillcolor(swiatlo)
            begin_fill()
            rt(90)
            fd(a/2)
            lt(90)
            fd(a)
            lt(90)
            fd(a)
            lt(90)
            fd(a)
            lt(90)
            fd(a/2)
            end_fill()
            pu()
            lt(90)
            fd(a+odleglosc_okien)
        setpos(poz+a+2*a,2.5*a)
    
def drzwi_do_wiezowca(poz):
    setpos(poz+2*a,0)
    pd()
    setheading(0)
    fillcolor("blue")
    begin_fill()
    fd(a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(a)
    end_fill()
    lt(90)
    width(3)
    fd(2*a)
def kształt_wiezowca(poz):
    pu()
    setpos(poz,0)
    pd()
    setheading(0)
    fillcolor("black")
    begin_fill()
    rt(90)
    for i in range(2):
        lt(90)
        fd(4*a)
        lt(90)
        fd(15*a)
    end_fill()
    pu()
    
def wiezowiec(poz):
    kształt_wiezowca(poz)
    drzwi_do_wiezowca(poz)
    okna_do_wiezowca(poz,a/2,"blue")

def ulica():
    pu()
    setpos(0,0)
    pd()
    setheading(0)
    fillcolor("darkgrey")
    begin_fill()
    fd(1000)
    rt(90)
    fd(150*a)
    rt(90)
    fd(2000)
    rt(90)
    fd(150*a)
    rt(90)
    fd(1000)
    end_fill()
    
def ludzie():
    pu()
    setpos(-350,-150)
    for i in range(7):
        ludek()
        pu()
        setheading(0)
        fd(5*a)
        rt(90)
        fd(4.5*a)
        pd()
    
def ludek():
    pd()
    setheading(0)
    lt(60)
    fd(3*a)
    rt(120)
    fd(3*a)
    rt(180)
    fd(3*a)
    rt(30)
    fd(2*a)
    rt(90)
    fillcolor("yellow")
    begin_fill()
    circle(25)
    end_fill()
    rt(90)
    fd(a)
    rt(90)
    fd(1*a)
    lt(90)
    fd(1*a)
    rt(180)
    fd(1*a)
    rt(90)
    fd(a)
    fd(1*a)
    lt(90)
    fd(a)

def duzo_wiezowcow():
    for i in range(3):
        if i%1 == 0:
            x=800
        if i%2== 0:
            x = 20*a
        if i == 0:
            x = 45*a
        wiezowiec(900-(x))
        setheading(0)
        fd(x)
        print(x)
        
    for j in range(3):
        if j%1 == 0:
            x= 0*a
        if j%2 == 0:
            x = 15*a
        wiezowiec(-450-x)
        setheading(0)
        fd(x)
        print(x)

def gwiazda():
    for i in range(4):
        width(3)
        setheading(0+45*i)
        color("yellow")
        fd(a/2)
        rt(180)
        fd(a)
        rt(180)
        fd(a/2)
        lt(45)

def gwiazdy_na_niebie():        
    for i in range(6):
        if i>3:
            x = 2*a
        else:
            x = a
        pu()
        setpos(-900+x*i,16*a+2*a*i)
        pd()
        for i in range(35):
            pd()
            gwiazda()
            setheading(0)
            pu()
            fd(50)

def tło():
    pu()
    fillcolor("#778899")
    col = pencolor()
    print (col)
    setpos(-1000,-750)
    begin_fill()
    pd()
    setheading(90)
    fd(1500)
    rt(90)
    fd(2000)
    rt(90)
    fd(1500)
    rt(90)
    fd(200)
    end_fill()

def glowny_budynek():
    pu()
    setpos(0,0)
    setheading(180)
    fd(325)
    pd()
    rt(180)
    fillcolor("black")
    begin_fill()
    b = a*math.sqrt(2)
    setheading(90)
    fd(200)
    rt(45)
    fd(2*b)
    lt(45)
    fd(100)
    rt(45)
    fd(1.5*b)
    rt(90)
    fd(1.5*b)
    rt(45)
    fd(100)
    lt(45)
    fd(b*2)
    rt(45)
    fd(200)
    rt(90)
    fd(150)
    end_fill()
    setheading(0)
    fd(75)
    setheading(90)
    fd(360)
    fillcolor("red")
    begin_fill()
    rt(90)
    fd(5)
    circle(7.5)
    end_fill()
    
speed(0)
NYC()

