# Declare a class named Figure with two attributes:
# type_fig: 'ellipse'
# color: 'red'
#
# Create an instance named fig1 of this class and add the following local attributes to it:
# start_pt: (10, 5)
# end_pt: (100, 20)
# color: 'blue'
#
# Remove the color property from the instance of the class and print a list of all local properties
# (without values) of the fig1 object in one line separated by a space in the order specified in the task.


class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
delattr(fig1, "color")
for key, value in fig1.__dict__.items():
    print(key, end=" ")
