# Declare three classes of geometric shapes: Line, Rect, Ellipse.
# It should be possible to create objects of each class with the following commands:
#
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
#
# Here, the arguments a, b, c, d
# represent the coordinates of the upper right and lower left corners (arbitrary numbers). In each object,
# the coordinates should be saved in the local properties sp (upper right corner)
# and ep (lower left corner) as tuples (a, b) and (c, d) respectively.
#
# Generate 217 objects of these classes: for each current object, the class is randomly selected
# (either Line, or Rect, or Ellipse). The coordinates are also generated randomly (numerical values).
# Save all objects in the elements list.
#
# Set the coordinates of the objects to zero only for the Line class in the elements list.
#
# P.S. There is no need to output anything on the screen in the program.


import random


class Line:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []

for _ in range(217):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)]))
