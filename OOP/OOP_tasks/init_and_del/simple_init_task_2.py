# Declare a class called Point so that objects of this class can be created with the following commands:
#
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')
#
# Here, the first two values are the coordinates of the point on the plane (local properties x, y),
# and the optional third argument is the color of the point (local property color).
# If the color is not specified, it defaults to black.
#
# Create a thousand such objects with coordinates (1, 1), (3, 3), (5, 5), ...,
# that is, with an increase of two for each new point.
# Each object should be placed in the points list (in order).
# For the second object in the points list, specify the color 'yellow'.
#
# P.S. There is no need to output anything on the screen in the program.

class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i, 'yellow') if i == 3 else Point(i, i) for i in range(1, 2000, 2)]
