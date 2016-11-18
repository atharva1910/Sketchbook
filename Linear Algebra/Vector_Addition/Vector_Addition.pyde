add_library('peasycam')
#Vector Addition
from vector import *
a = Vector(50,50,50)
b = Vector(65,65,32)
one,two,three = b.getCords()

def setup():
    size(800,800,P3D)
    PeasyCam(this,400)
    frameRate(5)
   
def draw():
    background(0)
    stroke(255)
    axes()
    a.represent(255,255,0)
    b.represent(0,128,0)
    saveFrame("###.png")
def mouseClicked():
    p,q,r = a.addVects(one,two,three)
    stroke(255,0,0)
    line(0,0,0,p,q,r)
    
def axes():
    line(-800, 0, 0, 800, 0, 0)
    line(0, -800, 0, 0, 800, 0)
    line(0, 0, -800, 0, 0, 800)