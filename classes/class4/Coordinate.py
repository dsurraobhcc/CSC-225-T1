import math
'''
2-dimensional coordinate (x, y) 
'''

class Coordinate():
    # constructor
    def __init__(self, x, y):
        self.x = x # instance variable
        self.y = y

    # sqrt((x1 - x2)**2 + (y1 - y2)**2)
    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    # special method: override
    def __str__(self):
        return f'({self.x}, {self.y})'
    

if __name__ == '__main__':
    origin = Coordinate(0, 0) # object: instance of Coordinate class
    point2 = Coordinate(3, 4)

    distance = origin.get_distance(point2)
    #print(distance)

    print(point2)