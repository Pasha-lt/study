# Please implement a singly linked list (not a Python list, do not store objects in the list,
# but form a linked structure shown in the figure) of objects of the ListObject class:
#
# [Diagram of the singly linked list]
#
# To do this, declare the ListObject class in the program, objects of which are created by the command:
#
# obj = ListObject(data)
# Each ListObject class object must have the following local properties:
#
# next_obj - a reference to the next attached object (if there is no next object, then next_obj = None);
# data - object data in the form of a string.
#
# The ListObject class itself should declare the method:
#
# link(self, obj) - to attach an object obj of the same class to the current object self
# (that is, the next_obj attribute of the self object must reference obj).
#
# Read a list of strings from the input stream with the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Then create a singly linked list, in the objects of which (in the data attribute)
# the strings from the lst_in list are stored (the first string in the first object, the second in the second, etc.).
# The variable head_obj should refer to the first object of the ListObject class.
#
# P.S. Do not print anything on the screen in the program.


import sys


# Here all the necessary classes are declared
class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


# Reading a list from the input stream (do not change this line)
lst_in = list(map(str.strip, sys.stdin.readlines()))  # Do not modify the lst_in list in the program

head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new
