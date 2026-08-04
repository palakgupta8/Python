class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14*self.radius**2

    def Perimeter(self):
        return 2*3.14*self.radius

cir = Circle(5)
print(cir.Area())
print(cir.Perimeter())