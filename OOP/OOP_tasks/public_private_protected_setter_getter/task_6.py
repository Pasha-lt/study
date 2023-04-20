# You need to implement a linked list (not a Python list and not storing objects in a Python list), where ObjList class objects are linked to their neighbors through private properties __next and __prev:

# To do this, declare a LinkedList class that will represent the linked list as a whole and have a set of the following methods:

# add_obj(self, obj) - adding a new ObjList class object obj to the end of the linked list;
# remove_obj(self) - removing the last object from the linked list;
# get_data(self) - getting a list of the __data local property strings of all the objects in the linked list.

# And in each object of this class, local public attributes should be created:

# head - reference to the first object of the linked list (if the list is empty, then head = None);
# tail - reference to the last object of the linked list (if the list is empty, then tail = None).

# ObjList class objects should have the following set of private local properties:

# __next - reference to the next object in the linked list (if there is no next object, then __next = None);
# __prev - reference to the previous object in the linked list (if there is no previous object, then __prev = None);
# __data - a string with data.

# Also, in the ObjList class, the following setters and getters should be implemented:

# set_next(self, obj) - changing the private property __next to the obj value;
# set_prev(self, obj) - changing the private property __prev to the obj value;
# get_next(self) - getting the value of the private property __next;
# get_prev(self) - getting the value of the private property __prev;
# set_data(self, data) - changing the private property __data to the data value;
# get_data(self) - getting the value of the private property __data.


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = self.__pref = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    
class LinkedList:
    def __init__(self):
       self.head = None
       self.tail = None

    def add_obj(self, obj):
       if self.tail:
           self.tail.set_next(obj)
       obj.set_prev(self.tail)
       self.tail = obj
       if not self.head:
           self.head = obj
           
    def remove_obj(self):
       if self.tail is None:
           return
       
       prev = self.tail.get_prev()
       if prev:
           prev.set_next(None)
       self.tail = prev
       if self.tail is None:
           self.head = None

    def get_data(self):
       s = []
       h = self.head
       while h:
           s.append(h.get_data())
           h = h.get_next()
       return s
