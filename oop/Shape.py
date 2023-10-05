
# Shape, Circle, Square, Rectangle, Triangle
# Attribute: width, height, radius
# Method: Area(), Perimeter()
import math
print(math.pi)

class Shape:
    def __init__(self):
        pass
    
class Square(Shape):
    def __init__(self, width):
        self.width = width
        
    def Area(self):
        return self.width * self.width
    
    def Perimeter(self):
        pass
    
    def Draw(self):
        pass

    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        
    def Area(self):
        return self.width * self.height
    
    def Draw(self):
        pass


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def Area(self):
        return self.width * self.height
    
    def Draw(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def Area(self):
        return self.radius * self.radius * math.pi
    
    def Perimeter(self):
        return self.radius * 2 * math.pi
    
s = Square(4)
print(s.Area())

c = Circle(10)
print(c.Area())
print(c.Perimeter())
