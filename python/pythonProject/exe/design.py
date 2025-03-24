from turtle import *
import colorsys
tracer(100)
bgcolor("black")
pensize(4)
h=0
for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.1
    fillcolor(c)
    begin_fill()
    rt(46.5)
    fd(i)
    lt(2)
    circle(20,185)
    end_fill()
    circle(i,20)
    fd(180)
done()