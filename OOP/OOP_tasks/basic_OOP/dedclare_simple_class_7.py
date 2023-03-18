# Declare a class named Graph with methods:
#
# set_data(data) - passing a set of data for subsequent display (data is a list of numeric data);
# draw() - displaying the data (in the same order as in the data list)
#
# and an attribute:
#
# LIMIT_Y = [0, 10]
#
# The set_data() method should create a local property called data in the Graph class object.
# The data attribute should refer to the list passed to the method.
# The draw() method should print the list on the screen as a string of numbers separated
# by spaces and belonging to the specified range of the LIMIT_Y attribute (boundaries are inclusive).
#
# Create a graph_1 object of the Graph class, call the set_data() method for it, and pass the list:
#
# [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
#
# Then, call the draw() method through the graph_1 object. A line with a corresponding set of numbers,
# separated by spaces, should appear on the screen. For example (output without quotes):
#
# "10 0 2 5 7"

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = []
        for i in data:
            if i <= self.LIMIT_Y[1] and i >= self.LIMIT_Y[0]:
                self.data.append(i)

    def draw(self):
        print(*self.data)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
