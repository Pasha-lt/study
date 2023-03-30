# Declare the AbstractClass class, objects of which should not be creatable. When executing the command:
#
# obj = AbstractClass()
# the variable obj should reference a string with the content:
#
# "Error: cannot create objects of an abstract class"
#
# P.S. Only declare the class in the program, no need to print anything on the screen.


class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Error: cannot create objects of an abstract class"


obj = AbstractClass()
