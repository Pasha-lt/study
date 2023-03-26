# Declare a class called Graph, objects of which can be created using the command:
#
# gr_1 = Graph(data)
#
# Here, data is a list of numerical data (data for the graph).
# The following local properties must be formed when creating each instance of the class:
#
# data - a reference to a list of numerical data (each object must have its own data list,
# so you need to create a copy of the passed list);
# is_show - a Boolean value (True/False) for showing (True) and hiding (False) the graph data (default is True);
#
# In this class, declare the following methods:
#
# set_data(self, data) - for passing a new data list to the current graph;
# show_table(self) - for displaying data as a string of numbers from the list (numbers are separated by spaces);
# show_graph(self) - for displaying data as a graph
# (the method outputs the message "Graphical representation of data:
# <string of numbers separated by spaces>" to the console);
# show_bar(self) - for displaying data as a bar chart
# (the method outputs the message "Bar chart: <string of numbers separated by spaces>" to the console);
# set_show(self, fl_show) - a method for changing the local property is_show to the passed value fl_show.
#
# If the local property is_show is False, the show_table(), show_graph(), and show_bar()
# methods should output the message:
# "Data display is closed"
#
# Read numerical data from the input stream using the command:
#
# data_graph = list(map(int, input().split()))
#
# Create an object gr of the Graph class with the set of read data, call the show_bar() method,
# then the set_show() method with the value fl_show = False, and call the show_table() method.
# Two corresponding lines should be displayed on the screen.
#
# Sample Input:
# 8 11 10 -32 0 7 18
#
# Sample Output:
# Bar chart: 8 11 10 -32 0 7 18
# Data display is closed


class Graph:
    def __init__(self, data, is_show=True):
        self.is_show = is_show
        self.data = data[:]  # make full cut

    def set_data(self, data):
        self.data.append(data)

    def show_table(self):
        if self.is_show == False:
            print("Data display is closed")
        else:
            print(*self.data)

    def show_graph(self):
        if self.is_show == False:
            print("Data display is closed")
        else:
            print("Graphical representation of data: ", *self.data)

    def show_bar(self):
        if self.is_show == False:
            print("Data display is closed")
        else:
            print("Bar chart: ", *self.data)

    def set_show(self, fl_show):
        self.is_show = fl_show

data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()
