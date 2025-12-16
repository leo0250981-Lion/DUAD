import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2) 
 #Example the area of a Circle 
circle = Circle(5)
print(circle.get_area())