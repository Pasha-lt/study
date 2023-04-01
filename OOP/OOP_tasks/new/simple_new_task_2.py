# Declare the SingletonFive class, which can be used to create objects using the command:
#
# a = SingletonFive(<name>)
# Here, <name> is the data that is saved in the local property name of the created object.
#
# This class should only create the first five objects. The rest (sixth, seventh, etc.)
# should be a reference to the last (fifth) created object.
#
# Create the first ten objects of the SingletonFive class using the following program fragment:
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# P.S. The program should not output anything to the screen.

class SingletonFive:
    __instance = None
    __counter = 0

    def __new__(cls, *args, **kwargs):
        if cls.__counter < 5:
            cls.__counter += 1
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
