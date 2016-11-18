class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.it = 0

    def getCords(self):
        return self.x, self.y, self.z

    def represent(self,r,g,b):
        stroke(r,g,b)
        line(0, 0, 0, self.x, self.y, self.z)

    def addVects(self, r, p, q):
        
        line(r, p, q, self.x + r, self.y + p, self.z + q)
        return self.x + r, self.y + p, self.z + q
        """
            for i in range(1,x+1):
            self.it += i
            self.x += i
            self.y += i
            self.z += i
            """
