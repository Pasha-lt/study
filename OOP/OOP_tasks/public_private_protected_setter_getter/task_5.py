# Declare two classes Point and Rectangle in the program. Objects of the first class should be created with the command:
# 
# pt = Point(x, y)
# where x, y are the coordinates of a point on the plane (integer or real numbers). At the same time,
# the following local properties should be formed in the objects of the Point class:
# 
# __x, __y - coordinates of the point on the plane.
# 
# and one getter:
# 
# get_coords() - returning a tuple of the current coordinates __x, __y
# 
# Objects of the second class Rectangle (rectangle) should be created with the commands:
# 
# r1 = Rectangle(Point(x1, y1), Point(x2, y2))
# or
# 
# r2 = Rectangle(x1, y1, x2, y2)
# Here the first coordinate (x1, y1) is the top-left corner, and the second coordinate (x2, y2)
# is the bottom-right corner. At the same time, 
# the following local properties should be formed in the objects of the Rectangle class
# (regardless of the way they are created):
# 
# __sp - object of the Point class with coordinates x1, y1 (top-left corner);
# __ep - object of the Point class with coordinates x2, y2 (bottom-right corner).
# 
# Also, the following methods should be implemented for the Rectangle class:
# 
# set_coords(self, sp, ep) - changing the current coordinates, where sp, ep are objects of the Point class;
# get_coords(self) - returning a tuple of objects of the Point class with the current coordinates of the rectangle
# (references to local properties __sp and __ep);
# draw(self) - displaying a message in the console: "Rectangle with coordinates: (x1, y1) (x2, y2)". 
# Here x1, y1, x2, y2 are the corresponding numerical values of the coordinates.
# 
# Create an object rect of the Rectangle class with coordinates (0, 0), (20, 34).
# 

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2=None, y2=None):
        if isinstance(x1, Point) and isinstance(y1, Point):
            self.__sp = x1
            self.__ep = y1
        else:
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Rectangle with coordinates: {(self.__sp.get_coords())} {(self.__ep.get_coords())}')


rect = Rectangle(0, 0, 20, 34)






