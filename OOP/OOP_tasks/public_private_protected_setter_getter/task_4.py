# Declare a Line class for describing a line on a plane, which is expected to be created using the command:
#
# line = Line(x1, y1, x2, y2)
# In the line object, the following private local properties should be created:
#
# __x1, __y1 - starting coordinate;
# __x2, __y2 - ending coordinate.
#
# The Line class itself should implement the following setters and getters:
#
# set_coords(self, x1, y1, x2, y2) - for changing the line coordinates;
# get_coords(self) - for getting a tuple of the current line coordinates.
#
# And also the method:
#
# draw(self) - for displaying in the console a list of the current line coordinates
# (in a single line separated by a space).

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())
