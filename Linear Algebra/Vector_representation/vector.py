class Vector:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    
    def represent(self):
        line(0,0,0,self.x,self.y,self.z)