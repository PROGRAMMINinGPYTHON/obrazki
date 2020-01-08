from turtle import *
global a
a = 20
def NYC():
    ulica()
    ludzie()
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
    for i in range(10):
        if i%2 == 0:
            odstep= 2*a
        else:
            odstęp=3*a
        if i%3 == 0:
            odstep = 5*a
        wiezowiec()
        
wiezowiec(0)  
