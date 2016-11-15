x,y,z = 1, 0, 0
alp,beta,rho = 15,5,35
hu = 1
def setup():
    size(800, 800,P3D)
    colorMode(HSB)
    background(0)

def draw():
    beginShape()
    translate(width/2,height/2)
    scale(5)
    global x,y,z,hu
    x += (alp * (y - x))*0.01
    y += (x * (rho - z) - y)*0.01
    z += (x * y - beta * z)*0.01
    stroke(hu,255,255)
    point(x,y,z)
    hu += 1
    if (hu >= 255):
        saveFrame()
        hu = 0
    print (hu)
    
