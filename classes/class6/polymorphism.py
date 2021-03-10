# abstract class shape that has a draw() and calculate_area() methods
# Shape does not have an implementation, cannot be instantiated
class Shape():
    def draw(self):
        pass
    
    def calculate_area(self):
        pass

class Polygon(Shape):
    # constructor
    def __init__(self, num_sides):
        # instance variable
        self.num_sides = num_sides

# concrete class
class Triangle(Polygon):
    def __init__(self, base, height):
        Polygon.__init__(self, 3)
        self.base = base
        self.height = height

    def draw(self):
        print("Drawing a triangle")

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Square(Polygon):
    def __init__(self, side):
        Polygon.__init__(self, 4)
        self.side = side

    def draw(self):
        print("Drawing a square")

    def calculate_area(self):
        return self.side * self.side  # self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print("Drawing a circle")

    def calculate_area(self):
        return 3.14 * (self.radius**2)

if __name__ == '__main__':
    t1 = Triangle(3, 4)
    t2 = Triangle(4, 7)
    s1 = Square(5)
    s2 = Square(9)
    c1 = Circle(3)
    c2 = Circle(8)

    shapes = [t1, t2, s1, s2, c1, c2]

    # polymorphism
    for s in shapes:
        s.draw()
        print(f'{s.calculate_area()}\n')