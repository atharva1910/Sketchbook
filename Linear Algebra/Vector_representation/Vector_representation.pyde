add_library('peasycam')
from vector import *
x,y,z=50,50,50
vec = Vector(x,y,z)
# represeting matrix
def setup():
    size(500, 500, P3D)
    PeasyCam(this, 500)
    
def draw():
    background(0)
    scale(2.5)
    stroke(255)
    axes()
    stroke(255,0,0)
    vec.represent()

def axes():
    line(-800, 0, 0, 800, 0, 0)
    line(0, -800, 0, 0, 800, 0)
    line(0, 0, -800, 0, 0, 800)
