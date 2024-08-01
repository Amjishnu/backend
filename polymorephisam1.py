class shape :
    def area(self):
        pass
class recatangle (shape):
    def __init__(self,width,height):
        self.width =width
        self.height =height

    def area(self):
        return self .width * self.height
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self .radius ** 2
    
class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self .height =height

    def area(self):
        return 0.5 * self. base * self .height
    
r=recatangle(4,5)
c=circle(3)
t=triangle(6, 7)

print(r.area())
print(c.area())
print(t.area())

     
