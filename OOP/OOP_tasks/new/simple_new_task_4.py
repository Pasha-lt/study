# Declare a class Point to represent points on a plane in Python programming.
# Objects of this class are supposed to be created with the command:
# pt = Point(x, y)
# Here, x and y are numerical coordinates of the point on the plane (numbers),
# which means that each object of this class creates local properties x and y
# that store specific coordinates of the point.
#
# It is necessary to implement a method clone(self) in the Point class,
# which would create a new object of the Point class as a copy of the current object
# with the local attributes x, y and corresponding values.
#
# Create an object pt of the Point class in the program and another object pt_clone by calling the clone method.
#
# P.S. The program does not need to print anything to the screen.


class Point:
    __instance = None

    def __new__(cls, *args, **kwargs):
        # __instance = super().__new__(cls)
        # return cls.__instance
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(pt.x, pt.y)


pt = Point(5, 10)
pt_clone = pt.clone()
